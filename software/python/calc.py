import tkinter as tk

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")

        self.result_var = tk.StringVar()
        self.memory = 0

        self.entry = tk.Entry(master, textvariable=self.result_var, width=16, font=('Arial', 24), bd=5, insertwidth=4, bg="light green", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'M+', 'M-', 'MR', 'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'C':
            self.result_var.set("")
        elif char == 'M+':
            self.memory += float(self.result_var.get())
        elif char == 'M-':
            self.memory -= float(self.result_var.get())
        elif char == 'MR':
            self.result_var.set(self.memory)
        else:
            self.result_var.set(self.result_var.get() + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = AdvancedCalculator(root)
    root.mainloop()
