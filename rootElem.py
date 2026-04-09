## rootElem.py
#
## This module controls the drawing of the main program window.  It also defined the objects to be referenced in this project (mainWindow, popup, dcmFile, etc.)
## This module should be initialized upon app startup.

import os
import tkinter as tk
import __DICOM.dicomReadWrite as dicomReadWrite
from __main__ import version


# Main Window Var. #
widthMultip = 0.45  # Main window (45% of monitor resolution width)
heightMultip = 0.90  # Main window (90% of monitor resolution height)

# Style Var. #
mainFontStyle = "Georgia"
mainWinColor = "lavender blush"


## Define main window as a Tk() class instance & obtain screen resolution.
mainWindow = tk.Tk()
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()
mainWidth = round(screenWidth * widthMultip)
mainHeight = round(screenHeight * heightMultip)


## Define main window components based on screen resolution.
mainWindow.title(f"Retrocat ({version}) -- DICOM Test File Generator")
mainWindow.iconbitmap(True, f"{os.getcwd()}\\icon\\lilretrocat.ico")
mainWindow.geometry(f"{mainWidth}x{mainHeight}")
mainWindow.resizable(False,False)
# mainWindow.resizable(True,True) ## for testing and drawing GUI elements. Keep commented out otherwise.
mainWindow.configure(bg=mainWinColor)


#Initialize an instance of a popup, which should be hidden
popup = tk.Toplevel(mainWindow)
popup.withdraw() #when calling functions that draw popups, be sure to call popup.deiconify() to actually redraw the popup.


## Create Directory for DICOM Files
newFilePathDCM = dicomReadWrite.create_dcm_file_dir()


## Draw Startup UI
import __GUI.mainElements as mainElements
import __GUI.popupElements as popupElements
mainElements.draw_startup_UI()


## Specify the behavior of the application when it is closed by the user
popup.protocol("WM_DELETE_WINDOW", popupElements.close_cancel_popup)
mainWindow.protocol("WM_DELETE_WINDOW", mainElements.close_mainWindow)


## Draw main window.
mainWindow.mainloop()