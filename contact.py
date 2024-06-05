import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont

# Initialize the main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("800x600")
root.configure(bg='#f0f4c3')

# List to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if not name or not phone:
        messagebox.showwarning("Warning", "Name and phone number are required.")
        return
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    update_contact_list()
    clear_entries()

# Function to update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to search contacts
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if not search_term:
        return
    result = [c for c in contacts if search_term.lower() in c['name'].lower() or search_term in c['phone']]
    if not result:
        messagebox.showinfo("Search Result", "No contact found.")
    else:
        contact_listbox.delete(0, tk.END)
        for contact in result:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to update a contact
def update_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a contact to update.")
        return
    
    selected_index = selected_index[0]
    contact = contacts[selected_index]
    
    name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact['name'])
    phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact['phone'])
    email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact['email'])
    address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact['address'])
    
    contacts[selected_index] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    update_contact_list()

# Function to delete a contact
def delete_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
        return
    
    selected_index = selected_index[0]
    del contacts[selected_index]
    update_contact_list()

# Fonts
heading_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
button_font = tkfont.Font(family="Helvetica", size=12)

# Labels and Entry widgets for contact details
tk.Label(root, text="Contact Manager", bg='#f0f4c3', font=heading_font).pack(pady=20)

tk.Label(root, text="Name:", bg='#f0f4c3', font=("Arial", 12)).pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack(pady=5)

tk.Label(root, text="Phone:", bg='#f0f4c3', font=("Arial", 12)).pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack(pady=5)

tk.Label(root, text="Email:", bg='#f0f4c3', font=("Arial", 12)).pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

tk.Label(root, text="Address:", bg='#f0f4c3', font=("Arial", 12)).pack()
address_entry = tk.Entry(root, width=50)
address_entry.pack(pady=5)

# Buttons for adding, searching, updating, and deleting contacts
tk.Button(root, text="Add Contact", command=add_contact, bg='#81c784', fg='white', font=button_font).pack(pady=10)
tk.Button(root, text="Search Contact", command=search_contact, bg='#ffcc80', fg='white', font=button_font).pack(pady=10)
tk.Button(root, text="Update Contact", command=update_contact, bg='#64b5f6', fg='white', font=button_font).pack(pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact, bg='#e57373', fg='white', font=button_font).pack(pady=10)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, width=80, height=10)
contact_listbox.pack(pady=20)

# Run the application
root.mainloop()
