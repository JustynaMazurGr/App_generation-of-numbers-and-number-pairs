Aplikacja, która znajduje wszystkie pary liczb naturalnych, których suma wynosi tyle ile chce użytkownik (np. 12).
Użytkowik wybiera również ile chce mieć wylosowanych liczb naturalnych oraz z jakiego zakresu, przy czym zakres początkowy to 0.
Na przykład: 100 liczb z zakresu od 0 do 18. 
Raz wykorzystana liczba do stworzenia pary nie może być częścią kolejnej pary.
Dane wejściowe:
Zbiór N liczb naturalnych o wartościach od 0 do 12
Przykład:
[4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
Dane wyjściowe:
Pary liczb sumujące się do 12. Parą mogą być zwracane w dowolnej kolejności. Pierwsza
liczba pary powinna być nie większa od drugiej. Przykład:
[0, 12], [4, 8], [4, 8], [1, 11], [0, 12]

Użytkownik może:
* wygenerować liczby oraz zapisać je do pliku,
* wygenerować pary liczb z wygenerowanych wcześniej liczb,
* zapisać do pliku wygenerowane pary liczb,
* pobrać własny plik csv z liczbami,
* wygenerować pary liczb z pobranego własnego pliku csv z liczbami.

W aplikacji wyświetlają się resultaty działań podjętych przez użytkownika. Na przykład: po kliknięciu w przycisk do generowania liczb, wyświetlają się liczby, które zostały wygenerowane.

_______________________________________________________________________________________________

An application that finds all pairs of natural numbers whose sum is as many as the user wants (e.g. 12).
The user also chooses how many natural numbers they want to have drawn and from which range, with the initial range being 0.
For example: 100 numbers from 0 to 18. 
Once a number is used to create a pair, it cannot be part of another pair.
Input data:
A set of N natural numbers with values from 0 to 12
Example:
[4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
Output:
Pairs of numbers adding up to 12. The pairs can be returned in any order. The first
number of the pair should be no greater than the second. Example:
[0, 12], [4, 8], [4, 8], [1, 11], [0, 12]

The user can:
* generate numbers and save them to a file,
* generate pairs of numbers from previously generated numbers,
* save to file the generated pairs of numbers,
* download their own csv file with the numbers,
* generate pairs of numbers from the downloaded own csv file with numbers.

The application displays the results of the actions taken by the user. For example: when the user clicks on the button to generate numbers, the numbers that have been generated are displayed.

Translated with DeepL.com (free version)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
