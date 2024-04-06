celsius_temperatures = [1, 11, 22, 33, 44]

convert_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32

fahrenheit_temperatures = list(map(convert_to_fahrenheit, celsius_temperatures))
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
