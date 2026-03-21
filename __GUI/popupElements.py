## popup.py
##
## The purpose of this module is to define methods used to draw various popups.
##
# This includes error popups, confirmation popups, and other user inputs.

import tkinter as tk
import __LOG.log as log
from __GUI.rootUI import mainHeight, mainWidth, mainFontStyle
from __GUI.rootUI import popup


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
    log.write_log_file("User clicked the Cancel button. Closing popup.", 8)
    clear_hide_popup()
    


## Define popup window as a Tk class instance
def define_basic_popup(title="", label="", yes_Label = "Yes", yes_Command="", no_Label = "No", no_Command="", cancel_Label = "Cancel", cancel_Command=cancel_popup):
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

    noButton = tk.Button(popup, 
                         text=no_Label,
                         font =(mainFontStyle, popupFontSize),
                         width = popupButtonWidth,
                         height = popupButtonHeight,
                         command=no_Command)
    noButton.place(x=leftButton_x, y=popupButton_y)

    cancelButton = tk.Button(popup, 
                       text=cancel_Label,
                       font =(mainFontStyle, popupFontSize),
                       width = popupButtonWidth,
                       height = popupButtonHeight,
                       command=cancel_Command)
    cancelButton.place(x=centerButton_x, y=popupButton_y)

    yesButton = tk.Button(popup, 
                          text=yes_Label, 
                          font =(mainFontStyle, popupFontSize),
                          width = popupButtonWidth,
                          height = popupButtonHeight,
                          command=yes_Command)
    yesButton.place(x=rightButton_x, y=popupButton_y)

    popup.deiconify() # This is required to show the popup, which may have previously been withdrawn.
    log.write_log_file("The 'Anonymize DICOM File(s)' popup was displayed.", 9)


# Functions for Drawing Various Popups
def draw_anonymize_confirmation():
    define_basic_popup(title="Anonymize File(s)?", label="Would you like to anonymize these DICOM files (according to the DICOM Standard Basic Profile Anonymization)?")


def clear_hide_popup():
    popup.withdraw()
    for widget in popup.winfo_children(): #destroy each widget within the popup. This is so that when it is redrawn, the popup is a clean slate.
        widget.destroy()
