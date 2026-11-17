# ROOT ve PyROOT — kısa uygulama notu

ROOT, parçacık fiziğinde olay verisi, histogram, ntuple, grafik ve istatistik için kullanılan C++ analiz çatısıdır. PyROOT, ROOT'un C++ sınıflarına Python içinden erişim sağlar; böylece Python akışıyla TH1D, TFile ve TCanvas gibi ROOT nesneleri kullanılabilir.

Bu depodaki analysis/pyroot_histogram.py dosyası:
1. Sentetik CSV dosyasını okur.
2. Hedefsiz referans ve alüminyum koşulları için iki TH1D histogramı doldurur.
3. Histogramları PNG olarak çizer.
4. Histogramları bir ROOT dosyasına yazar.

Çalıştırma:

    python analysis/pyroot_histogram.py

Komut, ROOT ve PyROOT'un etkin olduğu bir Python ortamında çalıştırılmalıdır. Her işletim sisteminde sıradan pip komutuyla ROOT kurulacağı varsayılmamalı; resmi ROOT kurulum yönergesi izlenmelidir.

Bu betik burada çalıştırılmadı. Çalıştırma kanıtı oluşmadan “PyROOT uygulaması başarıyla çalıştı” denmemelidir.

Kaynaklar:
- https://root-project.github.io/web/manual/python/
- https://root.cern/doc/master/group__tutorial__hist.html
