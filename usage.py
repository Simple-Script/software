import tkinter as tk
import psutil
import GPUtil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResourceMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Resource Monitor")
        self.root.overrideredirect(True)  # Remove title bar
        self.root.geometry("+{}+{}".format(root.winfo_screenwidth() - 300, 0))  # Position in top right

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

        self.update_resources()

    def update_resources(self):
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        gpus = GPUtil.getGPUs()
        gpu_usage = gpus[0].load * 100 if gpus else 0

        self.ax.clear()
        self.ax.bar(['CPU', 'RAM', 'GPU'], [cpu_usage, ram_usage, gpu_usage], color=['blue', 'green', 'red'])
        self.ax.set_ylim(0, 100)
        self.ax.set_title('Resource Usage (%)')
        self.canvas.draw()

        self.root.after(1000, self.update_resources)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    monitor = ResourceMonitor(root)
    root.mainloop()