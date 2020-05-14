# Write your code here
from math import floor
qty={'water':400, 'milk':540, 'coffee beans':120, 'disposable cups':9, 'money':550}

def display(qty):
    print('The coffee machine has:')
    matls = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']
    i = 0
    for matl in matls:
        if matl == 'money':
            print('${} of {}'.format(qty[matl], matl))
        else:
            print('{} of {}'.format(qty[matl], matl))
        i += 1

def fill(qty):
    for fluid in ('water', 'milk'):
        print('Write how many ml of {} do you want to add:'.format(fluid))
        qty[fluid] += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    qty['coffee beans'] += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    qty['disposable cups'] += int(input())
    return qty

def buy(qty, num):
    esp = {'water':-250, 'milk':0, 'coffee beans':-16, 'disposable cups':-1, 'money':4}
    lat = {'water':-350, 'milk':-75, 'coffee beans':-20, 'disposable cups':-1, 'money':7}
    cap = {'water':-200, 'milk':-100, 'coffee beans':-12, 'disposable cups':-1, 'money':6}
    choices = (3, esp, lat, cap)
    #       1 - espresso, 2 - latte, 3 - cappuccino,
    option = int(num)
    flag = True
    for ingr in qty:

        if qty[ingr] < abs(choices[option][ingr]):
            print('Sorry, not enough {}!'.format(ingr))
            flag = False
            break
    if flag == True:
        print('I have enough resources, making you a coffee!')
        for ingr in qty:
            qty[ingr] += choices[option][ingr]







while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    print()
    if action == 'exit':
        break
    elif action == 'remaining':
        display(qty)
    elif action == 'take':
        print('I gave you ${}'.format(qty['money']))
        qty['money'] = 0
    elif action == 'fill':
        qty = fill(qty)
    elif action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        option = input()
        if option == 'back':
            continue
        else:
            buy(qty, option)
