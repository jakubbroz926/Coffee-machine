amount_w = 400
amount_m = 540
coffee_b = 120
cups = 9
money = 550


def espresso():
    global amount_w
    global coffee_b
    global cups
    global money
    if amount_w >= 250 and coffee_b >= 16 and cups >= 1:
        print("I have enough resources, making you a coffee!")
        amount_w = amount_w - 250
        coffee_b = coffee_b - 16
        cups = cups - 1
        money = money + 4
    else:
        print("Sorry not enough water.")


def latte():
    global amount_w
    global amount_m
    global coffee_b
    global cups
    global money
    if amount_w >= 350 and coffee_b >= 20 and cups >= 1 and amount_m >= 75:
        print("I have enough resources, making you a coffee!")
        amount_w = amount_w - 350
        amount_m = amount_m - 75
        coffee_b = coffee_b - 20
        cups = cups - 1
        money = money + 7
    else:
        print("Sorry not enough water.")


def cappuccino():
    global amount_w
    global amount_m
    global coffee_b
    global cups
    global money
    if amount_w >= 200 and coffee_b >= 12 and cups >= 1 and amount_m >= 100:
        print("I have enough resources, making you a coffee!")
        amount_w = amount_w - 200
        amount_m = amount_m - 100
        coffee_b = coffee_b - 12
        cups = cups - 1
        money = money + 6
    else:
        print("Sorry not enough water.")


def buy():
    print("What do you want to buy? 1 -espresso, 2 - latte, 3 - cappuccino:")
    volba = input()
    if volba == "1":
        espresso()
    elif volba == "2":
        latte()
    elif volba == "3":
        cappuccino()
    elif volba == "back":
        pass


def fill():
    print("Write how many ml of water do you want to add:")
    global amount_w
    amount_w = amount_w + int(input())
    print("Write how many ml of milk do you want to add:")
    global amount_m
    amount_m = amount_m + int(input())
    print("Write how many grams of coffee beans do you want to add:")
    global coffee_b
    coffee_b = coffee_b + int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    global cups
    cups = cups + int(input())


def take():
    global money
    print("I gave you", money)
    money = 0


def remaining():
    print("The coffee machine has:")
    print(amount_w, "of water")
    print(amount_m, "of milk")
    print(coffee_b, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")


def akce(akce):
    if akce == "buy":
        buy()
    elif akce == "fill":
        fill()
    elif akce == "take":
        take()
    elif akce == "remaining":
        remaining()
    elif akce == "exit":
        quit()


print("Write action (buy,fill,take,remaining,exit):")
while akce(input()) != 0:
    print("Write action (buy,fill,take,remaining,exit):")
    akce(input())
