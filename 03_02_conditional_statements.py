def balances(phone_balance, bank_balance):
    print(phone_balance, bank_balance, "-->",end=' ')
    if phone_balance < 5:
        phone_balance += 10
        bank_balance  -= 10
    print(phone_balance, bank_balance)

balances(3,100)
balances(8,100)

def even_odd(n):
    if n % 2 == 0:
        print("Number "+str(n)+"is even")
    else:
        print("Number "+str(n)+"is odd")
    print(n)

even_odd(4)
even_odd(15)

def season_action(season):
    if season == 'spring':
        print('plant the garden!')
    elif season == 'summer':
        print('water the garden!')
    elif season == 'fall':
        print('harvest the garden!')
    elif season == 'winter':
        print('stay indoors!')
    else:
        print('unrecognised season')

season_action('spring')
season_action('winter')

def bus_ticket(age):
    # age limits for bus fares
    free_up_to_age = 4
    child_up_to_age = 18
    senior_from_age = 65

    # set bus fares
    concession_ticket = 1.25
    adult_ticket = 2.50

    # ticket price logic
    if age <= free_up_to_age:
        ticket_price = 0
    elif age <= child_up_to_age:
        ticket_price = concession_ticket
    elif age >= senior_from_age:
        ticket_price = concession_ticket
    else:
        ticket_price = adult_ticket

    message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
    print(message)
bus_ticket(35)