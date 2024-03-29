import json
import tkinter
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import pyperclip  # for clipboard operations
from tkinter import Toplevel, Label

class TemplatesPage(ctk.CTk):
    def __init__(self, master=None):
        super().__init__()
        
        self.master = master  # The master window (EmailGenny instance)

        # Hide the master window
        self.master.withdraw()

        # Load the image at the page level
        #self.templates_image = ctk.CTkImage(light_image=Image.open("Resources/templates.png"),
                                            #size=(200, 200))

        # Use templates_image in the label
        #self.templates_label = ctk.CTkLabel(self, image=self.templates_image, text="")
        #self.templates_label.place(x=0, y=0)

        # Textboxes for the email templates
        self.template_textbox_1 = ctk.CTkTextbox(self, width=600, height=125)
        self.template_textbox_2 = ctk.CTkTextbox(self, width=600, height=125)
        self.template_textbox_3 = ctk.CTkTextbox(self, width=600, height=125)

        self.template_textbox_1.grid(row=0, column=1, padx=20, pady=30, sticky='e')
        self.template_textbox_2.grid(row=1, column=1, padx=20, pady=30, sticky='e')
        self.template_textbox_3.grid(row=2, column=1, padx=20, pady=30, sticky='e')

        # Buttons for saving the templates
        self.save_button_1 = ctk.CTkButton(self, text="Save Template 1", command=self.save_template_1,)
        self.save_button_2 = ctk.CTkButton(self, text="Save Template 2", command=self.save_template_2,)
        self.save_button_3 = ctk.CTkButton(self, text="Save Template 3", command=self.save_template_3,)

        self.save_button_1.grid(row=0, column=1, padx=(0,20), pady=(10, 0), sticky='se')
        self.save_button_2.grid(row=1, column=1, padx=(0,20), pady=(10, 0), sticky='se')
        self.save_button_3.grid(row=2, column=1, padx=(0,20), pady=(10, 0), sticky='se')
        
        # Load the templates from the JSON file
        try:
            with open("templates.json", "r") as f:
                templates = json.load(f)
        except FileNotFoundError:
            templates = {}

        # Load the templates into the text boxes
        self.template_textbox_1.insert("1.0", templates.get("template_1", ""))
        self.template_textbox_2.insert("1.0", templates.get("template_2", ""))
        self.template_textbox_3.insert("1.0", templates.get("template_3", ""))

        # Buttons
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.grid(row=2, column=0, padx=(20,20), pady=(150,0), sticky="se")
        
    def go_back(self):
        # Call the master's go_back method
        self.master.go_back()

    def save_template_1(self):
        # Get the template text
        template_text = self.template_textbox_1.get("1.0", "end-1c")

        # Load the existing templates from the JSON file
        try:
            with open("templates.json", "r") as f:
                templates = json.load(f)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty dictionary
            templates = {}

        # Update the template text in the dictionary
        templates["template_1"] = template_text
        
        # Update the selected template index in the dictionary
        templates["selected_template"] = 1

        # Save the updated templates back to the JSON file
        with open("templates.json", "w") as f:
            json.dump(templates, f)
            
        # Show the success message using CTkMessagebox
        CTkMessagebox(title="Template 1 Successfully Saved", message="Have Peace of Mind!\nRest Easy Knowing Your Edits Have Been Saved!", icon="check")

    def save_template_2(self):
        template_text = self.template_textbox_2.get("1.0", "end-1c")

        try:
            with open("templates.json", "r") as f:
                templates = json.load(f)
        except FileNotFoundError:
            templates = {}

        # Update the template text in the dictionary
        templates["template_2"] = template_text
        
        # Update the selected template index in the dictionary
        templates["selected_template"] = 2


        with open("templates.json", "w") as f:
            json.dump(templates, f)
            
        # Show the success message using CTkMessagebox
        CTkMessagebox(title="Template 2 Successfully Saved", message="Have Peace of Mind!\nRest Easy Knowing Your Edits Have Been Saved!", icon="check")

    def save_template_3(self):
        template_text = self.template_textbox_3.get("1.0", "end-1c")

        try:
            with open("templates.json", "r") as f:
                templates = json.load(f)
        except FileNotFoundError:
            templates = {}

        # Update the template text in the dictionary
        templates["template_3"] = template_text
        
        # Update the selected template index in the dictionary
        templates["selected_template"] = 3


        with open("templates.json", "w") as f:
            json.dump(templates, f)
            
        # Show the success message using CTkMessagebox
        CTkMessagebox(title="Template 3 Successfully Saved", message="Have Peace of Mind!\nRest Easy Knowing Your Edits Have Been Saved!", icon="check")
            
