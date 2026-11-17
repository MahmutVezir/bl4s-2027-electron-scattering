# Veri toplama ve analiz planı

**Durum:** Önceden tanımlanacak analiz protokolü taslağı; henüz deney verisi yok.

## 1. Deney koşulları

İlk tarama matrisi:

- Momentum: 60, 100, 150 ve 220 MeV/c.
- Al folyo: 100 ve 200 µm.
- Referans: aynı momentum ve aynı dedektör geometrisinde boş tutucu/hedefsiz ölçüm.
- Nominal hedef–Timepix3 mesafesi: 200 mm; CERN onayı bekleniyor.
- Demet: mümkünse bir mikro-bunch/train ve düşük yoğunluk; olay yığılması testi yapılmadan sabitlenmeyecek.

Zaman ve beam-time sınırı nedeniyle tüm kombinasyonlar ancak CERN ekibi yeterli kararlılık ve ölçüm süresi onaylarsa uygulanmalıdır.

## 2. Ölçüm sırası

Her momentum bloğunda aşağıdaki mantık izlenir:

1. Hedefsiz/boş tutucu referansı al.
2. İlk folyo ölçümünü al.
3. Hedefsiz referansı tekrar al.
4. İkinci folyo ölçümünü al.
5. Hedefsiz referansı tekrar al.

Kalınlıkların sırası farklı momentum bloklarında değiştirilerek zamanla oluşabilecek demet kayması etkisi azaltılabilir. Gerçek sıra ve tekrar sayısı, CERN ekibiyle kararlaştırılmalı ve ilk veri alınmadan önce kaydedilmelidir.

## 3. Her koşul için kaydedilecek metadata

- run_id ve UTC zaman damgası
- momentum_mev_c
- target_state: empty_holder / aluminium_100um / aluminium_200um
- folyo üretici/alaşım/kalınlık ve kalınlığın nasıl doğrulandığı
- target_to_sensor_distance_mm
- Timepix3 konfigürasyonu, kalibrasyon ve yazılım/firmware sürümü
- mikro-bunch sayısı, tekrar frekansı ve zayıflatma ayarı
- tetikleme ve DAQ koşulları
- ham piksel hit koordinatları, zaman damgaları ve mevcutsa ToT
- demet merkezi/profil kontrolü ve varsa YAG görüntüsü
- koşul dışı olayların reddedilme nedeni

Ham dosyalar hiçbir zaman işlenmiş tabloların üzerine yazılmamalı; orijinalleri salt okunur saklanmalı ve SHA-256 özeti kaydedilmelidir.

## 4. Birincil ölçüt

Her koşul için x ve y düzlemlerindeki merkezi vuruş dağılımı genişliği ayrı hesaplanır. Merkezi Gauss benzeri bölge ve olası büyük açılı kuyruklar ayrı ele alınır.

Hedef kaynaklı ek genişlik için ilk yaklaşım:

\[
\sigma_{\mathrm{add},x}
=
\sqrt{\sigma_{\mathrm{target},x}^{2}
-
\sigma_{\mathrm{reference},x}^{2}}
\]

Aynı ifade y için de uygulanır. Farkın karesi sıfırdan küçük veya istatistiksel olarak ayırt edilemez çıkarsa, bu durum “ölçülemedi/çözülemedi” olarak raporlanır; yapay biçimde pozitif sonuç üretilmez.

Bu çıkarma, hedef ve referans dağılımlarının bağımsız genişleme bileşenleri olduğu, dedektör/beam koşullarının karşılaştırılabilir kaldığı varsayımına dayanır. Beam drift, kesilmiş sensör alanı, hedef hizalaması veya non-Gaussian kuyruklar bu varsayımı bozabilir.

## 5. İkincil ölçütler

- x ve y eksenlerinin ayrı karşılaştırması
- merkezi dağılımın %98'lik bölgesine göre genişlik
- merkezi modele göre dışarıda kalan kuyruk olaylarının oranı
- hedef kalınlığına ve momentumuna göre trend
- her koşulun tekrarları arasındaki kararlılık

## 6. İstatistik ve belirsizlik

Belirsizlik bütçesi en az şunları içermelidir:

- sınırlı olay sayısından gelen istatistiksel belirsizlik
- 55 µm piksel adımı ve piksel kümelendirme/konum kalibrasyonu
- demet merkezi ve profili değişimi
- hedef kalınlığının ve malzeme özelliklerinin belirsizliği
- hedef–sensör mesafesi ve hizalama belirsizliği
- olay yığılması, dead-time ve tetik verimi
- elektron enerji kaybı/bremsstrahlung ve teorik model farkı

Tek bir ölçümden kesin sonuç çıkarılmamalı. Tekrarlar ayrı saklanmalı, birleştirilmeden önce tutarlılıkları değerlendirilmelidir.

## 7. Sonuç raporlama ilkesi

Gerçek deney verisi oluşana kadar grafikler ve tablolar “teorik ön tahmin” veya “test verisi” etiketiyle işaretlenmelidir. Sentetik veri gerçek CERN verisi olarak sunulamaz. Ölçüm yoksa sonuç bölümü yerine “ölçüm yapılmadı; deneysel hipotez test edilmedi” denmelidir.
