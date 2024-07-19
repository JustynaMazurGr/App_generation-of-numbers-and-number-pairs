import unittest
import os
import numpy as np
import pandas as pd
from streamlit_app import generate_and_save_numbers, Numbers
 
class TestGenerateAndSaveNumbers(unittest.TestCase):

    def test_generate_and_save_numbers(self):
        # Testowanie czy funkcja generuje odpowiednią liczbę liczb losowych i zapisuje do pliku
        numbers_range = 1000  # Zakres liczb losowych
        amount_numbers = 100  # Ilość liczb do wygenerowania

        # Wywołanie funkcji
        result = generate_and_save_numbers(numbers_range, amount_numbers)

        # Sprawdzenie czy zwrócono poprawną liczbę liczb
        self.assertEqual(len(result), amount_numbers)

class TestNumbers(unittest.TestCase):
    
    def setUp(self):
        self.numbers_instance = Numbers([4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0])
        self.numbers_instance_short = Numbers([1,2,3,4])
    
    # Sprawdza czy generuje wszystkie możliwe pary ([1,2] [1,3] [1,4] [2,1] [2,3] [2,4][3,1][3,2][3,4][4,1][4,2][4,3])
    # A konkretnie sprawdza liczbę wygenerowanych par (z krótkiej listy powinien wygenerować 12 par)
    def test_generate_pairs(self):
        pairs = self.numbers_instance_short.generate_pairs()
        self.assertEqual(len(pairs), 12)        

    # Do metody choosing_pairs przekazuję max_sum jako argument. Metoda ta zwraca dataframe z parami liczb, których suma jest równa max_sum
    def test_choosing_pairs(self):
        max_sum = 12  # Ustawiam, że suma liczb ma wynosić 12
        pairs_df = self.numbers_instance.choosing_pairs(max_sum)
        
        # Sprawdzam, czy wynik zwrócony przez metodę choosing_pairs jest typu pd.DataFrame oraz czy ramka danych ma oczekiwane nazwy kolumn
        self.assertIsInstance(pairs_df, pd.DataFrame)
        self.assertListEqual(list(pairs_df.columns), ['Liczba 1', 'Liczba 2'])

        # Sprawdzenie czy oczekiwane pary są w dataframe: [0, 12], [4, 8], [4, 8], [1, 11], [0, 12]
        self.assertIn((0, 12), pairs_df.values)
        self.assertIn((4, 8), pairs_df.values)
        self.assertIn((1, 11), pairs_df.values)
        
        # Sprawdzam, czy para (0, 12) występuje dokładnie dwukrotnie
        pair_count = sum((pairs_df['Liczba 1'] == 0) & (pairs_df['Liczba 2'] == 12))
        self.assertEqual(pair_count, 2, "Oczekiwana para 0,12 występuje tylko raz, powinna 2 razy.")
        
        # Sprawdzam, czy metoda zwraca dokładnie 5 par liczb
        self.assertEqual(len(pairs_df), 5, "Niewłasciwa liczba par liczb!")

if __name__ == '__main__':
    unittest.main()