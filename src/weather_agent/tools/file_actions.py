from pathlib import Path
import shutil
class File_Services:
    def __init__(self):
        self.BASEPATH = Path.home()
    def listFiles(self,target):
        target_folder = self.BASEPATH / target
        return target_folder.iterdir()
            
    def deleteFile(self):
        pass
    def move_files(self,target):
        allfiles = self.listFiles(target)
        for file in allfiles:
            if file.is_dir():
                continue

            extension = file.suffix.lstrip(".").lower()
            destination_folder = self.BASEPATH / target/extension
            destination_folder.mkdir(exist_ok=True)
            destination = destination_folder /file.name
            shutil.move(str(file),str(destination))
            print(f"{file} has been moved to {destination_folder}")

