from pytube import YouTube


video_url = input("Video URL'sini girin: ")


print("Seçenekler: \n1. 720p\n2. 480p\n3. 360p\n4. 240p\n5. 144p")
quality = input("İndirmek istediğiniz kaliteyi seçin (ör. 720p): ")

# YouTube videosunu indirme
try:
    yt = YouTube(video_url)
    
    # Belirtilen kaliteyi bul ve indir
    video = yt.streams.filter(res=quality, file_extension='mp4').first()
    if video:
        print("İndirme başlıyor...")
        video.download()
        print("İndirme tamamlandı!")
    else:
        print(f"{quality} çözünürlüğünde video bulunamadı. Lütfen başka bir kalite seçin.")
except Exception as e:
    print("Bir hata oluştu:", e)
