Zadanie Suma ciągu jedynkowego (sum) - Baza zadań - Szkopuł

Kontakt

# Suma ciągu jedynkowego

### Limit pamięci: 32 MB

Ciąg liczbowy o wartościach będących liczbami całkowitymi nazywamy jedynkowym
jeżeli dwa dowolne jego sąsiednie wyrazy różnią się od siebie dokładnie o
jeden oraz jego pierwszy wyraz jest równy
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAAmSURBVAiZY2hgAIEGBgcgPACEBUA4gUEBzAZBBQYjhiogrGCwAgDG+AmJGHCAfgAAAABJRU5ErkJggg==).
Bardziej precyzyjnie:
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGEAAAARAQAAAAGSWM9ZAAAAAnRSTlMAAQGU/a4AAACpSURBVAiZfY69DcIwFIRvA3qW8QwsEToQDamCx0CiYQQGQMglDZILJDoUUUeKg1JYyo+P5yRQUryf792dZegKqoJ0/joJzLMFQAYpoqdDua8HFjWesOxkKGDbOAYD7JiTLUZ9iEXbNOxoNg2j9xQMaXA93NPkDOYFffHNjc9Psb+UapbDGpxQsuHtHamzQquLf2b5UansMZNc37J2opmwFqo8X/JX6mDxAa9IsunJMfMzAAAAAElFTkSuQmCC)
będzie ciągiem o wartościach całkowitych; powiedzmy, że ten ciąg jest
jedynkowy, jeżeli:

  * dla dowolnej liczby całkowitej ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAApSURBVAiZY2hgYGCAYAcgeYBhAxA6MCgwPACSCUB4gOEeEM5j6GMwAQC/QAn9uKaFtwAAAABJRU5ErkJggg==) spełniającej nierówność ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAAANAQAAAAFLzRUQAAAAAnRSTlMAAQGU/a4AAACJSURBVAiZJY3BCcJAEEV/B5aw6cAS1n685qZktwM7cK1kNzfLSEAPnlwkxAgO853gwAyP9+EPlog5ghFDxOKBiT0OIaK+AZq+2TKxjmDouEPi8OxRauCIUtab6XKDHI5q5ly6C5wma9MNLd3yxUJSUOmMppWE9Oq/rbkTnVDvRh/d8yoP+/of+QHh92UE6ZpdKgAAAABJRU5ErkJggg==) zachodzi warunek ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAAASAQAAAAEZ0s2wAAAAAnRSTlMAAQGU/a4AAACzSURBVAiZXY0xDoJAEEXHWFB6Ayk8gqWH8BbaaUUoNFlOYW1nZQ3RGGmo5QZD4gHERFCj+J1ZjBGn+H/e7v79ZCLqRSSKG01zVQMOyDmKAIhreaqcEkOESjYjh1ekNMbduo/iEbZTmgODELlmZLKPL798kPfqu9wz6mtUBk5GCQrh4C+X2R47srwatGhQSb7iVonckkYz2fp7du3dZCPmrZgtmbOGui2u/7woDbnz28C27w3KY84vRDlHXQAAAABJRU5ErkJggg==) oraz 
  * ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAAOAQAAAAHkXpg5AAAAAnRSTlMAAQGU/a4AAABmSURBVAiZHYuhDYAwFESPmViDDRAsgEVXIjsC3QMBOHbAVCCqoEE1oeQ4SP7Lu38/HwktMipMEdTMMA7JgR7kASMsL+VdJAyiEduSUKu7mdWTef31BIyMhVRabR7dqVsAJX2x//QCrhZMdqUddbYAAAAASUVORK5CYII=). 

## Zadanie

Napisz program, który:

  * wczyta ze standardowego wejścia dwie liczby całkowite: długości ciągu i sumę elementów ciągu; 
  * wyznaczy ciąg jedynkowy o zadanej długości i sumie elementów lub stwierdzi, że taki ciąg nie istnieje; 
  * zapisze rezultat na standardowe wyjście. 

