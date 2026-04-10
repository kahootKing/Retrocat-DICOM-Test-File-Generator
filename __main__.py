## Retrocat: Medical Imaging Test File Generator
#
# Developed by: Alyssa N. Merante (alyssa.mer14@gmail.com), aka KahootKing (or DuckDuckTheKahootKing)
#
# The purpose of this application is to provide a method of generating anonymized medical imaging test files (DICOM & HL7) to be used for testing purposes only.
# ** IMPORTANT ** It is the responsibility of the user to generate test files that do not violate HIPPA by using identifiable patient information.
#
# This application was developed as a fun & personal side-project and is not owned by any business entity. This application was strictly developed on personal time.
# This open-source code is available free-of-charge to anyone who would like to use it. 
#

from os import getcwd

version = "v0.0.2"
canLog = True ## Do not remove this, the definition of the canLog variable in __main__ is used directly every time the write_log_file method is called in __LOG.log

if __name__ == "__main__":

    # Initialize Logs #
    import __LOG.log as log
    canLog = log.create_log_dir()
    if canLog:
        canLog = log.write_log_file(f"The working directory for this program is: {getcwd()}", 4)
        log.write_log_file(f"Running Retrocat {version}.", 4)

    # Initialize GUI and main elements to be used in this program instance #
    import rootElem