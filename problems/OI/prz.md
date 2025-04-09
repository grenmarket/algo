Zadanie Przedziały (prz) - Baza zadań - Szkopuł

Kontakt

# Przedziały

### Limit pamięci: 32 MB

Dany jest ciąg
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
przedziałów domkniętych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAARAQAAAAHuPtOAAAAAAnRSTlMAAQGU/a4AAAB6SURBVAiZHYoxCgIxFETfsRZsvIOFndjtASwURJJLWHqKbdzKfwOxskw6W12RBBYdN2GYxzAz7Ch6VjtjZcjz9fw8R1+yGyNtH1mmyEFr3NRpnG4yHi/jnoz0MW7DvHZld5Jy4bUyZPaXcMpsZurPbBeha3BvqTCo+QOVx0kzTR3N+AAAAABJRU5ErkJggg==),
gdzie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAAAOAQAAAAGPGhQpAAAAAnRSTlMAAQGU/a4AAACSSURBVAiZLY09CsJAEIVf551E9ALaewtbQXCP4i0ESRE7yxxAZEs7swohaDb7ubPKFO9v5o0I8kFD0CHI9VGA9i1yRF0yp8I8l2lNgo8WabmqjiJF2yUNBi5HPH/QazsfoZOL62s1s3OoDV48XFEmEu1f+PMkWXf2bvlLpu8SnLTB+nf3pvHT0jPmgbYUMGC/PV8l+pgP/otCjwAAAABJRU5ErkJggg==).
Suma tych przedziałów może być przedstawiona w postaci sumy parami rozłącznych
przedziałów domkniętych. Zadanie polega na znalezieniu przedstawienia tej sumy
w postaci sumy minimalnej liczby parami rozłącznych przedziałów domkniętych.
Przedziały tworzące to przedstawienie należy zapisać w pliku wyjściowym w
rosnącej kolejności. Mówimy, że dwa przedziały rozłączne
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAARAQAAAAGR78FxAAAAAnRSTlMAAQGU/a4AAABjSURBVAiZYyhgUGAoYHjAkADEVQxSDH8Y/gHhLyBdf4ch/QxD+R6GeiD7A8P/Gwz/fzCc7WDYv4Nh/QqGozNAXKB4/f//D4DEZxDx/QFDefXzBIa0+ncJDHm73zyAyv7+/wAAWkg0HM9FWYQAAAAASUVORK5CYII=)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB0AAAARAQAAAAF+LapPAAAAAnRSTlMAAQGU/a4AAABfSURBVAiZLYkxCoAwEATnOT7Lxtp0aYR8KC+wSWMZyAsEHxAkhahFyHkBWXZ27xZD18GoXhioNG5WTXcxbTiP0/4iGamkSPCETPL91L8TKR1G0QzWnoVZosLu5l8fKR+W6jU5+ksYdwAAAABJRU5ErkJggg==)
są ustawione w rosnącej kolejności wtedy i tylko wtedy, gdy
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAAANAQAAAAEJjmaHAAAAAnRSTlMAAQGU/a4AAACbSURBVAiZTcqxDYJgFEXhu4EjMIQDsImOYGGM3f9GsLaRMUzUSGmJC6AFBZ1iiIKC70jp153kqKlkZ1FpUmm7DKop1fHSLFzk95sKTiKxqyOz/Pv+aEV8sY+4GwSRQu/aeBzmrSbh/e0aXTdH/Kmp24FWPoLKBA9iBh77EBFGBgW99j2+bOnShFxjVl7WNMO91oLWM6ImJdqJPz/snIJtvH6clAAAAABJRU5ErkJggg==).

## Zadanie

Napisz program, który:

  * wczyta ze standardowego wejścia opis ciągu przedziałów, 
  * wyznaczy parami rozłączne przedziały spełniające warunki zadania, 
  * wypisze wyznaczone przedziały w rosnącej kolejności na standardowe wyjście. 

## Wejście

