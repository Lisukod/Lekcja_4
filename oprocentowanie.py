# Obliczanie kredytu na każdy miesiąc w ciągu dwóch lat na podstawie podanego procentu, kwoty początkowej pożyczki oraz kwoty spłaty

# Deklaracja stałych
# LOAN = 12000
MONTHS = ["Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "Lipiec", "Sierpien", "Wrzesien", "Pazdziernik", "Listopad", "Grudzien"]
inflation = [1.592824484, -0.453509101, 2.324671717, 1.261254407, 1.782526286, 2.329384541, 1.502229842, 1.782526286, 2.328848994, 0.616921348, 2.352295886, 0.337779545, 1.577035247, -0.292781443, 2.48619659, 
0.267110318, 1.417952672, 1.054243267, 1.480520104, 1.577035247, -0.07742069, 1.165733399, -0.404186718, 1.499708521 ]
# Pobranie danych od użytkownika
print("Podaj kwote poczatkowa kredytu")
loan = int(input())
print("Podaj procent pozyczki")
loan_percentage = int(input())
print("Podaj kwote splaty")
loan_repayment_amount = int(input()) 
remaining_loan = loan
last_month_loan = loan
month = 0
print("Kredyt poczatkowy: {} \n".format(loan))
for percentage in inflation:
    # Wyliczenie pozostałego kredytu w nowym miesiacu
    remaining_loan = (1 + ((percentage + loan_percentage)/1200)) * last_month_loan - loan_repayment_amount
    print("{}: Twoja pozostala kwota kredytu to {}, to {} mniej niz w poprzednim miesiacu.\n".format(MONTHS[month], int(remaining_loan*1000000)/1000000, int((last_month_loan - remaining_loan)*100)/100))
    # Przypisanie kredytu z danego miesiaca jako poprzedniego
    last_month_loan = remaining_loan
    # Przejście przejście do następnego miesiąca
    if month == 11:
        month = 0
    else:
        month += 1
        
input("Wcisnij enter by zakonczyc program ")
