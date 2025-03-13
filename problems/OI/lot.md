Zadanie Lotniska (lot) - Baza zadań - Szkopuł

Kontakt

# Lotniska

### Limit pamięci: 32 MB

W państwie X istnieją lotniska w
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
miastach. Znane są maksymalne przepustowości tych lotnisk — lotnisko w mieście
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAOAQAAAAGWkfqPAAAAAnRSTlMAAQGU/a4AAABISURBVAiZHcYxCkBQAADQdxyju7nAv4ZSTuAANrvFKilloJSUgQk/w6tnMqGxuuM6qcMYVEFCIVcatDKP+Qy2qL+ihXrnfX4fuhsdM/m4dFIAAAAASUVORK5CYII=)
może mieć co najwyżej
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=)
połączeń lotniczych z innymi miastami. Należy zaplanować sieć połączeń
lotniczych między tymi miastami w taki sposób, by miasto
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAOAQAAAAGWkfqPAAAAAnRSTlMAAQGU/a4AAABISURBVAiZHcYxCkBQAADQdxyju7nAv4ZSTuAANrvFKilloJSUgQk/w6tnMqGxuuM6qcMYVEFCIVcatDKP+Qy2qL+ihXrnfX4fuhsdM/m4dFIAAAAASUVORK5CYII=)
miało dokładnie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=)
połączeń z innymi miastami, przy czym zakładamy, że każde połączenie jest
dwukierunkowe i każde miasto może mieć z innym tylko jedno połączenie.

## Zadanie

Napisz program, który:

  * wczytuje ze standardowego wejścia liczbę ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC) miast oraz liczby ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=), 
  * układa sieć połączeń lotniczych, taką że dla każdego ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==) od ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAALAQAAAAEDLvGtAAAAAnRSTlMAAQGU/a4AAAAfSURBVAiZY2hggMADDAxg+gEQNjAsgEMGBh2GNxAIAAbnDP3++BXkAAAAAElFTkSuQmCC) do ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC) miasto ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAOAQAAAAGWkfqPAAAAAnRSTlMAAQGU/a4AAABISURBVAiZHcYxCkBQAADQdxyju7nAv4ZSTuAANrvFKilloJSUgQk/w6tnMqGxuuM6qcMYVEFCIVcatDKP+Qy2qL+ihXrnfX4fuhsdM/m4dFIAAAAASUVORK5CYII=) ma dokładnie ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=) połączeń z innymi miastami, 
  * zapisuje na standardowe wyjście listę wszystkich tworzących sieć połączeń. 

Dane są tak dobrane, by rozwiązanie zadania istniało. Jeśli zadanie ma wiele
rozwiązań, Twój program powinien znajdować tylko jedno. Może się zdarzyć, że
podróż z jednego miasta do drugiego, nawet z przesiadkami, nie jest możliwa.

## Wejście

W pierwszym wierszu standardowego wejścia jest zapisana liczba całkowita
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
spełniająca nierówność
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFcAAAANAQAAAAGDof/GAAAAAnRSTlMAAQGU/a4AAACpSURBVAiZNY4xCoJgHMXfDbyBeoMgh6DFm9QSNCZIGBl8R6gT5CEaGgJza2ypsQwEx0SEDPz8v76lBz/e720PdBFlUBnuLo6jGZpGI+5uqBYbkBpFoTFNmPQBcqXUI0DCK70d/Irvg4v8zLTKkIotgwxPNVFm5Qn3pnzJ6bkQSyy+ELImWYs9H6KlY9wRade4aPYnTSmNd9wyNHyaFWJ+ZWkoo7F58o/8APWzchUXT/cBAAAAAElFTkSuQmCC).
Jest to liczba miast. W kolejnych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
wierszach są zapisane liczby całkowite dodatnie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=),
po jednej w każdym wierszu.

## Wyjście

Na standardowe wyjście należy zapisać wszystkie połączenia lotnicze sieci
utworzonej przez Twój program. Każde połączenie należy zapisać w osobnym
wierszu w postaci dwóch liczb całkowitych dodatnich oddzielonych pojedynczym
odstępem, tj. numerów dwóch połączonych miast. Numery miast w wierszu mogą
występować w dowolnej kolejności; również kolejność zapisywania połączeń w
pliku jest dowolna.

## Przykład

Dla danych wejściowych:

    
    
    6
    2
    3
    2
    4
    1
    2
    

poprawną odpowiedzią jest:

    
    
    5 4
    4 2
    1 2
    2 3
    6 3
    4 6
    4 1
    

_Autor zadania: Wojciech Guzicki._

