

def cost_calculator (*args, **kwargs):
    pizza_price_dict = dict({(): 13.00, "pepperoni": 1.00, "mushroom": 0.50, "olive": 0.50, "anchovy": 2.00, "ham": 1.50})
    drinks_price_dict = dict({"small": 2.00, "medium": 3.00, "large": 3.50, "tub": 3.75})
    wings_price_dict = dict({10: 5.00, 20: 9.00, 40: 17.50, 100: 48.00})
    total = 0.00
    coup = 0.00

    print(kwargs)
    for sides in kwargs:
        if sides == "wings":
            quantity_wings = kwargs[sides]
            for wing_size in quantity_wings:
                wing_price = wings_price_dict[wing_size]
                total += wing_price
                print("wing price", wing_price)

        elif sides == "drinks":
            quantity_drinks = kwargs[sides]
            for size in quantity_drinks:
                drink_price = drinks_price_dict[size]
                total += drink_price
                print("drink price", drink_price)
        else:
            coup = kwargs[sides]
            print("coupon", coup)


    for pizza_topp in args:
        if pizza_topp == []:
            total += pizza_price_dict[()]
            print("+13")

        else:
            total += pizza_price_dict[()]
            print("+13")
            for new in pizza_topp:
                pizza_price = pizza_price_dict[new]
                total += pizza_price
                print("toppings", pizza_price)
    print(total)
    tax = 0.0625 * total
    total = total * (1 - coup)
    print("before tax", total)
    total += tax
    print(total)
    total = round(total, 2)

    print(total)
    return total



cost_calculator([], [], ["pepperoni", "pepperoni"], wings=[10, 20], drinks=["small"])