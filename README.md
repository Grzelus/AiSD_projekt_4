# AiSD Projekt 4

To jest konsolowy program w Pythonie do pracy z grafami. Pozwala wczytać graf z pliku albo z klawiatury, wybrać reprezentację danych i uruchomić jeden z dwóch algorytmów wyszukiwania cyklu:

- algorytm Fleury'ego dla cyklu Eulera,
- algorytm Robert-Floresa dla cyklu Hamiltona.

Program obsługuje dwie reprezentacje:

- macierz sąsiedztwa,
- macierz następników.

Po uruchomieniu użytkownik wybiera format grafu, sposób wczytania oraz algorytm. Wynikiem działania jest znaleziony cykl, jeśli istnieje, oraz czas wykonania algorytmu.

## Format wejścia

Przykładowy plik wejściowy dla grafu wygląda tak:

```text
5 7
1 2
2 3
3 1
1 3
3 5
5 4
4 1
```

Pierwsza linia zawiera liczbę wierzchołków i liczbę krawędzi, a kolejne linie opisują krawędzie grafu.

## Jak uruchomić

Uruchom plik `App.py` w Pythonie i postępuj zgodnie z instrukcjami wyświetlanymi w terminalu.

## Podział pracy

Na podstawie historii repozytorium:

- Antek zrobił część z macierzą sąsiedztwa oraz związane z nią elementy programu, w tym obsługę wejścia z klawiatury.
- Kacper zrobił część z macierzą następników oraz algorytmy i logikę dla tej reprezentacji.

Główny plik `App.py` spina obie części w jeden interfejs tekstowy.