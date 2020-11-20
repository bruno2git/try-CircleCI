"""
Unit tests for the calculator library
"""

import pytest

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)
        assert 0 == calculator.add(2, -2)
        assert 0 == calculator.add(-2, 2)
        assert 2 == calculator.add(2, 0)
        assert -0.5 == calculator.add(2, -2.5)

    def test_addition_null_values(self):
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.add(2, None)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.add(None, 2)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.add(None, None)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
        assert 0 == calculator.subtract(4, 4)
        assert 0 == calculator.subtract(-4, -4)
        assert 8 == calculator.subtract(4, -4)
        assert -8 == calculator.subtract(-4, 4)
        assert 2.5 == calculator.subtract(4, 1.5)

    def test_subtraction_null_values(self):
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.subtract(2, None)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.subtract(None, 2)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.subtract(None, None)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
        assert 0 == calculator.multiply(10, 0)
        assert 0 == calculator.multiply(0, 10)
        assert 0 == calculator.multiply(0, 0)
        assert 5 == calculator.multiply(10, 0.5)
        assert 5 == calculator.multiply(0.5, 10)
        assert -100 == calculator.multiply(10, -10)
        assert -100 == calculator.multiply(-10, 10)
        assert 100 == calculator.multiply(-10, -10)

    def test_multiplication_null_values(self):
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.multiply(2, None)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.multiply(None, 2)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.multiply(None, None)

    def test_division(self):
        assert 1 == calculator.divide(10, 10)
        assert 5 == calculator.divide(10, 2)
        assert 0.2 == calculator.divide(2, 10)
        assert -0.2 == calculator.divide(-2, 10)
        assert -0.2 == calculator.divide(2, -10)
        assert 20 == calculator.divide(2, 0.1)
        assert 0.05 == calculator.divide(0.1, 2)
        assert 0 == calculator.divide(0, 2)
        assert 0 == calculator.divide(0, 0.1)

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="division by zero"):
            calculator.divide(2, 0)

    def test_division_null_values(self):
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.divide(2, None)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.divide(None, 2)
        with pytest.raises(TypeError, match="unsupported operand type"):
            calculator.divide(None, None)
