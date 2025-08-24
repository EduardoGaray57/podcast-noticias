# 🎙️ Podcast Automatizado de Noticias

Proyecto en **Python** que genera un podcast diario de noticias de forma automática.  
Se conecta a medios chilenos, obtiene los titulares, los resume usando un modelo de **Transformers** y los convierte a voz para generar un archivo `.mp3`.

---

## 🚀 Características
- 📌 **Scraping de noticias** desde medios chilenos (Ej: La Tercera, Cooperativa).
- 🧠 **Resumen automático** usando Hugging Face Transformers (modelo `facebook/bart-large-cnn`).
- 🔊 **Conversión a voz (TTS)** con `gTTS`.
- ⏰ **Automatización diaria** con `schedule`.

---

## 🛠️ Stack Tecnológico
- [requests](https://docs.python-requests.org/) → para hacer peticiones HTTP.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) → para extraer titulares de HTML.
- [transformers](https://huggingface.co/transformers/) → para resumir los textos.
- [gTTS](https://gtts.readthedocs.io/) → para convertir texto a voz.
- [schedule](https://schedule.readthedocs.io/en/stable/) → para programar la ejecución diaria.

---

## 📂 Estructura del proyecto
```
podcast-noticias/
│── scraper.py        # Script principal
│── requirements.txt  # Dependencias del proyecto
│── .gitignore        # Archivos ignorados por git
│── README.md         # Documentación del proyecto
```

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/EduardoGaray57/podcast-noticias.git
   cd podcast-noticias
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # En Windows PowerShell
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Uso
Ejecutar el script:

```bash
python scraper.py
```

Esto generará un archivo `podcast.mp3` con las noticias resumidas y narradas.

---

## 📅 Automatización
Puedes programar la ejecución diaria con la librería `schedule` o usando el **Task Scheduler** de Windows / **cron** en Linux.

---

## 🧑‍💻 Autor
👨‍💻 Eduardo Garay  
📍 Quilicura, Región Metropolitana, Chile  
📧 [eduardo.garay@ucen.cl](mailto:eduardo.garay@ucen.cl)  
🔗 [LinkedIn](https://www.linkedin.com/in/eduardo-garay-9b067b16) | [GitHub](https://github.com/EduardoGaray57)

---

## 🌟 Contribuciones
¡Las contribuciones son bienvenidas! Puedes hacer un fork y abrir un Pull Request.
