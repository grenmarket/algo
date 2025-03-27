Zadanie Paski (pas) - Baza zadań - Szkopuł

Kontakt

# Paski

### Limit pamięci: 32 MB

_Paski_ to gra dwuosobowa. Rekwizytami potrzebnymi do gry są paski w trzech
kolorach: czerwonym, zielonym i niebieskim. Wszystkie paski czerwone mają
wymiary
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAALAQAAAAFFmFIHAAAAAnRSTlMAAQGU/a4AAABTSURBVAiZY/jBUMHwAQj3NzD8Y0hneM7w/34DQ319A8P8ewwM//81gPHcfQ0MdXVAFUBsuwco/v//pwMM/38//3eAYfef+UCy/p89kKz+ef7fAQB7+CxYUwYchAAAAABJRU5ErkJggg==),
zielone
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAALAQAAAAFFmFIHAAAAAnRSTlMAAQGU/a4AAABSSURBVAiZDYqxCYBAEASnEi3BEizBjuT6eni/DAPR0FDxAw301mNhBoblYeaMJcPpuJGMrTeaFeSGViPn8BiP8LREl66CvuqF6kPwUBtM7+7lB7jlLlOU7DusAAAAAElFTkSuQmCC),
a niebieskie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAALAQAAAAGnREl+AAAAAnRSTlMAAQGU/a4AAABUSURBVAiZY/jBAII3GLYfYPjPwGDNwGDOwPD//wKG/fMXMDzPB7EdGP6/P8DAH3+AYf1+oCIgnf8eJP7/XwSQrPl/gyHv/2Qgeef/cSA5t97y/w0ArFgsf3Kw4l8AAAAASUVORK5CYII=),
gdzie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAAHAQAAAAF07DHWAAAAAnRSTlMAAQGU/a4AAAAfSURBVAiZY2hgYGBwAOIGhgQgBpEPGBQYdjDUMFQAAEOgBa0oRCEVAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHAQAAAAGbLlroAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgYGA4AMYXGAQYFjA8AMIFDJ8Y3jHsAgBiGgh7Lk4ioQAAAABJRU5ErkJggg==)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
są liczbami naturalnymi. Gracze dysponują nieograniczoną pulą pasków każdego
koloru.

Plansza do gry jest prostokątem o wymiarach
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAOAQAAAAEYS7PzAAAAAnRSTlMAAQGU/a4AAABlSURBVAiZY/jA8IPhA8MFhu0NDP/ByLqB4XsDQz2Q/f8Aw/X5Bxj68xmAbAeG/+8dGPrjHRj273dgWA+k579jAKv5////nw1Asub/Bobt9ZOB5Lv640Dy3H9LIHkfKP2BgR9EAgAhXTqc2vQSUAAAAABJRU5ErkJggg==)
i składa się z
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKAQAAAAE5eXmFAAAAAnRSTlMAAQGU/a4AAAA0SURBVAiZYzjAcICBgaGB4QGQPMDgwHCBoQPI28CwgGECwweG7QwM7xgYzjUw3G9g4G8AAB0xDWqK8YpAAAAAAElFTkSuQmCC)
pól o wymiarach
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAALAQAAAAFFmFIHAAAAAnRSTlMAAQGU/a4AAABQSURBVAiZJcXBDYAgEADB7YQSLMES7IhcJZYClOHD8PUJ0Ycm6p0Qs8ksFwu1dQuewomZYKMwZ4gqxCyE0O7/uxUGsz1R3kObOnXNdZ9N0wel5S0jVFoVWwAAAABJRU5ErkJggg==).

Gracze wykonują ruchy na przemian. Ruch polega na ułożeniu na planszy paska
dowolnego koloru. Obowiązują przy tym następujące zasady:

  * pasek nie może wystawać poza planszę, 
  * nie wolno przykrywać (nawet częściowo) pasków ułożonych wcześniej, 
  * końce paska muszą pokrywać się z brzegami pól planszy. Przegrywa gracz, który jako pierwszy nie może wykonać ruchu zgodnie z zasadami gry. 

**Pierwszy gracz** to gracz, który wykonuje pierwszy ruch w grze. Mówimy, że
pierwszy gracz ma strategię wygrywającą, jeżeli niezależnie od posunięć
drugiego gracza zawsze może wygrać.

## Zadanie

Napisz program, który

  * wczyta ze standardowego wejścia wymiary pasków i co najmniej jednej planszy,
  * dla każdej planszy stwierdzi, czy pierwszy gracz posiada strategię wygrywającą,
  * wypisze wyniki na standardowe wyjście.

## Wejście

