## Initialize the program. This should be run everytime the program is launched.

import os
import __LOG.log as log


# Var. #
rootPath = os.getcwd()

# Initialize #
logDir = log.create_log_dir(rootPath)
log.write_log_file(logDir, f"The working directory for this program is: {rootPath}", 3)
log.write_log_file(logDir, "-------------",7)