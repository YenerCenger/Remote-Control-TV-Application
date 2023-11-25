
from random import *
from time import *

class Kumanda():

    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["TRT"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_aç(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor")
            self.tv_durum = "Açık"

    def tv_kapa(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon kapatılıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttır: '>'\nÇıkış : 'çıkış'")
            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
                else:
                    print("Ses zaten kapalı")
            elif cevap == ">":
                if self.tv_ses != 100:
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
                else:
                    print("Ses Zaten full")
            elif cevap == "çıkış":
                print("Ses Güncellendi.\nGüncel Ses Düzeyi",self.tv_ses)
                break
            else:
                print("Geçersiz İşlem girdiniz.")
    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor")
        sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi.")

    def kanal_kaldır(self,silinecek_kanal):
        if silinecek_kanal in self.kanal_listesi:
            print("Kanal Siliniyor...")
            sleep(0.6)
            self.kanal_listesi.remove(silinecek_kanal)
            print("Kanal Silindi.")
        else:
            print("",silinecek_kanal,"Adlı Kanal Bulunamadı.")

    def mute(self):
        if self.tv_ses != 0:
            print("Televizyon sessize alınıyor..")
            return self.tv_ses == 0
        else:
            print("Televizyonun zaten sessizde..")
    def rastgele_kanal(self):

        rastgele = randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu Anki Kanal:",self.kanal)

    def kanal_değiştir(self,hedef_kanal):
        if hedef_kanal in self.kanal_listesi:
            self.kanal = hedef_kanal
            print("Kanal Değiştirildi.")
        else:
            print("Böyle Bir kanal Yok")

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞuanki Kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

print("""
*********************************************
Televizyon Uygulaması

İşlemler;

1.TV Aç

2.TV Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Kaldır

6.Kanal Sayısı Öğrenme

7.Rastgele kanala Geçme

8.Televizyon Bilgileri

9.Sessize Alma

10.Kanal Değiştirme

Çıkmak için 'q' ya Basın.

**********************************************
""")
kumanda = Kumanda()
while True:
    işlem = input("Lütfen Yapmak İstediğiniz İşlemi Giriniz:")
    if işlem == "q":
        print("Program Sonlandırılıyor")
        break
    elif işlem == "1":
        kumanda.tv_aç()
    elif işlem == "2":
        kumanda.tv_kapa()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        kanallar = input("Kanal İsimlerini ',' ile ayırarak girin:")
        kanal_listesi = kanallar.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif işlem == ("5"):
        silinecek_kanal = input("Silinecek kanalı giriniz:")
        kumanda.kanal_kaldır(silinecek_kanal)
    elif işlem == "6":
        print("Kanal Sayısı",len(kumanda))
    elif işlem == "7":
        kumanda.rastgele_kanal()
    elif işlem == "8":
        print(kumanda)
    elif işlem == "9":
        kumanda.mute()
    elif işlem == "10":
        hedef_kanal = input("Gitmek İstediğiniz Kanalı Girin:")
        kumanda.kanal_değiştir(hedef_kanal)
    else:
        print("Geçersiz İşlem....")