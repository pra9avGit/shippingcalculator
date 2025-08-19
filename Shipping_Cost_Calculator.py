"""
Shipping Calculator Application
--------------------------------
Calculates shipping cost based on package weight and rate per kilogram.
"""

def calculate_shipping_cost(weight: float, rate: float) -> float:
    """
    Calculate the shipping cost.

    Args:
        weight (float): Package weight in kilograms.
        rate (float): Shipping rate per kilogram.

    Returns:
        float: Total shipping cost.
    """
    return round(weight * rate, 2)


def main():
    print("=== Shipping Cost Calculator ===")

    try:
        weight = float(input("Enter the package weight (kg): "))
        rate = float(input("Enter the shipping rate per kilogram (USD): "))

        if weight <= 0 or rate <= 0:
            print("Error: Weight and rate must be positive values.")
            return

        cost = calculate_shipping_cost(weight, rate)
        print(f"Shipping Cost: {cost:.2f} USD")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
