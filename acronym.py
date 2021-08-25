#This program prints acronym backwards

phrase = input("Enter a phrase:")

phrase_split = phrase.split()
Acronym = ""

for i in phrase_split:
    Acronym = Acronym + i[0]

print("Acronym: ", Acronym)
print("Acronym backwards: ", Acronym[::-1])