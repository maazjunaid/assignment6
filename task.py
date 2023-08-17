class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")


# Example usage
if __name__ == "__main__":
    print("CAR INFORMATION AND MOTORCYCLE INFORMATION : ")
    print("="*43)
    car1 = Car("Toyota", "Corolla", 2023, 4)
    motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2022, "V-twin")

    car1.display_info()
    print("\n")
    motorcycle1.display_info()