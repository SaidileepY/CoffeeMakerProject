from Menu import menu, resources
from art import coffee_art
def resource_check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True

def process_coins():
    print("Please Enter Coins")
    total=0
    total+=float(input("How Many Quaters Did you enter:"))*0.25
    total+= float(input("How Many dimes Did you enter:")) * 0.1
    total+= float(input("How Many pennys Did you enter:")) * 0.01
    total+= float(input("How Many nickels Did you enter:")) * 0.05
    return total

def is_transcation_success(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here's your change{change}")
        print("Please Enjoy your drink.")
        global profit #as the profit is declared on global scope and we cannot directly use it here
                      #So we need to call global profit to make sure that can be used as local aswell.
        profit=profit+money_received-change
        return True
    else:
        print("Sorry that's not enough money. Money's refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {order}☕")

is_on=True
profit=0
while is_on:
    print("\n"*2)
    print(coffee_art)
    order=input("Please Enter your choice of drink (espresso/latte/cappuccino):").lower()
    if order=="off":
        is_on=False
    elif order=="report":
        print(f"water:{resources['water']}ml" )
        print(f"milk:{resources['milk']}ml" )
        print(f"coffee:{resources['coffee']}ml" )
        print(f"money:{profit}$" )
    else:
        drink=menu[order]
        if resource_check(drink["ingredients"]):
            payment=process_coins()
            if is_transcation_success(payment,drink["cost"]):
                make_coffee(order,drink["ingredients"])

