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
popupFontSize = 13
popupPosOffset = 50


# Calculated values commonly used in functions
popupWidth = round(mainWidth/2)
popupHeight = round(mainHeight/5)
popup_x = round((mainWidth/2)-(popupWidth/2))+popupPosOffset ## center popup with respect to the mainWindow
popup_y = round((mainHeight/2)-(popupHeight/2))+popupPosOffset ## center popup with respect to the mainWindow


## Define popup window as a Tk class instance
def define_popup(label="", text="", numButton=0):
    popup = tk.Toplevel(mainWindow)
    popup.geometry(f"{popupWidth}x{popupHeight}+{popup_x}+{popup_y}")
    popup.resizable(False,False)

    label = tk.Label(popup, text=label, font=(mainFontStyle, popupFontSize))
    label.pack(side="top")


## Define functions to call
#def draw_anonymize_confirmation_popup():
    