import pandas as pd
import openai
from openpyxl.reader.excel import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows


# Wczytanie danych z pliku
def wczytaj_dane(file):
    df = pd.read_excel(file)
    return df


# Zapis danych do pliku
def zapisz_dane(nazwa, gmina, powiat, opis):
    df = pd.DataFrame(zip(nazwa.split(), gmina.split(), powiat.split(), opis.split(None, 0)), columns=["Nazwa", "Gmina", "Powiat", "Opis"])

    wb = load_workbook(filename="wyniki.xlsx")
    ws = wb["Sheet1"]
    for r in dataframe_to_rows(df, index=False, header=False):  # No index and don't append the column headers
        ws.append(r)
    wb.save("wyniki.xlsx")
    return None


# Generowanie opisu wsi za pomocą GPT-4
def generuj_opis_wsi(nazwa, gmina, powiat):
    # Inicjalizacja GPT-4
    openai.api_key = 'sk-KLUCZ'
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": "Opisz wieś " + nazwa + " znajdującej się w gminie " + gmina + " w powiecie :" + powiat}
        ]
    )
    return res["choices"][0]["message"]["content"]


# # Przykładowe dane
input_file = 'dane_wsi.xlsx'
dane_wsi = wczytaj_dane(input_file)

for _, wiersz in dane_wsi.iterrows():
    nazwa = wiersz['Nazwa']
    gmina = wiersz['Gmina']
    powiat = wiersz['Powiat']

    wyniki = generuj_opis_wsi(nazwa, gmina, powiat)
    output_file = 'wyniki.xlsx'
    zapisz_dane(nazwa, gmina, powiat, wyniki)
