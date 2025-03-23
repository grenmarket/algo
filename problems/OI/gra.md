Zadanie Gra w wielokąty (gra) - Baza zadań - Szkopuł

Kontakt

# Gra w wielokąty

### Limit pamięci: 32 MB

W grze w wielokąty uczestniczy dwóch graczy. Rekwizytem jest wielokąt wypukły
o n wierzchołkach podzielony przez
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAALAQAAAAGnREl+AAAAAnRSTlMAAQGU/a4AAABQSURBVAiZFYmxEYAwDAO/o8wKbMJGMAIpWYIVWCEehCIdlC6pLJyT7u9PwvkyTjMES7YiGW0yHs3poKgUVa6SXxjb2KTog3pZkwd30jl3hf/4wi+MsFwLrgAAAABJRU5ErkJggg==)
przekątne na
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAALAQAAAAGnREl+AAAAAnRSTlMAAQGU/a4AAABNSURBVAiZY/jA8AMM9zcw/GdgsG8Aof//DzDsZ1/A8Bwo8h+E/x1g4AeKreM/AOQ7MOT/A4n///cATH5gyANSLxjuAMkZDHPr////AAAOyy/k1tULlQAAAABJRU5ErkJggg==)
trójkąty. Żadne dwie z tych przekątnych nie przecinają się poza wierzchołkami
wielokąta. Jeden z trójkątów jest czarny, a pozostałe - białe. Gracze na
przemian odcinają od wielokąta po jednym trójkącie, za każdym razem
przecinając wielokąt wzdłuż jednej z danych przekątnych. Gracz, który odetnie
czarny trójkąt wygrywa.

**PRZYPOMNIENIE:** Wielokąt jest wypukły, jeśli odcinek łączący dowolne dwa
jego punkty jest całkowicie zawarty w wielokącie.

## Zadanie

Napisz program, który:

  * czyta ze standardowego wejścia opis rekwizytu do gry,
  * sprawdza, czy gracz rozpoczynający grę ma strategię wygrywającą,
  * wypisuje wynik na standardowe wyjście.

## Wejście

Pierwszy wiersz standardowego wejścia zawiera liczbę naturalną
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGkAAAANAQAAAAH1m01NAAAAAnRSTlMAAQGU/a4AAAC6SURBVAiZTY0xCoJgHMVfJ+gIHqKhLTxHUI1tNUS4pTewtUWP0FhQoGODfEdQwcEhsEIiqc//65OW3vLjB+/xwDOo4caYHHEYLnPUNXN83mMP1WJtg/K0URSMkYUM2tMRmTtzO/qScZBcwBurercFI0a3KofISJYdN+LuDaMgCjuGDGVletKXPnlHyQfJhx7NkyTx8KJl1GrllaapUc2Po9mqn/boS0nfPKXTKcy20Vc2rXKUUh74H+8L7vaS2LnUrBMAAAAASUVORK5CYII=).
Jest to liczba wierzchołków wielokąta. Wierzchołki wielokąta są ponumerowane
kolejnymi liczbami od
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAAmSURBVAiZY2hgAIEGBgcgPACEBUA4gUEBzAZBBQYjhiogrGCwAgDG+AmJGHCAfgAAAABJRU5ErkJggg==)
do
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAALAQAAAAGnREl+AAAAAnRSTlMAAQGU/a4AAABCSURBVAiZY/jBAIH7DzD8Z2CwB6P//xcw7GdfwPD8P4jtAMQHGPiBeB3/ATA7Hyz+/18EiPx/gyEPTN4Bk3PrgSQA6HAvRzuLfA4AAAAASUVORK5CYII=),
zgodnie z ruchem wskazówek zegara. Następnych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAALAQAAAAGnREl+AAAAAnRSTlMAAQGU/a4AAABNSURBVAiZY/jA8AMM9zcw/GdgsG8Aof//DzDsZ1/A8Bwo8h+E/x1g4AeKreM/AOQ7MOT/A4n///cATH5gyANSLxjuAMkZDHPr////AAAOyy/k1tULlQAAAABJRU5ErkJggg==)
wierszy zawiera opisy trójkątów w wielokącie. W wierszu o numerze
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAANAQAAAAGXNGEnAAAAAnRSTlMAAQGU/a4AAABESURBVAiZFchBEYAwEEPRbwyQVBysLW4VgAhwQI/MlDZsJsk7hEbjzgXKFZ7MFMfG+qHhxmBfbLxI+eg0nctUU0x++gEz0S3jFgqx0gAAAABJRU5ErkJggg==),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF8AAAANAQAAAAGQdr8yAAAAAnRSTlMAAQGU/a4AAACYSURBVAiZRYzBCcJAEEV/B5ZgCVagKcUOxKMiMiWkBNvwIO7RowUIURD0uBHRLJrMc3Ny4PP/O7wRtV5zcVFVq5mZnne0ajrFygXoekBs3Mho6y6NtcEokkK0QK7g8NbeV8lce1t2i4lCL3w0dPtaLR+kIusjHvnhMIetYj96hp1iC+HIKZClSIklmgJuGZKfKe9TaMX//Ac0iIP0jJO3ZAAAAABJRU5ErkJggg==),
znajdują się trzy liczby naturalne
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHAQAAAAGbLlroAAAAAnRSTlMAAQGU/a4AAAAeSURBVAiZY2hgAAEHhgMMBQwNQAhiOTDsYjBiKAEARngFkS8eMZwAAAAASUVORK5CYII=),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAAtSURBVAiZY2hgYGBoAEMHIDzAsIHhAcMEhgVAkoEhASiiwHCO4R7DHIYdDJsA44ILU0NWMXIAAAAASUVORK5CYII=),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAAHAQAAAAF07DHWAAAAAnRSTlMAAQGU/a4AAAAfSURBVAiZY2hgYGBwAOIGhgQgBpEPGBQYdjDUMFQAAEOgBa0oRCEVAAAAAElFTkSuQmCC)
oddzielone pojedynczymi odstępami. Są to numery wierzchołków
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tego
trójkąta. Pierwszy trójkąt w ciągu jest czarny.

## Wyjście

Standardowe wyjście powinno składać się z jednego wiersza zawierającego jedno
słowo:

  * `TAK`, jeśli gracz rozpoczynający grę ma strategię wygrywającą,
  * `NIE`, jeśli nie ma.

## Przykład

Dla danych wejściowych:

    
    
    6
    0 1 2
    2 4 3
    4 2 0
    0 5 4
    

poprawną odpowiedzią jest:

    
    
    TAK
    

_Autor zadania: Grzegorz Jakacki._

