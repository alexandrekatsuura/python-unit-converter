from converter import Converter

class Main:
    def __init__(self):
        self._converter = Converter()
        
    def run(self):
        """Main function to run Unit Converter."""
        print("Welcome to the Unit Converter!")

        while True:
            print("\nSelect the conversion type:")
            print("1. Temperature")
            print("2. Mass")
            print("3. Distance")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '4':
                break

            try:
                value = float(input("Enter the value to convert: "))
                from_unit = input("Enter the source unit: ").lower()
                to_unit = input("Enter the target unit: ").lower()

                if choice == '1':
                    result = self._converter.convert_temperature(value, from_unit, to_unit)
                    print(f"Result: {result:.2f} {to_unit}")
                elif choice == '2':
                    result = self._converter.convert_mass(value, from_unit, to_unit)
                    print(f"Result: {result:.2f} {to_unit}")
                elif choice == '3':
                    result = self._converter.convert_distance(value, from_unit, to_unit)
                    print(f"Result: {result:.2f} {to_unit}")
                else:
                    print("Invalid choice. Please try again.")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main = Main()
    main.run()