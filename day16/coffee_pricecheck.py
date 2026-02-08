profit=0
def check_price(price):
    global profit
    one = int(input("How many 1₹ coins : ")) * 1
    two = int(input("How many 2₹ coins : ")) * 2
    five = int(input("How many 5₹ coins : ")) * 5
    ten = int(input("How many 10₹ coins : ")) * 10
    total=one+two+five+ten
    if price>total:
        print("Sorry ❌ insufficient funds")
        return False
    else:
        print(f"Here is your Change 💵{total-price} ")
        profit+=price
        return True
