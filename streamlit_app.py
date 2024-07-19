import streamlit as st
import pandas as pd
import numpy as np
import os
import unittest

# %%
st.title(":1234: App - Generator n losowych liczb naturalnych i par liczb z zadaną sumą")

# %%
# Wprowadzenie wartości przez użytkownika jeśli chce wygenerować swój zbiór liczb
st.markdown(":white_check_mark: **Możesz wygenerować zakres liczb jaki chcesz.**")

numbers_range = st.number_input("Podaj liczbę odnoszącą się do tego jaką maksymalną wartość ma mieć zbiór N liczb naturalnych, np. 12:", min_value=0, value=12)    #value ustawione na wartość domyślną 12
numbers_range = numbers_range + 1    #Plus jeden bo żeby zakres był taki jak chcę (czyli jak użytkownik poda 12, to żeby rzeczywiście zakres był do 12).

amount_numbers = st.number_input("Podaj liczbę odnoszącą się do tego ile ma być liczb w zbiorze liczb (minimum 2), np. 20:", min_value=2, value=12)    #value ustawione na wartość domyślną 12

#Pole do wpisania wartości sumy jaką użytkownik chce uzyskać w parze liczb:
max_sum = st.number_input("Uwaga :heavy_exclamation_mark: Podaj liczbę odnoszącą się do tego jaka ma być suma liczb w każdej parze, np. 12:", min_value=0, value=12)    #value ustawione na wartość domyślną 12

# %%
# Funkcja do generowania losowych liczb naturalnych i zapisu do pliku
def generate_and_save_numbers(numbers_range, amount_numbers):
    numbers = np.random.randint(0, numbers_range, amount_numbers)
    df = pd.DataFrame(numbers, columns=['Liczby'])
    df.to_csv('file1.csv', index=False)
    return numbers

# Definicja klasy Numbers, tu są generowane pary liczb z wygenerowanej wcześniej listy liczb, lub z listy liczb z pliku od użytkownika
class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers  # Zbiór N liczb naturalnych przekazanych bezpośrednio
        self.max_sum = None
        self.all_pairs = self.generate_pairs()
        self.chosen_pairs = None

    def generate_pairs(self):
        return [(x, y) for x in self.numbers for y in self.numbers if x != y]

    def choosing_pairs(self, max_sum):
        self.max_sum = max_sum  # Ustawia wartość żądanej sumy
        pairs = []
        used_indices = set()
        for i in range(len(self.numbers)):
            if i in used_indices:
                continue
            for j in range(i + 1, len(self.numbers)):
                if j in used_indices:
                    continue
                if self.numbers[i] + self.numbers[j] == self.max_sum:
                    pairs.append((min(self.numbers[i], self.numbers[j]), max(self.numbers[i], self.numbers[j])))
                    used_indices.add(i)
                    used_indices.add(j)
                    break
        df = pd.DataFrame(pairs, columns=['Liczba 1', 'Liczba 2'])
        df.to_csv('file2.csv', index=False)
        return df

# %%
# Inicjalizacja stanu sesji, aby wyświetlały się wyniki (wygenerowane liczby i pary), inaczej po kliknięciu w przycisk znikają wyświetlone dane (nie chcę żeby znikały):
if 'generated_numbers' not in st.session_state:
    st.session_state.generated_numbers = None
if 'numbers_list' not in st.session_state:
    st.session_state.numbers_list = None
if 'generated_pairs_from_generated' not in st.session_state:
    st.session_state.generated_pairs_from_generated = None
if 'generated_pairs_from_file' not in st.session_state:
    st.session_state.generated_pairs_from_file = None

# %%
# Przycisk do generowania i zapisu pliku z losowymi liczbami
if st.button('Generuj losowe liczby'):
    generated_numbers = generate_and_save_numbers(numbers_range, amount_numbers)
    st.session_state.generated_numbers = Numbers(generated_numbers)

# Wyświetlanie wygenerowanych liczb jeśli był użyty przycisk wygeneruj liczby
if st.session_state.generated_numbers is not None:
    st.write("Wygenerowane liczby:")
    st.write(st.session_state.generated_numbers.numbers)
    with open('file1.csv', 'rb') as file:
        st.download_button(label="Pobierz plik z wygenerowanymi liczbami", data=file, file_name='file1.csv')

