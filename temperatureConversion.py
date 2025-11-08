# Temperature Converter between Celcius to Fahrenheit
# Fahrenheit to Celcius using different functions

# Function for converting into Fahrenheit
def convertToFahrenheit(degreeCelsius):
    return degreeCelsius * (9/5) + 32

# Function for converting into Celcius
def convertToCelsius(degreeFahrenheit):
    return (degreeFahrenheit - 32) * (5/9)

# assert statements for verifying the logical assumptions
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
