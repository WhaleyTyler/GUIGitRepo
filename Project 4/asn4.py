import tkinter as tk
from PIL import ImageTk, Image

class FoodGUI:
    def __init__(self):
        # Create Main Window
        self.root = tk.Tk()
        self.root.title("Food Viewer")
        self.root.minsize(400, 300)

        # Create Frames
        self.img_frame = tk.Frame(self.root)
        self.rbdBtn_frame = tk.Frame(self.root)

        # Create Label for image
        self.lbl = tk.Label(self.img_frame)
        self.lbl.pack()
        self.img_frame.pack()

        # File names
        self.img1 = "chicken.jpg"
        self.img2 = "pie.jpg"
        self.img3 = "pizza.jpg"
        self.img4 = "steak.jpg"

        # Images
        self.imgOne = ImageTk.PhotoImage(Image.open(self.img1).resize((400, 300)))
        self.imgTwo = ImageTk.PhotoImage(Image.open(self.img2).resize((400, 300)))
        self.imgThree = ImageTk.PhotoImage(Image.open(self.img3).resize((350, 300)))
        self.imgFour = ImageTk.PhotoImage(Image.open(self.img4).resize((300, 300)))

        # IntVar for Radiobutton selection
        self.var = tk.IntVar()
        self.var.set(1)  # default to Chicken

        # Create Radio buttons
        self.radio_a = tk.Radiobutton(self.rbdBtn_frame, text = "Chicken", variable = self.var, value = 1, command = self.on_radio_select)
        self.radio_a.pack(side="left", padx=5)

        self.radio_b = tk.Radiobutton(self.rbdBtn_frame, text = "Pie", variable = self.var, value = 2, command = self.on_radio_select)
        self.radio_b.pack(side="left", padx=5)

        self.radio_c = tk.Radiobutton(self.rbdBtn_frame, text = "Pizza", variable=self.var, value=3, command=self.on_radio_select)
        self.radio_c.pack(side="left", padx=5)

        self.radio_d = tk.Radiobutton(self.rbdBtn_frame, text = "Steak", variable=self.var, value=4, command=self.on_radio_select)
        self.radio_d.pack(side="left", padx=5)

        self.rbdBtn_frame.pack()

        # Show default image
        self.on_radio_select()

        self.root.mainloop()

    def on_radio_select(self):
        choice = self.var.get()

        # Update image based on user choice
        if choice == 1:
            self.lbl.config(image = self.imgOne)
            self.lbl.image = self.imgOne
        elif choice == 2:
            self.lbl.config(image = self.imgTwo)
            self.lbl.image = self.imgTwo
        elif choice == 3:
            self.lbl.config(image = self.imgThree)
            self.lbl.image = self.imgThree
        elif choice == 4:
            self.lbl.config(image = self.imgFour)
            self.lbl.image = self.imgFour


if __name__ == '__main__':
    FoodGUI()