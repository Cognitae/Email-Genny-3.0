import tkinter
import customtkinter as ctk
from PIL import Image, ImageTk

class TemplatesPage(ctk.CTk):
    def __init__(self, master=None):
        super().__init__()

        self.master = master  # The master window (EmailGenny instance)

        # Hide the master window
        self.master.withdraw()

        # Set up the main window
        self.title("E-Mail Genny - Templates")
        self.geometry("900x610")

        # Textboxes for the email templates
        self.template_textbox_1 = ctk.CTkTextbox(self, width=600, height=150)
        self.template_textbox_2 = ctk.CTkTextbox(self, width=600, height=150)
        self.template_textbox_3 = ctk.CTkTextbox(self, width=600, height=150)

        self.template_textbox_1.grid(row=0, column=1, padx=20, pady=20, sticky='w')
        self.template_textbox_2.grid(row=1, column=1, padx=20, pady=20, sticky='w')
        self.template_textbox_3.grid(row=2, column=1, padx=20, pady=20, sticky='w')

        # Buttons for saving the templates
        self.save_button_1 = ctk.CTkButton(self, text="Save Template 1", command=self.save_template_1,)
        self.save_button_2 = ctk.CTkButton(self, text="Save Template 2", command=self.save_template_2,)
        self.save_button_3 = ctk.CTkButton(self, text="Save Template 3", command=self.save_template_3,)

        self.save_button_1.grid(row=0, column=0, padx=20, pady=(20, 0), sticky='sw')
        self.save_button_2.grid(row=1, column=0, padx=20, pady=(20, 0), sticky='sw')
        self.save_button_3.grid(row=2, column=0, padx=20, pady=(20, 0), sticky='sw')

        # Buttons
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.grid(row=2, column=1, padx=(20,20), pady=(180,0), sticky="se")

    def go_back(self):
        # Call the master's go_back method
        self.master.go_back()

    def save_template_1(self):
        # TODO: Implement the save logic for template 1
        pass

    def save_template_2(self):
        # TODO: Implement the save logic for template 2
        pass

    def save_template_3(self):
        # TODO: Implement the save logic for template 3
        pass


class EmailGenny(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.title("E-Mail Genny")
        self.geometry("900x610")

        # Frame for template selection radio buttons
        self.template_frame = ctk.CTkFrame(self, border_width=1, corner_radius=10)
        self.template_frame.grid(row=2, column=0, padx=25, pady=(100,0))

        # Label for the template selection
        self.template_label = ctk.CTkLabel(self.template_frame, text="              Templates              ")
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
        self.email_textbox.grid(row=2, column=1, padx=(5,150), pady=(30,0))

        # Fields for the variables
        self.var_frame = ctk.CTkFrame(self)
        self.var_frame.grid(row=0, column=1, padx=(20,160), pady=20)

        self.var_labels = []
        self.var_entries = []
        var_names = ["Company Name", "Contact Name", "Craft", "Module", "Number of Images", "Custom Var"]

        for i, name in enumerate(var_names):
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
        self.subject_entry.grid(row=1, column=1, padx=(55,200), pady=(40,0))

        # Buttons
        self.generate_button = ctk.CTkButton(self, text="Generate Email", command=self.generate_email,)
        self.copy_button = ctk.CTkButton(self, text="Copy", command=self.copy_email , width=20)
        self.edit_button = ctk.CTkButton(self, text="Edit Templates", command=self.edit_templates, width=120)

        self.generate_button.grid(row=3, column=1, padx=(50,225), pady=(15,20))
        self.copy_button.grid(row=3, column=1, padx=(400, 40), pady=(15,20))
        self.edit_button.place(x=47, y=300)

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
        self.darkmode_switch.place(relx=0, rely=1, x=20, y=-20, anchor='sw')

        image = Image.open("Resources/logo.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(image) 
        self.logo_label = ctk.CTkLabel(self, image=self.logo, text="")  # Create a label with the logo
        self.logo_label.grid(row=0, column=0, padx=0, pady=0)  # Place the logo label in the grid

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
        try:
            # Save the current window geometry
            self.prev_geometry = self.winfo_geometry()
            # Open the TemplatesPage window
            self.templates_page = TemplatesPage(master=self)
            self.templates_page.geometry(self.prev_geometry)
            self.templates_page.mainloop()
        except Exception as e:
            print(f"An error occurred: {e}")

    def go_back(self):
    # Destroy the TemplatesPage window and show the EmailGenny window
        self.templates_page.destroy()
        self.templates_page = None
        # Restore the previous window geometry
        self.geometry(self.prev_geometry)
        self.deiconify()

# Run the application
if __name__ == "__main__":
    app = EmailGenny()
    app.mainloop()
