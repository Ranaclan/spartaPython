# Outcome (By doing this you should): Practice using lists and dictionaries
# Script should act like a waiter at a restaurant taking orders

menu = {
    "starters" : {
        "Name" : "starter",
        "Cheese" : 5,
        "Bread" : 4,
        "Soup" : 8,
        "Nothing" : 0
    },

    "mains" : {
        "Name" : "main",
        "Pie" : 10,
        "Meat" : 15,
        "Fish" : 11,
        "Nothing" : 0
    },

    "desserts" : {
        "Name" : "dessert",
        "Cake" : 6,
        "Ice Cream" : 3,
        "Chocolate" : 4,
        "Nothing" : 0
    }
}


def print_course_options(courseList, valueList):
    print(f"What {valueList[0]} would you like?")
    for i in range(1, len(courseList)):
        print(f"{courseList[i]}, £{valueList[i]}")

def get_choice(courseList):
    choice = input().capitalize()
    while choice not in courseList:
        print("That is not an option")
        choice = input().capitalize()
    return choice

def take_order():
    confirm = False
    while not confirm:
        order = []
        for course in menu.values():
            courseList = list(course.keys())
            valueList = list(course.values())

            print_course_options(courseList, valueList)
            order.append(get_choice(courseList))

        print(f"Confirm (y/n), you would like {order[0].lower()} for your starter, {order[1].lower()} for your main and {order[2].lower()} for dessert?")
        confirm = input() == "y"
    return order

def calculate_price(order):
    price = 0
    i = 0
    for course in menu.values():
        price += course.get(order[i])
        i += 1
    return price

print("Hello")
print(f"Total price: £{calculate_price(take_order())}")