1. Uruchomienie wtyczki
- Pobieramy folder z wtyczką z rozszerzeniem .zip
- Otwieramy program Qgis
- Znajdujemy w górnym pasku Wtyczki -> Zarządzanie wtyczkami -> Instaluj z pliku ZIP (Załączamy folder ZIP z wtyczką i klikamy zainstaluj wtyczkę)
- Następnie po poprawnym zainstalowaniu powinna się pojawić jej ikonka na pasku
2. Import warstw w pliku txt
- W celu poprawnego działania wtyczki niezbędne jest odpowiednia kolejność importowanych danych (nr;x92;y92), nasza wtyczka pobiera współrzędne z tabeli atrybutów warstwy
- Przykład poprawnej kolejności :
- 1;672600;352600;198.34	
- 2;672700;352600;197.49	
- 3;672800;352600;199.61	
- 4;672500;352700;185.96
- Warstwa -> Dodaj warstwę -> Dodaj warstwę tekstową CSV
3. Uwagi dotyczące importu
- Ustawiamy format pliku na "średnik"
- W sekcji przykładowe dane współrzędna X i Y przyjmuje  typ "Integer 64bit", a wysokosć H "Decimal Double"
- Po wykonaniu powyższych czynności wszystkie punkty powinny zostać zaimportowane prawidłowo.
4. Działanie wtyczki
- Kliknięcie przycisku Zlicz wyświetla się ilość obiektów znajduj¡cych się w wybranej warstwie.
-  Jeżeli chcemy obliczyć różnicę wysokości wybieramy 2 punkty dla których chcemy policzyć dH i klikamy przycisk ObliczdH
-  Taka sama sytuacja występuje przy liczeniu pola, wybieramy min. 3 punkty, w przeciwnym razie będzie występował komunikat informujący o błędzie oraz co należy zrobić, aby obliczenia wyszły poprawnie
5. Jednostki wyjściowe
- Dla obliczonych przewyższeń -> wynik w metrach
- Dla obliczonego pola -> wynik w metrach
