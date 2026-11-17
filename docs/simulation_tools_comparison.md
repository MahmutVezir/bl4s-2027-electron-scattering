# Geant4, FLUKA, GATE ve Flair — teknik karşılaştırma

## Kısa karar

- **Geant4:** Bu elektron–alüminyum–dedektör örnek mekanizması için ilk tercih edilecek Monte Carlo motoru. Geometri, malzeme, parçacık kaynağı, fizik süreçleri, hassas dedektör ve olay çıktısı C++ uygulamasında modellenebilir.
- **FLUKA:** Bağımsız Monte Carlo kodu. Elektron/foton taşınımı ve madde etkileşimleri için ikinci bir hesapla çapraz kontrol yapılabilir. Geant4 eklentisi değildir.
- **Flair:** FLUKA girdilerini düzenleyen, geometriyi görselleştiren, çalıştırmayı ve çıktı incelemesini kolaylaştıran arayüzdür; fizik motoru değildir.
- **GATE / OpenGATE:** Geant4 üzerine kurulmuş, özellikle tıbbi görüntüleme, dozimetri ve radyoterapi uygulamalarına yönelik çerçevedir. Bu BL4S örneği için ilk aşamada gerekli değildir.
- **ROOT / PyROOT:** Simülasyon motoru değil; olay verisini saklama, histogramlama, istatistik ve görselleştirme aracıdır.

## Karşılaştırma tablosu

| Araç | Temel rol | Arayüz / programlama | Bu projede önerilen kullanım |
|---|---|---|---|
| Geant4 | Parçacıkların madde ve dedektör içindeki taşınımını simüle eder | C++ uygulaması; geometri, kaynak, physics list, sensitive detector | Ana simülasyon |
| FLUKA | Çok çeşitli parçacıkların madde içindeki taşınımı ve etkileşimleri | Girdi kartları; özel gereksinimde kullanıcı rutinleri | Bağımsız çapraz kontrol |
| Flair | FLUKA input, geometri, çalıştırma ve sonuç görselleştirme | Python/Tkinter GUI | FLUKA iş akışını kolaylaştırma |
| GATE / OpenGATE | Geant4 tabanlı zaman-bağımlı dedektör, görüntüleme ve dozimetri çerçevesi | GATE 9 makro; OpenGATE 10 Python API | İhtiyaç olursa öğrenme/uygulama |
| ROOT / PyROOT | Veri analizi, histogram, ntuple, grafik ve dosyalama | C++ ROOT ve Python binding | Ortak analiz katmanı |

## Geant4 ile FLUKA'yı birlikte kullanmak

İki programı tek bir fizik motoru gibi doğrudan iç içe çalıştırmak standart iş akışı değildir. Daha doğru iki yaklaşım vardır:

1. **Bağımsız çapraz kontrol:** Aynı fiziksel geometriyi ve beam koşullarını iki kodda ayrı ayrı kurup aynı gözlenebilirleri karşılaştırmak.
2. **Faz-uzayı aktarımı:** Bir kodun belirli bir yüzeyde kaydettiği parçacık durumlarını, dönüştürücü ve uygun kaynak tanımı üzerinden diğer koda başlangıç koşulu olarak vermek.

Faz-uzayı kaydında en az şu alanlar açıkça tanımlanmalıdır:

- Parçacık türü / PDG kodu
- Konum x, y, z
- Yön ux, uy, uz
- Kinetik enerji veya momentum
- Zaman
- İstatistiksel ağırlık
- Olay / birincil parçacık kimliği (mümkünse)

Dönüşümde birimler, koordinat sistemi, yüzey yönü, parçacık kodları, enerji tanımı, ağırlıklar ve olay korelasyonları korunmalıdır. Bir ROOT veya CSV dosyasının diğer programa otomatik ve doğrudan okutulacağı varsayılmamalıdır; doğrulanmış bir dönüştürücü ya da kullanıcı kaynak tanımı gerekir.

FLUKA, seçilen ayarlara göre parçacık izleri, enerji bırakımı, kaynak parçacıkları, sınır geçişleri ve etkileşimleri collision/phase-space dosyasına kaydedebilir. Geant4 tarafında benzer kayıt, uygulamanın sensitive detector, stepping veya event action koduyla üretilir.

## Bu proje için tavsiye edilen mimari

1. Geant4 ana model: elektron kaynağı → Al folyo → dedektör/scoring düzlemi.
2. Çıktı: olay bazında hedef sonrası x/y hit konumları, enerji, yön, zaman ve ağırlık.
3. ROOT/PyROOT: hit verilerinden histogram, ortalama, standart sapma, belirsizlik ve karşılaştırma grafikleri.
4. FLUKA çapraz kontrolü: aynı beam enerjisi, Al kalınlığı ve geometrik koşullar için bağımsız tahmin.
5. GATE: ancak zaman-bağımlı dedektör yanıtı, görüntüleme veya dozimetri gibi özel bir ihtiyaç ortaya çıkarsa ekle.

## Simülasyon disiplini

- Geant4 ve FLUKA karşılaştırılmadan önce geometri, malzeme, kaynak spektrumu, kesim/threshold ve scoring tanımları eşleştirilmeli.
- Fizik modeli/listesi, sürümler, random seed, olay sayısı ve parametreler kaydedilmeli.
- İki bağımsız Monte Carlo örneklemi aynı rastgele olaylar gibi sunulmamalı.
- Bir kodun ürettiği parçacıklar ikinci koda aktarılırken ilk kodun zaten modellediği malzeme ikinci kez taşınmamalı.
- İki kodun uyuşması tek başına doğruluk kanıtı değildir; deneysel veri veya güvenilir benchmark ile doğrulama gerekir.

## Kaynaklar

- Geant4 kapsamı: https://geant4.web.cern.ch/documentation/dev/intro_html/IntroductionToGeant4/IntroductionToG4.html
- Geant4 geliştirici belgeleri: https://geant4.org/docs/
- Geant4 temel örnekleri: https://geant4.web.cern.ch/documentation/dev/bfad_html/ForApplicationDevelopers/Examples/BasicCodes.html
- FLUKA kapsamı: https://fluka.cern/about
- FLUKA phase-space/collision kayıtları: https://www.fluka.eu/content/manuals/online/7.19.html
- Flair: https://fluka.cern/documentation/running/flair-gui
- OpenGATE: https://opengate-python.readthedocs.io/
- PyROOT: https://root-project.github.io/web/manual/python/

Kaynaklar 17 Kasım 2026 tarihinde kontrol edilmiştir.
