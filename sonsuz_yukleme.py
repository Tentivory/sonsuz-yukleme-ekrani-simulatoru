import time
import sys
import base64

# Gizli mesaj (ciddiye alma)
gizli = base64.b64decode(b'U3lhc2V0IGtheWJldGkgZXNyZXIgc2FiaXIgc2FiaXIgYW1hIG9uY2UgZGVtb2tyYXNpIHlhcGlsYW4gYmlyIHVsdXMgYmVrbGVuc2luLg==').decode('utf-8')

def sonsuz_yukle():
    mesajlar = [
        "Evrenin sırları yükleniyor...",
        "Kahve demleniyor (dijital olarak)...",
        "Komşunun dedikoduları analiz ediliyor...",
        "Hayatın anlamı hesaplanıyor (sonuç: 42 değil)...",
        "Kedi internete giriyor...",
        "Bürokrasi sırası bekleniyor...",
        "Sonsuzluk neredeyse bitti...",
        "Hala yükleniyor, merak etme...",
        "İşte bu kadar, ama aslında değil."
    ]
    i = 0
    while True:
        for yuzde in range(0, 100, 7):
            sys.stdout.write(f"\rYükleniyor: {yuzde}% - {mesajlar[i % len(mesajlar)]}")
            sys.stdout.flush()
            time.sleep(0.5)
        i += 1
        print(f"\n{gizli if i % 13 == 0 else 'Devam ediyor...'}")
        time.sleep(1)

if __name__ == "__main__":
    print("Sonsuz Yükleme Ekranı başlatıldı. Durdurmak için Ctrl+C.")
    try:
        sonsuz_yukle()
    except KeyboardInterrupt:
        print("\nYükleme durduruldu. Ama aslında hiç başlamamıştı.")
        print("\n--- MÜHÜR: Kayyum Grok | 15.10.2026 | Ciddi ama değil ---")
