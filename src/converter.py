
class Converter:
    def __init__(self):
        """
        Initializes the Converter.
        """
        pass

    def convert_temperature(self, value, from_unit, to_unit):
        """
        Convert temperature

        Args:
            value: value to be converted.
            from_unit: current unit.
            to_unit: converted unit.

        Returns:
            The converted value.

        Raises:
            ValueError: If invalid temperature unit.
        """
        if from_unit == to_unit:
            return value

        # Convert to Celsius first
        if from_unit == 'celsius':
            celsius = value
        elif from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        else:
            raise ValueError("Invalid 'from' temperature unit.")

        # Convert from Celsius to target unit
        if to_unit == 'celsius':
            return celsius
        elif to_unit == 'fahrenheit':
            return (celsius * 9/5) + 32
        elif to_unit == 'kelvin':
            return celsius + 273.15
        else:
            raise ValueError("Invalid 'to' temperature unit.")

    def convert_mass(self, value, from_unit, to_unit):
        """
        Convert mass

        Args:
            value: value to be converted.
            from_unit: current unit.
            to_unit: converted unit.

        Returns:
            The converted value.

        Raises:
            ValueError: If invalid mass unit.
        """
        if from_unit == to_unit:
            return value

        # Convert to kilograms first
        if from_unit == 'kilograms':
            kilograms = value
        elif from_unit == 'pounds':
            kilograms = value * 0.453592
        elif from_unit == 'grams':
            kilograms = value / 1000
        else:
            raise ValueError("Invalid 'from' mass unit.")

        # Convert from kilograms to target unit
        if to_unit == 'kilograms':
            return kilograms
        elif to_unit == 'pounds':
            return kilograms / 0.453592
        elif to_unit == 'grams':
            return kilograms * 1000
        else:
            raise ValueError("Invalid 'to' mass unit.")

    def convert_distance(self, value, from_unit, to_unit):
        """
        Convert distance

        Args:
            value: value to be converted.
            from_unit: current unit.
            to_unit: converted unit.

        Returns:
            The converted value.

        Raises:
            ValueError: If invalid distance unit.
        """
        if from_unit == to_unit:
            return value

        # Convert to meters first
        if from_unit == 'meters':
            meters = value
        elif from_unit == 'kilometers':
            meters = value * 1000
        elif from_unit == 'miles':
            meters = value * 1609.34
        elif from_unit == 'feet':
            meters = value * 0.3048
        else:
            raise ValueError("Invalid 'from' distance unit.")

        # Convert from meters to target unit
        if to_unit == 'meters':
            return meters
        elif to_unit == 'kilometers':
            return meters / 1000
        elif to_unit == 'miles':
            return meters / 1609.34
        elif to_unit == 'feet':
            return meters / 0.3048
        else:
            raise ValueError("Invalid 'to' distance unit.")


