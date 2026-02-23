import tkinter as tk
from tkinter import messagebox

def displayData():
    # Use the .get() method on the entry widget objects
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()

    output = (
        f'Welcome to tkinter, {first} \n'
        'You entered:\n'
        f"Name: {first} {last}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
    )
    messagebox.showinfo("Tkinter Welcome Message", output)


def Clear():
    """Deletes all characters in the entry box."""
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)

# --- Main Form ---
root = tk.Tk()
root.title("tkinter Form")
root.minsize(500,300)

# --- Label Frame ---
lblFrPerson = tk.LabelFrame(root, text="Personal Information")
lblFrPerson.pack()

lblFirst = tk.Label(lblFrPerson, text="*First Name: ", bg="blue", fg="white")
lblFirst.grid(row=0, column=0, padx=5, pady=3)

entFirst = tk.Entry(lblFrPerson)
entFirst.grid(row=0, column=1)

# --- Last Name label/entry ---
lblLast = tk.Label(lblFrPerson, text="*Last Name: ", bg="blue", fg="white")
lblLast.grid(row=1, column=0, padx=5, pady=3)

entLast = tk.Entry(lblFrPerson)
entLast.grid(row=1, column=1)

# --- Email label/entry ---

lblEmail = tk.Label(lblFrPerson, text="Email: ")
lblEmail.grid(row=2, column=0, padx=5, pady=3)

entEmail = tk.Entry(lblFrPerson)
entEmail.grid(row=2, column=1)

# --- Phone label/entry ---

lblPhone = tk.Label(lblFrPerson, text="Phone: ")
lblPhone.grid(row=3, column=0, padx=5, pady=3)

entPhone = tk.Entry(lblFrPerson)
entPhone.grid(row=3, column=1)

# --- Button Frame ---
fraButtons = tk.Frame(root)
fraButtons.pack()

# --- Buttons ---
btnS = tk.Button(fraButtons, text="Submit", width=5, command=displayData)
btnS.pack(side=tk.LEFT, padx=5)

btnR = tk.Button(fraButtons, text="Reset",width=5, command=Clear)
btnR.pack(side=tk.LEFT, padx=5)

btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy)
btnQ.pack(side=tk.LEFT, padx=5)

root.mainloop()