class Car:
    TAX_RATE = 0.1

    def __init__(self, car_type, model, color, price):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.price = price

    def calculate_total_price(self):
        return self.price * (1 + self.TAX_RATE)

    def display_info(self):
        print(f"\nSelected Car Information:")
        print(f"Type: {self.car_type}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Base Price: ${self.price:.2f}")
        print(f"Total Price (with tax): ${self.calculate_total_price():.2f}")


def get_choice(options, prompt):
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")


def main():
    car_types = {
        "Sedan": [("Model S1", 20000), ("Model S2", 25000)],
        "Hatchback": [("Model H1", 18000), ("Model H2", 22000)],
        "Coupe": [("Model C1", 25000), ("Model C2", 30000)],
        "Minivan": [("Model M1", 22000), ("Model M2", 27000)],
        "SUV": [("Model X1", 30000), ("Model X2", 35000)]
    }
    colors = ["Black", "White", "Gray"]

    print("\nWelcome to the Car Purchase System!")
    car_type = get_choice(list(car_types.keys()), "Select a car type: ")

    print(f"\nAvailable models for {car_type}:")
    models = car_types[car_type]
    model_name, model_price = get_choice(models, "Select a model: ")

    print("\nAvailable colors:")
    color = get_choice(colors, "Select a color: ")

    car = Car(car_type, model_name, color, model_price)
    car.display_info()

    confirm = input("\nDo you want to confirm the purchase? (yes/no): ").strip().lower()
    if confirm == "yes":
        print(f"\nFinal Price: ${car.calculate_total_price():.2f}")
        print("Purchase complete. Thank you!")
    else:
        print("Purchase canceled.")


if __name__ == "__main__":
    main()
