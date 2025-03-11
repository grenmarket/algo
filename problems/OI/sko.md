Zadanie Skok w bok (sko) - Baza zadań - Szkopuł

Kontakt

# Skok w bok

### Limit pamięci: 32 MB

Plansza do gry „Skok w bok” jest nieskończoną taśmą pól, nieograniczoną
zarówno w lewo jak i w prawo. Na polach planszy stoją pionki. Ich liczba jest
skończona. Na jednym polu może stać równocześnie wiele pionków. Zakładamy, że
pierwsze od lewej pole, na którym jest przynajmniej jeden pionek, ma numer
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAAmSURBVAiZY2hgAIEGBgcgPACEBUA4gUEBzAZBBQYjhiogrGCwAgDG+AmJGHCAfgAAAABJRU5ErkJggg==).
Pola na prawo od niego są oznaczone kolejno liczbami naturalnymi
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAAAOAQAAAAHARxf5AAAAAnRSTlMAAQGU/a4AAABsSURBVAiZJY09DkBQEITnDgrHUEi0bqRRKEgcQeE+9ghOwCt1lK8gxqyX2Xz5stkfRBABIr26ERwRiS1IgveEOSsbWF0TtpsQHOZ4tZPn1ak5WcH2PVwu9rySRE5JVqmL3Utchgc67NEL+8MPIXVeAbTY5AAAAAAASUVORK5CYII=),
a pola w lewo liczbami ujemnymi:
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGUAAAAOAQAAAAFpM99tAAAAAnRSTlMAAQGU/a4AAACZSURBVAiZPU67EcIwDFUFQ1AwCEVGYASGoKCgIJuwBp29ASWVzyk4KCG4sO/s+PFkuBR+H0t6kuAiSJKTIuAtAVZe3vSqCN73kqMqRGQMsizrtCHX7dg9nJWKgCeUJ9z+HMmLsnofmmcuuezG0921WFR6fCj2QD5Dd2vbkc/MLrKvm921xTSXOWSQXQgD06ZfobYaL2wR/ExftdutMPRb2XkAAAAASUVORK5CYII=).
Ustawienie pionków na taśmie, które będziemy także nazywać konfiguracją, można
opisać w ten sposób, że dla każdego pola, na którym jest co najmniej jeden
pionek, podaje się numer pola i liczbę pionków na tym polu.

Są dwa rodzaje ruchów, zmieniających konfiguracje: skok w prawo i skok w lewo.
Skok w prawo polega na zabraniu po jednym pionku z wybranych dwóch sąsiednich
pól o numerach
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKAQAAAAE5eXmFAAAAAnRSTlMAAQGU/a4AAAA0SURBVAiZYzjAcICBgaGB4QGQPMDgwHCBoQPI28CwgGECwweG7QwM7xgYzjUw3G9g4G8AAB0xDWqK8YpAAAAAAElFTkSuQmCC)
oraz
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAOAQAAAAEYS7PzAAAAAnRSTlMAAQGU/a4AAABZSURBVAiZHcmxDYAwDATA7ygzEtksbJARGIF0dEkmoKRlA3BJgfR8LNtn6w3DC1O1BfSe3STZcU4dmdAdwRaRNTVEbNprVd66fs9XhizY0/B2D08uaQgk7Qc3CDvDI2jFzgAAAABJRU5ErkJggg==)
i dodaniu jednego pionka na polu
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAOAQAAAAEYS7PzAAAAAnRSTlMAAQGU/a4AAABcSURBVAiZJYrBEUBAEAT75ykVGZAZGQhBCJ5+5yJQXr5E4C4BN6ao3e3p2hoy/6wD8kL7SW+WyFFFxoK9Q66MvlB3zGtkCv47pfT8vFj6pJ3bbNiUdHGamVpSfgFA+jxHpmxopwAAAABJRU5ErkJggg==).
Skok w lewo: zabieramy jeden pionek z pola
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAOAQAAAAEYS7PzAAAAAnRSTlMAAQGU/a4AAABcSURBVAiZJYrBEUBAEAT75ykVGZAZGQhBCJ5+5yJQXr5E4C4BN6ao3e3p2hoy/6wD8kL7SW+WyFFFxoK9Q66MvlB3zGtkCv47pfT8vFj6pJ3bbNiUdHGamVpSfgFA+jxHpmxopwAAAABJRU5ErkJggg==),
a dodajemy po jednym na polach
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKAQAAAAE5eXmFAAAAAnRSTlMAAQGU/a4AAAA0SURBVAiZYzjAcICBgaGB4QGQPMDgwHCBoQPI28CwgGECwweG7QwM7xgYzjUw3G9g4G8AAB0xDWqK8YpAAAAAAElFTkSuQmCC)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAOAQAAAAEYS7PzAAAAAnRSTlMAAQGU/a4AAABZSURBVAiZHcmxDYAwDATA7ygzEtksbJARGIF0dEkmoKRlA3BJgfR8LNtn6w3DC1O1BfSe3STZcU4dmdAdwRaRNTVEbNprVd66fs9XhizY0/B2D08uaQgk7Qc3CDvDI2jFzgAAAABJRU5ErkJggg==).

