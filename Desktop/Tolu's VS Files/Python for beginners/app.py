name = input ("What is your name? ")
print ("Hello " + name)

birth_year = input ("Enter your birth year: ")
age = 2025 - int(birth_year)
print (age)

temperature = int(input("Temperature: "))
if temperature > int(30):
    print("It's a hot day.")
    print("Drink plenty of water.")
elif temperature > 20:
    print ("It's a nice day.")
elif temperature > 10:
    print ("It's a bit cold.")
else:
    print("It's cold.")