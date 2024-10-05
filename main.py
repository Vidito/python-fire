# pip install fire
import fire

class Calculator:
    """A simple calculator class."""

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

if __name__ == '__main__':
    fire.Fire(Calculator)

python calculator.py add 10 5        # Outputs: 15
python calculator.py subtract 10 5   # Outputs: 5
python calculator.py multiply 10 5   # Outputs: 50
python calculator.py divide 10 5     # Outputs: 2.0
python calculator.py divide 10 0     # Outputs: Error: Division by zero
