import tkinter as tk
import random
import string

# Generate password function
def generate_password():
    length = int(length_entry.get())

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(length))

    result_var.set(password)


# Create window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.configure(bg="#0f172a")  # Dark background

# Title
title = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"),
                 fg="#22c55e", bg="#0f172a")
title.pack(pady=10)

# Length input
length_label = tk.Label(root, text="Password Length:", fg="white", bg="#0f172a")
length_label.pack()

length_entry = tk.Entry(root, justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password,
                         bg="#22c55e", fg="black", padx=10, pady=5)
generate_btn.pack(pady=10)

# Result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12),
                        fg="#38bdf8", bg="#0f172a")
result_label.pack(pady=10)

# Run app
root.mainloop()
