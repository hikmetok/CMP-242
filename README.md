🛒 Market System
📄 Project Overview
This project is a simple console-based market management system written in Python.
It allows users to:
View available products
Sell products and update stock
Add new products to the market
Save all changes to a text file (products.txt)
It’s designed as a beginner-friendly OOP2 project, using one main class: Product.


🧩 Features
✅ Load products from a text file
✅ Show all products in stock
✅ Sell a product (updates stock and shows total price)
✅ Add a new product to the list
✅ Automatically save all changes to the file



🧠 Object-Oriented Programming (OOP) Used
Class:
Product – represents a single product with:
name
price
stock
Concepts applied:
Class and Object creation
Attributes and methods
File operations (read/write)



📁 File Structure
Market_system/
│
├── market_system.py      # main program file
├── products.txt          # stores product data
└── README.md             # project description


🗂️ Example products.txt
Egg,60.0,5
Bread,15.0,100
Potato,80.0,40
Cereal,120.0,15
Chicken,80.0,10
Rice,40.0,15
Pasta,30.0,5
Coffee,50.0,100

▶️ How to Run
Make sure you have Python 3 installed.
Create a file named products.txt in the same folder as the program.
Add some sample products (like in the example above).
Run the program in the terminal:
python Market_system.py
Use the menu options to list, sell, or add products.


🧾 Example Output
=== SIMPLE MARKET MENU ===
1. Show all products
2. Sell a product
3. Add a new product
4. Exit

Enter your choice: 2
Product name: Egg
Quantity to sell: 2
Sold 2 Milk(s) for TL120.00


👨‍💻 Author
Name: Hikmet Ok
Course: OOP2 (Python)
Instructor: İdrissa Adamu
Date: 13/11/2025
