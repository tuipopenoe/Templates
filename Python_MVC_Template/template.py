#!python2
# Tui Popenoe
# MVC Template


from tkinter import *

class TemplateController():
    def __init__(self, parent):
        self.parent = parent
        # Initialize Model
        self.model = TemplateModel(self)
        # Initialize View
        self.view = TemplateView(self)

        # Initialize properties in view
        pass

        # Initialize properties in model
        pass

    # event handler - add functions called by command attribute in view
    def event_handler_method(self):
        pass

    # delegates - add functions called by delegates in model or view
    def model_did_change_delegate(self):
        pass


class TemplateView(Frame):
    def load_view(self):
        pass
    def __init__(self, vc):
        # Create the view
        self.frame = Frame()
        self.frame.grid(row=0, column=0)

        # Set the delegate pointer
        self.vc = vc

        # Control variables 
        control_var_one = StringVar()
        control_var_one = ('nil')

    # Get/Set for control variables
    def get_control_var_one(self):
        return self.entry_text.get()
    def set_control_var_one(self, text):
        self.entry_text.set(text)

class TemplateModel():
    def __init__(self, vc):
        # Set delegate pointer
        self.vc = vc
        # Initialize model
        self.template_model = 0

    # Delegate, model calls on internal change
    def model_did_change(self):
        self.vc.list_changed_delegate()
    # Get/Set for model
    def get_model(self):
        return self.template_model
    def set_model(self, data):
        self.template_model = data
        # Delegate called on change
        self.model_did_change()

def main():
    root = Tk()
    frame = Frame(root)
    root.title('MVC Template')
    app = TemplateController(root)
    root.mainloop()

if __name__ == '__main__':
    main()