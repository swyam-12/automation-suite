import tkinter as tk
import os

# Functions
def run_file_organizer():
    os.system("py main.py")
    status_label.config(text="File Organizer Executed")

def run_web_scraper():
    os.system("py web_scraper.py")
    status_label.config(text="Web Scraper Executed")

def run_email():
    os.system("py email_automation.py")
    status_label.config(text="Email Sent")

def run_monitor():
    os.system("py system_monitor.py")
    status_label.config(text="System Monitor Running")

# Window
root = tk.Tk()
root.title("Automation Suite")
root.geometry("400x350")

title = tk.Label(root, text="Automation Suite", font=("Arial", 18))
title.pack(pady=15)

# Buttons
tk.Button(root, text="File Organizer", width=25, command=run_file_organizer).pack(pady=5)
tk.Button(root, text="Web Scraper", width=25, command=run_web_scraper).pack(pady=5)
tk.Button(root, text="Email Automation", width=25, command=run_email).pack(pady=5)
tk.Button(root, text="System Monitor", width=25, command=run_monitor).pack(pady=5)

# Status Label
status_label = tk.Label(root, text="Status: Ready", fg="blue")
status_label.pack(pady=20)

# Run
root.mainloop()