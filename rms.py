import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
import datetime
class User:
    def __init__(self, username, password, designation, id):
        self.username = username
        self.password = password
        self.designation = designation
        self.id = id

    def login(self, username, password):
        return self.username == username and self.password == password

# Create some users
check1 = User("fabihatariq04", "04jan2006", "Admin", 1)
check2 = User("fabihatariq", "04jan", "Manager", 2)
check3 = User("fabiha", "pass", "Finance Head", 3)

users = [check1, check2, check3]

def attempt_login():
    username = entry_username.get()
    password = entry_password.get()
    
    for user in users:
        if user.login(username, password):
            messagebox.showinfo("Login Success", f"Welcome!! {user.designation}, You have logged in successfully")
            show_menu(user)
            return
    
    messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

def show_menu(user):
    login_frame.pack_forget()

    global menu_frame
    menu_frame = tk.Frame(canvas_frame)
    menu_frame.pack()

    tk.Label(menu_frame, text=f"You are logged in as {user.designation}", font=("Arial", 14)).pack(pady=10)

    if user.id == 1:
        tk.Label(menu_frame, text="Admin Menu:").pack()
        tk.Button(menu_frame, text="Employees", command=show_employee_options).pack()
        tk.Button(menu_frame, text="Menu Management", command=show_menu_options).pack()
        tk.Button(menu_frame, text="Bill Management", command=lambda: show_pos_system(menu_frame)).pack()
        tk.Button(menu_frame, text="Settings", command=lambda: messagebox.showinfo("Admin", "Settings")).pack()

    elif user.id == 2:
        tk.Label(menu_frame, text="Manager Menu:").pack()
        tk.Button(menu_frame, text="Menu Management", command=show_menu_options).pack()
        tk.Button(menu_frame, text="Bill Management", command=lambda: show_pos_system(menu_frame)).pack()
       
    elif user.id == 3:
        tk.Label(menu_frame, text="Finance Head Menu:").pack()
        tk.Button(menu_frame, text="Employees", command=show_employee_options).pack()
        tk.Button(menu_frame, text="Bill Management", command=lambda: show_pos_system(menu_frame)).pack()

    tk.Button(menu_frame, text="Logout", command=lambda: logout(menu_frame)).pack(pady=10)

def show_employee_options():
    menu_frame.pack_forget()

    employee_frame = tk.Frame(canvas_frame)
    employee_frame.pack()

    tk.Label(employee_frame, text="Employee Options", font=("Arial", 14)).pack(pady=10)
    tk.Button(employee_frame, text="View Employee List", command=lambda: show_emp_options(employee_frame)).pack()
    tk.Button(employee_frame, text="Back to Menu", command=lambda: back_to_menu(employee_frame)).pack(pady=10)

def show_emp_options(menu_frame):
    menu_frame.pack_forget()


    emp_frame = tk.Frame(canvas_frame)
    emp_frame.pack()

    tk.Label(emp_frame, text="Employees List", font=("Arial", 14)).pack(pady=10)

    # Create a scrolled text box for displaying the menu
    emp_output = scrolledtext.ScrolledText(emp_frame, width=40, height=15)
    emp_output.pack(pady=10)

    # Display the formatted menu
    emp_output.insert(tk.END, "Employee List\n")
    emp_output.insert(tk.END, "=" * 40 + "\n")

    global emp
    emp = {
        "Employees": [
            {"name": "Fabiha","surname": "Tariq", "designation": "Manager", "phone": "+92 300 0000000", "salary": 1150},
            {"name": "Eman","surname": "Afzal", "designation": "Manager", "phone": "+92 300 0000000", "salary": 1200},
            {"name": "Subuha", "surname": "Ejaz", "designation": "Cheif", "phone": "+92 300 0000000", "salary": 1250},
            {"name": "Maryam", "surname": "Tariq", "designation": "Waiter", "phone": "+92 300 0000000", "salary": 1300},
            {"name": "Zainab","surname": "Khan", "designation": "Cashier", "phone": "+92 300 0000000", "salary": 1350},
        ]
    }

    # Insert menu data
    for employee, items in emp.items():
        emp_output.insert(tk.END, f"{employee}:\n")
        for emps in items:
            emp_output.insert(tk.END, f"{emps['name']} {emps['surname']} - {emps['designation']} - {emps['phone']} - Rs. {emps['salary']}\n")
        emp_output.insert(tk.END, "-" * 40 + "\n")

    tk.Button(emp_frame, text="Back to Menu", command=lambda: back_to_menu(emp_frame)).pack(pady=10)



