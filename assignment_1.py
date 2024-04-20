#Temperature Converter

class TemperatureConverter:
    @staticmethod
    def convert_temperature(temperature, source_unit, target_unit):
        if source_unit == 'F' and target_unit == 'C':
            converted_temperature = (temperature - 32) * 5/9
        elif source_unit == 'C' and target_unit == 'F':
            converted_temperature = (temperature * 9/5) + 32
        else:
            return "Invalid units. Please use 'F' for Fahrenheit or 'C' for Celsius."
        
        return round(converted_temperature, 2)

# Get user input
temperature = float(input("Enter the temperature: "))
source_unit = input("Enter the source unit (F/C): ").upper()
target_unit = input("Enter the target unit (F/C): ").upper()

# Convert temperature
converted_temperature = TemperatureConverter.convert_temperature(temperature, source_unit, target_unit)

# Print the result
print(f"The converted temperature is: {converted_temperature}")