Pierwszy wiersz standardowego wejścia zawiera trzy liczby naturalne
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAAHAQAAAAF07DHWAAAAAnRSTlMAAQGU/a4AAAAfSURBVAiZY2hgYGBwAOIGhgQgBpEPGBQYdjDUMFQAAEOgBa0oRCEVAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHAQAAAAGbLlroAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgYGA4AMYXGAQYFjA8AMIFDJ8Y3jHsAgBiGgh7Lk4ioQAAAABJRU5ErkJggg==)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH0AAAAOAQAAAAFdSh5xAAAAAnRSTlMAAQGU/a4AAADMSURBVAiZLYyxSgNBFEXvH/gJW6aSgLWwPxO0tJS4uPMJdlZiSn9A0CpTKkFJaaOusGhSqKMEsgmM7zib7K3OO497xY9oRKUKNTd9p0VVowKuFQ6PJmLWTFQzMzEC8pNv4UrGJBjRO8+ttycf0uv1YyDvE7jqVmP281NaKM3HFvxlW0+QsXvl7GAg26GJGVF9ftnmbj28eLhXINve0VG8fM0VIhwvA9MFneDM+JviLad4fH9LYmXL9VMZqBk+f8616Tt8t7zaCGtVJ/4B9QC4Sv4P6kgAAAAASUVORK5CYII=),
równe długościom pasków, odpowiednio, czerwonych, zielonych i niebieskich.
Liczby w wierszu są pooddzielane pojedynczymi znakami odstępu.

Drugi wiersz standardowego wejścia zawiera jedną liczbę
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAHAQAAAAFnO3EiAAAAAnRSTlMAAQGU/a4AAAAoSURBVAiZYzjAcIDhAwMDgwLDHoY3DEwM6xheMVQx+JUw3HnDMPcEAI8BCjxqsh6UAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGMAAAANAQAAAAHiud2EAAAAAnRSTlMAAQGU/a4AAAC5SURBVAiZTY4xCsJAEEWns/QAFvEGKSzEzouIh0iRIkUWPEBKy01tJVjYuSkEm4BlBIUExKRcVHAjye53Iwj+4j/+MMwfQkGvE5k1ZQmpwYPRswajACtGEoIRtLXr287AoeQsIYTBsSPHGftySkKiuaSMhEDVKKKd6fEvw3neUfBMdXSMQmr3TB8L2Hsu7rCKbqU3Gtoyx4YaWvrbmGQLPcmrX0IET7ShluNl91ZtfBcHXXmbmPCn4gMmWYshBrdc2wAAAABJRU5ErkJggg==),
równą liczbie różnych plansz do rozpatrzenia. Wiersze od
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAALAQAAAAEDLvGtAAAAAnRSTlMAAQGU/a4AAAAnSURBVAiZY2hgAIEGhgYo6cBwAEgqAMkFQHwAyCpg+MJwhOEHQwUAwFwKudjxMCEAAAAASUVORK5CYII=)
do
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAANAQAAAAFrIUrtAAAAAnRSTlMAAQGU/a4AAABoSURBVAiZJYrBCYNQFAQHUoilpIO048HD+xZiDbGBwPfsJQXk4FFQ47uZgLr+GFiYHXZZGXE+bJGtQ4Esco0oZXEeTc+0pP5z1Vzk3Etn0JMinZVckr05McMtl+2B1yz7BqpWpv+mcADtmT/PwHunhgAAAABJRU5ErkJggg==)
zawierają po jednej liczbie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKAQAAAAE5eXmFAAAAAnRSTlMAAQGU/a4AAAA0SURBVAiZYzjAcICBgaGB4QGQPMDgwHCBoQPI28CwgGECwweG7QwM7xgYzjUw3G9g4G8AAB0xDWqK8YpAAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF0AAAAOAQAAAAESFx2hAAAAAnRSTlMAAQGU/a4AAACpSURBVAiZLc4xCsJAEIXhdwKvkNJS8AI5iV2wFixCjLBH8AJCLmEhCG4rQWsbTQRRU6gbETGBOM9ddJpv/qkGBF4DsMS2xNtXeJKIOYMJU5ApjhQwIUd3UI0dCf2s3YU2lHMArZnncyzFVw7Vo0Un4vDEz/oBpEWyQYcPK+toul7B0LP7hfH+VsA0/Cwa9Q9OOKzJeHM62KgktIdody3sOxT+pnJRqX98AZX1id1cPFE2AAAAAElFTkSuQmCC).
Liczba w wierszu
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAANAQAAAAGXNGEnAAAAAnRSTlMAAQGU/a4AAABJSURBVAiZFYrBCYBAEMTSmFrSWYHb1v1sRNQOPPDjIbvjSiCPEBqNMzHEQuFK4qVOjA/qKLBgHjBhWYRc26+dw+Wsrpvi+WXTByxYLbtbZeUYAAAAAElFTkSuQmCC)
jest długością
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tej
planszy.

## Wyjście

Standardowe wyjście powinno zawierać
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAHAQAAAAFnO3EiAAAAAnRSTlMAAQGU/a4AAAAoSURBVAiZYzjAcIDhAwMDgwLDHoY3DEwM6xheMVQx+JUw3HnDMPcEAI8BCjxqsh6UAAAAAElFTkSuQmCC)
wierszy. W
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tym
wierszu pliku powinna być zapisana ty;lp jedna liczba:

  * 1 - jeżeli pierwszy gracz ma strategię wygrywającą dla ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tej planszy 
  * 2 - w przeciwnym przypadku. 

## Przykład

Dla danych wejściowych:

    
    
    1 5 1
    3
    1
    5
    6
    

poprawną odpowiedzią jest:

    
    
    1
    1
    2
    

_Autor zadania: Adam Borowski._

