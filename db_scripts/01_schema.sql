-- Bu dosya, tedarik zinciri veritabanı şemasını oluşturur.

CREATE TABLE Tedarikci (
    tedarikciNo SERIAL PRIMARY KEY,
    tedarikciAdi VARCHAR(100) NOT NULL,
    adres TEXT
);

CREATE TABLE Parca (
    parcaNo SERIAL PRIMARY KEY,
    parcaAdi VARCHAR(100) NOT NULL,
    renk VARCHAR(50),
    agirlik NUMERIC(10, 2),
    depolandigiSehir VARCHAR(50)
);

CREATE TABLE Musteri (
    musteriNo SERIAL PRIMARY KEY,
    musteriAdi VARCHAR(50) NOT NULL,
    musteriSoyadi VARCHAR(50) NOT NULL
);

-- Şimdi ilişki tablolar

-- Katalog tablosu, Tedarikci ve Parca arasında N-N (çoktan çoğa) ilişki kurar.
CREATE TABLE Katalog (
    tedarikciNo INT REFERENCES Tedarikci(tedarikciNo),
    parcaNo INT REFERENCES Parca(parcaNo),
    fiyat NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY (tedarikciNo, parcaNo) -- Bir tedarikçi bir parçayı listeye sadece bir kez ekleyebilir.
);

-- Siparis tablosu, tüm işlemleri bir araya getiren ana işlem tablosudur.
CREATE TABLE Siparis (
    siparis_id SERIAL PRIMARY KEY, -- Her bir sipariş satırını benzersiz yapmak için kendi ID'sini ekledik.
    musteriNo INT REFERENCES Musteri(musteriNo),
    tedarikciNo INT REFERENCES Tedarikci(tedarikciNo),
    parcaNo INT REFERENCES Parca(parcaNo),
    siparisTarihi DATE NOT NULL,
    adet INT NOT NULL
);