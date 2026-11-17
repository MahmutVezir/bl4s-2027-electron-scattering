# Fizik temeli ve yaklaşık hesap

## Çoklu Coulomb saçılması

Yüklü bir parçacık maddeden geçerken atom çekirdeklerinin Coulomb alanlarıyla çok sayıda küçük açılı saçılmaya uğrar. Birçok küçük saçılmanın toplamı dağılımın merkezinde yaklaşık Gauss biçimine yaklaşabilir. Daha seyrek büyük açılı saçılmalar Gauss dışı kuyruklar üretir.

Particle Data Group (PDG), merkezi %98'lik izdüşürülmüş açısal dağılım için Lynch–Dahl yaklaşık ifadesini verir:

\[
\theta_0 =
\frac{13.6\,\mathrm{MeV}}{\beta c p}|z|
\sqrt{\frac{x}{X_0}}
\left[
1+0.038\ln\left(
\frac{x z^2}{X_0\beta^2}
\right)
\right]
\]

Burada:

- \(\theta_0\): tek izdüşürülmüş düzlemde merkezi dağılımın açısal RMS genişliği
- \(p\): gelen parçacığın momentumu
- \(\beta c\): parçacık hızı
- \(z\): temel yük birimi cinsinden yük sayısı; elektron için \(|z|=1\)
- \(x\): malzemenin kütle kalınlığı
- \(X_0\): radyasyon uzunluğu

Momentum MeV/c cinsinden girildiğinde hesaplamada \(c=1\) birim geleneği kullanılır. Elektron için \(\beta=p/\sqrt{p^2+m_e^2}\), \(m_ec^2=0.51099895\) MeV.

PDG, bu ifadenin Molière dağılımının merkezi %98'ine yönelik bir Gauss yaklaşımı olduğunu; küçük açılar ve büyük açılı saçılmaların bulunmadığı durumda nicel tahminlerin geçerli olduğunu belirtir. Bu sebeple merkezi genişlik ve kuyruklar ayrı raporlanmalıdır.

## Alüminyum malzeme girdileri

PDG Atomic and Nuclear Properties of Materials tablosu:

- Yoğunluk: 2.699 g/cm³
- Kütle radyasyon uzunluğu: 24.01 g/cm²
- Uzunluk cinsinden radyasyon uzunluğu: yaklaşık 8.897 cm
- Elektron kritik enerjisi: 42.70 MeV

Kalınlık 100 µm olduğunda:

\[
x = \rho t = 2.699 \times 0.0100
= 0.02699\ \mathrm{g/cm^2}
\]

\[
x/X_0 \approx 0.02699/24.01
\approx 1.124\times10^{-3}
\]

200 µm folyo için oran bunun iki katıdır.

## Ön tahminler

Aşağıdaki tahminler Lynch–Dahl ifadesiyle, 200 mm hedef–dedektör uzaklığı varsayılarak hesaplanmıştır. Küçük açı yaklaşımında konumsal ölçek yaklaşık \(s \approx L\theta_0\) olur.

| Momentum (MeV/c) | Al 100 µm: \(\theta_0\) (mrad) | 100 µm: \(L\theta_0\) (mm) | Al 200 µm: \(\theta_0\) (mrad) | 200 µm: \(L\theta_0\) (mm) |
|---:|---:|---:|---:|---:|
| 60 | 5.639 | 1.128 | 8.258 | 1.652 |
| 100 | 3.383 | 0.677 | 4.954 | 0.991 |
| 150 | 2.255 | 0.451 | 3.303 | 0.661 |
| 220 | 1.538 | 0.308 | 2.252 | 0.450 |

Bu değerler sensörde gözlenecek toplam genişlik değildir. Sensörün göreceği dağılım; başlangıç demet profili, beam divergence, hedefin içindeki saçılma konumu, hedef–sensör uzaklığı, sensör yanıtı ve enerji kaybının birleşimidir. Hedefsiz referans ölçümü bu yüzden zorunludur.

## Elektronlara özgü dikkat

CLEAR demetindeki parçacıklar elektrondur. PDG, elektron ve pozitronların enerji kaybında Møller/Bhabha saçılması ve bremsstrahlung gibi süreçlerin bulunduğunu, bremsstrahlung kayıplarının kritik enerjinin üzerinde önemli hâle geldiğini açıklar. Alüminyumun elektron kritik enerjisi yaklaşık 42.70 MeV olduğundan 60–220 MeV/c aralığında enerji kaybı ve bremsstrahlung ihmal edilmemelidir.

Önerilen ince folyoların \(x/X_0\) oranı küçük tutulmuştur; bu yalnızca katkıyı azaltmaya yöneliktir. Hesaplama tam elektron taşınımı simülasyonu yerine geçmez. Başvuru öncesinde mümkünse Geant4 veya eşdeğer bir Monte Carlo çalışmasıyla kontrol edilmelidir.

## Tek Timepix3 ile ölçümün sınırı

Bu tasarım, tek sensör düzlemindeki hit koordinatlarının hedefli/hedefsiz koşullardaki dağılım genişliğini karşılaştırır. Sensör öncesi ve sonrası iz ölçümü olmadığı için parçacığın tek tek saçılma açısını doğrudan vermemektedir. Bu sınıra uygun bilimsel ifade kullanılmalıdır.
