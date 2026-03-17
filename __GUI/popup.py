## popup.py
##
## The purpose of this module is to define methods used to draw various popups.
##
# This includes error popups, confirmation popups, and other user inputs.

import tkinter as tk
import __LOG.log as log
from __GUI.mainwindow import mainHeight, mainWidth, mainWinColor, mainFontStyle
from __GUI.mainwindow import mainWindow

popup = tk.Toplevel(mainWindow)
popup.withdraw()

## Define drawing variables for popups
popupFontSize = 11
popupPosOffset = 50


# Calculated values commonly used in functions (the math is messed up because I'm confused so don't try to understand it and DON'T TOUCH IT)
popupWidth = round(mainWidth/2)
popup_x = round((mainWidth/2)-(popupWidth/2))+popupPosOffset ## center popup with respect to the mainWindow
buttonPadding_x = round(popupWidth/20)
popupButtonWidth = round((popupWidth - (buttonPadding_x*4))/28)
rightButton_x = round((10*popupButtonWidth) + (8*buttonPadding_x))
centerButton_x = round((5*popupButtonWidth) + (4.5*buttonPadding_x))
leftButton_x = buttonPadding_x

popupHeight = round(mainHeight/5.5)
popup_y = round((mainHeight/2)-(popupHeight/2))+popupPosOffset ## center popup with respect to the mainWindow
buttonPadding_y = round(popupHeight/15)
popupButtonHeight = round((popupHeight/12)-buttonPadding_y)
popupButton_y = round(popupHeight/2)


# Functions after Clicking Buttons in Popups
def cancel_popup():
    print("123")
    popup.withdraw()


## Define popup window as a Tk class instance
def define_basic_popup(title="", label="", yes_Command="", no_Command="", cancel_Command=cancel_popup):
    popup = tk.Toplevel(mainWindow)
    popup.title(title)
    popup.geometry(f"{popupWidth}x{popupHeight}+{popup_x}+{popup_y}")
    popup.resizable(False,False)
    message = tk.Message(popup, 
                         text=label, 
                         font=(mainFontStyle, popupFontSize), 
                         width=popupWidth)
    message.pack(side="top", 
                 padx=10, 
                 pady=10)

    yesButton = tk.Button(popup, 
                          text="Yes", 
                          font =(mainFontStyle, popupFontSize),
                          width = popupButtonWidth,
                          height = popupButtonHeight,
                          command=yes_Command)
    yesButton.place(x=rightButton_x, y=popupButton_y)

    noButton = tk.Button(popup, 
                         text="No",
                         font =(mainFontStyle, popupFontSize),
                         width = popupButtonWidth,
                         height = popupButtonHeight,
                         command=no_Command)
    noButton.place(x=leftButton_x, y=popupButton_y)

    cancelButton = tk.Button(popup, 
                       text="Cancel",
                       font =(mainFontStyle, popupFontSize),
                       width = popupButtonWidth,
                       height = popupButtonHeight,
                       command=cancel_Command)
    cancelButton.place(x=centerButton_x, y=popupButton_y)

    return popup


# Functions for Drawing Various Popups
def draw_anonymize_confirmation():
    define_basic_popup(title="Anonymize File(s)?", label="Would you like to anonymize these DICOM files (according to the DICOM Standard Basic Profile Anonymization)?")


