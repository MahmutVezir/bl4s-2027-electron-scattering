# CLEAR fizibilitesi, çelişkiler ve risk kaydı

**Kontrol tarihi:** 17 Kasım 2026  
**Birincil teknik kaynak:** CERN'in Kasım 2026 CLEAR fizibilite föyü.

## Resmi kaynaklarda görülen kısıtlar

| Başlık | Yayımlanan bilgi | Tasarıma etkisi |
|---|---|---|
| Demet türü | Saf elektron demeti | Elektronla uyumlu tek hedef deney gerekir |
| Momentum | Fizibilite föyü 50–220 MeV/c | Genel Beams & Detectors dokümanıyla alt sınır çelişkisi var |
| Bunch yükü | 0.01–1.5 nC | Bunch başına yük ayarı deney koşulunu etkiler |
| Zayıflatma | Ortalama bir elektron/bunch seviyesine indirilebilir | Seyrek vuruş ölçümü için umut verici; ayrıştırma teyit edilmeli |
| Tekrarlama | 0.8–10 Hz | Veri toplama süresini ve istatistiği sınırlar |
| Mikro-bunch | Train içinde 1–150 | Öneri tek mikro-bunch/train seçeneğini sorgulamalı |
| Deney alanı | 1 m × 1 m | Kompakt düzenek şart |
| Süre | 10 günden kısa; günde 12 saat demet | Çok fazla konfigürasyon planlanmamalı |
| Erişim | Hafta içi günde 2–3 kez | Uzaktan veri izleme ve önceden kurulmuş düzenek önemli |
| Veri toplama | En fazla 2000 olay/s | Yüksek olay oranı tek başına hedef değil; gerçek hız dedektörle sınırlanabilir |
| Tercih | Elektronik/optik algılayıcıyla anlık geri bildirim | Timepix3 yaklaşımı bu öncelikle uyumlu olabilir |

## CLEAR için listelenen algılayıcılar

Kasım 2026 fizibilite föyü aşağıdakileri listeliyor:

- 3 adet sintilatör: 10 × 10 cm, EJ200, PMT, yaklaşık %95 verim; yalnızca düşük yoğunluklu demetle kullanılabilir.
- 3 adet lead-glass kalorimetre: 10 × 10 cm kesit, 37 cm uzunluk, PMT ve QDC; yalnızca düşük yoğunluklu demetle kullanılabilir.
- 1 adet WENDI nötron doz ölçer.
- YAG ekranları ve CCD/CMOS kameralar.
- Timepix3 ve Katherine okuma sistemi: 256 × 256 piksel, 55 µm piksel adımı; varış zamanı ve Time-over-Threshold bilgisi alınabilir.
- Takımın getirdiği dedektör prototipleri, ayrı güvenlik/teknik değerlendirmeyle ve 2.000 ABD doları yapım bütçesi sınırıyla denenebilir.

## Belge tutarsızlıkları — çözülmeden kesin kabul edilmemeli

1. **Momentum alt sınırı:** Kasım 2026 CLEAR fizibilite föyü 50 MeV/c, 2027 Beams & Detectors PDF'si 60 MeV/c alt sınırını veriyor. Bu tasarımda ortak ve temkinli aralık olan 60–220 MeV/c kullanılıyor.
2. **Lead-glass kalorimetre:** Beams & Detectors PDF'sinin dedektör uygunluk tablosu CERN için elektromanyetik kalorimetreyi “no” gösterirken, CLEAR fizibilite föyü üç lead-glass kalorimetre listeliyor. Bu deney kalorimetreye dayanmıyor; tutarsızlık yine de BL4S ekibine sorulmalı.

## Bu deney için kritik riskler

### R1 — Tek düzlemden doğrudan açı ölçümü yapılamaması
Timepix3 tek bir düzlemde konum/zaman verir. Giriş ve çıkış izlerini ölçen bir teleskop olarak kabul edilmemeli.  
**Azaltım:** hedef yok/hedef var koşullarındaki aşağı akış dağılım genişliğini karşılaştır; ölçüm büyüklüğünü “vuruş dağılımı genişliği” olarak adlandır. Doğrudan açı iddiası ancak uygun ek iz düzlemleri ve onaylı düzenek sağlanırsa yapılabilir.

### R2 — Aktif alanın küçük olması
Timepix3 aktif alanı yaklaşık 14.08 mm × 14.08 mm'dir.  
**Azaltım:** demet odak boyutu ve sensör konumu CERN ekibiyle doğrulanmalı; kesilmiş dağılımın ölçüm yanlılığı yaratmadığı gösterilmeli.

### R3 — Yığınlaşma / pile-up
Ortalama bir elektron/bunch ayarı tek başına olayların sensörde ayrılacağını garanti etmez. Aynı train içindeki mikro-bunch zaman aralığı ve sensör okuması önemlidir.  
**Azaltım:** tek mikro-bunch/train ve düşük yoğunluk talep et; Timepix3 ve DAQ ile olay kümelerinin ayrılabilirliğini test et.

### R4 — Demet kayması ve odak değişimi
Hedefsiz referans ve hedefli koşullar arasında demet merkezi/şekli değişirse, saçılma kaynaklı genişleme yanlış tahmin edilir.  
**Azaltım:** hedefsiz koşulu hedefli ölçümlerin öncesi ve sonrasında al; demet profili/merkezini izle; ölçüm sırasını bloklar içinde dengele.

### R5 — Geometri onaysız
200 mm hedef–Timepix3 mesafesi yalnızca hesap varsayımıdır. Hedef tutucu ve sensörün 1 × 1 m alan içindeki kesin yerleşimi bilinmiyor.  
**Azaltım:** CLEAR ekibinden izin verilen mesafe aralığı, montaj/yerleşim ve güvenlik onayı alınmalı.

### R6 — Elektron enerji kaybı ve bremsstrahlung
50–220 MeV/c elektronlar için enerji kaybı ve bremsstrahlung ihmal edilebilir kabul edilemez. Al hedefte çok küçük x/X0 seçimi bu katkıyı azaltmayı amaçlar; sıfırlamaz.  
**Azaltım:** sonuçları yalnızca basit tek-formül tahminine dayandırma; Geant4/eşdeğer elektron taşınımı ile kontrol et ve enerji spektrumu etkisini sistematik belirsizlik olarak kaydet.

### R7 — Belirsiz hedef özellikleri
Folyoların gerçek kalınlığı, yüzey durumu, alaşım saflığı, tutucu malzemesi ve hizalaması ölçüm sonucuna etki edebilir.  
**Azaltım:** sertifikalı/ölçülmüş folyo kullan; kalınlığı ve malzeme bilgisini veri kaydına yaz; boş tutucu kontrolü yap.

### R8 — Teorik dağılımın kuyrukları
Çoklu saçılma dağılımının merkez bölgesi yaklaşık Gauss olabilir; seyrek büyük açılı saçılmalar Gauss dışı kuyruk üretir.  
**Azaltım:** yalnızca RMS raporlayıp kuyrukları gizleme; merkezi genişlikle birlikte kuyruk oranını da ayrı raporla.

## Ön fizibilite hükmü

**Koşullu / açık teknik onaya bağlı.** CLEAR'de Timepix3 ve alüminyum hedef tabanlı bir konum dağılımı karşılaştırması prensipte makul görünüyor. Fakat tek Timepix3'nin olay ayrıştırması, aktif alan, gerçek hedef–sensör mesafesi ve beam spot uyumu teyit edilmeden “uygulanabilir” olarak kesin sınıflandırılamaz.
