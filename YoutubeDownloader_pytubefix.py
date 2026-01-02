from pytubefix import YouTube
from pytubefix.cli import on_progress
import os


def download_con_pytube():
    url = input("Incolla l'URL di YouTube: ")
    cartella = input("Cartella di destinazione (Premi Invio per quella corrente): ") or "."

    if not os.path.exists(cartella):
        os.makedirs(cartella)

    try:
        # Crea l'oggetto YouTube
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"\nAnalisi di: {yt.title}")

        print("\nCosa vuoi scaricare?")
        print("1. Video (MP4 - 720p con Audio)")
        print("2. Solo Audio (M4A)")
        scelta = input("Scegli (1 o 2): ")

        if scelta == '1':
            # Filtra per stream progressivi (Video + Audio insieme)
            stream = yt.streams.get_highest_resolution()
            print("Download video in corso...")
        else:
            # Filtra solo per l'audio
            stream = yt.streams.get_audio_only()
            print("Download audio in corso...")

        # Scarica il file
        stream.download(output_path=cartella)
        print(f"\nCompletato! Salvato in: {os.path.abspath(cartella)}")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")


if __name__ == "__main__":
    download_con_pytube()