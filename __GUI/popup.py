## popup.py
##
## The purpose of this module is to define methods used to draw various popups.
##
# This includes error popups, confirmation popups, and other user inputs.

import tkinter as tk
import __LOG.log as log
from __GUI.mainwindow import mainHeight, mainWidth, mainWinColor, mainFontStyle
from __GUI.mainwindow import mainWindow


## Define drawing variables for popups
popupFontSize = 14


# Calculated values commonly used in functions
popupWidth = round(mainWidth/2)
popupHeight = round(mainHeight/5)


## Define popup window as a Tk class instance
def define_popup(label="", text="", numButton=0):
    popup = tk.Toplevel(mainWindow)
    popup.tkraise(mainWindow)
    popup.geometry(f"{popupWidth}x{popupHeight}")
    popup.resizable(False,False)

    label = tk.Label(popup, text=label)
    label.pack(side="top")


## Define functions to call
#def draw_anonymize_confirmation_popup():
    