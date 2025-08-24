import requests
from bs4 import BeautifulSoup
from transformers import BartTokenizer, pipeline
from gtts import gTTS
import schedule
import time
from datetime import datetime
import os

# URLs de ejemplo
urls = {
    "emol": "https://www.emol.com",
    "latercera": "https://www.latercera.com"
}

def get_headline_latercera():
    r = requests.get(urls["latercera"])
    soup = BeautifulSoup(r.text, "html.parser")

    headlines = []
    # Titulares en la Tercera
    for h2 in soup.find_all("h2", class_="story-card__headline"):
        headlines.append(h2.text.strip())
    #headlines = [h.get_text(strip=True) for h in soup.select("h2.story-card__headline")[:limit]]
    return headlines

def get_headlines_emol():
    r = requests.get(urls["emol"])
    soup = BeautifulSoup(r.text, "html.parser")

    headlines = []

    # 1️⃣ Titular principal
    h1 = soup.find("div#ucHomePage_cuNoticiasCentral_contTitular h1 a")
    if h1 and h1.a:
        headlines.append(h1.a.text.strip())

    # 2️⃣ Titulares secundarios
    secondary = soup.find_all("div[id^='ucHomePage_cuNoticiasCentral_repNoticiasCetral_cajaSec'] h3 a")
    for h3 in secondary:
        if h3.a:
            headlines.append(h3.a.text.strip())

    return headlines

# Modelo y tokenizer
model_name = "facebook/bart-large-cnn"
resumidor = pipeline("summarization", model=model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

# Función que divide un texto largo en chunks seguros por tokens
def dividir_en_chunks(texto, max_tokens=900):
    """
    Divide el texto en bloques seguros para BART (máximo 1024 tokens).
    Usamos 900 como margen de seguridad.
    """
    tokens = tokenizer.encode(texto)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        parte = tokens[i:i+max_tokens]
        chunk = tokenizer.decode(parte, skip_special_tokens=True)
        chunks.append(chunk)
    print(f" Dividiendo chucks de texto...")
    return chunks

# 2. Resumir cada trozo
def trozo_resumen(chunks):
    resumenes = []
    for chunk in chunks:
        r = resumidor(chunk, max_length=130, min_length=50, do_sample=False)
        resumenes.append(r[0]['summary_text'])
    # 3. Juntar los resúmenes en uno solo
    texto_resumido = " ".join(resumenes)
    print(f"✅ Resumen generado")
    return texto_resumido

def guardar_archivos(resumen):
    # Fecha actual
    fecha= datetime.now().strftime("%Y-%m-%d")

    # Carpeta de salida
    os.makedirs("podcasts", exist_ok=True)

    # Archivos
    archivo_mp3 = f"podcasts/podcast_{fecha}.mp3"
    archivo_txt = f"podcasts/podcast_{fecha}.txt"

    # Guardar audio
    tts = gTTS(text=resumen, lang='es')
    tts.save(archivo_mp3)

    # Guardar texto
    with open(archivo_txt, "w", encoding="utf-8") as f:
        f.write(resumen)
    
    print(f"✅ Podcast generado: {archivo_mp3}")
    print(f"📝 Resumen guardado: {archivo_txt}")

def crear_podcast():
    print("🎙️ Generando podcast de noticias...")
    titulares = get_headlines_emol() + get_headline_latercera()
    texto_para_resumir = ". ".join(titulares)
    # --- Tu texto largo aquí ---
    texto_para_resumir = texto_para_resumir # 9874 caracteres
    # 1. Dividir automáticamente en trozos seguros
    chunks = dividir_en_chunks(texto_para_resumir)
    resumen = trozo_resumen(chunks)
    guardar_archivos(resumen)

# Automatización
schedule.every().day.at("08:00").do(crear_podcast)

print("⏳ Esperando la hora programada (08:00 cada día)...")
while True:
    schedule.run_pending()
    time.sleep(60)
