# Geant4 çalışma notu — elektron, alüminyum ve dedektör düzlemi

## Geant4 ne yapar?

Geant4, parçacıkların maddeden geçişini Monte Carlo yöntemiyle modellemek için kullanılan C++ tabanlı bir araç takımıdır. Kullanıcı uygulaması; geometriyi, malzemeleri, birincil parçacık kaynağını, fizik süreçlerini, parçacık izlemeyi, hassas dedektörleri, olay çıktısını ve görselleştirmeyi tanımlar.

## Bir Geant4 uygulamasının ana bileşenleri

1. **Detector construction:** Dünya hacmi, hedef, destek malzemeleri ve dedektör düzlemlerinin geometrisi.
2. **Materials:** Alüminyum folyo ve sensör/support malzemelerinin yoğunluk ve bileşim tanımları.
3. **Primary generator:** Elektron parçacık türü, momentum/enerji, başlangıç konumu ve yön dağılımı.
4. **Physics list:** Elektromanyetik etkileşimler, saçılma, iyonizasyon ve bremsstrahlung gibi süreçlerin seçimi.
5. **Sensitive detector / scoring:** Dedektör düzleminden geçen parçacıkların hit koordinatı, enerji ve zaman bilgilerinin kaydı.
6. **Run/event actions:** Olay sayısı, istatistik ve çıktı dosyalarının düzenlenmesi.
7. **Analysis/output:** ROOT, CSV veya başka bir açık biçimde olay/hit verisinin saklanması.

## BL4S örnek mekanizmasına uyarlama

Geometri taslağı:

- Dünya hacmi (vakum veya uygun ortam)
- İnce alüminyum hedef
- Hedefin aşağı akışında ince bir scoring düzlemi
- Elektron birincil kaynağı

İlk simülasyon soruları:

- Hedef yokken scoring düzlemindeki x/y dağılımı nedir?
- Al hedef eklendiğinde dağılım genişliği nasıl değişir?
- Momentum ve folyo kalınlığı değişince merkezi hit dağılımı nasıl değişir?
- Enerji kaybı ve bremsstrahlung katkıları hangi koşullarda önem kazanır?

Tek scoring düzlemi ile tek tek parçacıkların saçılma açısını ölçtüğümüz söylenmemelidir. Açı ölçümü için hedef öncesi ve sonrası yön/iz bilgisi gerekir. Bu örnekte hedef sonrası konum dağılımı ve hedefsiz referans karşılaştırılır.

## Öğrenme sırası

1. Geant4 Basic Example B1: basit geometri, malzeme, kaynak ve scoring kavramları.
2. Basic Example B2: tracker geometry, magnetic field ve sensitive detector/hits.
3. Kendi uygulamamızda elektron kaynağı ve alüminyum folyo.
4. Scoring düzleminden hit koordinatlarını dışa aktarma.
5. ROOT/PyROOT ile histogram ve belirsizlik analizi.

Resmi dokümantasyon başlangıç için Application Developer Guide ve Basic Examples sayfalarını önerir. Bu depo için önce B1/B2 örneklerini anlamak, doğrudan büyük bir simülasyon yazmaya çalışmaktan daha verimlidir.

## Şu anki durum

Bu not kavramsal incelemedir. Bu depoda henüz derlenmiş veya çalıştırılmış bir Geant4 uygulaması yoktur. Geant4 kurulumu ve C++ derlemesi, uygun bilgisayar/Linux ortamı gerektirir.

## Kaynaklar

- https://geant4.org/docs/
- https://geant4.web.cern.ch/documentation/dev/intro_html/IntroductionToGeant4/IntroductionToG4.html
- https://geant4.web.cern.ch/documentation/dev/bfad_html/ForApplicationDevelopers/Examples/BasicCodes.html
