import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import webbrowser
import os

def run_html_code():
    html_code = simpledialog.askstring("Input HTML", "Please enter your HTML code:")
    if html_code:
        with open("temp.html", "w") as file:
            file.write(html_code)
        webbrowser.open("temp.html")

def run_html_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    if file_path:
        webbrowser.open(file_path)

def main():
    root = tk.Tk()
    root.title("HTML Runner with Custom Window Size")
    root.geometry("300x150")  # Set custom window size
    
    run_code_button = tk.Button(root, text="Run HTML Code", command=run_html_code)
    run_code_button.pack(pady=10)

    run_file_button = tk.Button(root, text="Run HTML File", command=run_html_file)
    run_file_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
