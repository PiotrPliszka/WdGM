# WdGM — laboratoria z grafiki

Rozwiązania zadań laboratoryjnych w Pythonie. Każde laboratorium ma osobny katalog z kodem, obrazami i treścią zadania.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-obrazy-informational)
![NumPy](https://img.shields.io/badge/NumPy-tablice-013243?logo=numpy&logoColor=white)

## Spis laboratoriów

| Katalog | Temat | Opis |
|---------|-------|------|
| [`zad00`](zad00/) | Obrazy czarno-białe i w odcieniach szarości | Wczytywanie bitmapy, odczyt trybu, formatu i rozmiaru, konwersja obrazu na tablicę NumPy, zapis do pliku tekstowego i odtwarzanie obrazu jako `bool_` oraz `uint8` |

## Struktura repozytorium

```
WdGM/
├── zad00/
│   ├── main.py        # rozwiązanie zadań z lab1
│   ├── PP.bmp         # inicjały 100×50 px
│   ├── obrazek.bmp
│   └── lab1.pdf       # treść zadania
├── pyproject.toml
└── README.md
```

## Uruchomienie

1. Sklonuj repozytorium i utwórz środowisko wirtualne:

   ```bash
   git clone https://github.com/PiotrPliszka/WdGM.git
   cd WdGM
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Zainstaluj zależności:

   ```bash
   pip install pillow numpy
   ```

3. Uruchom wybrane laboratorium **z jego katalogu**, bo skrypty otwierają obrazy po ścieżce względnej:

   ```bash
   cd zad00
   python main.py
   ```

> W PyCharmie ustaw w konfiguracji uruchamiania **Working directory** na katalog danego laboratorium, np. `WdGM/zad00`.

## Technologie

- **[Pillow](https://python-pillow.org/)**: wczytywanie, wyświetlanie i zapis obrazów
- **[NumPy](https://numpy.org/)**: operacje na tablicach pikseli

## Autor

Piotr Pliszka
