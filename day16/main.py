#Coffee Machine Console App (Python (OOPS)  )
#Day 15 Update version 
import coffee_items
import coffee_pricecheck

while True:
    print(f"Here is today our memu \n1.Cappuccino\n2.latte\n3.Espresso")
    user_choice=input("What do you want : ").title()
    if user_choice in coffee_items.menu:
        k=coffee_items.Coffee(user_choice)
        if k=='ok':
            money=coffee_pricecheck.check_price(coffee_items.menu[user_choice]['cost'])
            if money is not False:
                print(f"here your ☕️ {user_choice}")
        else:
            print(k)
    elif user_choice=='Profit':
        print(f'\n Today Profit {coffee_pricecheck.profit}')
    elif user_choice=='Report':
        print(f'\n left stock {coffee_items.storage}')
    elif user_choice=='Off':
        break
    else:
        print('❌ invalid source ')
