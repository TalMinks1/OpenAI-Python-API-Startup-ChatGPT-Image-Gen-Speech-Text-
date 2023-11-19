import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Create window with title, size, and bg
        self.title("AIGenerator.py")
        self.geometry("1100x590")
        self.bg_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.bg_frame.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew")

        # configure grid layout (3x4)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2), weight=1)
        self.grid_rowconfigure(3, weight=1)



app = App()
app.mainloop()