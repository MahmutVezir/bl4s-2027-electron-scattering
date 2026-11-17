# Sentetik veri analizi — yöntem ve yorum sınırları

## Veri kaynağı

example_hits.csv, sabit bir tohumla üretilmiş 480 adet sentetik x-konumu içerir:
- 240 no-target reference örneği
- 240 aluminium foil örneği

İki koşul için örnekler farklı normal dağılımlardan üretilmiştir. Bu nedenle alüminyum koşulunun daha geniş çıkması, üretim tasarımının beklenen özelliğidir; fiziksel bir keşif veya deneysel kanıt değildir.

## İstatistik tanımları

Örnek ortalama:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

Örnek standart sapma (yansız varyans kestirimi, ddof=1):

\[
s=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
\]

Ortalamanın standart hatası:

\[
SEM=\frac{s}{\sqrt{n}}
\]

Standart sapma örneklerin yayılımını, SEM ise ortalama kestiriminin örnekleme belirsizliğini özetler. SEM, tekil olayların dağılım genişliği veya tüm deney belirsizliği değildir.

## Bu örnek için özet

| Koşul | n | Ortalama x (mm) | Örnek SD (mm) | SEM (mm) |
|---|---:|---:|---:|---:|
| Hedefsiz referans | 240 | 0.124837 | 0.396792 | 0.025613 |
| Alüminyum folyo (sentetik) | 240 | -0.017438 | 0.687532 | 0.044380 |

## Grafikler

- Histogram: ../figures/synthetic_hit_histograms.svg
- Ortalama ve SEM: ../figures/synthetic_mean_errorbars.svg

## Yorum

Bu sentetik örnekte alüminyum koşulunun örnek standart sapması daha büyüktür. Ancak bu, yalnızca veri üretim parametrelerinin tasarlanmış sonucudur. Gerçek BL4S deneyinde beam spot, demet divergence, hizalama, dedektör yanıtı, kesilmiş aktif alan, olay yığılması, enerji kaybı ve sistematik belirsizlikler hesaba katılmadan aynı yorum yapılamaz.
