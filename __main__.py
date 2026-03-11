## Retrocat: Medical Imaging Test File Generator
#
# Developed by: Alyssa Merante (alyssa.merante@gmail.com)
#
# The purpose of this application is to provide a method of generating anonymized medical imaging test files (DICOM & HL7)  to be used for testing purposes only.
# 
# ** IMPORTANT ** It is the responsibility of the user to generate test files that do not violate HIPPA by using identifiable patient information.

from os import getcwd

# Initialize Application

canLog = True ## Do not remove this, the definition of the canLog variable in __main__ is used directly every time the write_log_file method is called in __LOG.log
if __name__ == "__main__":

    # Initialize Logs #
    import __LOG.log as log
    canLog = log.create_log_dir()

    if canLog:
        canLog = log.write_log_file(f"The working directory for this program is: {getcwd()}", 4)
        log.write_log_file("-------------", 1)

    # Initialize GUI #
    import __GUI.mainwindow as mainwin