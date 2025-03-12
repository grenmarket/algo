Zadanie Tanie podróże (tan) - Baza zadań - Szkopuł

Kontakt

# Tanie podróże

### Limit pamięci: 32 MB

Pasażerowie autokarów turystycznych, przewożących wycieczki transkontynentalną
autostradą, spędzają w drodze wiele dni, zatem opłaty za noclegi stanowią
poważną część kosztów podróży. Ze względu na bezpieczeństwo jazdy i wygodę
pasażerów każdy autokar jedzie tylko w ciągu dnia i nie może przejechać więcej
niż
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAALAQAAAAHLQht7AAAAAnRSTlMAAQGU/a4AAABBSURBVAiZY3jAAAIPGKYwhDDUMOxhKC9guF7AMHMCg7ECw90DDLYHGGIPgBhAbrGxEYN1dRVDOxBXVlYwWFtbAQBGOBLQgj4T2gAAAABJRU5ErkJggg==)
km dziennie. Noce na trasie (poza jej początkiem i końcem) pasażerowie i
kierowca spędzają w hotelach.

Dotychczas planowano przejazdy tak, by liczba noclegów na trasie była jak
najmniejsza. Dążąc do obniżki kosztów, przedsiębiorstwo przewozowe zdecydowało
zbadać, czy opłaci się układanie planów podróży tak, by suma opłat za noclegi
była możliwie najniższa, nawet gdyby to miało przedłużyć podróż. W tych
obliczeniach można korzystać z ofert hoteli położonych przy autostradzie. W
każdej ofercie jest podana odległość hotelu od początku trasy i cena jednego
noclegu jednej osoby.

Podróż jest tylko w jedną stronę. Trasa nie ma rozgałęzień. Przez każdy punkt
trasy autokar przejeżdża jeden raz. Nigdzie na trasie nie ma dwóch hoteli w
jednym punkcie, więc dla zidentyfikowania hotelu wystarczy podać jego
odległość od początku trasy. Nie planuje się noclegu na początku ani na końcu
trasy. Liczba osób w autobusie nie zmienia się i w każdym hotelu wszyscy
(łącznie z kierowcą) płacą za nocleg jednakowo — zgodnie z ofertą. Pojemność
hoteli jest na tyle duża, że nie istnieje problem braku miejsc. Zawsze można
liczyć na to, że w dowolnej chwili w każdym hotelu będzie wystarczająco dużo
wolnych miejsc, by przenocować wszystkich pasażerów autobusu.

Na każdym odcinku trasy o długości
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAALAQAAAAHLQht7AAAAAnRSTlMAAQGU/a4AAABBSURBVAiZY3jAAAIPGKYwhDDUMOxhKC9guF7AMHMCg7ECw90DDLYHGGIPgBhAbrGxEYN1dRVDOxBXVlYwWFtbAQBGOBLQgj4T2gAAAABJRU5ErkJggg==)
km jest przynajmniej jeden hotel, co oznacza, że przejechanie trasy z
zachowaniem podanych wyżej warunków jest możliwe.

## Zadanie

Napisz program, który:

  * wczytuje ze standardowego wejścia dane: długość trasy, liczbę hoteli oraz oferty hoteli; 
  * znajduje dwa plany podróży: 
    * najtańszej, tzn. takiej, żeby suma opłat za hotele była najmniejsza, a jeśli takich rozwiązań jest wiele, wybiera jedno z najmniejszą liczbą noclegów, 
    * najszybszej, tzn. takiej, żeby liczba noclegów była najmniejsza, a jeśli takich rozwiązań jest wiele, wybiera jedno z najmniejszą sumą opłat za noclegi; 
  * zapisuje wyniki, tj. dwa plany podróży — najtańszej i najszybszej, na standardowe wyjście. 

## Wejście

W pierwszym wierszu standardowego wejścia są zapisane dwie liczby całkowite
dodatnie, oddzielone pojedynczym odstępem: długość trasy
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAAoSURBVAiZY2hgYGCAYBB5gOEBQwGQBaIbGByAtAPDH4YfDLsYjBhKANxsC0WNInA/AAAAAElFTkSuQmCC)
w kilometrach oraz liczba hoteli
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALAQAAAAEd58EeAAAAAnRSTlMAAQGU/a4AAAAtSURBVAiZY2hgYGBoAEMHIOsAwwaGB0CWAcMHBgGGAoYAhgsM94FwLsNuBjMA1yQK3SHRc1oAAAAASUVORK5CYII=),
gdzie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAANAQAAAAG6xk6dAAAAAnRSTlMAAQGU/a4AAACYSURBVAiZNcoxCsJAFATQuYGFB/AIFrlALmGjsCk9gISUuzeIrY05RoRFTGmx7BF+AuldxUKFmHEV/DCPgflgA91gAFYGNTvcY+zSYL5IwTxFHx9CVdsDtD5GS07dGW3Y7LbgiZcOe/ZRpUO0rb5mTOI6Tsgr3ryNWeGcM3hxRqGIGNiBlPWvJiwpD1EKyPmkFN57A/7PfABLH2TrPmagmQAAAABJRU5ErkJggg==)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEMAAAANAQAAAAGt5N5UAAAAAnRSTlMAAQGU/a4AAACKSURBVAiZY3jPwFDTwPCT4R7D9i8NDB//NzDUZzUw2APp30D8GYj33/9feoDhvT2I9P8/55wDg/37PWcaGP7P372fgUGuHkTWg8n4+yDy/n8ZoOw//v9Avff///iv/yytWAHI6v///n1++QKGuf/qoazd/48DWfrmDQxm///Uv3+eXryA4T8UPAAAIBtXT6Z153AAAAAASUVORK5CYII=).

W kolejnych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALAQAAAAEd58EeAAAAAnRSTlMAAQGU/a4AAAAtSURBVAiZY2hgYGBoAEMHIOsAwwaGB0CWAcMHBgGGAoYAhgsM94FwLsNuBjMA1yQK3SHRc1oAAAAASUVORK5CYII=)
wierszach są zapisane oferty hoteli — każda oferta w osobnym wierszu. Są one
uporządkowane według rosnącej odległości hoteli od początku trasy. Każda
oferta jest zapisana w postaci dwóch liczb całkowitych dodatnich oddzielonych
pojedynczym odstępem, pierwsza liczba — to odległość hotelu od początku trasy
w kilometrach, a druga — to cena jednego noclegu w tym hotelu nie większa niż
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAALAQAAAAGqWjk5AAAAAnRSTlMAAQGU/a4AAABFSURBVAiZY3jAcINhA8MBhk8NDFkNDP8hKPYAGM955sCw50wDw+7vDChYBiim/6zYWIHh/fvy7QvgpPn0Bob3z4s3LwAAhicosLMEI+kAAAAASUVORK5CYII=).

## Wyjście

W pierwszym wierszu standardowego wyjścia należy zapisać plan podróży
najtańszej — odległości kolejnych miejsc noclegu od początku trasy. W drugim
wierszu należy — w taki sam sposób — zapisać plan podróży najszybszej. Liczby
w wierszu powinny być pooddzielane pojedynczym odstępem.

## Przykład

Dla danych wejściowych:

    
    
    2000 7
    100 54
    120 70
    400 17
    700 38
    1000 25
    1200 18
    1440 40

poprawną odpowiedzią jest:

    
    
    400 1200 
    400 1200 
    

_Autor zadania: Stanisław Waligórski._

