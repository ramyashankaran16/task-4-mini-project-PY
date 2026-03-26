# ###Mini Project 1: Employee Management System
# employees = []
  
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))

    emp = {"name": name, "age": age, "role": role, "salary": salary}
    employees.append(emp)

def display_employees():
    if not employees:
        print("No employees found")
    else:
        for i, emp in enumerate(employees):
            print(i, emp)

  


def update_employee():
    display_employees()
    index = int(input("Enter index to update: "))
    
    if 0 <= index < len(employees):
        employees[index]["name"] = input("Enter new name: ")
        employees[index]["age"] = int(input("Enter new age: "))
        employees[index]["role"] = input("Enter new role: ")
        employees[index]["salary"] = float(input("Enter new salary: "))
        print("Employee Updated")
    else:
        print("Invalid index")

def delete_employee():
    display_employees()
    index = int(input("Enter index to delete: "))
    
    if 0 <= index < len(employees):
        employees.pop(index)
        print("Employee Deleted")
    else:
        print("Invalid index")       


 #main menu

 
def main():
    while True:
        print("=== Employee Management System ===")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

# Run program
main()


# mini project 2

students = {}

def add_student():
    name = input("Enter Student Name: ")
    m1 = int(input("Enter Mark 1: "))
    m2 = int(input("Enter Mark 2: "))
    m3 = int(input("Enter Mark 3: "))
    
    students[name] = {"Mark1": m1, "Mark2": m2, "Mark3": m3}
    print("Student Record Added")

def display_report():
    name = input("Enter Student Name to View Report: ")
    
    if name in students:
        m1 = students[name]["Mark1"]
        m2 = students[name]["Mark2"]
        m3 = students[name]["Mark3"]
        
        total = m1 + m2 + m3
        avg = total / 3
        
        if avg >= 90:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "Fail"
        
        print("\n------ REPORT CARD ------")
        print(f"Student Name : {name}")
        print(f"Mark1        : {m1}")
        print(f"Mark2        : {m2}")
        print(f"Mark3        : {m3}")
        print(f"Total        : {total}")
        print(f"Average      : {avg:.2f}")
        print(f"Grade        : {grade}")
        print("-------------------------")
    else:
        print("Student Not Found")

while True:
    print("\n1.Add Student 2.Display Report 3.Exit")
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        display_report()
    elif choice == 3:
        break
    else:
        print("Enter your Choice")

## ----------- Mini Project 3: Shopping Cart System -----------

# cart = []

def add_product():
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))
    
    product = {"name": name, "price": price, "qty": qty}
    cart.append(product)
    print("Product Added to Cart")

def display_cart():
    if not cart:
        print("Cart is Empty")
    else:
        print("\n------ CART ITEMS ------")
        print("Name\tPrice\tQty\tTotal")
        
        for item in cart:
            total = item["price"] * item["qty"]
            print(f"{item['name']}\t{item['price']}\t{item['qty']}\t{total}")
        print("------------------------")

def remove_product():
    name = input("Enter Product Name to Remove: ")
    
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            print("Product Removed")
            return
    print("Product Not Found")

def total_bill():
    bill = 0
    for item in cart:
        bill += item["price"] * item["qty"]
    
    print(f"Total Bill Amount = {bill}")

while True:
    print("\n1.Add Product 2.Display Cart 3.Remove Product 4.Total Bill 5.Exit")
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        add_product()
    elif choice == 2:
        display_cart()
    elif choice == 3:
        remove_product()
    elif choice == 4:
        total_bill()
    elif choice == 5:
        break
    else:
        print("Enter vlid choice")



 ## ------------- Mini Project 4: Login & User Validation ------------

# Dictionary to store users
users = {
    "admin": "1234",
    "Ramya": "pass",
    "user1": "1231"
}

# Taking login input
username = input("Enter Username: ")
password = input("Enter Password: ")

# Validation using condition
if username in users:
    if users[username] == password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Username Not Found")     


## ---------- Mini Project 5: Unique Visitor Counter ------------

# Set to store unique visitors
visitors = set()

