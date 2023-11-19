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


        #Text column
        self.text_gen_label = customtkinter.CTkLabel(self, height=33, corner_radius=5, fg_color=("gray95", "gray22"), text="Text Generator", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.text_gen_label.grid(row=0, column=0, padx=(20, 20), pady=(15, 0), sticky="new")

        self.text_prompt = customtkinter.CTkTextbox(self, height=110)
        self.text_prompt.grid(row=0, column=0, padx=(20, 20), pady=(60, 0), sticky="new")

        self.text_gen_button = customtkinter.CTkButton(self, height=40, text="Generate")
        self.text_gen_button.grid(row=1, column=0, padx=(20, 20), pady=(10, 0), sticky="new")

        self.text_complete = customtkinter.CTkTextbox(self, width=250, height=450)
        self.text_complete.grid(row=1, column=0, padx=(20, 20), pady=(60, 0), sticky="nsew")

        self.appearance_mode_label = customtkinter.CTkLabel(self, bg_color=("gray95", "gray22"), text="Appearance Mode:")
        self.appearance_mode_label.grid(row=2, column=0, padx=(50, 150), pady=(0, 40), sticky="sw")

        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"])
        self.appearance_mode_option_menu.grid(row=2, column=0, padx=(35, 150), pady=(20, 10), sticky="sw")


app = App()
app.mainloop()