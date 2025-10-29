import tkinter as tk
from widget_ui import CountdownWidget

# Create the tkinter window
root = tk.Tk();

# Create an "instance" of our CountdownWidget. We pass the 'root' window
# to it so the widget knows where to draw itself
app = CountdownWidget(root);

# Call the 'start' method of our app object. This will trigger the
# update loop and show the window
app.start();