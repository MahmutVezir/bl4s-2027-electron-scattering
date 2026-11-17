# Mahmut'un BL4S 2027 yazılım görevi — uygulama kaydı

## Amaç

Python veri analizi, ROOT/PyROOT ve parçacık simülasyon araçlarının işlevlerini elektron–alüminyum örnek mekanizması üzerinden öğrenmek. Bu depo hazırlık ve örnek çalışma içerir; CERN'de yapılmış deney veya gerçek beam verisi içermez.

## Teslim maddeleri

### 1. Python / NumPy / Matplotlib

- [x] 480 satırlık deterministik sentetik örnek hit verisi oluşturuldu: data/synthetic/example_hits.csv.
- [x] İki koşul için histogram üretildi: figures/synthetic_hit_histograms.svg.
- [x] Ortalama, örnek standart sapma ve standart hata hesaplandı: data/synthetic/summary.csv.
- [x] Ortalama ± standart hata karşılaştırma grafiği oluşturuldu: figures/synthetic_mean_errorbars.svg.
- [x] Analizi yeniden üreten NumPy/Matplotlib betiği eklendi: analysis/analyze_synthetic_hits.py.

**Bilimsel sınır:** Veri sentetiktir. Gerçek dedektör verisi değildir ve saçılma fiziğini doğrulamaz. Hata çubukları yalnızca standart hatayı gösterir; sistematik belirsizlikleri kapsamaz.

### 2. ROOT / PyROOT

- [x] İki TH1D histogramı dolduran örnek PyROOT betiği eklendi: analysis/pyroot_histogram.py.
- [ ] ROOT kurulu bilgisayarda çalıştırma ve üretilen ROOT dosyasını açarak doğrulama.

PyROOT betiği bu depo hazırlığı sırasında çalıştırılmış olarak raporlanmıyor; ROOT ortamı gerektirir.

### 3. Geant4

- [x] Kaynak, geometri, malzeme, fizik listesi, sensitive detector ve scoring kavramları için resmi dokümantasyon notu eklendi.
- [ ] C++ örnek uygulama oluşturma ve derleme.
- [ ] Elektron + Al folyo + scoring düzlemi örneği çalıştırma.
- [ ] Geant4 sürümü, physics list ve seed kayıtlarını ekleme.

### 4. FLUKA / Flair

- [x] FLUKA ve Flair rol ayrımı ile Geant4 karşılaştırması belgelendi.
- [ ] FLUKA erişimi/kurulumu ve Flair ile örnek input çalıştırma.
- [ ] Aynı basit geometri için scoring sonuçlarını kaydetme.

### 5. GATE / OpenGATE

- [x] GATE'in Geant4 tabanlı olduğu ve başlıca tıbbi görüntüleme/dozimetri kullanım alanları not edildi.
- [ ] İhtiyaç doğarsa küçük bir OpenGATE örneği çalıştırma.

## Sonraki mantıklı sıra

1. NumPy/Matplotlib betiğini yerel Python ortamında çalıştırıp iki PNG çıktısını üret.
2. ROOT/PyROOT örneğini ROOT kurulu ortamda çalıştır.
3. Geant4 Basic Example B1 veya B2'yi derle/çalıştır; ardından elektron-Al düzeneğine uyarlamayı planla.
4. FLUKA/Flair ile aynı basit gözlenebilir için bağımsız kontrol kur.
5. GATE'i yalnızca gerekçeli bir kullanım ihtiyacı varsa ele al.

## Bilgisayar/kurulum notu

Geant4, FLUKA ve ROOT kurulumları ciddi yazılım bağımlılıkları ve derleme ortamı gerektirebilir. Telefon üzerinden kodu incelemek mümkün olsa da bu araçları gerçek anlamda çalıştırmak için bilgisayar veya uygun Linux/uzak hesaplama ortamı gerekir. Kurulum yapılmadıysa “öğrenildi/çalıştırıldı” değil, “dokümantasyonu incelendi/örnek kod hazırlandı” denmelidir.


## Doğrulama notu

Sentetik CSV, NumPy ile bağımsız olarak okundu; 480 satır, iki koşul ve ortalama/SD/SEM değerleri yeniden hesaplandı. İki grafik üretim işlemi test ortamında başarıyla çalıştı. GitHub Actions denemesi ise job adımları başlamadan başarısız sonlandı (runner atanmadı); bu nedenle CI için başarılı test iddiası yoktur. PyROOT, Geant4 ve FLUKA'nın gerçek yazılım kurulumlarında çalıştırılması hâlâ bekliyor.
