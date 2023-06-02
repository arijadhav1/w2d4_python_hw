def calcArea(length, width):
    return "Your area is " + str(length * width) 

def calcCircle(radius):
    return "The circle's circumference is " + radius * 2 *  p

def shop():
    d = []
    flag = True
    
    while flag:
        item = input("What item would you like to add to your shopping cart?")
        d.append(item)
    
        decision = input("Is there any item you would like to remove?")
        if decision.lower() == "yes":
            rem = input("What item would you like to remove?")
            d.remove(rem)
        quitting = input("Are you done with your shopping cart?")
        if quitting.lower() == "yes":
            flag = False
        print(f"Your current shopping cart is: {d}")
    
    return f"This is ur final shopping cart! {d} Thank you for shopping with us!"

shop()