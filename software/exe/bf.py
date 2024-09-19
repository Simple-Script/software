import tkinter as tk
from tkinter import filedialog
import subprocess

def decode_brainfuck(code):
    # Brainfuck interpreter logic remains the same
    code = ''.join(filter(lambda x: x in ('<', '>', '+', '-', '.', ',', '[', ']'), code))
    memory = [0] * 30000
    pointer = 0
    output = ''
    loop_stack = []
    i = 0

    while i < len(code):
        command = code[i]
        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output += chr(memory[pointer])
        elif command == ',':
            pass  # Input not handled
        elif command == '[':
            if memory[pointer] == 0:
                open_brackets = 1
                while open_brackets > 0:
                    i += 1
                    if code[i] == '[':
                        open_brackets += 1
                    elif code[i] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(i)
        elif command == ']':
            if memory[pointer] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1

    return output

def load_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        code = file.read()
        output = decode_brainfuck(code)
        with open("output.html", "w") as f:
            f.write(f"<html><body><pre>{output}</pre></body></html>")
        subprocess.Popen(["start", "output.html"], shell=True)

root = tk.Tk()
root.title("Brainfuck File Decoder")

load_button = tk.Button(root, text="Load Brainfuck File", command=load_file)
load_button.pack()

root.mainloop()
