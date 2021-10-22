# Inventario
# programa que calcula la existencia de una mercancia

item = input('item: ')

print("you bought: ", end='')
bought = int(input())
print(bought, item)

print("times it has been sold: ", end='')
sold = int(input())
print ("you sold", sold, item)

quantity = (bought - sold)
print("so you have", quantity, item, "left")



