# Wies-Plus
Wieś Plus - zadanie rekrutacyjne

**DO DZIAŁANIA APLIKACJI KONIECZNE JEST WPISANIE KLUCZA AUTORYZACYJNEGO DLA GPT API W PLIKU config.py**

**wczytaj_dane(file)** funkcja pobiera nazwę pliku, z którego pobierać będzie dane wsi(nazwa, gmina, powiat)

**zapisz_dane(output_file, nazwa, gmina, powiat, opis):** funkcja pobiera wartości tekstowe reprezentujace odpowiednio:
- output_file: nazwa pliku od którego zapisywane będą dane
- nazwa: nazwa wsi
- gmina: nazwa gminy
- powiat: nazwa powiatu
- opis: opis (pobrany z API)

**generuj_opis_wsi(nazwa, gmina, powiat)** funkcja wysyła zapytanie do API żądając opisu wsi na podstawie podanych danych wejściowych w postaci danych tekstowych:
- nazwa: nazwa wsi
- gmina: nazwa gminy
- powiat: nazwa powiatu