W pierwszym wierszu standardowego wejścia znajduje się jedna liczba całkowita
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC),
spełniająca nierówność
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGkAAAANAQAAAAH1m01NAAAAAnRSTlMAAQGU/a4AAAC+SURBVAiZTc0xDgFBGAXgdwNHcAiFDudQUOooRBQSMzeg1dgjKEmI3Y5iMzcwu4lCIVlkI4TZ/xnReM2Xl7zkgRsoBxXhsMKy2kuR50wxejU1su6gAcq9geOREdoB58V6hUS11ddAElbiPeoXZvlsiiRkeMlSbKUmPa8di1p4k3kYfK0zkL7fSUlK5BV93kjeXK0Tx7HGg2Vfy4U8rLUaO8f30LEwv/rmRE6c+CfbagEjPt2Zz8IMjTEa/I/+AGdPkFKRZLEwAAAAAElFTkSuQmCC).
Jest to liczba przedziałów. W
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAASAQAAAAGdVCqeAAAAAnRSTlMAAQGU/a4AAAB7SURBVAiZY/jD4MPwAwhvAHH9A4Z6BRD5P4FhsQPD/gQw+/8Whvz/O8D4//8/QPwCyK5gqN//geH8/h8M7/h/MPwH0uf3G4DFQPL3/////y+BYf//9//iFzDY/3///34DQx2IOsBQC6Gq68EUSO7/AqBKIEhgeA/S9wAA9zZY1IvYp2UAAAAASUVORK5CYII=)-szym
wierszu pliku,
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAANAQAAAAFCJrVqAAAAAnRSTlMAAQGU/a4AAACDSURBVAiZLY2xDcJQEEPfBoyQERgBJmIAEOQ2yAYwBh0/HR0sgERBQZcIUfyPQs5cJFxYz3ZhsjEa4k5ewftpbDLdDYnHGR28jrXejhA4QOqVjJRcxsmHEr77DNHsfW1ULgeflYUx10tSpZY+fApBX6m+6riMrnEVdROVMam5xM9f7Q+dCV/PlqEitwAAAABJRU5ErkJggg==),
znajduje się opis przedziału
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAARAQAAAAHuPtOAAAAAAnRSTlMAAQGU/a4AAAB6SURBVAiZHYoxCgIxFETfsRZsvIOFndjtASwURJJLWHqKbdzKfwOxskw6W12RBBYdN2GYxzAz7Ch6VjtjZcjz9fw8R1+yGyNtH1mmyEFr3NRpnG4yHi/jnoz0MW7DvHZld5Jy4bUyZPaXcMpsZurPbBeha3BvqTCo+QOVx0kzTR3N+AAAAABJRU5ErkJggg==)
w postaci dwóch liczb całkowitych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAKAQAAAAE9jKm4AAAAAnRSTlMAAQGU/a4AAAAvSURBVAiZYzjAcICBgaGBQYEhgeEBENYA2TMYIhhuAPEHht0PGIwPMJQ2MPwHIQAhmA7OLwm1fAAAAABJRU5ErkJggg==)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAOAQAAAAFJ34CQAAAAAnRSTlMAAQGU/a4AAAA8SURBVAiZYzjA4MDQAIQLGEAsByB5gGEHwwuGGUDyB4MEQwVDBIMCkHX+AMP9AwxzDzDsbGDYzMDwH4QAMyATvqMJy3IAAAAASUVORK5CYII=)
oddzielonych pojedynczym odstępem, będących odpowiednio jego początkiem i
końcem,
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKMAAAAOAQAAAAEckqGLAAAAAnRSTlMAAQGU/a4AAAEFSURBVBiVbY+xSsRAEIbnDXyE+AYKW1hEODtfwUauFMTKK0IIOgEfIKUI4t4bWFhYBNwTCxvhKrEQyUHgAiIuR5BNuLv93b2INk4x883MP/wMYT4h2+wRjjbpBSMyef58nFLdNkBKyRJfhynpKPcdcOJLOWtXnURV1Cbi/RGB+4XRHUvs4gHlxeV0h5TGvFhqsf2UklLQMHh7NUR36Kms+OFTSDXuWF2p6rruOEDgLVa3dk2fmXvA+25g5iGogceWhRDTgVgn7dRwG4MFg5Mk0dHtkPQCiDBGxU79N0VmD7jBZ9/2wHEc661z9yQa+87IPiRKcBiG1eBmSN7KsksSvzH5f/oNV2zpvxqV+kgAAAAASUVORK5CYII=).

## Wyjście

W kolejnych wierszach standardowego wyjścia należy zapisać opisy znalezionych
parami rozłącznych przedziałów. W każdym wierszu ma być zapisany opis jednego
przedziału w postaci dwóch liczb całkowitych oddzielonych pojedynczym
odstępem, będących odpowiednio początkiem i końcem tego przedziału. Przedziały
w pliku wyjściowym powinny być zapisane w rosnącej kolejności.

## Przykład

Dla danych wejściowych:

    
    
    5
    5 6
    1 4
    10 10
    6 9
    8 10

poprawną odpowiedzią jest:

    
    
    1 4
    5 10

_Autor zadania: Wojciech Guzicki._

