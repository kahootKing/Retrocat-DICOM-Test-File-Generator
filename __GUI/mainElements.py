## mainElements.py
#
## This module controls the actions of the UI components within the root of the application (known as mainWindow).
## The UI elements in this module should be called within the mainwindow, which should have already been initialized with the application.

import os
import tkinter as tk
from tkinter import filedialog
from rootElem import mainHeight, mainWidth, mainWinColor, mainFontStyle
from rootElem import mainWindow
import __GUI.popupElements as popupElements
import __LOG.log as log


# Variables for Drawing
headerMultip = 0.1 # Top Header
curStepMultip = 0.17 
headerFontSize = 24
headerFontColor = "gray15"
subHeaderFontSize = 20
subHeaderFontColor = "gray50"
textFontSize = 12
textFontColor = "gray15"
borderLineColor = "black"
buttonHeightDiv  = 250
buttonWidthDiv = 25
buttonFontSize = 14


# Calculated values commonly used in functions
buttonHeight = round(mainHeight / buttonHeightDiv)
buttonWidth = round(mainWidth / buttonWidthDiv)
headerHeight = round(mainHeight * headerMultip)
curStepHeight = round(mainHeight * curStepMultip)    


# Buttons to Draw on App Initialization
def draw_dcm_file_button():
    chooseDCMFile = tk.Button(mainWindow,
                             text = "Choose DICOM File (*.dcm)",
                             font=(mainFontStyle, buttonFontSize),
                             height=buttonHeight,
                             width=buttonWidth,
                             command=choose_DCM_file_click)
    chooseDCMFile.place(x=mainWidth/4, y=mainHeight/4)



# General GUI Elements
def draw_header(text=""):
    header = tk.Frame(mainWindow,
                      bg=mainWinColor,
                      width= mainWidth,
                      height= headerHeight,
                      highlightthickness=1, 
                      highlightbackground=borderLineColor)
    header.place(x=0, y=0)
    headerLabel = tk.Label(header, 
                            text=text, 
                            font=(mainFontStyle, headerFontSize),
                            fg=headerFontColor,
                            bg=mainWinColor)
    headerLabel.place(x=8, y=(round(headerHeight * 0.2)))


def draw_current_Step():                    
    curStep = tk.Frame(mainWindow,
                      bg=mainWinColor,
                      width= mainWidth,
                      height= curStepHeight,
                      highlightthickness=1, 
                      highlightbackground=borderLineColor)
    curStep.place(x=0, y=headerHeight)
    curStepLabel = tk.Label(curStep, 
                            text="1) Patient Demographics \n2) Study Information \n3) Series & Image Information \n4) Order Information \n5) Report Information", 
                            font=(mainFontStyle, textFontSize),
                            fg=headerFontColor,
                            bg=mainWinColor,
                            justify="left")
    curStepLabel.place(x=4, y=(round(curStepHeight * 0.12)))



## Functions to call after clicking buttons.
def close_mainWindow():
    log.write_log_file(
        """User closed the program.
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------""", 5)
    mainWindow.destroy()


def choose_DCM_file_click():
    log.write_log_file("User clicked the 'Choose DICOM File(s)' button.", 8)
    draw_header("Choose DICOM File(s) to Update")
    dcmFilePath = filedialog.askopenfilenames(
        initialdir=os.getcwd(),
        title="Choose DICOM Image File(s) -- (*.dcm or *.zip)",
        filetypes=(("DICOM (*.dcm)","*.dcm"), 
                   ("Zip (*.zip)","*.zip"),
                   ("All Files (*)","*"))
    )
    if dcmFilePath:
        log.write_log_file(f"User selected the following file(s): {dcmFilePath}.", 8)
        popupElements.draw_anonymize_confirmation(dcmFilePath)
    else:
        log.write_log_file("User closed the File Explorer without choosing a file.", 8)


## Startup UI Main Function
def draw_startup_UI():
    draw_header("Select an Option")
    draw_dcm_file_button()