class EmailGenny(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Load the image at the application level
        self.logo_image = ctk.CTkImage(light_image=Image.open("Resources/logo.png"),
                                        size=(200, 200))

        # Then you can use logo_image wherever you need it
        self.image_label = ctk.CTkLabel(self, image=self.logo_image, text="")
        self.image_label.place(x=0, y=0)
        
        # Initialize the selected template variable
        self.template_var = tkinter.IntVar()
        
        # Set up the main window
        self.title("E-Mail Genny")
        self.geometry("900x580")

        # Frame for template selection radio buttons
        self.template_frame = ctk.CTkFrame(self, border_width=1, corner_radius=10)
        self.template_frame.grid(row=1, column=0, padx=(30,0), pady=(50,80))

        # Label for the template selection
        self.template_label = ctk.CTkLabel(self.template_frame, text="         Templates         ")
        self.template_label.grid(row=0, column=0, padx=10, pady=(20,10))

        # Radio buttons for template selection
        self.template_radio_1 = ctk.CTkRadioButton(self.template_frame, text="Initial Email", variable=self.template_var, value=1)
        self.template_radio_2 = ctk.CTkRadioButton(self.template_frame, text="In The Past ", variable=self.template_var, value=2)
        self.template_radio_3 = ctk.CTkRadioButton(self.template_frame, text="No Reply   ", variable=self.template_var, value=3)
        self.template_radio_1.grid(row=1, column=0, padx=10, pady=10)
        self.template_radio_2.grid(row=2, column=0, padx=10, pady=10)
        self.template_radio_3.grid(row=3, column=0, padx=10, pady=10)

        # Textbox for the generated email
        self.email_textbox = ctk.CTkTextbox(self, width=550, height=250)
        self.email_textbox.insert(1.0, "Email Generated Here...") #Placeholder text
        self.email_textbox.bind('<FocusIn>') #self.clear_textbox) #Clear placeholder text when clicked
        self.email_textbox.grid(row=1, column=1, padx=(5,150), pady=(40,0)) 
        
        # Fields for the variables
        self.var_frame = ctk.CTkFrame(self)
        self.var_frame.grid(row=0, column=1, padx=(20,160), pady=20)

        self.var_labels = []
        self.var_entries = []
        var_names = ["Company Name", "Contact Name", "Craft", "Module", "Number of Images", "Video"]

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

        # Frame for the subject line and the copy button
        self.subject_frame = ctk.CTkFrame(self)
        self.subject_frame.grid(row=1, column=1, padx=(55,200), pady=(0,290))

        # Entry for the generated subject line
        self.subject_entry = ctk.CTkEntry(self.subject_frame, width=520)  # Reduce the width to make room for the button
        self.subject_entry.insert(0, "Subject Generated Here...")  # Insert guiding text
        self.subject_entry.bind('<FocusIn>')  # Bind function to clear text on focus
        self.subject_entry.pack(side=tkinter.LEFT)  # Pack to the left side of the frame

        # Button for copying the subject line
        self.copy_subject_button = ctk.CTkButton(self.subject_frame, text="C", command=self.copy_subject, width=20)
        self.copy_subject_button.pack(side=tkinter.RIGHT)  # Pack to the right side of the frame



        # Buttons
        self.generate_button = ctk.CTkButton(self, text="Generate Email", command=self.generate_email,)
        self.copy_button = ctk.CTkButton(self, text="Copy", command=self.copy_email , width=20)
        self.edit_button = ctk.CTkButton(self, text="Edit Templates", command=self.edit_templates, width=135)

        self.generate_button.grid(row=3, column=1, padx=(50,225), pady=(15,0))
        self.copy_button.grid(row=3, column=1, padx=(400, 40), pady=(15,0))
        self.edit_button.place(x=30, y=460)

        # Set up the main window
        self.title("E-Mail Genny")
        self.geometry("900x580")

        # Initialize the appearance mode as Dark Mode
        self.appearance_mode = ctk.StringVar(value="dark")
        ctk.set_appearance_mode(self.appearance_mode.get())

        # Set up the switch in the bottom left corner
        self.darkmode_switch = ctk.CTkSwitch(self, text="Toggle Dark Mode", variable=self.appearance_mode,
                                             onvalue="dark", offvalue="light", command=self.toggle_dark_mode)
        # To place the switch at the bottom left, we use the place() method instead of grid().
        self.darkmode_switch.place(relx=0, rely=1, x=20, y=-20, anchor='sw')
        
        self.load_templates()  # Add this line at the end of the __init__ method
        # Load the templates from the JSON file
        try:
            with open("templates.json", "r") as f:
                templates = json.load(f)
        except FileNotFoundError:
            templates = {}

        # Load the selected template index
        self.template_var.set(templates.get("selected_template", 1))

    # This function can be put at the top of your EmailGenny class
    @staticmethod
    def generate_module_sentence(here_text, module):
        if module:
            return f"""{here_text} to use in our module on "{module}"."""
        else:
            return f"{here_text}."
    @staticmethod    
    def generate_video_sentence(here_text, craft, video):
        if video:
            return f"""{here_text} to use in our CraftPro {craft} video on "{video}"."""
        else:
            return f"{here_text}."    
    
    @staticmethod
    def generate_sentence(here_text, module, craft, video):
        if module:
            return EmailGenny.generate_module_sentence(here_text, module)
        elif video:
            return EmailGenny.generate_video_sentence(here_text, craft, video)
        else:
            return f"{here_text}."
        

    def generate_email(self):
        try:    
            # Retrieve user inputs
            company_name = self.var_entries[0].get().strip()  # Company Name
            name = self.var_entries[1].get().strip()  # Contact Name
            craft = self.var_entries[2].get().strip()  # Craft
            module = self.var_entries[3].get().strip()  # Module
            # Ensure the number of images is a non-negative integer
            num_images_str = self.var_entries[4].get().strip()  # Number of Images
            if not num_images_str:  # If the field is empty
                raise ValueError("Number of Images must be filled out.")
            if not num_images_str.isdigit():
                raise ValueError("Number of Images must be a non-negative integer.")
            image_numbers = int(num_images_str)
            if image_numbers <= 0:  # If the field is zero or negative
                raise ValueError("Number of Images must be greater than zero.")
            video = self.var_entries[5].get().strip()  # Video
            # Check if both module and video are filled in
            if module and video:
                raise ValueError("Please only fill out either the 'Module' field or the 'Video' field, not both. Leave both blank if unsure.")
        except ValueError as e:
            CTkMessagebox(title="Invalid Input", message=str(e), icon="cancel")

        # Determine the text based on the number of images
        if image_numbers == 1:
            image_text = "this image"
            here_text = "Here"
            imag_text = "image"
            some_text = "an"
        else:
            image_text = "these images"
            imag_text = "images"
            some_text = "some"
            here_text_list = ["Here"] * image_numbers
            if image_numbers > 9:  # If there are more than 15 images
                here_text = "Here"
            elif image_numbers > 2:
                here_text = ", ".join(here_text_list[:-1]) + ", and " + here_text_list[-1]    
            else:
                here_text = " and ".join(here_text_list)

        # Generate the subject line
        subject_line = f"Permission to use {company_name} {imag_text} for NCCER {craft} Curriculum"
        self.subject_entry.delete(0, tkinter.END)  # Clear the previous subject line
        self.subject_entry.insert(0, subject_line)  # Insert the new subject line


        # Generate module sentence based on whether module is provided
        sentence = self.generate_sentence(here_text, module, craft, video)


        # Retrieve the selected template and format it with actual values
        selected_template_index = self.template_var.get() - 1  # Subtract 1 because the radio buttons start at 1
        selected_template_text = [self.template_1, self.template_2, self.template_3][selected_template_index]

        generated_email = selected_template_text.format(
            name=name,
            craft=craft,
            image_text=image_text,
            imag_text=imag_text,
            some_text=some_text,
            here_text=sentence,  # Use the module_sentence here
            company_name=company_name,
            video=video
        )
        self.email_textbox.delete("1.0", tkinter.END)  # Clear the previous email body
        self.email_textbox.insert(tkinter.END, generated_email)  # Insert the new email body

    def toggle_dark_mode(self):
        # Set the appearance mode based on the switch's value
        ctk.set_appearance_mode(self.appearance_mode.get())


    # Load the templates from the JSON file
        self.load_templates()

    def load_templates(self):
        # Try to open the JSON file and load the templates
        try:
            with open("templates.json", "r") as f:
                templates = json.load(f)
        except FileNotFoundError:
            # If the file does not exist, use default templates
            templates = {
                "template_1": "Default Template 1",
                "template_2": "Default Template 2",
                "template_3": "Default Template 3",
            }

        # Load the templates into variables
        self.template_1 = templates.get("template_1", "")
        self.template_2 = templates.get("template_2", "")
        self.template_3 = templates.get("template_3", "")
        
    def copy_email(self):
        # Get the generated email text
        email_text = self.email_textbox.get("1.0", "end-1c")

        # Copy the email to the clipboard
        pyperclip.copy(email_text)
        
        # Create a new Toplevel window
        pop_up = Toplevel(self)
        
        # Customize the appearance of the pop-up
        pop_up.geometry("175x50")  # set size
        pop_up.configure(bg="black")  # set background color
        pop_up.overrideredirect(True)  # remove border
        pop_up.configure(relief="ridge")  # round the corners
        # Add a label with your message
        Label(pop_up, text="Copied to clipboard!", bg="black", fg="white").place(relx=0.5, rely=0.5, anchor="center")

        # Schedule the pop-up to destroy itself after 1 seconds (1000 milliseconds)
        pop_up.after(1000, pop_up.destroy)
        # Calculate the position of the pop-up window
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        window_x = self.winfo_x()
        window_y = self.winfo_y()

        pop_up_width = 125
        pop_up_height = 25

        pop_up_x = window_x + (window_width // 2) - (pop_up_width // 2)
        pop_up_y = window_y

        # Set the position of the pop-up window
        pop_up.geometry(f"+{pop_up_x}+{pop_up_y}")
        
    #def clear_subject_entry(self, event):
        #self.subject_entry.delete(0, 'end')  # Clear the entry field
        
    def copy_subject(self):
        # Get the generated subject line
        subject_line = self.subject_entry.get()

        # Copy the subject line to the clipboard
        pyperclip.copy(subject_line)

        # Create a new Toplevel window
        pop_up = Toplevel(self)

        # Customize the appearance of the pop-up
        pop_up.geometry("175x50")  # set size
        pop_up.configure(bg="black")  # set background color
        pop_up.overrideredirect(True)  # remove border
        pop_up.configure(relief="ridge")  # round the corners
        # Add a label with your message
        Label(pop_up, text="Subject line copied to clipboard!", bg="black", fg="white").place(relx=0.5, rely=0.5, anchor="center")

        # Schedule the pop-up to destroy itself after 1 seconds (1000 milliseconds)
        pop_up.after(1000, pop_up.destroy)
        # Calculate the position of the pop-up window
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        window_x = self.winfo_x()
        window_y = self.winfo_y()

        pop_up_width = 125
        pop_up_height = 25

        pop_up_x = window_x + (window_width // 2) - (pop_up_width // 2)
        pop_up_y = window_y

        # Set the position of the pop-up window
        pop_up.geometry(f"+{pop_up_x}+{pop_up_y}")
    
    

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
        self.load_templates()  # Add this line at the end of the go_back method
            
    # Run the application
if __name__ == "__main__":
    app = EmailGenny()
    app.mainloop()
