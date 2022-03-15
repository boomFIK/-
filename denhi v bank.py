saving  = int(input("сколько вы хотите положить"))
interest = int(input("под какой процент")) / 100
time = int(input("на сколько лет"))


def bank(s, i=0.02, t=1):
    if i > 0.05:
        print('макс. процент в нашем банке 5% годовых')
        return False
    savings = calculate_savings(s, i, t)


def calculate_savings(saving, interest, time):
    for t in range(time):
        saving += saving * interest
        return saving


total_savings = bank(saving, interest, time)
print(f'ваш итоговый счет в банке: {total_savings}')

    


    


    