Mówimy, że konfiguracja jest końcowa, jeśli na dowolnych dwóch sąsiednich
polach znajduje się co najwyżej jeden pionek. Dla każdej konfiguracji istnieje
dokładnie jedna konfiguracja końcowa, którą można z niej otrzymać w wyniku
skończonej liczby skoków w prawo lub w lewo.

## Zadanie

Ułóż program, który:

  * wczytuje opis konfiguracji początkowej ze standardowego wejścia, 
  * znajduje konfigurację końcową, do jakiej można doprowadzić daną konfigurację początkową i zapisuje wynik na standardowe wyjście. 

## Wejście

W pierwszym wierszu standardowego wejścia jest zapisana jedna liczba całkowita
dodatnia
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC).
Jest to liczba niepustych pól danej konfiguracji początkowej,
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGkAAAANAQAAAAH1m01NAAAAAnRSTlMAAQGU/a4AAAC2SURBVAiZTY4xCsIwGIX/G/QIPYJDBxcRT1JHxw4OHQSbG9TVxVyjICSODqUHEIyFDg5CYynSQmOeqYP4hvfxwRseYUYwhBNdM+qmuqS2RUmb4cKojl4LAlxVlRuAg7+PGSFZJiO5vSHIzyQ19Hq/Iykho7okYef4cmuTkfIg+Ugf3AZuZz3rAU+aoAHQGLHK85yRhu/Uh+iUUk4Nhtjgp0jtHSlEq8KQnPbmgR4iLoqCuZN/YR/Vp5HSits5ywAAAABJRU5ErkJggg==).

W każdym z kolejnych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
wierszy znajduje się opis jednego niepustego pola konfiguracji początkowej w
postaci pary liczb całkowitych oddzielonych odstępem. Pierwsza liczba to numer
pola, a druga — to liczba pionków na tym polu. Te opisy są uporządkowane
rosnąco według numerów pól. Największy numer pola nie przekracza
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAALAQAAAAG5jXnNAAAAAnRSTlMAAQGU/a4AAABNSURBVAiZY/jAsIZhBsMDhjsLGKIWMPx/AELfv94B45nnUhg2nznBsHd/AQoWBorpGz8rNlZgeF/9vnz7AjhV+d58egPDe+vnxZsXAAAYxC4ahDJf2gAAAABJRU5ErkJggg==),
a liczba pionków na żadnym polu nie przekracza
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAOAQAAAAF0TeH2AAAAAnRSTlMAAQGU/a4AAABHSURBVAiZY3jA8IDhABAXMPxh+MBwguEFEP9vYPgHRA8Y/iuAkOkDhu0KDNsfMGx7ACL//zdhOH+4heH93gIg/gPHzYf/AABjTSac5bMi8AAAAABJRU5ErkJggg==).

## Wyjście

W pierwszym wierszu standardowego wyjścia należy zapisać konfigurację końcową,
do której można przekształcić daną konfigurację początkową — numery kolejnych
niepustych pól konfiguracji końcowej. Numery te powinny być uporządkowane
rosnąco. Liczby w wierszu powinny być pooddzielane pojedynczym odstępem.

## Przykład

Dla danych wejściowych:

    
    
    2
    0 5
    3 3
    

poprawną odpowiedzią jest:

    
    
    -4 -1 1 3 5 

_Autor zadania: Bogdan S. Chlebus._

