## Initialize the program. This should be run FIRST everytime the program is launched.

import os
import __LOG.log as log


# Initialize Logs #
canLog = log.create_log_dir()
canLog = log.write_log_file(f"The working directory for this program is: {os.getcwd()}", canLog, 4)
canLog = log.write_log_file("-------------", canLog, 1)

# Initialize GUI #
import __GUI.mainwindow as mainwin