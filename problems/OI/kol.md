Zadanie Koleje (kol) - Baza zadań - Szkopuł

Kontakt

# Koleje

### Limit pamięci: 32 MB

Bajtockie Koleje Państwowe postanowiły pójść z duchem czasu i wprowadzić do
swojej oferty połączenie InterCity. Ze względu na brak sprawnych lokomotyw,
czystych wagonów i prostych torów można było uruchomić tylko jedno takie
połączenie. Kolejną przeszkodą okazał się brak informatycznego systemu
rezerwacji miejsc. Napisanie głównej części tego systemu jest Twoim zadaniem.

Dla uproszczenia przyjmujemy, że połączenie InterCity przebiega przez
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
miast ponumerowanych kolejno od
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAALAQAAAAEDLvGtAAAAAnRSTlMAAQGU/a4AAAAfSURBVAiZY2hggMADDAxg+gEQNjAsgEMGBh2GNxAIAAbnDP3++BXkAAAAAElFTkSuQmCC)
do
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
(miasto na początku trasy ma numer
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAALAQAAAAEDLvGtAAAAAnRSTlMAAQGU/a4AAAAfSURBVAiZY2hggMADDAxg+gEQNjAsgEMGBh2GNxAIAAbnDP3++BXkAAAAAElFTkSuQmCC),
a na końcu
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)).
W pociągu jest
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAHAQAAAAFnO3EiAAAAAnRSTlMAAQGU/a4AAAAoSURBVAiZYzjAcIDhAwMDgwLDHoY3DEwM6xheMVQx+JUw3HnDMPcEAI8BCjxqsh6UAAAAAElFTkSuQmCC)
miejsc i między żadnymi dwiema kolejnymi stacjami nie można przewieźć większej
liczby pasażerów.

System informatyczny ma przyjmować kolejne zgłoszenia i stwierdzać, czy można
je zrealizować. Zgłoszenie jest akceptowane, gdy na danym odcinku trasy w
pociągu jest wystarczająca liczba wolnych miejsc, w przeciwnym przypadku
zgłoszenie jest odrzucane. Nie jest możliwe częściowe zaakceptowanie
zgłoszenia, np. na część trasy, albo dla mniejszej liczby pasażerów. Po
zaakceptowaniu zgłoszenia uaktualniany jest stan wolnych miejsc w pociągu.
Zgłoszenia przetwarzane są jedno po drugim w kolejności nadchodzenia.

## Zadanie

Napisz program, który:

  * wczyta ze standardowego wejścia opis połączenia oraz listę zgłoszonych rezerwacji, 
  * obliczy które zgłoszenia zostaną przyjęte, a które odrzucone, 
  * zapisze na standardowe wyjście odpowiedzi na wszystkie zgłoszenia. 

## Wejście

