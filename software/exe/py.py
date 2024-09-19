import tkinter as tk
from tkinter import scrolledtext, filedialog
import sys
import io

class CodeExecutor:
    def __init__(self, master):
        self.master = master
        master.title("Python Code Executor")

        self.label = tk.Label(master, text="Enter Python Code or Load a File:")
        self.label.pack()

        self.code_input = scrolledtext.ScrolledText(master, width=50, height=10)
        self.code_input.pack()

        self.load_button = tk.Button(master, text="Load File", command=self.load_file)
        self.load_button.pack()

        self.run_button = tk.Button(master, text="Run Code", command=self.run_code)
        self.run_button.pack()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, 'r') as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)

    def run_code(self):
        code = self.code_input.get("1.0", tk.END)
        output_window = tk.Toplevel(self.master)
        output_window.title("Output")

        output = io.StringIO()
        sys.stdout = output

        try:
            exec(code)
        except Exception as e:
            print(f"Error: {e}")

        sys.stdout = sys.__stdout__
        output_text = output.getvalue()

        output_display = scrolledtext.ScrolledText(output_window, width=50, height=10)
        output_display.pack()
        output_display.insert(tk.END, output_text)

if __name__ == "__main__":
    root = tk.Tk()
    executor = CodeExecutor(root)
    root.mainloop()
