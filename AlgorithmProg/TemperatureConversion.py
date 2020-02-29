# To the Util Class add temperaturConversion static function, given the temperature
# in fahrenheit as input outputs the temperature in Celsius or viceversa using the
# formula
# Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
# Fahrenheit to Celsius: (°F − 32) x 5/9 = °C
# --------------------------------------------------------------------------------------

# function for temperature conversion
def tempconversion(choice, temperature):
    #if input is in farenheit then it coverts to celsius
    if choice == 1:
        #celsius to Fahrenheit
        return (temperature * 9 / 5) + 32
    else:
        # Fahrenheit to celsius
        return (temperature - 32) * 5 / 9
# driver program
if __name__ == '__main__':
    print(tempconversion(int(input("Enter choice: \n 1. celsius to Fahrenheit \n 2.Farenheit to celsius")),float(input("Enter temperature:"))))