W pierwszym wierszu standardowego wejścia znajdują się trzy liczby całkowite
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAHAQAAAAFnO3EiAAAAAnRSTlMAAQGU/a4AAAAoSURBVAiZYzjAcIDhAwMDgwLDHoY3DEwM6xheMVQx+JUw3HnDMPcEAI8BCjxqsh6UAAAAAElFTkSuQmCC)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHAQAAAAGbLlroAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgYGA4AMYXGAQYFjA8AMIFDJ8Y3jHsAgBiGgh7Lk4ioQAAAABJRU5ErkJggg==)
(![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGkAAAANAQAAAAH1m01NAAAAAnRSTlMAAQGU/a4AAAC4SURBVAiZTYoxCsJAFETnBh4hR7CwsBHJOSy0tNNCJIWguYG2Nu4RbAXBtbQIuYExkMJC2ChBImTzxw1YODA8HjywB1rwjOsBZXeaoiiYYlENQpjJ3Afl7SPLXEBFVR8P4Gq0bKjkxk50gc6Zz7YbaM1TblKcpM9pw6Ws9o56p1VDj0qaTlrSIp9o80XyJWYcRVGInJ5Tr5YySRKnllVgaeOfci13rmtTJMMhnH7sw90EcRyH4P/CL3jgkmaQ28XmAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG4AAAANAQAAAAEXR1Y0AAAAAnRSTlMAAQGU/a4AAAC7SURBVAiZTYq9DsFQAEa/9zD0ESQWk/AmFmEjwYZ0MBq8gMQTYJQg7gs0jMY2Ee1CbxuSqz/u5zYWZzk5yQE9pAvwgMsbLCkPz4QRRp9VA2F150Ex9XCNzUbBwO3m0HbTVcZLreg8KxAuM8fvQ9Qps2yNg96ImfFRq+XeWBxFUNjilsWXW5ySGmVeabBUe+ycWpC6biqmlJNH+IJMmA7EmX7vl7R0YL8pe7WbH5mM87DJedAZ38Mh+E/+BXVIlrkNrdfLAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGkAAAANAQAAAAH1m01NAAAAAnRSTlMAAQGU/a4AAAC2SURBVAiZTY07CsJAFEXvDtyAkCVY2ImYbMI12NlaBEx2oO0U4jbE31ha+FmBGkiRRh1DQCNO5joDFr7mcC4HHtgGNbjBqcSLUYKiYILw042h+q0AfM4DpKkNOKVU9xkYmaGjVTbFFlLx0hNjSMnOZ5BgzTpDx2jNhaW0oaNnfOM6U9Me+UCDOcnUXI9C7Ow32tX4VaVWq7NVTWZv6v1POeKFXnXLlsszrJYcMNdXNZkcYvD/4i9Yv5FNvfH9ygAAAABJRU5ErkJggg==))
pooddzielane pojedynczymi odstępami, oznaczające odpowiednio: liczbę miast na
trasie, liczbę miejsc w pociągu i liczbę zgłoszeń. W kolejnych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHAQAAAAGbLlroAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgYGA4AMYXGAQYFjA8AMIFDJ8Y3jHsAgBiGgh7Lk4ioQAAAABJRU5ErkJggg==)
wierszach opisane są kolejne zgłoszenia. W wierszu o numerze
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAANAQAAAAGXNGEnAAAAAnRSTlMAAQGU/a4AAABESURBVAiZFchBEYAwEEPRbwyQVBysLW4VgAhwQI/MlDZsJsk7hEbjzgXKFZ7MFMfG+qHhxmBfbLxI+eg0nctUU0x++gEz0S3jFgqx0gAAAABJRU5ErkJggg==)
opisane jest
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-te
zgłoszenie. Zapisane są w nim trzy liczby całkowite
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKAQAAAAE5eXmFAAAAAnRSTlMAAQGU/a4AAAA0SURBVAiZYzjAcICBgaGB4QGQPMDgwHCBoQPI28CwgGECwweG7QwM7xgYzjUw3G9g4G8AAB0xDWqK8YpAAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAApSURBVAiZY2hgYGCAYAcgeYBhAxA6MCgwPACSCUB4gOEeEM5j6GMwAQC/QAn9uKaFtwAAAABJRU5ErkJggg==)
i
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAKAQAAAAEuW+lMAAAAAnRSTlMAAQGU/a4AAAAbSURBVAiZY2hgYGBAYAcGGGhgOMCwAAgTGBwAVIQFYVvoLrkAAAAASUVORK5CYII=)
(![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAOAQAAAAGG8bRTAAAAAnRSTlMAAQGU/a4AAAC1SURBVAiZNcwxDoJAFATQOYFX4AiWVmS5hpewsdDEyO4N9AZ4Aw9gBDpL6SwpKKwEzBZgXP64hDjNz5tJPrhF14MFHi26RQ1YVgY7oUETrwDWnUHFpwETllQ5qPciYpBQldlgkDUUljmyzF+dIxUVhy5CqpfiBt8nMugwQiDqqgjIjHRBjjnf9BHyxhYNA4+70OlRjsOlp6Plq/DbgWvrF1Hfo1cvGwafMyt7wvRhSjuq13/9ADyumvFEZiJxAAAAAElFTkSuQmCC),
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAANAQAAAAGkD34uAAAAAnRSTlMAAQGU/a4AAACNSURBVAiZLYq9CcJQHAdvA0fICPY2OpKVjZCXDRzh2blF8jo7cQDBQAQ7EwkSzcf/5xO86jiOLuMFyrhCZ9DeA9suUF9WWB2ojgH5VA1KP9Mab244UzzkSop8VElubb8nT4chUHjrSxKTBWzWxGeup5wtZdSKvdLPRpm8DovYdlMcHpto78kpOd3QH/sCSppoqAcL82UAAAAASUVORK5CYII=))
pooddzielane pojedynczymi odstępami, oznaczające odpowiednio: numer stacji
początkowej, numer stacji docelowej i wymaganą liczbę miejsc.

### Wyjście

Twój program powinien zapisać na standardowe wyjście
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHAQAAAAGbLlroAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgYGA4AMYXGAQYFjA8AMIFDJ8Y3jHsAgBiGgh7Lk4ioQAAAABJRU5ErkJggg==)
wierszy. W
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-tym
wierszu powinien zostać zapisany dokładnie jeden znak:

  * T - jeśli ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAALAQAAAAEH2yGQAAAAAnRSTlMAAQGU/a4AAAAgSURBVAiZY2hgaGCAgAaGA2D2ASB0gMIPQHiBYQNDAgCW6AkBJunwlwAAAABJRU5ErkJggg==)-te zgłoszenie zostało zaakceptowane,
  * N - w przeciwnym przypadku. 

## Przykład

Dla danych wejściowych:

    
    
    4 6 4
    1 4 2
    1 3 2
    2 4 3
    1 2 3

poprawną odpowiedzią jest:

    
    
    T
    T
    N
    N

_Autor zadania: Tomasz Waleń._