# Przycisk do generowania i zapisu pliku z parami liczb, które wcześniej były wygenerowane
if st.button('Wygeneruj pary liczb z wygenerowanych wcześniej liczb'):
    if st.session_state.generated_numbers is not None:
        generated_pairs_from_generated = st.session_state.generated_numbers.choosing_pairs(max_sum)
        st.session_state.generated_pairs_from_generated = pd.DataFrame(generated_pairs_from_generated, columns=['Liczba 1', 'Liczba 2'])
        st.session_state.generated_pairs_from_generated.to_csv('file2.csv', index=False)

# Wyświetlanie wygenerowanych par liczb z wcześniej wygenerowanej listy liczb 
if st.session_state.generated_pairs_from_generated is not None:
    if st.session_state.generated_pairs_from_generated.empty:
        st.write("*Uwaga: Z podanego zbioru liczb nie można wygenerować żadnej pary liczb, która spełniałaby warunek żądanej sumy. Wybierz inną wartość żądanej sumy pary liczb.*")
    else:
        st.write("Wygenerowane pary liczb z wcześniej wygenerowanej listy liczb:")
        st.write(st.session_state.generated_pairs_from_generated)
        if os.path.exists('file2.csv'):
            with open('file2.csv', 'rb') as file:
                st.download_button(label="Pobierz plik z wygenerowanymi parami liczb", data=file, file_name='file2.csv')

# %%
# Przycisk do pobierania pliku użytkownika i wczytanie danych
st.markdown(":white_check_mark: **Możesz nie generować liczb, a zamiast tego możesz pobrać swój plik z liczbami, a następnie z niego wygenerować pary liczb:**")
uploaded_file = st.file_uploader("Wybierz plik CSV z Twoją listą liczb.", type=["csv"])

if uploaded_file is not None:
    st.write("Dane z wczytanego pliku:")
    dataframe = pd.read_csv(uploaded_file, index_col=False, sep=",", header=None)
    st.session_state.dataframe = dataframe  # Przechowywanie dataframe w session_state
    st.write(dataframe)
    # Przekształcenie DataFrame na listę, pomijając nieliczbowe wartości jeśli takie występują w pobranym pliku
    numbers_list = pd.to_numeric(dataframe.values.flatten(), errors='coerce')        #Potrzebne jeśli zakładam, że użytkownik ma pełno liczb w różnych kolumnach oraz nie tylko liczby
    numbers_list = numbers_list.astype(int).tolist()    #Bez tego robi listę np [0.0, 12.0] zamiast [0,12]
    st.session_state.numbers_list = Numbers(numbers_list)

st.write("Uwaga: jeśli pobrany plik będzie zawierał również dane inne niż liczbowe, pominie te dane.")

if st.button('Wygeneruj pary liczb z Twojego pliku z listą liczb.'):
    if uploaded_file is not None:
        generated_pairs_from_file = st.session_state.numbers_list.choosing_pairs(max_sum)
        st.session_state.generated_pairs_from_file = pd.DataFrame(generated_pairs_from_file, columns=['Liczba 1', 'Liczba 2'])
        st.session_state.generated_pairs_from_file.to_csv('file2.csv', index=False)

# Wyświetlanie wygenerowanych par liczb z listy liczb z pliku użytkownika
if st.session_state.generated_pairs_from_file is not None:
    if st.session_state.generated_pairs_from_file.empty:
        st.write("*Uwaga: Z podanego zbioru liczb nie można wygenerować żadnej pary liczb, która spełniałaby warunek żądanej sumy. Wybierz inną wartość żądanej sumy pary liczb.*")
    else:
        st.write("Wygenerowane pary liczb z listy liczb z pliku użytkownika:")
        st.write(st.session_state.generated_pairs_from_file)
        if os.path.exists('file2.csv'):
            with open('file2.csv', 'rb') as file:
                st.download_button(label="Pobierz plik z wygenerowanymi parami liczb z listy liczb z pliku użytkownika", data=file, file_name='file2.csv')

