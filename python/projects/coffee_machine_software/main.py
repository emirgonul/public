from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#menu_item = MenuItem()
is_on = True

#The prompt should show every time action has completed
while is_on:
    # Check the user’s input to decide what to do next.
    options = menu.get_items()
    choice = input(f"What would you like? {options}\nEnter report for resources or off to shutdown \n:")
    #Turn off the Coffee Machine by entering “off” to the prompt
    if choice == 'off':
        is_on = False
        print("Machine turned off")
    #Print report when requested
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:     
        #Check resources sufficient, drink is the choice out of the menu_find_drink
        drink = menu.find_drink(choice)     
        #If there are sufficient resources to make the drink selected, then process coins
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost): #call on drink.cost to process price and coin
            #make drink
            coffee_maker.make_coffee(drink)