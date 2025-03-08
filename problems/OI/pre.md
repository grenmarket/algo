Zadanie Pręty (pre) - Baza zadań - Szkopuł

Kontakt

# Pręty

### Limit pamięci: 32 MB

W laboratoriach pewnej firmy w czasie prac doświadczalnych nad nowym
materiałem nazwanym politoksyparenem odkryto jego ciekawą właściwość. Otóż
wykonany z tego materiału prosty pręt o małym przekroju, przy odpowiednim
unieruchomieniu końców, po podgrzaniu wydłuża się i wygina dokładnie w łuk
okręgu oparty na cięciwie, pokrywającej się z początkowym położeniem pręta.
Załóżmy, że do doświadczeń potwierdzających tę właściwość użyto
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
prętów o zaniedbywalnie małym przekroju i początkowych długościach
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAOAQAAAAG8IQsgAAAAAnRSTlMAAQGU/a4AAAAtSURBVAiZY2hgYGBoAMIDQOgAxRsYCoCiCVD4AIgPMNxj2AeENQwRDD8YfgAAZV8Ov4sTNrMAAAAASUVORK5CYII=)
(![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHEAAAAOAQAAAAFHdv7/AAAAAnRSTlMAAQGU/a4AAAC9SURBVAiZZY4xCsJAEEXnBrmBOYJFKsFDeIKUprMRtBCS3CC1IKz3EHYvEFLaiIuQwkJIjAF3wWS+G0Es/MW8efAZhsyIDBMudN6RMTdLbQtLm9dxT3Xdz4jhRlniThCJ6E+HlBAj+SyCfQTTPCVVoV5OtqQk1IIrksz4MOZkoBIQA30GB67HnvQA0BgNEjSdnEd57u7UcA34kE+jtXbegdHh58h6gwzy0eowJOe2j2AhV+uiKNxnLld88+dv1eWnr/ucwFQAAAAASUVORK5CYII=)),
oraz że w wyniku podgrzania wydłużyły się one odpowiednio o
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=)
(![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAAAOAQAAAAEb/L3bAAAAAnRSTlMAAQGU/a4AAACiSURBVAiZVc2xDYJgEIbhr2MMRnCEfxPXsCARWjs2YA0L47UmEmiIiQ2QUGj3Q0wkBLjPM7HxinvzXHNgD+0xAk0LOsVrUkTrE35X4R1V6IYFlMbPR+iemSVjwPwCaWS8pxDHsm5xonOWs4pYRMRbQhUeUiyhD+zNhh1HqrvmeQKvjg87zHVtmKie2Q8MlzIeDFsYhvUWM5yLIgFtNP5u/uMDny6IhYss/l0AAAAASUVORK5CYII=)),
przy czym
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAASAQAAAAFYJrAPAAAAAnRSTlMAAQGU/a4AAACZSURBVAiZJYs7CsJAGITnJl5B8EB7CsFCSWFjlwP42CtYK0GtLLWy9N9CSJkFoxvZx7jRgYEP5hsQMxAJt9yYoFfgG4cdfMJgASY0sdmiFE6hnpcWPKUAkgHi5QHWMoHW0kGJtBCXV0UxcHPXe/En54hFJMvI6ogPO3pWBnvWGYorRhIKd+cQY83za0MD6nxa0/5h2UMfT/sFMvZ8ZVVcAtwAAAAASUVORK5CYII=).
Wszystkie wielkości są wyrażone w milimetrach.

## Zadanie

Napisz program, który:

  * wczytuje ze standardowego wejścia liczbę prętów ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC), a następnie ich długości ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAOAQAAAAG8IQsgAAAAAnRSTlMAAQGU/a4AAAAtSURBVAiZY2hgYGBoAMIDQOgAxRsYCoCiCVD4AIgPMNxj2AeENQwRDD8YfgAAZV8Ov4sTNrMAAAAASUVORK5CYII=) oraz wydłużenia ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=), 
  * dla każdego pręta oblicza odległość w milimetrach, na jaką odchylił się po podgrzaniu środek pręta od swojego pierwotnego położenia (zakładamy, że pręt ma pomijalnie mały przekrój oraz że w końcowym położeniu przyjął kształt łuku opartego na cięciwie odpowiadającej początkowemu położeniu); wynik obliczenia ma być liczbą całkowitą różniącą się nie o więcej niż o ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAOAQAAAAGSZCqyAAAAAnRSTlMAAQGU/a4AAABPSURBVAiZFcahDYAwEEDRPxNIQtJRKpFYgujNwTS3RyE9iQPZpOIo4ud9jEhAWaks3LzdpCThCMxwCScU+WeAJow1sjfrCZsrUxb8MbzYBzqoIAl2HRx5AAAAAElFTkSuQmCC) od dokładnej wartości odchylenia, 
  * zapisuje wynik na standardowe wyjście. 

## Wejście

W pierwszym wierszu standardowego wejścia jest zapisana jedna liczba całkowita
dodatnia
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
(![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAANAQAAAAFc74XZAAAAAnRSTlMAAQGU/a4AAACXSURBVAiZLYqhDsIwAETPIZFIPgOB2H4DNBaQSOaw2Ipl/ADBsgTS+Qlml41kCQk4ytTSlPXoMk683F0eLKASmAAMIGUFzQrt/IDJ0sf06KN2m8qaM2T0dnxRPBdgM+t429xLDL2R40k2jlTds+6dAfkFab2d0ELsXX1QXk1RZFgxYtzXkjXbi0nTBOGW4zjUeZ4595/PD2mDaRYVOPCHAAAAAElFTkSuQmCC)).
W każdym z kolejnych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
wierszy są zapisane dwie liczby całkowite oddzielone pojedynczym odstępem —
pierwotna długość kolejnego pręta
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAOAQAAAAG8IQsgAAAAAnRSTlMAAQGU/a4AAAAtSURBVAiZY2hgYGBoAMIDQOgAxRsYCoCiCVD4AIgPMNxj2AeENQwRDD8YfgAAZV8Ov4sTNrMAAAAASUVORK5CYII=)
oraz jego wydłużenie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOAQAAAAGmHeuuAAAAAnRSTlMAAQGU/a4AAAA/SURBVAiZYzjA4MDQwMDAsIDhARArAMkHDG8YaoBiNxh+MMxgiADSEQwfGP4+YPj5gGH3AwbjAwylDQz/QQgAWSwWgJoSHMUAAAAASUVORK5CYII=).

## Wyjście

W każdym z
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
kolejnych wierszy standardowego wyjścia należy zapisać jedną liczbę całkowitą
nieujemną — odchylenie odpowiedniego pręta obliczone z żądaną dokładnością.

## Przykład

Dla danych wejściowych:

    
    
    2
    1000 20
    15000 10
    

poprawną odpowiedzią jest:

    
    
    87
    237
    

_Autor zadania: Piotr Chrząstowski-Wachtel._

