"""
This program prompts the user to enter a list of names separated by comma. 
then returns Last name and first initial followed my '.'  
"""

userinput = input ("Please enter your list of names(firstname lastname) separated by comma: ")
names = userinput.split(" , ")
initial = ""

for i in names:
    person = i.split(" ") 
    initial = person[0][0]
    print(person[1], initial + ".") 

print("Thank you for using my name organizer!")