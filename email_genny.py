import tkinter
import tkinter.messagebox
import customtkinter as ctk

# Initialize the customtkinter appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
#ctk.set_default_color_theme(r"C:\Users\adamr\Documents\GitHub\Email Genny 3.0\cognitae_theme.json")

class EmailGenny(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.title("E-Mail Genny")
        self.geometry("900x610")

        # Frame for template selection radio buttons
        self.template_frame = ctk.CTkFrame(self, border_width=1, corner_radius=10)
        self.template_frame.grid(row=0, column=0, padx=20, pady=20)

        # Label for the template selection
        self.template_label = ctk.CTkLabel(self.template_frame, text="Templates")
        self.template_label.grid(row=0, column=0, padx=10, pady=10)

        # Radio buttons for template selection
        self.template_var = tkinter.IntVar()
        self.template_radio_1 = ctk.CTkRadioButton(self.template_frame, text="Template 1", variable=self.template_var, value=1)
        self.template_radio_2 = ctk.CTkRadioButton(self.template_frame, text="Template 2", variable=self.template_var, value=2)
        self.template_radio_3 = ctk.CTkRadioButton(self.template_frame, text="Template 3", variable=self.template_var, value=3)
        self.template_radio_1.grid(row=1, column=0, padx=10, pady=10)
        self.template_radio_2.grid(row=2, column=0, padx=10, pady=10)
        self.template_radio_3.grid(row=3, column=0, padx=10, pady=10)

        # Textbox for the generated email
        self.email_textbox = ctk.CTkTextbox(self, width=550, height=250)
        self.email_textbox.grid(row=2, column=1, padx=105, pady=(30,0))


        # Fields for the variables
        self.var_frame = ctk.CTkFrame(self)
        self.var_frame.grid(row=0, column=1, padx=20, pady=20)

        self.var_labels = []
        self.var_entries = []
        var_names = ["Company Name", "Contact Name", "Craft", "Module", "Number of Images", "Custom Var"]
        
        for i, name in enumerate(var_names):
            # Calculate the row and column for each variable.
            # For the first three variables, row is 0 and column goes from 0 to 2.
            # For the last three variables, row is 1 and column goes from 0 to 2
            # Create the entry field
            row = i // 2
            col = i % 2
            
            # Create the label
            label = ctk.CTkLabel(self.var_frame, text=name)
            label.grid(row=row, column=2*col, padx=10, pady=10)
            
            # Create the entry field
            entry = ctk.CTkEntry(self.var_frame)
            entry.grid(row=row, column=2*col + 1, padx=10, pady=10)
            
            self.var_labels.append(label)
            self.var_entries.append(entry)
            
            # Label and Entry for the generated subject line
            self.subject_entry = ctk.CTkEntry(self, width=550)
            self.subject_entry.grid(row=1, column=1, padx=105, pady=(40,0))
        
        # Buttons
        self.generate_button = ctk.CTkButton(self, text="Generate Email", command=self.generate_email,)
        self.copy_button = ctk.CTkButton(self, text="Copy", command=self.copy_email , width=20)
        self.edit_button = ctk.CTkButton(self, text="Edit Templates", command=self.edit_templates, width=120)
          
        self.generate_button.grid(row=3, column=1, padx=20, pady=10)
        self.copy_button.grid(row=3, column=1, padx=(500, 10), pady=10)
        self.edit_button.grid(row=1, column=0, padx=20, pady=20)
        
         # Set up the main window
        self.title("E-Mail Genny")
        self.geometry("900x610")

        # Initialize the appearance mode as Dark Mode
        self.appearance_mode = ctk.StringVar(value="dark")
        ctk.set_appearance_mode(self.appearance_mode.get())

        # Set up the switch in the bottom left corner
        self.darkmode_switch = ctk.CTkSwitch(self, text="Toggle Dark Mode", variable=self.appearance_mode,
                                             onvalue="dark", offvalue="light", command=self.toggle_dark_mode)
        # To place the switch at the bottom left, we use the place() method instead of grid().
        self.darkmode_switch.place(relx=0, rely=1, anchor='sw')

    def toggle_dark_mode(self):
        # Set the appearance mode based on the switch's value
        ctk.set_appearance_mode(self.appearance_mode.get())


    def generate_email(self):
        # TODO: Implement the email generation logic
        pass

    def copy_email(self):
        # TODO: Implement the email copying logic
        pass

    def edit_templates(self):
        # TODO: Implement the template editing logic
        pass



# Run the application
if __name__ == "__main__":
    app = EmailGenny()
    app.mainloop()
