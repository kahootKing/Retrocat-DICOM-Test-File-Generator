## mainElements.py
#
## This module controls the actions of the UI components within the root of the application (known as mainWindow).
## The UI elements in this module should be called within the mainwindow, which should have already been initialized with the application.

import os
import tkinter as tk
from tkinter import filedialog
from rootElem import mainHeight, mainWidth, mainWinColor, mainFontStyle # type: ignore
from rootElem import mainWindow # type: ignore
import __GUI.popupElements as popupElements # type: ignore
import __LOG.log as log # type: ignore


# Variables for Drawing
headerMultip = 0.07 # Top Header
curStepMultip = 0.17 
headerFontSize = 24
headerFontColor = "gray15"
subHeaderFontSize = 20
subHeaderFontColor = "gray50"
textFontSize = 10
textFontColor = "gray15"
textFontColor_grayedOut = "gray45"
borderLineColor = "black"
buttonHeightDiv  = 300
buttonWidthDiv = 25
buttonFontSize = 14


# Calculated values commonly used in functions
buttonHeight = round(mainHeight / buttonHeightDiv)
buttonWidth = round(mainWidth / buttonWidthDiv)
headerHeight = round(mainHeight * headerMultip)
header_y = round(headerHeight * 0.18)
curStepHeight = round(mainHeight * curStepMultip)    
button_dcmOps_x = round(mainWidth/2)
buttonDesc_dcmOps_x = round(mainWidth/40)


# Buttons to Draw
def draw_bulk_anon_button(hasDesc = True): ## This button is the topmost button
    bulkAnonBttn = tk.Button(mainWindow,
                             text = "Bulk Anonymize DCM File(s)",
                             font=(mainFontStyle, buttonFontSize),
                             height=buttonHeight,
                             width=buttonWidth,
                             command=choose_bulk_anon_click,
                             state="active")
    button_x = button_dcmOps_x
    button_y = round(headerHeight + (mainHeight/35))
    bulkAnonBttn.place(x= button_x, y = button_y)

    if hasDesc:
        draw_button_descriptor(x = buttonDesc_dcmOps_x,
                               y = button_y,
                               desc =
                               "-- Select one or more DICOM files to anonymize. " 
                               "This provides a clean template to use for future testing.  "
                               "\n\n-- All Study, Series, &  SOP Instance UIDs will be randomized to minimize the risk of metadata collisions with the PACS under test.")


def draw_dcm_file_button(hasDesc=True): ## This button is beneath the topmost button (Bulk Anonymization)
    chooseDCMBttn = tk.Button(mainWindow,
                             text = "Edit DICOM File(s) (*.dcm)",
                             font=(mainFontStyle, buttonFontSize),
                             height=buttonHeight,
                             width=buttonWidth,
                             command=choose_DCM_file_click,
                             state="disabled")
    button_x = button_dcmOps_x
    button_y = round(headerHeight + (mainHeight/5.5))
    chooseDCMBttn.place(x = button_x, y = button_y)

    if hasDesc:
        draw_button_descriptor(x = buttonDesc_dcmOps_x,
                               y = button_y,
                               desc =
                               "                      ****  UNDER CONSTRUCTION  ****\n"
                               "-- Start with one or more DICOM files to use as a basis for creating new test data. " 
                               "\n\n-- Once selected, you will be guided through a series of windows to edit patient, study, and series information.",
                               textColor = textFontColor_grayedOut)


def draw_choose_cfg_button(hasDesc = True):
    chooseCfgBttn = tk.Button(mainWindow,
                             text = "Choose Config. File (*.cfg)",
                             font=(mainFontStyle, buttonFontSize),
                             height=buttonHeight,
                             width=buttonWidth,
                             command=choose_DCM_file_click,
                             state="disabled")
    button_x = button_dcmOps_x
    button_y = round(headerHeight + (mainHeight/2.95))
    chooseCfgBttn.place(x = button_x, y = button_y)

    if hasDesc:
        draw_button_descriptor(x = buttonDesc_dcmOps_x,
                               y = button_y,
                               desc =
                               "                      ****  UNDER CONSTRUCTION  ****\n"
                               "-- Start with a configuration file to automatically generate test data that meets certain criteria." 
                               "\n\n-- Config. files can be created & updated using the Configuration Editor.",
                               textColor = textFontColor_grayedOut)


# General GUI Elements
def draw_header(text="", frame_x = 0, frame_y = 0, label_x = 8, label_y = header_y):
    header = tk.Frame(mainWindow,
                      bg=mainWinColor,
                      width= mainWidth,
                      height= headerHeight,
                      highlightthickness=1, 
                      highlightbackground=borderLineColor)
    header.place(x=frame_x, y=frame_y)
    headerLabel = tk.Label(header, 
                            text=text, 
                            font=(mainFontStyle, headerFontSize),
                            fg=headerFontColor,
                            bg=mainWinColor)
    headerLabel.place(x = label_x, y = label_y)


def draw_button_descriptor(x, y, desc="", textColor = textFontColor):
    descrip = tk.Label(mainWindow,
                       text = desc,
                       font = (mainFontStyle, textFontSize),
                       fg = textColor,
                       bg = mainWinColor,
                       justify="left",
                       wraplength=round(mainWidth/2.25))
    descrip.place(x = x, y = y)


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


def choose_bulk_anon_click():
    log.write_log_file("User clicked the 'Bulk Anonymize' button.", 8)
    #draw_header("Choose DICOM File(s) to Anonymize")
    dcmFilePath = filedialog.askopenfilenames(
        initialdir=os.getcwd(),
        title="Choose DICOM Image File(s) -- (*.dcm)",
        filetypes=(("DICOM (*.dcm)","*.dcm"), 
                   #("Zip (*.zip)","*.zip"), ## Add support for .zip files
                   ("All Files (*)","*"))
    )
    if dcmFilePath:
        log.write_log_file(f"User selected the following file(s): {dcmFilePath}.", 8)
        popupElements.draw_anonymize_confirmation(dcmFilePath)
    else:
        log.write_log_file("User closed the File Explorer without choosing a file.", 8)
        draw_header("Select an Option")


def choose_DCM_file_click():
    log.write_log_file("User clicked the 'Edit DICOM File(s)' button.", 8)
    #draw_header("Choose DICOM File(s) to Update")
    dcmFilePath = filedialog.askopenfilenames(
        initialdir=os.getcwd(),
        title="Choose DICOM Image File(s) -- (*.dcm)",
        filetypes=(("DICOM (*.dcm)","*.dcm"), 
                   #("Zip (*.zip)","*.zip"), ## Add support for .zip files
                   ("All Files (*)","*"))
    )
    if dcmFilePath:
        log.write_log_file(f"User selected the following file(s): {dcmFilePath}.", 8)
        popupElements.draw_anonymize_confirmation(dcmFilePath)
    else:
        log.write_log_file("User closed the File Explorer without choosing a file.", 8)
        draw_header("Select an Option")


## Startup UI Main Function
def draw_startup_UI():
    draw_header(text = "Select an Option")
    draw_bulk_anon_button(hasDesc = True)
    draw_dcm_file_button(hasDesc = True)
    draw_choose_cfg_button(hasDesc = True)
    draw_header(text = "Configuration & Settings", frame_y = round(mainWidth/1.6), label_y =header_y)
    print("12")