def show_menu_options():
    menu_frame.pack_forget()

    menucard_frame = tk.Frame(canvas_frame)
    menucard_frame.pack()

    tk.Label(menucard_frame, text="Menu Options", font=("Arial", 14)).pack(pady=10)
    tk.Button(menucard_frame, text="View Category List", command=lambda: show_cat_list_options(menucard_frame)).pack()
    tk.Button(menucard_frame, text="View Cuisine List", command=lambda: show_cuisine_list_options(menucard_frame)).pack()
    tk.Button(menucard_frame, text="View Menu Card", command=lambda: show_menu_card_options(menucard_frame)).pack()

    tk.Button(menucard_frame, text="Back to Menu", command=lambda: back_to_menu(menucard_frame)).pack(pady=10)

def show_cat_list_options(menu_frame):
    menu_frame.pack_forget()

    cat_frame = tk.Frame(canvas_frame)
    cat_frame.pack()

    tk.Label(cat_frame, text="Category ", font=("Arial", 14)).pack(pady=10)

    menu_output = scrolledtext.ScrolledText(cat_frame, width=60, height=25)
    menu_output.pack(pady=10)

    # Display the formatted menu
    menu_output.insert(tk.END, "Category List\n")
    menu_output.insert(tk.END, "=" * 40 + "\n")

    dishes = {
        "Categories": [
            {"name": "Beverages" },
            {"name": "Appetizers" },
            {"name": "Desserts" },
            {"name": "Main Course" },
        ],
    }

    # Insert menu data
    for category, items in dishes.items():
        menu_output.insert(tk.END, f"{category}:\n")
        for dish in items:
            menu_output.insert(tk.END, f"{dish['name']}\n")
        menu_output.insert(tk.END, "-" * 40 + "\n")

    tk.Button(cat_frame, text="Back to Menu", command=lambda: back_to_menu(cat_frame)).pack(pady=10)

def show_cuisine_list_options(menu_frame):
    menu_frame.pack_forget()

    cuisine_list = tk.Frame(canvas_frame)
    cuisine_list.pack()

    tk.Label(cuisine_list, text="Cuisine ", font=("Arial", 14)).pack(pady=10)

    menu_output = scrolledtext.ScrolledText(cuisine_list, width=60, height=25)
    menu_output.pack(pady=10)

    # Display the formatted menu
    menu_output.insert(tk.END, "Cuisine List\n")
    menu_output.insert(tk.END, "=" * 40 + "\n")

    dishes = {
        "Beverages": [
            {"name": "Pakistani" },
            {"name": "Indian" },
            {"name": "Chinese" },
            {"name": "Japanese" },
            {"name": "Thai" },
        ],
    }

    # Insert menu data
    for category, items in dishes.items():
        menu_output.insert(tk.END, f"{category}:\n")
        for dish in items:
            menu_output.insert(tk.END, f"{dish['name']}\n")
        menu_output.insert(tk.END, "-" * 40 + "\n")

    tk.Button(cuisine_list, text="Back to Menu", command=lambda: back_to_menu(cuisine_list)).pack(pady=10)

def show_menu_card_options(menu_frame):
    menu_frame.pack_forget()


    menu_card_frame = tk.Frame(canvas_frame)
    menu_card_frame.pack()

    tk.Label(menu_card_frame, text="Menu Card", font=("Arial", 14)).pack(pady=10)

    # Create a scrolled text box for displaying the menu
    menu_output = scrolledtext.ScrolledText(menu_card_frame, width=40, height=15)
    menu_output.pack(pady=10)

    # Display the formatted menu
    menu_output.insert(tk.END, "Menu Card\n")
    menu_output.insert(tk.END, "=" * 40 + "\n")

    global dishes
    dishes = {
        "Beverages": [
            {"name": "Falooda", "price": 1150},
            {"name": "Masala Chai", "price": 1200},
            {"name": "Cha Yen", "price": 1250},
            {"name": "Royal Milk Tea", "price": 1300},
            {"name": "Green Tea", "price": 1350},
        ],
        "Main Course": [
            {"name": "Biryani", "price": 400},
            {"name": "Dosa", "price": 450},
            {"name": "Green Pad Thai", "price": 500},
            {"name": "Fried Rice", "price": 600},
            {"name": "Wonton Soup", "price": 550},
        ],
        "Appetizers": [
            {"name": "Samosay", "price": 650},
            {"name": "Vada Pav", "price": 700},
            {"name": "Miang Kham", "price": 750},
            {"name": "Edamame Hummus", "price": 800},
            {"name": "Chinese Chicken Wings", "price": 850},
        ],
        "Desserts": [
            {"name": "Kheer", "price": 900},
            {"name": "Kaju Katli", "price": 950},
            {"name": "Tau Suan", "price": 1000},
            {"name": "Anpan Cake", "price": 1050},
            {"name": "Sankaya", "price": 1100},
        ],
    }

    # Insert menu data
    for category, items in dishes.items():
        menu_output.insert(tk.END, f"{category}:\n")
        for dish in items:
            menu_output.insert(tk.END, f"{dish['name']} - ${dish['price']}\n")
        menu_output.insert(tk.END, "-" * 40 + "\n")

    tk.Button(menu_card_frame, text="Back to Menu", command=lambda: back_to_menu(menu_card_frame)).pack(pady=10)

