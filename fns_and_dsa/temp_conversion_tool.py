FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = input("Enter the temperature to convert: ")

try:
    temperature = float(temp)  # use float to allow decimals
    print("Valid temperature value!")
except ValueError:
    print("Invalid temperature. Please enter a numeric value")
    exit()

temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit):
    result = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{temperature}°F is {result}°C") 
    return result


def convert_to_fahrenheit(celsius):
    fahrenheit = 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR 
    print(f"{temperature}°C is {fahrenheit}°F")
    return fahrenheit

match temperature_type:
    case temp if temperature_type.upper() == 'F':
        convert_to_celsius(temperature)

    case temp if temperature_type.upper() == 'C':
        convert_to_fahrenheit(temperature)

    case _:
        print(f"Invalid temperature unit")
        


