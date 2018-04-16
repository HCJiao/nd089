def example_1():
    manifest = [
        ("bananas", 15),
        ("mattresses", 34),
        ("dog kennels", 42),
        ("machine", 120),
        ("cheeses", 5)
    ]

    weight = 0
    items = []
    for cargo in manifest:
        if weight >= 100:
            print("breaking loop now!")
            break
        else:
            print(" adding {} ({})".format(cargo[0], cargo[1]))
            items.append(cargo[0])
            weight += cargo[1]
    print(weight)
    print(items)

def example_2():
    fruit = ["orange", "strawberry", "apple"]
    foods = ["apple", "apple", "hummus", "toast"]
    fruit_count = 0
    for food in foods:
        if food not in fruit:
            print("Not a fruit")
            continue
        fruit_count += 1
        print("Found a fruit!")
    print("Total fruit: ", fruit_count)
    
example_1()
example_2()