# Geant4 ↔ FLUKA faz-uzayı arayüzü — tasarım notu

## Amaç

Geant4 ve FLUKA'yı tek bir simülasyon motoru gibi birleştirmek değil; gerekirse bir simülasyonun belirli bir sınır yüzeyindeki parçacık durumlarını diğer simülasyona kontrollü biçimde aktarmak veya iki kodu bağımsız karşılaştırmak.

## Önerilen ortak parçacık kaydı

| Alan | Anlam | Önerilen birim/biçim |
|---|---|---|
| event_id | Olay kimliği | integer |
| track_id | İz kimliği | integer |
| pdg_code | Parçacık türü | PDG integer |
| x, y, z | Konum | mm |
| ux, uy, uz | Birim yön vektörü | boyutsuz |
| kinetic_energy | Kinetik enerji | MeV |
| global_time | Olay zamanı | ns |
| weight | İstatistiksel ağırlık | boyutsuz |
| surface_id | Kayıt yüzeyi | string/integer |

Momentum veya toplam enerji de tutulacaksa kinetik enerjiyle karıştırılmamalı. Kayıt yüzeyinin konumu, normali ve koordinat sistemi ayrıca metadata dosyasında tanımlanmalıdır.

## Dönüştürücüde yapılması gereken kontroller

- Geant4 ve FLUKA koordinat eksenlerinin aynı yönde tanımlandığını doğrula.
- mm/cm, MeV/GeV ve ns/s dönüşümlerini açıkça uygula.
- PDG kodlarını hedef programın parçacık tanımlarıyla eşleştir.
- Yön vektörünün normunu kontrol et.
- Enerji ve momentum tanımlarını karıştırma.
- İstatistiksel ağırlığı koru; ağırlıklı örneklemde belirsizlik hesabını buna göre yap.
- Olay korelasyonları gerekiyorsa event_id/track_id bilgisini kaybetme.
- Yüzeyin bir tarafına geçen parçacıkların yönünü ve işaretini doğrula.
- Dosya başlığına yazılım sürümü, seed, kaynak koşulları ve geometri hash/versiyonunu ekle.

## İki güvenli kullanım biçimi

### A. Bağımsız karşılaştırma — önerilen ilk yöntem

Aynı geometri, kaynak ve gözlenebilir Geant4 ve FLUKA'da ayrı ayrı modellenir. Ortalama enerji bırakımı, merkezi saçılma genişliği veya başka bir uygun scoring sonucu istatistiksel belirsizliklerle karşılaştırılır. Bu, dosya dönüştürücü karmaşıklığı olmadan kodlar arası çapraz kontrol sağlar.

### B. Sınır yüzeyinde aktarım

Örneğin Geant4'te hedefe kadar taşınan parçacıklar bir yüzeyde kaydedilir; bu kayıt FLUKA için kaynak girdisine dönüştürülür. Tersi yön de teorik olarak benzer şekilde tasarlanabilir. Ancak bu otomatik, tek tıklamalı bir bağlantı değildir: FLUKA'nın kullanıcı kaynak tanımı veya uygun phase-space okuma yöntemi ve Geant4'ün olay kaydı kodlanmalıdır.

## Fiziksel çift sayımı önleme

Geant4'te Al folyo içinden geçmiş parçacığı FLUKA'ya aktarırken FLUKA geometrisinde aynı Al folyo yeniden taşınırsa, hedef etkileşimi iki kez modellenmiş olur. Aktarım yüzeyi ve hangi malzemenin hangi motorda modellendiği kesin tanımlanmalıdır.

## BL4S projesi için karar

Şimdilik Geant4'ü ana motor, FLUKA'yı ileride bağımsız çapraz kontrol olarak konumlandır. İlk öğrenme aşamasında iki motoru dosya alışverişiyle bağlamaya çalışma. Önce tek motorla basit ve doğrulanabilir sonuç üret; ardından FLUKA ile aynı gözlenebiliri karşılaştır.
