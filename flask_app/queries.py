


EN_COK_SİPARİS_VEREN="""SELECT
p.parcaadi,
m.musteriadi,   
m.musterisoyadi,
Toplamlar.toplam_adet
FROM
(
SELECT
parcaNo,
musteriNo,
SUM(adet) AS toplam_adet
FROM Siparis
GROUP BY parcaNo, musteriNo
) AS Toplamlar
JOIN Musteri m ON Toplamlar.musteriNo = m.musteriNo
JOIN Parca p ON Toplamlar.parcaNo = p.parcaNo
WHERE
Toplamlar.toplam_adet = (
SELECT MAX(T2.toplam_adet)
FROM (
SELECT parcaNo, SUM(adet) AS toplam_adet
FROM Siparis
GROUP BY parcaNo, musteriNo
) AS T2
WHERE T2.parcaNo = Toplamlar.parcaNo
);"""

RENK_SORGUSU_ISKELETI = """
SELECT
    m.musteriadi,
    m.musterisoyadi,
    p.parcaadi,
    p.renk
FROM Musteri m
JOIN Siparis s ON m.musterino = s.musterino
JOIN Parca p ON s.parcano = p.parcano
WHERE p.renk IN %s
ORDER BY m.musteriadi, p.parcaadi;
"""


TEK_TEDARIKCILI_URUN_SIPARISLERI = """
SELECT
    s.siparisTarihi,
    s.adet,
    -- Parça adını bir alt sorgu ile al
    (SELECT p.parcaAdi FROM Parca p WHERE p.parcaNo = s.parcaNo) AS parcaAdi,
    -- Tedarikçi adını bir alt sorgu ile al
    (SELECT t.tedarikciAdi FROM Tedarikci t WHERE t.tedarikciNo = s.tedarikciNo) AS tedarikciAdi
FROM
    Siparis s
WHERE
    s.parcaNo IN (
        -- Ana filtre: Sadece 1 tedarikçisi olan parçaları bul
        SELECT parcaNo
        FROM Katalog
        GROUP BY parcaNo
        HAVING COUNT(tedarikciNo) = 1
    )
ORDER BY
    s.siparisTarihi DESC;
"""

ORTALAMA_USTU_FIYAT_SORGUSU = """
SELECT
    T.tedarikciAdi,
    P.parcaAdi,
    K.fiyat
FROM Katalog K
JOIN Tedarikci T ON T.tedarikciNo = K.tedarikciNo
JOIN Parca P ON K.parcaNo = P.parcaNo
JOIN (
    SELECT
        parcaNo,
        AVG(fiyat) AS ortalama_fiyat
    FROM Katalog
    GROUP BY parcaNo
) AS Ortalamalar ON K.parcaNo = Ortalamalar.parcaNo
WHERE
    K.fiyat > Ortalamalar.ortalama_fiyat
ORDER BY P.parcaAdi, K.fiyat DESC;
"""
