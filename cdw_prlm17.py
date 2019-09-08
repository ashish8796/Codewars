'''
Their preference is to get the orders as a nice clean string with spaces and capitals like so:
"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
'''

order = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"


def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza",
            "Sandwich", "Onionrings", "Milkshake", "Coke"]
    result = ''
    for i in menu:
        ord_num = order.count(i.lower())
        if ord_num:     result += (i + " ")*ord_num
    return result.rstrip()
            

print(get_order(order))

