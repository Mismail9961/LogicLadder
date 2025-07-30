import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
        root.title(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text.get("1.0", tk.END))
        root.title(f"Simple Text Editor - {filepath}")
        messagebox.showinfo("Success", "File saved successfully!")

# Create main window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# Add text area
text = tk.Text(root, wrap="word")
text.pack(expand=1, fill="both")

# Create menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Run the application
root.mainloop()
