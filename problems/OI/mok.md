Zadanie Mokra robota (mok) - Baza zadań - Szkopuł

Kontakt

# Mokra robota

### Limit pamięci: 32 MB

Dysponujemy
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
naczyniami, gdzie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAANAQAAAAGg+q4TAAAAAnRSTlMAAQGU/a4AAACJSURBVAiZLYqxDcJAEAS3A0r4EgjJMJ1QAiEBwdMBKdm7EOS7MkiQgw8IkHhZDjDy65ZDsFqtRqMFj/j15rtSjKPiMAPPHfAikLN7YWphcRtbJOvdSs+ikIaiuNiais4suukkbRCY/FODLRRLZpIDzyjWOAVeUd6c95VfYrA7TxVOQ31w8h//mT4m3GLPU5+OygAAAABJRU5ErkJggg==).
Wszystkie naczynia są początkowo całkowicie wypełnione wodą. Pojemność
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tego
naczynia
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKAQAAAAHSTsKGAAAAAnRSTlMAAQGU/a4AAAAwSURBVAiZYzjA0MDAAMQJDA4MB4Awg2EHwwyGCoYbDAoMPxj2HmCobGAoZmD4D0IAD9YM6Irrlj4AAAAASUVORK5CYII=),
mierzona w litrach, jest liczbą naturalną spełniającą nierówności
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAOAQAAAAHn6ZYRAAAAAnRSTlMAAQGU/a4AAACWSURBVAiZTcwhDsJAAETRcUiOUInkCL0SDtGE5QZwAsoROAG7BoEgSFwRTTBN2DYVpUD3s3WYyRMzI5yCE2vdnDpbq+1rZcNefrkVn4PKphY5vhLG5E/lzDjJerpe1nINOpKmMVd3+5bd4QslGM4KUz9BcxogpP1FniSyZCjkv5DF25FsQmsa3CLyFR6GJHYZR2bMP/4AESJ4hq5VSi8AAAAASUVORK5CYII=).

Wolno wykonywać trzy rodzaje ruchów:

  * Przelanie całej zawartości z jednego naczynia do drugiego. Ruch ten można wykonać tylko wtedy, gdy w drugim naczyniu jest wystarczająco dużo wolnego miejsca. 
  * Dolanie wody do pełna z jednego naczynia do drugiego. 
  * Wylanie całej zawartości jednego naczynia do zlewu. 

## Zadanie

Napisz program, który:

  * wczytuje ze standardowego wejścia liczbę naczyń ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC), pojemność każdego naczynia i zadaną końcową ilość wody w każdym z naczyń, 
  * bada, czy można w skończonej liczbie ruchów doprowadzić do zadanej sytuacji końcowej i jeśli tak, znajduje minimalną liczbę ruchów prowadzących do niej, 
  * zapisuje wynik, tj. słowo `NIE` lub minimalną liczbę ruchów na standardowe wyjście. 

## Wejście

W pierwszym wierszu standardowego wejścia jest zapisana jedna liczba całkowita
dodatnia
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
(![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAANAQAAAAGE4yHTAAAAAnRSTlMAAQGU/a4AAABmSURBVAiZFYmxDcJAEAQnI3Q5Dgi+I1PC0wg1EBL+ZQ7/CkByQADhow9AMmJ93pVWo1lefKONm/E2ZIzG0ejBtVFK4xlSH0eLM2TnmoKrc9IZHRrSL/fYWSuTUuxdj/gu+Z92H9kANtE8jjAUT3MAAAAASUVORK5CYII=))
— jest to liczba naczyń. W drugim wierszu jest zapisanych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
liczb naturalnych. Koleina
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-ta
liczba
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAOAQAAAAHn6ZYRAAAAAnRSTlMAAQGU/a4AAACWSURBVAiZTcwhDsJAAETRcUiOUInkCL0SDtGE5QZwAsoROAG7BoEgSFwRTTBN2DYVpUD3s3WYyRMzI5yCE2vdnDpbq+1rZcNefrkVn4PKphY5vhLG5E/lzDjJerpe1nINOpKmMVd3+5bd4QslGM4KUz9BcxogpP1FniSyZCjkv5DF25FsQmsa3CLyFR6GJHYZR2bMP/4AESJ4hq5VSi8AAAAASUVORK5CYII=)
jest pojemnością
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tego
naczynia. W trzecim wierszu jest zapisanych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
liczb naturalnych. Koleina
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-ta
liczba
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE8AAAAOAQAAAAExTEx0AAAAAnRSTlMAAQGU/a4AAACeSURBVAiZTcshDsJAFATQuUEFB+ghEAhEj4GswyIQhFTsEbC4HoIDsHiSVhGCaEUbcN1takq2+4etY5JJnpgBNfYaSuOhcUhLDJNFJhbGlaAv0TwtVE5HKLX5GOSM2CIx9IL6ykFQSVq8UanUvFCHZYWEC3aQiLcJS/YMaSjIGAdJMnMiL+pL3+HIE1c7xu6ONUduC/bujPnDInT84w8yZnaSQO44RQAAAABJRU5ErkJggg==)
jest zadaną końcową ilością wody w odpowiednim
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tym
naczyniu. Liczby w wierszach drugim i trzecim są pooddzielane pojedynczym
odstępem.

## Wyjście

Jeśli nie można doprowadzić do zadanej sytuacji końcowej, to w pierwszym i
jedynym wierszu standardowego wyjścia należy zapisać jedno słowo `NIE`, a w
przeciwnym przypadku minimalną liczbę ruchów prowadzących do zadanej sytuacji
końcowej.

## Przykład

Dla danych wejściowych:

    
    
    3
    3 5 5
    0 0 4
    

poprawną odpowiedzią jest:

    
    
    6
    

natomiast dla danych:

    
    
    2
    20 25
    10 16
    

poprawnym wynikiem jest:

    
    
    NIE
    

_Autor zadania: Piotr Chrząstowski-Wachtel._

