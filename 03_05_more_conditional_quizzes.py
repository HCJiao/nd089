def question_1(answer, guess):
    print(
        "Nice!  Your guess matched the answer!" if guess == answer else
        "Oops!  Your guess was too low."        if guess < answer else
        "Oops!  Your guess was too high."
    )
def question_2_v1(state, purchase_amount):
    tax_amount = {
        'CA': 0.075,
        'MN': 0.095,
        'NY': 0.089
    }
    print(
        "Since you're from {}, your total cost is {}.".format(
            state,
            purchase_amount*(1+tax_amount[state])
        )
    )

def question_2_v2(state, purchase_amount):
    if state == 'CA':
        tax_amount = .075
        
    elif state == 'MN':
        tax_amount = .095

    elif state == 'NY':
        tax_amount = .089

    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
    print(result)

question_1(0,0)
question_1(1,0)
question_1(0,1)
question_2_v1('CA',100)
question_2_v2('CA',100)
question_2_v1('MN',100)
question_2_v2('MN',100)
question_2_v1('NY',100)
question_2_v2('NY',100)