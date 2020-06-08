#headings
titleProduct= "Product"
titleItems = "Items"
titleCost = "Cost"

#Data to be placed under headings
product = "cookies"
items = 2
cost = '$2.52'

print("%-15s %-15s %s" %(titleProduct, titleItems, titleCost ))
print("%-15s %-15s %s" %(product, items, cost ) )

cs = '\u2665'
print('\033[1;31;20m\u2665' )