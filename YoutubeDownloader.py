import yt_dlp
import os

def download_con_ytdlp():
    url = input("Incolla l'URL di YouTube: ")
    cartella = input("Cartella di destinazione (Premi Invio per quella corrente): ") or "."

    if not os.path.exists(cartella):
        os.makedirs(cartella)

    print("\nCosa vuoi scaricare?")
    print("1. Video (Massima qualità disponibile - 1080p, 4K, 8K)")
    print("2. Solo Audio (Migliore qualità MP3/M4A)")
    scelta = input("Scegli (1 o 2): ")

    # Configurazione base delle opzioni
    ydl_opts = {
        'outtmpl': f'{cartella}/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    if scelta == '1':
        # Seleziona il miglior video + il miglior audio e li unisce
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
        ydl_opts['merge_output_format'] = 'mp4'  # Forza il contenitore finale in MP4
    else:
        # Scarica solo l'audio e lo converte in MP3
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nInizio download...")
            ydl.download([url])
        print(f"\nOperazione completata con successo!")
    except Exception as e:
        print(f"\nSi è verificato un errore: {e}")

if __name__ == "__main__":
    download_con_ytdlp()