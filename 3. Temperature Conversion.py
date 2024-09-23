select = input("Selete 'F' to convert Celsius to Farhenheit or 'C' to convert Fahrenheit to Celsius: ")

if select.upper() == 'F':
    celsius = float(input("Enter Temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit is ", fahrenheit)
elif select.upper() == 'C':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Celsius is ", celsius)
else:
    print("Invalid Selection. Please try 'C' or 'F'.")