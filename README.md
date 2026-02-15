# 🎧 YouTube Downloader by MichiMiau_u1 📥

Un potente script de Python para descargar videos, audios y listas de reproducción de YouTube con una interfaz de terminal intuitiva y una barra de progreso visual.

---

## ✨ Características principal

* **🎬 Descarga de Video:** Obtiene la mejor calidad disponible en formato `.mp4`.
* **🎵 Conversión a MP3:** Extrae el audio en alta fidelidad (192kbps) automáticamente.
* **📃 Soporte de Playlists:** Descarga listas de reproducción completas de una sola vez.
* **🚀 Barra de Progreso:** Visualización en tiempo real del estado de la descarga gracias a `tqdm`.
* **📁 Organización Automática:** Crea la carpeta de destino si no existe para mantener tu PC ordenado.

---

## 🛠️ Requisitos del Sistema

Para que el script funcione correctamente, asegúrate de tener instalado lo siguiente:

### 1. Python 3.x
Debes tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

### 2. FFmpeg (Crucial)
**FFmpeg** es necesario para procesar los archivos de video y convertir a MP3.
* **Windows:** Descarga los binarios, extráelos y añade la carpeta `bin` a tu **PATH** del sistema.
* **Linux:** `sudo apt install ffmpeg`
* **macOS:** `brew install ffmpeg`

### 3. Librerías de Python
Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:

```bash
pip install yt-dlp tqdm
