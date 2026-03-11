## mainwindow.py
#
## This module controls the drawing of the main program window.
## This module should be initialized upon app startup.

import os
import tkinter as tk


# Main Window Var. #
widthMultip = 0.45  # Main window
heightMultip = 0.75  # Main window

# Style Var. #
mainFontStyle = "Georgia"
mainWinColor = "lavender blush"


## Define main window as a Tk() class instance & obtain screen resolution.
mainWindow = tk.Tk()
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()
mainWidth = round(screenWidth * widthMultip)
mainHeight = round(screenHeight *heightMultip)


## Define main window components based on screen resolution.
mainWindow.title("Retrocat")
mainWindow.iconbitmap(True, f"{os.getcwd()}\\__GUI\\lilretrocat.ico")
mainWindow.geometry(f"{mainWidth}x{mainHeight}")
mainWindow.resizable(False,False)
mainWindow.configure(bg=mainWinColor)


## Step (1): Draw Startup UI
import __GUI.startup as startup
startup.draw_dcm_File_button()
startup.draw_header("Select an Option")


## Draw main window.
mainWindow.mainloop()