## Wejście

Na standardowym wejściu znajdą się:

  * w pierwszym wierszu — liczba ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC) elementów ciągu, spełniająca nierówność ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGkAAAANAQAAAAH1m01NAAAAAnRSTlMAAQGU/a4AAAC2SURBVAiZTY4xCsIwGIX/G/QIPYJDBxcRT1JHxw4OHQSbG9TVxVyjICSODqUHEIyFDg5CYynSQmOeqYP4hvfxwRseYUYwhBNdM+qmuqS2RUmb4cKojl4LAlxVlRuAg7+PGSFZJiO5vSHIzyQ19Hq/Iykho7okYef4cmuTkfIg+Ugf3AZuZz3rAU+aoAHQGLHK85yRhu/Uh+iUUk4Nhtjgp0jtHSlEq8KQnPbmgR4iLoqCuZN/YR/Vp5HSits5ywAAAABJRU5ErkJggg==); 
  * w drugim wierszu — liczba ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAALAQAAAAEZEhEjAAAAAnRSTlMAAQGU/a4AAAA1SURBVAiZY2hgcGBgYGhgWMAAYh1g2MDwg0ECSP9gmMHwAgglGM47MNw/wPDhAMO/Awy2BwBORxByZB1pTwAAAABJRU5ErkJggg==) będąca żądaną sumą elementów ciągu, spełniająca nierówność ![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAAASAQAAAAHcoFchAAAAAnRSTlMAAQGU/a4AAADHSURBVBiVfYy/DsFQFMbPGxiNnsPUNxCTtZvOYkCK8xw3UfoSImlaBoMBNYqodjBICNUYqmndo3qHhsHJyfc7fz+QExBJCfiZKkR3KF5qOtCnmm4rOrzCVGbncVXMGmjYSpmBoj5nBr+B3FczYltK9/Q5yhiQOqx3WOpKV2/SgtMjyhjHXJALLigSd3f8+kdCygO6IXJpvorYYMMYgx7hkTw33h98y7IACzgiJ299DIi76nJ9Mk0Tmh5SybGjneNrmvbr/Ld9A6F3z1EBCXpKAAAAAElFTkSuQmCC). 

## Wyjście

W pierwszych
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
wierszach standardowego wyjścia należy zapisać
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHAQAAAAGF52pbAAAAAnRSTlMAAQGU/a4AAAAiSURBVAiZYzjAwMDwgAEEdoDpBQwfGBIY8hoY7jQwzGUAAHG1CBC4It4cAAAAAElFTkSuQmCC)
liczb całkowitych (po jednej w wierszu) będących kolejnymi wyrazami ciągu
jedynkowego
(![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAApSURBVAiZY2hgYGCAYAcgeYBhAxA6MCgwPACSCUB4gOEeEM5j6GMwAQC/QAn9uKaFtwAAAABJRU5ErkJggg==)-ty
wyraz w
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAALAQAAAAHs7JqTAAAAAnRSTlMAAQGU/a4AAAApSURBVAiZY2hgYGCAYAcgeYBhAxA6MCgwPACSCUB4gOEeEM5j6GMwAQC/QAn9uKaFtwAAAABJRU5ErkJggg==)-tym
wierszu) o zadanej sumie
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAALAQAAAAEZEhEjAAAAAnRSTlMAAQGU/a4AAAA1SURBVAiZY2hgcGBgYGhgWMAAYh1g2MDwg0ECSP9gmMHwAgglGM47MNw/wPDhAMO/Awy2BwBORxByZB1pTwAAAABJRU5ErkJggg==)
lub słowo `NIE`, jeżeli taki ciąg nie istnieje.

## Przykład

Dla danych wejściowych:

    
    
    8
    4
    

poprawną odpowiedzią jest:

    
    
    0
    1
    2
    1
    0
    -1
    0
    1
    

_Autor zadania: Grzegorz Jakacki._

