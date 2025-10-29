import tkinter as tk;
from time_logic import countdown_status;

class CountdownWidget:
    def __init__(self, root):
        self.root = root;
        
        # These will store the mouse position for dragging the widget around
        self.x = 0;
        self.y = 0;

        # Calling helper methods.
        self._setup_window();
        self._setup_widgets();
        self._bind_events();

    # A helper method to set up the main window's properties
    def _setup_window(self):
        # All the code to center the window and make it borderless.
        window_width = 1000;
        window_height = 100;

        screen_width = self.root.winfo_screenwidth();
        screen_height = self.root.winfo_screenheight();

        center_x = int((screen_width - window_width) / 2);
        center_y = int((screen_height - window_height) / 2);

        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}');
        self.root.overrideredirect(True);
        self.root.attributes('-topmost', False);
        self.root.config(bg="black");

    # A helper method to create the widgets
    def _setup_widgets(self):
        self.label = tk.Label(
            self.root,
            text="Loading...",
            font=("DS-Digital", 40, "bold"),
            fg="#FFFFFF",
            bg="black"
        );
        self.label.pack(expand = True);

    # A helper method to set up the event bindings 
    def _bind_events(self):
        # When a left-click (<Button-1>) happens on the window, call self._start_drag
        self.root.bind("<Button-1>", self._start_drag);

        # When the mouse is moved with the left button held down (<B1-Motion>), call self._do_drag
        self.root.bind("<B1-Motion>", self._do_drag);

    # This method is called when the user first clicks the widget
    def _start_drag(self, event):
        # It records the x and y coordinates of the mouse click
        self.x = event.x;
        self.y = event.y;

    # This method is called repeatedly as the user drags the mouse
    def _do_drag(self, event):
        # It calculates how far the mouse has moved from the initial click
        # and moves the entire window by that amount.
        deltax = event.x - self.x;
        deltay = event.y - self.y;

        new_x = self.root.winfo_x() + deltax;
        new_y = self.root.winfo_y() + deltay;

        self.root.geometry(f'+{new_x}+{new_y}');

    # This is the repeating update loop for the display text.
    def _update_display(self):
        # Call our imported function from time_logic.py to get the current status string
        countdown_string = countdown_status();
        
        # Update the text of label widget with this new string
        self.label.config(text=countdown_string);
        
        # Tell Tkinter to run this same function again after 1000ms (1 second)
        # This creates the live, second-by-second update
        self.root.after(1000, self._update_display);

    # Public method we call from main.py to kick everything off
    def start(self):
        # Start the update loop for the first time
        self._update_display();
        
        # Start the main Tkinter event loop, which draws the window and listens for events
        self.root.mainloop();