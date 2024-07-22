import tkinter as tk
from tkinter import messagebox

# Function to calculate the tax
def calculate_tax():
    try:
        income = float(entry_income.get())
        tax_rate = float(entry_tax_rate.get()) / 100
        tax_amount = income * tax_rate
        total_income = income - tax_amount
        
        # Display the results
        label_tax_amount.config(text=f"Tax Amount: ${tax_amount:.2f}")
        label_total_income.config(text=f"Total Income after Tax: ${total_income:.2f}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Tax Calculator")

# Create labels and entries for income and tax rate
label_income = tk.Label(root, text="Enter Income:")
label_income.grid(row=0, column=0, padx=10, pady=10)
entry_income = tk.Entry(root)
entry_income.grid(row=0, column=1, padx=10, pady=10)

label_tax_rate = tk.Label(root, text="Enter Tax Rate (%):")
label_tax_rate.grid(row=1, column=0, padx=10, pady=10)
entry_tax_rate = tk.Entry(root)
entry_tax_rate.grid(row=1, column=1, padx=10, pady=10)

# Button to calculate tax
button_calculate = tk.Button(root, text="Calculate Tax", command=calculate_tax)
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Labels to display results
label_tax_amount = tk.Label(root, text="Tax Amount: ")
label_tax_amount.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

label_total_income = tk.Label(root, text="Total Income after Tax: ")
label_total_income.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Start the main tkinter loop
root.mainloop()
