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
import webbrowser


# Variables for Drawing
headerMultip = 0.07 # Top Header
curStepMultip = 0.17 
headerFontSize = 23
smallHeaderFontSize = 15
headerFontColor = "gray15"
headerColor = "rosy brown"
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
smallHeader_y = round(headerHeight * 0.1)
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
                               #"                      ****  UNDER CONSTRUCTION  ****\n"
                               "-- Start with one or more DICOM files to use as a basis for creating new test data. " 
                               "\n\n-- Once selected, you will be guided through a series of windows to edit patient, study, and series information.",
                               textColor = textFontColor_grayedOut)


def draw_choose_cfg_button(hasDesc = True): ## This button is below the Edit DICOM File button
    chooseCfgBttn = tk.Button(mainWindow,
                             text = "Choose Configuration File (*.cfg)",
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
                               #"                      ****  UNDER CONSTRUCTION  ****\n"
                               "-- Start with a configuration file to automatically generate test data that meets certain criteria." 
                               "\n\n-- Configuration files can be created & updated using the Configuration Editor.",
                               textColor = textFontColor_grayedOut)


def draw_cfg_editor_button():
    cfgEditBttn = tk.Button(mainWindow,
                            text = "Configuration Editor",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/2),
                            width=round(buttonWidth/2),
                            state="disabled")
    button_x = round(mainWidth/15)
    button_y = round(mainHeight/1.52)
    cfgEditBttn.place(x=button_x, y=button_y)


def draw_patient_db_editor_button():
    ptdbEditBttn = tk.Button(mainWindow,
                            text = "Patient DB Editor",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/2),
                            width=round(buttonWidth/2),
                            state="disabled")
    button_x = round(mainWidth/2.7)
    button_y = round(mainHeight/1.52)
    ptdbEditBttn.place(x=button_x, y=button_y)


def draw_attribute_db_editor_button():
    attrdbEditBttn = tk.Button(mainWindow,
                            text = "DICOM DB Editor",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/2),
                            width=round(buttonWidth/2),
                            state="disabled")
    button_x = round(mainWidth/1.48)
    button_y = round(mainHeight/1.52)
    attrdbEditBttn.place(x=button_x, y=button_y)


def draw_gen_settings_button():
    genSetBttn = tk.Button(mainWindow,
                            text = "General Settings",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/2),
                            width=round(buttonWidth/2),
                            state="disabled")
    button_x = round(mainWidth/15)
    button_y = round(mainHeight/1.3)
    genSetBttn.place(x=button_x, y=button_y)


def draw_dcm_template_button():
    dcmTempBttn = tk.Button(mainWindow,
                            text = "DCM Template Editor",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/2),
                            width=round(buttonWidth/2),
                            state="disabled")
    button_x = round(mainWidth/2.7)
    button_y = round(mainHeight/1.3)
    dcmTempBttn.place(x=button_x, y=button_y)


def draw_log_button():
    logBttn = tk.Button(mainWindow,
                            text = "Log Files",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/2),
                            width=round(buttonWidth/2),
                            command=log.open_log_dir,
                            state="active")
    button_x = round(mainWidth/1.48)
    button_y = round(mainHeight/1.3)
    logBttn.place(x=button_x, y=button_y)


def draw_guides_button():
    guidesBttn = tk.Button(mainWindow,
                            text = "Guides",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/4),
                            width=round(buttonWidth/2),
                            state="disabled")
    button_x = round(mainWidth/4.8)
    button_y = round(mainHeight/1.059)
    guidesBttn.place(x=button_x, y=button_y)


def draw_dcm_url_button():
    guidesBttn = tk.Button(mainWindow,
                            text = "DICOM Help",
                            font=(mainFontStyle, buttonFontSize),
                            height=round(buttonHeight/4),
                            width=round(buttonWidth/2),
                            command=lambda : webbrowser.open("https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_e.html"),
                            state="active")
    button_x = round(mainWidth/1.9)
    button_y = round(mainHeight/1.059)
    guidesBttn.place(x=button_x, y=button_y)


# General GUI Elements
def draw_header(text="", frame_x = 0, frame_y = 0, label_x = 8, label_y = header_y):
    header = tk.Frame(mainWindow,
                      bg=headerColor,
                      width= mainWidth,
                      height= headerHeight,
                      highlightthickness=1, 
                      highlightbackground=borderLineColor)
    header.place(x=frame_x, y=frame_y)
    headerLabel = tk.Label(header, 
                            text=text, 
                            font=(mainFontStyle, headerFontSize),
                            fg=headerFontColor,
                            bg=headerColor)
    headerLabel.place(x = label_x, y = label_y)


def draw_small_header(text="", frame_x = 0, frame_y = 0, label_x = 8, label_y = header_y):
    header = tk.Frame(mainWindow,
                      bg=headerColor,
                      width= mainWidth,
                      height= headerHeight/1.5,
                      highlightthickness=1, 
                      highlightbackground=borderLineColor)
    header.place(x=frame_x, y=frame_y)
    headerLabel = tk.Label(header, 
                            text=text, 
                            font=(mainFontStyle, smallHeaderFontSize),
                            fg=headerFontColor,
                            bg=headerColor)
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


def choose_files_from_explorer():
    dcmFilePath = filedialog.askopenfilenames(
        initialdir=os.getcwd(),
        title="Choose DICOM Image File(s) -- (*.dcm)",
        filetypes=(("DICOM (*.dcm)","*.dcm"), 
                   #("Zip (*.zip)","*.zip"), ## Add support for .zip files
                   ("All Files (*)","*"))
    )
    if dcmFilePath:
        log.write_log_file(f"User selected the following file(s): {dcmFilePath}.", 8)
    else:
        log.write_log_file("User closed the File Explorer without choosing a file.", 8)
    return dcmFilePath


def choose_bulk_anon_click():
    log.write_log_file("User clicked the 'Bulk Anonymize' button.", 8)
    dcmFilePath = choose_files_from_explorer()
    if dcmFilePath:
        popupElements.draw_anonymize_confirmation(dcmFilePath)


def choose_DCM_file_click():
    log.write_log_file("User clicked the 'Edit DICOM File(s)' button.", 8)
    dcmFilePath = choose_files_from_explorer()
    if dcmFilePath:
        popupElements.draw_anonymize_confirmation(dcmFilePath)


## -----------------------------------------------------------------------------------------------##
## Startup UI Main Function

def draw_startup_UI():
    draw_header(text = " Select an Option")
    draw_bulk_anon_button(hasDesc = True)
    draw_dcm_file_button(hasDesc = True)
    draw_choose_cfg_button(hasDesc = True)
    draw_header(text = " Configuration & Settings", frame_y = round(mainWidth/1.6), label_y =header_y)
    draw_cfg_editor_button()
    draw_patient_db_editor_button()
    draw_attribute_db_editor_button()
    draw_gen_settings_button()
    draw_dcm_template_button()
    draw_log_button()
    draw_small_header(text = " Docs & Info", frame_y = round(mainWidth/1.01), label_y = smallHeader_y)
    draw_guides_button()
    draw_dcm_url_button()