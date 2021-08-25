#This program repeteadly asks the user for the price of a product, until the user enters a negative number to indecate there are no more prices to enter 
#(sentinel value). The program should then return the average price.


print("------------------------------------------")
print("Welcome to the average price calculator!")
print("------------------------------------------")

print("Please enter the price of each item, one at a time.")
print("Enter a negative number when there are no more prices to enter.")

num_item = 0
sum_items = 0

price_per_item = float(input("Enter the price of an item: "))
while price_per_item >= 0:
	num_item = num_item + 1
	sum_items = sum_items + price_per_item
	average_price = (sum_items)/ num_item
	price_per_item = float(input("Enter the price of an item: "))

	if price_per_item < 0:
		if average_price == 0:
			print(0)
		else:
			print("The average price is ", average_price)
print("Total cost: ", sum_items)
 