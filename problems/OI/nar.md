Zadanie Narciarze (nar) - Baza zadań - Szkopuł

Kontakt

# Narciarze

### Limit pamięci: 32 MB

Drużyna narciarska organizuje trening na Bajtogórze. Na północnym stoku góry
znajduje się jeden wyciąg. Wszystkie trasy prowadzą od górnej do dolnej stacji
wyciągu. W trakcie treningu członkowie drużyny będą razem startować z górnej
stacji wyciągu i spotykać się przy dolnej stacji. Poza tymi dwoma punktami
trasy zawodników nie mogą się przecinać, ani stykać. Wszystkie trasy muszą
cały czas prowadzić w dół.

Mapa tras narciarskich składa się z sieci polan połączonych przecinkami. Każda
polana leży na innej wysokości. Dwie polany mogą być bezpośrednio połączone co
najwyżej jedną przecinką. Zjeżdżając od górnej do dolnej stacji wyciągu można
tak wybrać drogę, żeby odwiedzić dowolną polanę (choć być może nie wszystkie w
jednym zjeździe). Trasy narciarskie mogą się przecinać tylko na polanach i nie
prowadzą przez tunele, ani estakady.

## Zadanie

Napisz program, który:

  * wczyta ze standardowego wejścia mapę tras narciarskich, 
  * wyznaczy maksymalną liczbę zawodników, którzy mogą brać udział w treningu, 
  * wypisze wynik na standardowe wyjście. 

## Wejście

W pierwszym wierszu standardowego wejścia znajduje się jedna liczba całkowita
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
równa liczbie polan,
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGEAAAANAQAAAAHmTA25AAAAAnRSTlMAAQGU/a4AAACsSURBVAiZTY5BCoJAGIXfDTzCHCOCsFO0tSMUtCgQmrmBazd6jgj0AmKrVtG4cCEUGOJCQflfQ6ve5uNbfPDAEzhCGzz3GBaOfU+DcHqh3W2geUddEzplOl0NqLf64aik4qowWH/YXmJUOTNpYcUXv0V2Fu2MSZ44KKZcxhBPPBIHdiQ7UUXh8pDKmRJaaw2GmdNxpjQ/uzGShhEHGwTAxHF+c5SmLEt342/mC4ypgna+i6oZAAAAAElFTkSuQmCC).

W każdym z kolejnych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAALAQAAAAGnREl+AAAAAnRSTlMAAQGU/a4AAABCSURBVAiZY/jBAIH7DzD8Z2CwB6P//xcw7GdfwPD8P4jtAMQHGPiBeB3/ATA7Hyz+/18EiPx/gyEPTN4Bk3PrgSQA6HAvRzuLfA4AAAAASUVORK5CYII=)
wierszy znajduje się ciąg liczb całkowitych pooddzielanych pojedynczymi
odstępami. Liczby w
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAASAQAAAAGdVCqeAAAAAnRSTlMAAQGU/a4AAAB7SURBVAiZY/jD4MPwAwhvAHH9A4Z6BRD5P4FhsQPD/gQw+/8Whvz/O8D4//8/QPwCyK5gqN//geH8/h8M7/h/MPwH0uf3G4DFQPL3/////y+BYf//9//iFzDY/3///34DQx2IOsBQC6Gq68EUSO7/AqBKIEhgeA/S9wAA9zZY1IvYp2UAAAAASUVORK5CYII=)-szym
wierszu pliku określają, do których polan prowadzą w dół przecinki od polany
nr
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==).
Pierwsza liczba
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAApSURBVAiZY2hgYGCAYAcgeYBhAxA6MCgwPACSCUB4gOEeEM5j6GMwAQC/QAn9uKaFtwAAAABJRU5ErkJggg==)
w wierszu określa liczbę tych polan, a kolejne
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAApSURBVAiZY2hgYGCAYAcgeYBhAxA6MCgwPACSCUB4gOEeEM5j6GMwAQC/QAn9uKaFtwAAAABJRU5ErkJggg==)
liczb to ich numery, które są uporządkowane wg ułożenia prowadzących do nich
przecinek w kierunku ze wschodu na zachód. Polany są ponumerowane liczbami od
1 do
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC).
Górna stacja wyciągu znajduje się na polanie numer 1, a dolna na polanie numer
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC).

## Wyjście

W pierwszym i jedynym wierszu standardowego wyjścia powinna znajdować się
dokładnie jedna liczba całkowita - maksymalna liczba narciarzy mogących wziąć
udział w treningu.

## Przykład

Dla danych wejściowych:

    
    
    15
    5 3 5 9 2 4 
    1 9
    2 7 5 
    2 6 8 
    1 7 
    1 10
    2 14 11 
    2 10 12 
    2 13 10
    3 13 15 12 
    2 14 15
    1 15 
    1 15 
    1 15
    

poprawną odpowiedzią jest:

    
    
    3
    

_Autor zadania: Marcin Kubica._

