# task1.py

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

# Create two car objects
car1 = Car("Toyota", "Corolla", 2021)
car2 = Car("Honda", "Civic", 2020)

# Display car details
car1.display_info()
car2.display_info()