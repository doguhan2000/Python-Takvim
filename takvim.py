import calendar
from datetime import datetime

class TakvimUygulamasi:
    def __init__(self):
        self.takvim = calendar.Calendar()
        self.etkinlikler = {}

    def takvimi_goster(self, yil, ay):
        takvim_ayi = self.takvim.monthdatescalendar(yil, ay)
        print(f"\n{calendar.month_name[ay]} {yil}\n")
        print(" Pzt Sal Çar Per Cum Cmt Paz")
        for hafta in takvim_ayi:
            for gun in hafta:
                if gun.month == ay:
                    etkinlikler = self.etkinlikler.get(gun, [])
                    etiket = "*" if len(etkinlikler) > 0 else " "
                    print(f"{etiket}{gun.day:2d} ", end=" ")
                else:
                    print("   ", end=" ")
            print()

    def etkinlik_ekle(self, tarih, etkinlik):
        if tarih not in self.etkinlikler:
            self.etkinlikler[tarih] = []
        self.etkinlikler[tarih].append(etkinlik)

    def etkinlikleri_goster(self, tarih):
        etkinlikler = self.etkinlikler.get(tarih, [])
        if etkinlikler:
            print(f"\n{tarih.strftime('%d %B %Y')}'deki Etkinlikler:")
            for i, etkinlik in enumerate(etkinlikler, 1):
                print(f"{i}. {etkinlik}")
        else:
            print(f"\n{tarih.strftime('%d %B %Y')}'de herhangi bir etkinlik yok.")

    def etkinlik_sil(self, tarih, indeks):
        etkinlikler = self.etkinlikler.get(tarih, [])
        if etkinlikler and 0 < indeks <= len(etkinlikler):
            etkinlikler.pop(indeks - 1)
            print("Etkinlik başarıyla silindi.")
        else:
            print("Belirtilen indekse sahip bir etkinlik bulunamadı.")

    def ana_menu(self):
        while True:
            print("\n***** Takvim Uygulaması *****")
            print("1. Takvimi Göster")
            print("2. Etkinlik Ekle")
            print("3. Etkinlikleri Görüntüle")
            print("4. Etkinlik Sil")
            print("5. Çıkış")

            secim = input("\nYapmak istediğiniz işlemi seçin (1/2/3/4/5): ")

            if secim == '1':
                yil = int(input("Yıl girin (örn. 2024): "))
                ay = int(input("Ay girin (1-12): "))
                self.takvimi_goster(yil, ay)
            elif secim == '2':
                tarih = input("Etkinlik tarihini (GG.AA.YYYY) girin: ")
                etkinlik = input("Etkinlik açıklamasını girin: ")
                try:
                    tarih = datetime.strptime(tarih, "%d.%m.%Y")
                    self.etkinlik_ekle(tarih, etkinlik)
                    print("Etkinlik başarıyla eklendi.")
                except ValueError:
                    print("Geçersiz tarih formatı. Lütfen GG.AA.YYYY formatında girin.")
            elif secim == '3':
                tarih = input("Etkinliklerini görmek istediğiniz tarihi (GG.AA.YYYY) girin: ")
                try:
                    tarih = datetime.strptime(tarih, "%d.%m.%Y")
                    self.etkinlikleri_goster(tarih)
                except ValueError:
                    print("Geçersiz tarih formatı. Lütfen GG.AA.YYYY formatında girin.")
            elif secim == '4':
                tarih = input("Etkinlik silmek istediğiniz tarihi (GG.AA.YYYY) girin: ")
                try:
                    tarih = datetime.strptime(tarih, "%d.%m.%Y")
                    self.etkinlikleri_goster(tarih)
                    if tarih in self.etkinlikler:
                        indeks = int(input("Silmek istediğiniz etkinliğin indeksini girin: "))
                        self.etkinlik_sil(tarih, indeks)
                except ValueError:
                    print("Geçersiz tarih formatı. Lütfen GG.AA.YYYY formatında girin.")
            elif secim == '5':
                print("Takvim uygulaması kapatılıyor...")
                break
            else:
                print("Geçersiz işlem. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    takvim_uygulamasi = TakvimUygulamasi()
    takvim_uygulamasi.ana_menu()
