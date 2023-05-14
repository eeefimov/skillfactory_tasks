import pytest
from app.calculator import Calculator


class TestCalcFunc:
    def setup(self):
        self.calc = Calculator

    def test_mult_positiv(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_divis_positiv(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_subtract_positiv(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_add_positiv(self):
        assert self.calc.adding(self, 7, 2) == 9

    def teardown(self):
        print("Execution Teardown method")