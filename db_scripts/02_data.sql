



INSERT INTO Tedarikci (tedarikciAdi, adres) VALUES
('OtoParça A.Ş.', 'Kocaeli Sanayi Sitesi No:12'),
('Vida Dünyası Ltd.', 'İstanbul İkitelli OSB'),
('Elektronik Market', 'Ankara Ostim Sanayi');


INSERT INTO Tedarikci (tedarikciAdi, adres) VALUES
('Bursa Rulman', 'Bursa Nilüfer OSB'),
('İzmir Hidrolik', 'İzmir Pınarbaşı Sanayi');


INSERT INTO Parca (parcaAdi, renk, agirlik, depolandigiSehir) VALUES
('Motor Pistonu', 'Gümüş', 1.20, 'Kocaeli'),
('M5 Civata', 'Siyah', 0.01, 'İstanbul'),
('Fren Balatası', 'Siyah', 0.80, 'Kocaeli'),
('LED Far Ampülü', 'Beyaz', 0.15, 'Ankara');


INSERT INTO Parca (parcaAdi, renk, agirlik, depolandigiSehir) VALUES
('Teker Rulmanı', 'Metalik', 0.60, 'Bursa'),
('Hidrolik Pompa', 'Gri', 4.50, 'İzmir'),
('Hava Filtresi', 'Sarı', 0.40, 'Kocaeli'),
('Yağ Filtresi', 'Mavi', 0.50, 'Kocaeli');


INSERT INTO Musteri (musteriAdi, musteriSoyadi) VALUES
('Ali', 'Vural'),
('Zeynep', 'Güneş'),
('Osman', 'Yıldırım');

INSERT INTO Musteri (musteriAdi, musteriSoyadi) VALUES
('Hasan', 'Çelik'),
('Elif', 'Aksoy');


INSERT INTO Katalog (tedarikciNo, parcaNo, fiyat) VALUES
(1, 1, 450.00), -- OtoParça A.Ş., Motor Pistonu satıyor
(1, 3, 220.50), -- OtoParça A.Ş., Fren Balatası satıyor
(2, 2, 0.50),   -- Vida Dünyası, M5 Civata satıyor
(3, 4, 150.75); -- Elektronik Market, LED Far Ampülü satıyor


INSERT INTO Katalog (tedarikciNo, parcaNo, fiyat) VALUES
(1, 7, 75.00),  -- OtoParça A.Ş., Hava Filtresi satıyor
(1, 8, 90.00),  -- OtoParça A.Ş., Yağ Filtresi satıyor (1. Tedarikçi)
(4, 5, 180.00), -- Bursa Rulman, Teker Rulmanı satıyor
(4, 8, 85.50),  -- Bursa Rulman, Yağ Filtresi satıyor (2. Tedarikçi, daha ucuz)
(5, 6, 2300.00);-- İzmir Hidrolik, Hidrolik Pompa satıyor


INSERT INTO Siparis (musteriNo, tedarikciNo, parcaNo, siparisTarihi, adet) VALUES
(1, 1, 1, '2025-07-20', 4),  -- Ali Vural, OtoParça'dan 4 piston sipariş etti
(2, 3, 4, '2025-07-21', 2),  -- Zeynep Güneş, Elektronik Market'ten 2 LED ampül sipariş etti
(1, 2, 2, '2025-07-22', 500);-- Ali Vural, Vida Dünyası'ndan 500 civata sipariş etti


INSERT INTO Siparis (musteriNo, tedarikciNo, parcaNo, siparisTarihi, adet) VALUES
(3, 1, 3, '2025-07-23', 2),  -- Osman Yıldırım, OtoParça'dan 2 fren balatası sipariş etti
(4, 4, 5, '2025-07-24', 4),  -- Hasan Çelik, Bursa Rulman'dan 4 teker rulmanı sipariş etti
(5, 4, 8, '2025-07-25', 10), -- Elif Aksoy, Bursa Rulman'dan (ucuz olan) 10 yağ filtresi sipariş etti
(1, 1, 7, '2025-07-26', 3),  -- Ali Vural, OtoParça'dan 3 hava filtresi sipariş etti
(2, 5, 6, '2025-07-27', 1);  -- Zeynep Güneş, İzmir Hidrolik'ten 1 hidrolik pompa sipariş etti
