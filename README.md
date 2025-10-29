# NYSE-Countdown-Widget
A simple multi-file project built with Python and Tkinter. This project was a short and little fun project I wanted to create to fill in a gap on my black wallpaper on my personal windows machine. Tkinter was used to create the simple GUI and Pytz was used to work with the New York timezone.
<img width="721" height="168" alt="image" src="https://github.com/user-attachments/assets/168d6f7c-f9a6-4ff0-813f-c9315d97297d" />

# Key Features
- **A live countdown timer that reflects the NYSE market open:** If the market is open, the label displayed on the widget will say so. Otherwise, a live countdown will be displayed until the next NYSE market open between 9:30AM and 4:00PM New York time.
- **Accounts for weekends:** The countdown on Saturday for example will show the remaining time until NYSE opens on the next trading day which would be Monday.
- **Tkinter used to build simple GUI:** A very simple widget that is borderless and clean. You can drag it around anywhere on your desktop.

# Local Setup & Installation
To run this project locally, follow these steps:

1.  **Prerequisites:**
    *   Python3 installed on your machine.

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/NYSE-Countdown-Widget.git
    cd NYSE-Countdown-Widget
    ```
    *(Replace `your-username` with your actual GitHub username)*

3.  **Install dependencies:**
    The only external dependency is pytz. You can install it directly using pip.
    ```bash
    pip install pytz
    ```

5.  **Running the application:**
    To run the widget, execute the main.py file from the root of the project folder.
    ```bash
    python3 main.py
    ```

6.  **Set up to run on Windows startup (optional):**
    To make the widget launch automatically every time you log in, you can create a batch script and place a shortcut in the Windows    startup folder.

    Create a **start_widget.bat** file inside the project directory with the following content. You must replace the placeholder paths with the actual paths on your system.
    ```bash
    @echo off

    "C:\Path\To\Your\Project\NYSE-Countdown-Widget"
    
    "C:\Path\To\Your\pythonw.exe" "main.py"
    ```
    Open the Windows Startup folder** by pressing `Win + R`, typing `shell:startup`, and pressing Enter. Create a shortcut to your `start_widget.bat` file and place it inside this Startup folder.

    The widget will now launch automatically the next time you log into Windows.

## Project Structure

The project follows a simple multi-file structure to organise the logic and display/GUI seperately.

```
/
├── main.py             # Main entry point: initializes and starts the application
├── widget_ui.py        # Handles all GUI creation, layout, and event handling (e.g., window dragging)
├── time_logic.py       # Core countdown logic: handles timezone math and status text generation
└── README.md           # Project documentation, setup, and usage instructions
```
