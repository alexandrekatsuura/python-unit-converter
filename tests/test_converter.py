import pytest
from src.converter import Converter

@pytest.fixture
def converter():
    return Converter()

def test_temperature_celsius_to_fahrenheit(converter):
    assert converter.convert_temperature(0, 'celsius', 'fahrenheit') == 32.0
    assert converter.convert_temperature(100, 'celsius', 'fahrenheit') == 212.0

def test_temperature_fahrenheit_to_celsius(converter):
    assert converter.convert_temperature(32, 'fahrenheit', 'celsius') == 0.0
    assert converter.convert_temperature(212, 'fahrenheit', 'celsius') == 100.0

def test_temperature_celsius_to_kelvin(converter):
    assert converter.convert_temperature(0, 'celsius', 'kelvin') == 273.15

def test_temperature_kelvin_to_celsius(converter):
    assert converter.convert_temperature(273.15, 'kelvin', 'celsius') == 0.0

def test_mass_kilograms_to_pounds(converter):
    assert converter.convert_mass(1, 'kilograms', 'pounds') == pytest.approx(2.20462262)

def test_mass_pounds_to_kilograms(converter):
    assert converter.convert_mass(2.20462262, 'pounds', 'kilograms') == pytest.approx(1.0)

def test_distance_meters_to_feet(converter):
    assert converter.convert_distance(1, 'meters', 'feet') == pytest.approx(3.28084)

def test_distance_feet_to_meters(converter):
    assert converter.convert_distance(3.28084, 'feet', 'meters') == pytest.approx(1.0)

def test_invalid_unit(converter):
    with pytest.raises(ValueError):
        converter.convert_temperature(0, 'celsius', 'invalid_unit')
    with pytest.raises(ValueError):
        converter.convert_mass(0, 'kilograms', 'invalid_unit')
    with pytest.raises(ValueError):
        converter.convert_distance(0, 'meters', 'invalid_unit')


