import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root, title="Digital Clock", font_size=80, 
                bg_color='black', fg_color='cyan', time_format='%H:%M:%S'):
        """
        Initialize the digital clock
        :param root: Tkinter root window
        :param title: Window title
        :param font_size: Font size for display
        :param bg_color: Background color
        :param fg_color: Text color
        :param time_format: Time format string
        """
        self.root = root
        self.root.title(title)
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)  # Disable resizing
        
        self.time_format = time_format
        self.font = ('calibri', font_size, 'bold')
        self.bg_color = bg_color
        self.fg_color = fg_color
        
        # Create main label
        self.clock_label = tk.Label(root, font=self.font, 
                                  bg=bg_color, fg=fg_color)
        self.clock_label.pack(anchor='center', pady=20)
        
        # Add date display
        self.date_label = tk.Label(root, font=('calibri', 20), 
                                 bg=bg_color, fg=fg_color)
        self.date_label.pack(anchor='s')
        
        self.update_time()  # Initial call to start updates

    def update_time(self):
        """Update the time and date every second"""
        current_time = strftime(self.time_format)
        
        # For 12-hour format with AM/PM
        if '%I' in self.time_format:
            current_time += " " + strftime('%p')
        
        self.clock_label.config(text=current_time)
        
        # Update date
        current_date = strftime('%A, %B %d, %Y')
        self.date_label.config(text=current_date)
        
        # Schedule next update
        self.clock_label.after(1000, self.update_time)

if __name__ == "__main__":
    # Create main window
    window = tk.Tk()
    
    # Customize your clock here:
    clock = DigitalClock(
        root=window,
        title="My Digital Clock",
        font_size=100,
        bg_color='yellow',
        fg_color='Black',
        time_format='%I:%M:%S'  # 12-hour format with seconds
    )
    
    # Run the application
    window.mainloop()