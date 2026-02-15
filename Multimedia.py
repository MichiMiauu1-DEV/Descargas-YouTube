import yt_dlp
from tqdm import tqdm
import os

# 📂 Ruta fija de descarga
RUTA_DESCARGA = r"C:\Descargas"

# Crear carpeta si no existe
os.makedirs(RUTA_DESCARGA, exist_ok=True)

def barra_progreso(d):
    if d['status'] == 'downloading':
        if not hasattr(barra_progreso, "pbar"):
            barra_progreso.pbar = tqdm(
                total=d.get('total_bytes', 0),
                unit='B',
                unit_scale=True,
                dynamic_ncols=True,
                desc="🚀 Descargando..."
            )

        if d.get('downloaded_bytes'):
            barra_progreso.pbar.total = d.get('total_bytes', barra_progreso.pbar.total)
            barra_progreso.pbar.update(d['downloaded_bytes'] - barra_progreso.pbar.n)

    elif d['status'] == 'finished':
        barra_progreso.pbar.close()
        print("\n✨ Descarga completa!\n")


def descargar_video(url):
    opciones = {
        "progress_hooks": [barra_progreso],
        "noplaylist": True,
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(RUTA_DESCARGA, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


def descargar_mp3(url):
    opciones = {
        "progress_hooks": [barra_progreso],
        "format": "bestaudio/best",
        "outtmpl": os.path.join(RUTA_DESCARGA, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


def descargar_playlist(url, mp3=False):
    opciones = {
        "progress_hooks": [barra_progreso],
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(RUTA_DESCARGA, "%(playlist_title)s/%(title)s.%(ext)s"),
        "yes_playlist": True,
        "merge_output_format": "mp4"
    }

    if mp3:
        opciones["format"] = "bestaudio/best"
        opciones["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


# ==========================
#        PROGRAMA
# ==========================

print("🎧 Bienvenido al descargador YouTube 📥")

url = input("🔗 Ingresa el enlace: ")
preg = input("📂 ¿Es una lista de reproducción? (si/no): ").strip().lower()
mp3 = input("🎵 ¿Quieres descargar en MP3? (si/no): ").strip().lower() == "si"

if preg == "si":
    print("\n📃 Descargando playlist completa...\n")
    descargar_playlist(url, mp3)
else:
    print("\n🎬 Descargando video individual...\n")
    if mp3:
        descargar_mp3(url)
    else:
        descargar_video(url)

print("\n✅ ¡Todo listo! 😺🔥")
print(f"📁 Archivos guardados en: {RUTA_DESCARGA}")
print("Script hecho por MichiMiau_u1")
