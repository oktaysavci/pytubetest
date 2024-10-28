from pytube import YouTube

def download_youtube_video():
  
    video_url = input("Video URL'sini girin: ")
  
    resolution = input("İstediğiniz çözünürlüğü girin (örneğin 1080p, 720p): ")
    
    yt = YouTube(video_url)
    
    stream = yt.streams.filter(res=resolution, file_extension="mp4").first()
    
    if stream is None:
        print(f"{resolution} çözünürlüğünde bir video bulunamadı. Mevcut olan çözünürlükler:")
        for stream in yt.streams.filter(file_extension="mp4"):
            print(f"- {stream.resolution}")
        return

    print(f"Video Başlığı: {yt.title}")
    print(f"Çözünürlük: {stream.resolution}")
    
    stream.download()
    print("İndirme işlemi tamamlandı.")

download_youtube_video()