def show_pos_system(menu_frame):
    menu_frame.pack_forget()

    pos_frame = tk.Frame(canvas_frame)
    pos_frame.pack()

    tk.Label(pos_frame, text="POS System", font=("Arial", 14)).pack(pady=10)

    menu_output = scrolledtext.ScrolledText(pos_frame, width=40, height=15)
    menu_output.pack(pady=10)

    bill_list = []
    total_cost = tk.DoubleVar()
    total_cost.set(0.0)

    def add_to_bill(item_name, item_price, quantity):
        quantity = int(quantity)
        if quantity <= 0:
            messagebox.showwarning("Invalid Quantity", "Quantity must be a positive integer.")
            return
        
        total_item_cost = item_price * quantity
        bill_list.append(f"{item_name} x{quantity} - ${total_item_cost:.2f}")
        total_cost.set(total_cost.get() + total_item_cost)

        # Display the updated bill
        menu_output.delete(1.0, tk.END)
        for item in bill_list:
            menu_output.insert(tk.END, f"{item}\n")
        menu_output.insert(tk.END, f"\nTotal: ${total_cost.get():.2f}")

    def print_bill():
        with open("bill.txt", "w") as file:
            file.write("Restaurant Management System \n\n")
            file.write("Bill Generated on: " + str(datetime.datetime.now()) + "\n\n")
            file.write("Items Ordered:\n")
            for item in bill_list:
                file.write(f"{item}\n")
            file.write(f"\nTotal: Rs. {total_cost.get():.2f}\n")
        
        messagebox.showinfo("Print Bill", "Bill has been printed to 'bill.txt'.")

    for category, items in dishes.items():
        tk.Label(pos_frame, text=f"{category}").pack(pady=5)
        
        for item in items:
            item_frame = tk.Frame(pos_frame)
            item_frame.pack(pady=5)

            tk.Label(item_frame, text=f"{item['name']} - ${item['price']}").pack(side=tk.LEFT)
            quantity_entry = tk.Entry(item_frame, width=5)
            quantity_entry.pack(side=tk.LEFT, padx=5)

            tk.Button(item_frame, text="Add", command=lambda item=item, qty_entry=quantity_entry: add_to_bill(item['name'], item['price'], qty_entry.get())) \
                .pack(side=tk.LEFT)

    tk.Label(pos_frame, text="Total: ", font=("Arial", 12)).pack(pady=10)
    tk.Label(pos_frame, textvariable=total_cost, font=("Arial", 12)).pack(pady=10)

    # Add Print Bill Button
    tk.Button(pos_frame, text="Print Bill", command=print_bill).pack(pady=10)

    tk.Button(pos_frame, text="Back to Menu", command=lambda: back_to_menu(pos_frame)).pack(pady=10)


def logout(current_frame):
    current_frame.pack_forget()
    login_frame.pack()

def back_to_menu(current_frame):
    current_frame.pack_forget()
    menu_frame.pack()


# Tkinter window setup
root = tk.Tk()
root.title("Restaurant Management System")

# Add a canvas with a scrollbar
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

canvas_frame = tk.Frame(canvas)
canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Sample Menu Data (same as before)
dishes = {
    "Beverages": [
        {"name": "Falooda", "price": 1150},
        {"name": "Masala Chai", "price": 1200},
        {"name": "Cha Yen", "price": 1250},
        {"name": "Royal Milk Tea", "price": 1300},
        {"name": "Green Tea", "price": 1350},
    ],
    "Main Course": [
        {"name": "Biryani", "price": 400},
        {"name": "Dosa", "price": 450},
        {"name": "Green Pad Thai", "price": 500},
        {"name": "Fried Rice", "price": 600},
        {"name": "Wonton Soup", "price": 550},
    ],
    "Appetizers": [
        {"name": "Samosay", "price": 650},
        {"name": "Vada Pav", "price": 700},
        {"name": "Miang Kham", "price": 750},
        {"name": "Edamame Hummus", "price": 800},
        {"name": "Chinese Chicken Wings", "price": 850},
    ],
    "Desserts": [
        {"name": "Kheer", "price": 900},
        {"name": "Kaju Katli", "price": 950},
        {"name": "Tau Suan", "price": 1000},
        {"name": "Anpan Cake", "price": 1050},
        {"name": "Sankaya", "price": 1100},
    ],
}

# Login frame
login_frame = tk.Frame(canvas_frame)
login_frame.pack()

tk.Label(login_frame, text="Login", font=("Arial", 14)).pack(pady=10)

tk.Label(login_frame, text="Username:").pack()
entry_username = tk.Entry(login_frame)
entry_username.pack(pady=5)

tk.Label(login_frame, text="Password:").pack()
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack(pady=5)

tk.Button(login_frame, text="Login", command=attempt_login).pack(pady=10)

root.mainloop()
