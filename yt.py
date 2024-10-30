import yt_dlp

video_url = input("Video URL'sini girin: ")

print("Çözünürlük seçenekleri: \n1. 720p\n2. 480p\n3. 360p\n4. 240p\n5. 144p")
quality = input("İndirmek istediğiniz kaliteyi seçin (ör. 720p): ")

name = input("Video ismini girin: ")

# İndirilecek kaliteye göre format ayarlarını yapılandır
ydl_opts = {
    'format': f'bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]',
    'outtmpl': f'{name}.%(ext)s',  # Kullanıcının girdiği adı dosya adı olarak ayarla
    'merge_output_format': 'mp4',  # Çıktıyı mp4 formatında birleştir
}

# Video indirme işlemi
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([video_url])
        print("Video başarıyla indirildi!")
    except Exception as e:
        print("Bir hata oluştu:", e)