while True:
    print("\n1.Add Visitor 2.Show Visitors 3.Total Count 4.Exit")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Enter Visitor Name: ")
        visitors.add(name)
        print("Visitor Added")

    elif choice == 2:
        print("Visitor List:")
        for v in visitors:
            print(v)

    elif choice == 3:
        print("Total Unique Visitors =", len(visitors))

    elif choice == 4:
        break

    else:
        print("Invalid Choice")


## ------------ Mini Project 6: String Formatter Tool -----------

Taking input
name = input("Enter Name: ")
product = input("Enter Product: ")

# Formatted sentence
print("\nFormatted Sentence:")
print(f"{name} purchased {product} successfully.")

# Padding Output
print("\nLeft Padding:")
print(name.ljust(20, "*"))

print("\nRight Padding:")
print(name.rjust(20, "*"))

print("\nCenter Padding:")
print(name.center(20, "*"))



## ------------- Mini Project 7: Bank Account System -------------

# Dictionary to store account details
accounts = {}

Function to create account
def create_account():
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    accounts[name] = balance
    print("Account Created Successfully")

# Function to deposit money
def deposit():
    name = input("Enter Account Holder Name: ")
    if name in accounts:
        amount = float(input("Enter Deposit Amount: "))
        accounts[name] += amount
        print("Amount Deposited")
    else:
        print("Account Not Found")

# Function to withdraw money
def withdraw():
    name = input("Enter Account Holder Name: ")
    if name in accounts:
        amount = float(input("Enter Withdraw Amount: "))
        if accounts[name] >= amount:
            accounts[name] -= amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")
    else:
        print("Account Not Found")

# Function to check balance
def check_balance():
    name = input("Enter Account Holder Name: ")
    if name in accounts:
        print("Current Balance =", accounts[name])
    else:
        print("Account Not Found")

# Menu Driven Loop
while True:
    print("\n1.Create Account 2.Deposit 3.Withdraw 4.Check Balance 5.Exit")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")

# ------------ Mini Project 8: Voting System ----------------
Dictionary to store candidates and vote count
votes = {
    "Ramya": 0,
    "sanjana": 2,
    "priya": 0
}

while True:
    print("\n1. Add Vote")
    print("2. Show Winner")
    print("3. Exit")
    
    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Enter Candidate Name: ")
        
        if name in votes:
            votes[name] += 1
            print("Vote Added Successfully")
        else:
            print("Candidate Not Found")

    elif choice == 2:
        print("\nVote Count:")
        for candidate in votes:
            print(candidate, "=", votes[candidate])

        winner = max(votes, key=votes.get)
        print("Winner is:", winner)

    elif choice == 3:
        break

    else:
        print("Enter Choice")


## --------- Mini Project 9: Course Enrollment System ----------

Dictionary to store students and their course list
students = {}

def add_student():
    name = input("Enter Student Name: ")
    courses = input("Enter Courses (comma separated): ").split(",")
    students[name] = courses
    print("Student Added Successfully")

def update_course():
    name = input("Enter Student Name to Update Course: ")
    if name in students:
        new_course = input("Enter New Course to Add: ")
        students[name].append(new_course)
        print("Course Updated Successfully")
    else:
        print("Student Not Found")

def display_students():
    if not students:
        print("No Students Found")
    else:
        print("\nStudent Details:")
        for name, course_list in students.items():
            print("Name:", name)
            print("Courses:", ", ".join(course_list))
            print("-------------------")

while True:
    print("\n1.Add Student 2.Update Course 3.Display Students 4.Exit")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        update_course()
    elif choice == 3:
        display_students()
    elif choice == 4:
        break
    else:
        print("Enter valid Choice")



## ---------- Mini Project 10: Number Utility Tool ------------

# Function to convert number
def convert_number(num):
    print("\nNumber Conversions:")
    print("Binary =", bin(num))
    print("Octal  =", oct(num))
    print("Hex    =", hex(num))

# Function for formatting
def format_number(num):
    print("\nFormatted Number:")
    print("With Commas      = {:,}".format(num))
    print("Scientific Format= {:.2e}".format(num))

# Menu Driven Loop
while True:
    print("\n1.Convert Number 2.Format Number 3.Exit")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        n = int(input("Enter Number: "))
        convert_number(n)

    elif choice == 2:
        n = int(input("Enter Large Number: "))
        format_number(n)

    elif choice == 3:
        break

    else:
        print("Invalid Choice")



      
   
      

 
