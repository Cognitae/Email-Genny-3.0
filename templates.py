import tkinter
import customtkinter as ctk

class TemplatesPage(ctk.CTk):
    def __init__(self):
        super().__init__()

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
        # Buttons
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.grid(row=2, column=1, padx=(20,20), pady=(180,0), sticky="se")

    def go_back(self):
        # TODO: Implement the logic to switch back to the main page
        pass
 

    def save_template_1(self):
        # TODO: Implement the save logic for template 1
        pass

    def save_template_2(self):
        # TODO: Implement the save logic for template 2
        pass

    def save_template_3(self):
        # TODO: Implement the save logic for template 3
        pass
    

# Run the application
if __name__ == "__main__":
    app = TemplatesPage()
    app.mainloop()
