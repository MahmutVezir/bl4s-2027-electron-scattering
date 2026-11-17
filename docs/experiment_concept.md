# Deney fikri — ince alüminyum folyoda elektronların çoklu Coulomb saçılması

**Durum:** Ön fizibilite; CERN tarafından onaylanmış bir deney tasarımı değildir.

## Çalışma başlığı

**İnce alüminyum folyolardan geçen elektron demetinin enine vuruş dağılımının momentumla değişimi**

## Araştırma sorusu

Sabit kalınlıktaki ince bir alüminyum folyodan geçen CLEAR elektron demetinin, folyodan sonraki Timepix3 düzleminde ölçülen merkezi iki boyutlu konum dağılımı genişliği, elektron momentumu değiştikçe nasıl değişir?

İkincil soru: aynı momentumda folyo kalınlığı artırıldığında hedef kaynaklı ek genişleme artıyor mu?

## Hipotezler

1. Aynı folyo ve aynı geometri için momentum yükseldikçe hedef kaynaklı merkezi dağılım genişliği azalır.
2. Aynı momentumda daha kalın folyo, daha büyük saçılma genişliği üretir.
3. Hedef yokken ölçülen referans dağılımı çıkarıldığında, hedef kaynaklı genişleme ilk yaklaşımda çoklu saçılma teorisiyle uyumlu bir momentum/kalınlık eğilimi gösterir.

Bunlar test edilecek hipotezlerdir; elde edilmiş sonuç değildir.

## Önerilen ilk ölçüm matrisi

| Parametre | Ön seçim | Gerekçe / durum |
|---|---:|---|
| Parçacık | Elektron | CLEAR 2027 için yayımlanan parçacık türü |
| Momentum | 60, 100, 150, 220 MeV/c | 60–220 MeV/c iki resmi belgede de ortak aralık; 50 MeV/c alt sınırı ayrıca açıklığa kavuşturulacak |
| Hedef | Alüminyum folyo | Yanıcı/biolojik olmayan basit metal; hedef ve tutucu CERN onayına tabi |
| Hedef kalınlığı | 100 ve 200 µm | Ön hesaplama için seçilmiş aday değerler; tedarik ve izin doğrulanmadı |
| Referans | Hedef yok / boş tutucu | Demetin kendi genişliğini ve cihaz tabanını belirlemek için |
| Birincil dedektör | Timepix3 + Katherine okuma sistemi | CLEAR fizibilite föyünde listeleniyor |
| Hedef–dedektör mesafesi | 200 mm varsayımı | Yalnızca ilk ölçek hesabı; CERN yerleşim onayı bekliyor |

50 MeV/c, genel Beams & Detectors PDF'sinde verilen 60 MeV/c alt sınırıyla çeliştiği için ön tasarımda kullanılmıyor. CERN 50 MeV/c kullanımını teyit ederse matris güncellenebilir.

## Düzenek taslağı

Elektron demeti → çıkarılabilir ince Al folyo tutucu → yaklaşık 200 mm aşağı akışta Timepix3 düzlemi → Katherine okuma sistemi.

YAG ekranı ve kamera, uygun bir konuma yerleştirilebiliyorsa hizalama ve demet profili kontrolü için ayrı referans ölçümlerinde kullanılabilir. YAG ekranının aynı anda veya belirli konumlarda kullanılabileceği henüz doğrulanmadı.

Timepix3'nin 256 × 256 piksel ve 55 µm piksel adımı, yaklaşık 14.08 mm × 14.08 mm aktif alan verir. Demetin ve saçılan parçacıkların bu alan içinde kalıp kalmayacağı, deney alanındaki gerçek demet profili ve hedef–sensör uzaklığıyla doğrulanmalıdır.

**Ölçüm iddiasının sınırı:** tek Timepix3 düzlemi parçacığın o düzlemdeki vuruş koordinatını ve zaman bilgisini sağlar. Tek başına giriş ve çıkış izini yeniden kurmaz; bu tasarım doğrudan saçılma açısı ölçümü diye adlandırılmamalıdır. Temel gözlem, hedef varken ve yokken aşağı akış vuruş dağılımının genişliğindeki değişimdir.

## Demet koşulu

CLEAR föyü, demetin ortalama olarak her bunch başına tek elektrona kadar zayıflatılabileceğini ve 1–150 mikro-bunch/train seçeneği olduğunu bildirir. Başlangıç tasarımında, Timepix3'te üst üste binen çoklu izleri sınırlamak için tek mikro-bunch/train ve düşük yoğunluk düşünülmektedir. Bu ayarın gerçekten uygulanabildiği, Timepix3 zaman çözünürlüğüyle uyumu ve olay kümesi ayrımı CERN ekibi tarafından teyit edilmelidir.

## Değişkenler

- **Bağımsız değişkenler:** momentum, Al folyo kalınlığı, hedefin var/yok durumu.
- **Bağımlı değişken:** Timepix3 düzlemindeki merkezi x/y vuruş dağılımı genişliği; hedef kaynaklı ek genişlik.
- **Kontrol edilmesi gerekenler:** hedef–sensör uzaklığı, sensör yönelimi, demet odak/konumu, bunch sayısı, bunch yükü/zayıflatma, tetik/DAQ ayarı, sensör kalibrasyonu ve ölçüm sırası.

## İlk hesaplamanın kapsamı

\`physics/scattering_estimates.py\`, PDG Lynch–Dahl küçük-açı çoklu saçılma ifadesini kullanarak merkezi dağılım için ilk mertebe açısal RMS tahmini ve seçilen sensör mesafesindeki yaklaşık konumsal genişlemeyi hesaplar.

Hesaplama gerçek bir demet simülasyonu değildir. Elektronların enerji kaybı, bremsstrahlung, büyük açılı kuyruklar, sensör yanıtı, demet optiği ve hedef saçılma noktasının konumu tam modellenmemiştir. Bu sebeple yalnızca ölçümün büyüklük mertebesini ve olası çözünürlük ihtiyacını tartışmak içindir.

## Deneyin tamamlanmış sayılması için gerekenler

1. CERN ekibinden Timepix3, hedef tutucu, mesafe, düşük yoğunluk ve demet parametrelerine ilişkin yazılı yanıt.
2. Gerçek CLEAR geometrisine göre güncellenmiş düzenek çizimi.
3. Elektron taşınımı ve sensör yanıtını içeren Geant4 veya eşdeğer bir Monte Carlo ön çalışması.
4. Hedefsiz referans, hedefli koşul ve tekrarlar için önceden tanımlı veri toplama/analiz protokolü.
5. Ancak BL4S seçilirse laboratuvarda alınacak gerçek ölçüm verileri.
