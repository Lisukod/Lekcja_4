# Calculating and printing loan for every month for three years while taking into account inflation

LOAN = 12000
inflation = [1.592824484, -0.453509101, 2.324671717, 1.261254407, 1.782526286, 2.329384541, 1.502229842, 2.328848994, 0.616921348, 2.352295886, 0.337779545, 1.577035247, -0.292781443, 2.48619659,
0.267110318, 1.417952672, 1.054243267, 1.480520104 ,-0.07742069, 1.165733399, -0.404186718, 1.499708521]
months = ["Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "Lipiec", "Wrzesien", "Pazdziernik", "Listopad", "Grudzien"]

def interest_per_month(LOAN, months, inflation):
    remaining_loan = LOAN
    last_month_loan = LOAN
    month = 0
    print("Kredyt poczatkowy: " + str(LOAN) + "\n")
    for percentage in inflation:
        remaining_loan = (1 + ((percentage+3)/LOAN))*remaining_loan-200
        print(months[month] + ": Twoja pozostala kwota kredytu to " + str(remaining_loan) + ", to " + str(last_month_loan - remaining_loan) + " mniej niz w poprzednim miesiacu \n")
        last_month_loan = remaining_loan
        if month == 10:
            month = 0
        else:
            month += 1

interest_per_month(LOAN, months, inflation)