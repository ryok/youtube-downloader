import yt_dlp

def download_audio_as_mp3(youtube_url, output_path="downloaded_audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # 音声のみを抽出
        'audioformat': 'mp3',  # MP3フォーマットで保存
        'outtmpl': output_path,  # 出力ファイル名
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    url = input("YouTubeのURLを入力: ")
    download_audio_as_mp3(url)
    print("MP3ファイルのダウンロードが完了しました！")

