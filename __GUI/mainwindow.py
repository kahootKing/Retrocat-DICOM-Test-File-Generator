## mainwindow.py
#
## This module controls the drawing of the main program window.
## This module should be initialized upon app startup.

import os
import tkinter as tk
#from tkinter import ttk

# Main Window Var. #
widthMultip = 0.45  # Main window
heightMultip = 0.75  # Main window


# Style Var. #
fontStyle = "Arial"
mainWinColor = "lavender blush"
borderLineColor = "black"
headerFontSize = 24
headerFontColor = "gray15"
subHeaderFontSize = 20
subHeaderFontColor = "gray50"
textFontSize = 12
textFontColor = "gray15"


## Define main window as a Tk() class instance & obtain screen resolution.
mainWindow = tk.Tk()
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()
mainWidth = round(screenWidth * widthMultip)
mainHeight = round(screenHeight *heightMultip)


## Define main window components based on screen resolution.
mainWindow.title("Retrocat")
mainWindow.iconbitmap(True, f"{os.getcwd()}\__GUI\lilretrocat.ico")
mainWindow.geometry(f"{mainWidth}x{mainHeight}")
mainWindow.resizable(True,True)
mainWindow.configure(bg=mainWinColor)


## Define Frame (A): Header
headerMultip = 0.1 # Top Header
headerHeight = round(mainHeight * headerMultip)
header = tk.Frame(mainWindow,
                  bg=mainWinColor,
                  width= mainWidth,
                  height= headerHeight,
                  highlightthickness=1, 
                  highlightbackground=borderLineColor)
header.place(x=0, y=0)
headerLabel = tk.Label(header, 
                        text="Build Patient Jacket", 
                        font=(fontStyle, headerFontSize),
                        fg=headerFontColor,
                        bg=mainWinColor)
headerLabel.place(x=8, y=(round(headerHeight * 0.24)))


## Define Frame (B): Current Step
curStepMultip = 0.17
curStepHeight = round(mainHeight * curStepMultip)                        
curStep = tk.Frame(mainWindow,
                  bg=mainWinColor,
                  width= mainWidth,
                  height= curStepHeight,
                  highlightthickness=1, 
                  highlightbackground=borderLineColor)
curStep.place(x=0, y=headerHeight)
curStepLabel = tk.Label(curStep, 
                        text="1) Patient Demographics \n2) Study Information \n3) Series & Image Information \n4) Order Information \n5) Report Information", 
                        font=(fontStyle, textFontSize),
                        fg=headerFontColor,
                        bg=mainWinColor,
                        justify="left")
curStepLabel.place(x=4, y=(round(curStepHeight * 0.12)))



#ttk.Button(frm, text="Quit", command=mainWindow.destroy).grid(column=1, row=0)

## Draw main window.
mainWindow.mainloop()