import os

# -------------------------------
# Task 1: Write Sales Records to File
# -------------------------------

print("Task 1: Write Sales Records to File")

sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as file:
    for s in sales:
        file.write(str(s) + "\n")

print("Sales written to file.")

with open("sales_data.txt", "r") as file:
    print("File Content:")
    print(file.read())


# -------------------------------
# Task 2: Read File in Different Ways
# -------------------------------

print("\nTask 2: Read File in Different Ways")

with open("sales_data.txt", "r") as file:
    content = file.read()
    print("Using read():")
    print(content)

with open("sales_data.txt", "r") as file:
    first_line = file.readline()
    print("Using readline():")
    print(first_line)

with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    sales_list = [int(line.strip()) for line in lines]
    print("Using readlines():")
    print(sales_list)


# -------------------------------
# Task 3: Append New Sales
# -------------------------------

print("\nTask 3: Append New Sales")

new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as file:
    for s in new_sales:
        file.write(str(s) + "\n")

print("New sales appended.")

with open("sales_data.txt", "r") as file:
    updated = file.readlines()

print("Updated File:")
for line in updated:
    print(line.strip())

print("Total lines after append:", len(updated))


# -------------------------------
# Task 4: Generate Summary Report
# -------------------------------

print("\nTask 4: Sales Summary")

with open("sales_data.txt", "r") as file:
    sales = [int(line.strip()) for line in file.readlines()]

total_sales = sum(sales)
highest = max(sales)
lowest = min(sales)
average = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Highest Sale:", highest)
print("Lowest Sale:", lowest)
print("Average Sale:", average)


# -------------------------------
# Task 5: Create Product Info File
# -------------------------------

print("\nTask 5: Product Info File")

products = []

for i in range(3):
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    products.append((name, price))

with open("products.txt", "w") as file:
    for name, price in products:
        file.write(f"{name} | {price}\n")

print("\nProduct File Content:")

with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())


# -------------------------------
# Task 6: Read File Safely
# -------------------------------

print("\nTask 6: Safe File Reading")

filename = input("Enter filename to open: ")

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File not found. Please check the filename.")


# -------------------------------
# Task 7: Mini Project – Discount Report
# -------------------------------

print("\nTask 7: Discount Report")

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

with open("discount_report.txt", "w") as file:
    total_discounted = 0
    count = 0

    file.write("Product | Original Price | Discounted Price\n")

    for product, price in prices.items():
        discounted = price - (price * discount / 100)
        total_discounted += discounted
        count += 1

        file.write(f"{product} | {price} | {discounted}\n")

    average = total_discounted / count

    file.write("\nSummary\n")
    file.write(f"Total Items: {count}\n")
    file.write(f"Average Discounted Price: {average}\n")

print("Discount report created.\n")

with open("discount_report.txt", "r") as file:
    print(file.read())