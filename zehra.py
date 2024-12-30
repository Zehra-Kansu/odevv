# Öğrenci Yönetim Sistemi

class Ogrenci:
    def __init__(self, isim, soyisim, ogrenci_no):
        self.isim = isim
        self.soyisim = soyisim
        self.ogrenci_no = ogrenci_no
        self.notlar = []

    def not_ekle(self, not_degeri):
        self.notlar.append(not_degeri)

    def ortalama_hesapla(self):
        if len(self.notlar) == 0:
            return 0
        return sum(self.notlar) / len(self.notlar)

    def __str__(self):
        return f"{self.ogrenci_no} - {self.isim} {self.soyisim}"


class OgrenciYonetimSistemi:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, isim, soyisim, ogrenci_no):
        yeni_ogrenci = Ogrenci(isim, soyisim, ogrenci_no)
        self.ogrenciler.append(yeni_ogrenci)
        print(f"Öğrenci eklendi: {yeni_ogrenci}")

    def ogrenci_listele(self):
        if not self.ogrenciler:
            print("Henüz öğrenci eklenmedi.")
            return
        print("\nSistemdeki Öğrenciler:")
        for ogrenci in self.ogrenciler:
            print(ogrenci)

    def not_ekle(self, ogrenci_no, not_degeri):
        for ogrenci in self.ogrenciler:
            if ogrenci.ogrenci_no == ogrenci_no:
                ogrenci.not_ekle(not_degeri)
                print(f"{ogrenci} öğrencisine {not_degeri} notu eklendi.")
                return
        print(f"Öğrenci bulunamadı: {ogrenci_no}")

    def not_analizi(self, ogrenci_no):
        for ogrenci in self.ogrenciler:
            if ogrenci.ogrenci_no == ogrenci_no:
                ortalama = ogrenci.ortalama_hesapla()
                print(f"{ogrenci} öğrencisinin notları: {ogrenci.notlar}")
                print(f"Not Ortalaması: {ortalama:.2f}")
                return
        print(f"Öğrenci bulunamadı: {ogrenci_no}")


# Ana program
def menu():
    sistem = OgrenciYonetimSistemi()

    while True:
        print("\n=== Öğrenci Yönetim Sistemi ===")
        print("1. Öğrenci Ekle")
        print("2. Öğrencileri Listele")
        print("3. Öğrenciye Not Ekle")
        print("4. Not Analizi Yap")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            isim = input("Öğrenci İsmi: ")
            soyisim = input("Öğrenci Soyismi: ")
            ogrenci_no = input("Öğrenci Numarası: ")
            sistem.ogrenci_ekle(isim, soyisim, ogrenci_no)
        elif secim == "2":
            sistem.ogrenci_listele()
        elif secim == "3":
            ogrenci_no = input("Not eklenecek öğrenci numarası: ")
            not_degeri = float(input("Eklenecek Not: "))
            sistem.not_ekle(ogrenci_no, not_degeri)
        elif secim == "4":
            ogrenci_no = input("Not analizi yapılacak öğrenci numarası: ")
            sistem.not_analizi(ogrenci_no)
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


# Programı çalıştır
if __name__ == "__main__":
    menu()
