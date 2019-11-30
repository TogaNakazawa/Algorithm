salaries = range(100, 50000, 50)
donation_rate = [0.001, 0.005, 0.01, 0.05, 0.1, 0.25]
import copy
profit = 0

def tax_and_deduction(salary):
    if salary < 195:
        return 0.05, 0
    if salary < 330:
        return 0.1, 9.75
    if salary < 695:
        return 0.2, 42.75
    if salary < 900:
        return 0.23, 63.6
    if salary < 1800:
        return 0.33, 153.6
    if salary < 4000:
        return 0.4, 279.6
    return 0.45, 479.6

for salary in salaries:
    tax, deduction = tax_and_deduction(salary)
    non_donation_outcome = (1-tax)*salary + deduction

    for d in donation_rate:
        donation = salary * d * 0.4
        tax, deduction = tax_and_deduction(salary-donation)
        donated_outcome = (1-tax)*(salary - donation) + deduction

        profit = donated_outcome - non_donation_outcome

        if profit > 0:
            print("利益: " + str(round(profit)) + "万円", end = " ")
            print("給与: " + str(salary) + "万円", end = " ")
            print("手取り(寄付なし) : " + str(round(non_donation_outcome)) + "万円", end = "  ")
            print("手取り(寄付あり) : " + str(round(donated_outcome)) + "万円", end = "  ")
            print("寄付額: " + str(round(donation))+ "万円")
