print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

selection = input("Enter The selection (1, 2)): ")
selection = int(selection) - 1

temperature = input("Enter a temperature: ")
temperature = float(temperature)

converted = (temperature * 9 / 5 + 32) * (1 - selection) + ((temperature - 32) * 5 / 9) * selection

print(f"Result: {converted}") 