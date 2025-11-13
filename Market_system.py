class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def __str__(self):
        return f"{self.name} - TL{self.price:.2f} (Stock: {self.stock})"

def load_products(filename):
    products = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                name, price, stock = line.strip().split(",")
                products.append(Product(name, price, stock))
    except FileNotFoundError:
        print("File not found, starting with an empty market.")
    return products

def save_products(filename, products):
    with open(filename, "w", encoding="utf-8") as f:
        for p in products:
            f.write(f"{p.name},{p.price},{p.stock}\n")

def main():
    filename = "products.txt"
    products = load_products(filename)

    while True:
        print("""
=== SIMPLE MARKET MENU ===
1. Show all products
2. Sell a product
3. Add a new product
4. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Product List ---")
            for p in products:
                print(p)

        elif choice == "2":
            name = input("Product name: ")
            quantity = int(input("Quantity to sell: "))

            found = False
            for p in products:
                if p.name.lower() == name.lower():
                    found = True
                    if p.stock >= quantity:
                        p.stock -= quantity
                        total = p.price * quantity
                        print(f"Sold {quantity} {p.name}(s) for TL{total:.2f}")
                    else:
                        print("Not enough stock.")
                    break
            if not found:
                print("Product not found.")
            save_products(filename, products)

        elif choice == "3":
            name = input("New product name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            products.append(Product(name, price, stock))
            save_products(filename, products)
            print("Product added!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
