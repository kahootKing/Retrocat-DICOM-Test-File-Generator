## Initialize the program. This should be run FIRST everytime the program is launched.

import os
import __LOG.log as log


# Var. #
rootPath = os.getcwd()

# Initialize #
logDir, canLog = log.create_log_dir(rootPath)
canLog = log.write_log_file(logDir, f"The working directory for this program is: {rootPath}", canLog, 4)
canLog = log.write_log_file(logDir, "-------------", canLog, 1)