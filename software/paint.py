import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw

class AdvancedDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Drawing App")
        
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()
        
        self.brush_size = 5
        self.color = "black"
        self.last_x, self.last_y = None, None
        self.history = []
        
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        
        self.create_widgets()
        
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

    def create_widgets(self):
        self.size_slider = tk.Scale(self.root, from_=1, to=50, orient=tk.HORIZONTAL, label="Brush Size")
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT)

        self.color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(self.root, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT)

        self.undo_button = tk.Button(self.root, text="Undo", command=self.undo)
        self.undo_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_image)
        self.save_button.pack(side=tk.LEFT)

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def use_eraser(self):
        self.color = "white"

    def paint(self, event):
        if self.last_x and self.last_y:
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.color, width=self.brush_size)
            self.draw.line([self.last_x, self.last_y, x, y], fill=self.color, width=self.brush_size)
            self.history.append(self.image.copy())
        self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def undo(self):
        if self.history:
            self.image = self.history.pop()
            self.redraw_canvas()

    def redraw_canvas(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG files", "*.jpeg")])
        if file_path:
            self.image.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedDrawingApp(root)
    root.mainloop()
