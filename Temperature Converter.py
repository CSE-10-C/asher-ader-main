'''
the title screen to the code telling the user what it does
'''

print("Temperature Converter")
print("1 = Celsius to Fahrenheit")
print("2 = Fahrenheit to Celsius")
print("3 = Celsius to Kelvin")
print("4 = Fahrenheit to Kelvin")

#telling the user to chose a number 1-4 

choice = int(input("Choose a conversion (1-4): "))

# Celsius to Fahrenheit
if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(c, "°C is", f, "°F")

# Fahrenheit to Celsius
elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f, "°F is", c, "°C")

# Celsius to Kelvin
elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    k = c + 273.15
    print(c, "°C is", k, "K")

# Fahrenheit to Kelvin
elif choice == 4:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    k = c + 273.15
    print(f, "°F is", k, "K")
#if they dont input a number from 1-4
else:
    print("Invalid choice")