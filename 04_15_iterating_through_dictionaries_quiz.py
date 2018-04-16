def question_1(basket_items, fruits):
    print(sum(basket_items[item] for item in basket_items if item in fruits))

def question_2(basket_items, fruits):
    for basket_items_example in basket_items_examples:
        question_1(basket_items_examples[basket_items_example], fruits)

def question_3(basket_items, fruits):
    # fruit_count = sum(basket_items[item] for item in basket_items if item in fruits)
    # not_fruit_count = sum(basket_items[item] for item in basket_items if item not in fruits)
    fruit_set = set(fruits)
    fruit_count, not_fruit_count = 0, 0
    for k, v in basket_items.items():
        if k in fruit_set:
            fruit_count += v
        else:
            not_fruit_count += v

    print(fruit_count, not_fruit_count)

fruits = ['apples','oranges','pears','peaches','grapes','bananas']
basket_items_examples = {
    'example_1': {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4},
    'example_2': {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4},
    'example_3': {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
}

# question_1({'apples':4,'oranges':19,'kites':3,'sandwiches':8}, fruits)
# question_2(basket_items_examples, fruits)
question_3({'apples':4,'oranges':19,'kites':3,'sandwiches':8}, fruits)