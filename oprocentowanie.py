# Calculating and printing loan for every month for three years while taking into account inflation

# Deklaracja danych. LOAN i MOTNHS są stałymi
LOAN = 12000
MONTHS = ["Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "Lipiec", "Wrzesien", "Pazdziernik", "Listopad", "Grudzien"]
inflation = [1.592824484, -0.453509101, 2.324671717, 1.261254407, 1.782526286, 2.329384541, 1.502229842, 2.328848994, 0.616921348, 2.352295886, 0.337779545, 1.577035247, -0.292781443, 2.48619659,
0.267110318, 1.417952672, 1.054243267, 1.480520104 ,-0.07742069, 1.165733399, -0.404186718, 1.499708521]

def interest_per_month(LOAN, MONTHS, inflation):
    remaining_loan = LOAN
    last_month_loan = LOAN
    month = 0
    print("Kredyt poczatkowy: " + str(LOAN) + "\n")
    for percentage in inflation:
        # Wyliczenie pozostałego kredytu w nowym miesiacu
        remaining_loan = (1 + ((percentage+3)/LOAN))*remaining_loan-200
        print(MONTHS[month] + ": Twoja pozostala kwota kredytu to " + str(round(remaining_loan, 2)) + ", to " + str(round(last_month_loan - remaining_loan, 2)) + " mniej niz w poprzednim miesiacu \n")
        # Przypisanie kredytu z danego miesiaca jako poprzedniego
        last_month_loan = remaining_loan
        # Przejście przejście do następnego miesiąca
        if month == 10:
            month = 0
        else:
            month += 1

interest_per_month(LOAN, MONTHS, inflation)

user_input = 0
while user_input == 0:
    user_input = input("Enter something to quit: ")
    