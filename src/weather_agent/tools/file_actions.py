from pathlib import Path
import shutil
class File_Services:
    def __init__(self):
        self.BASEPATH = Path.home()
    def listFiles(self,target):
        target_folder = self.BASEPATH / target
        if not target_folder.exists():
            raise FileNotFoundError(f"{target_folder} does not exist")

        return [
            file
            for file in target_folder.iterdir()
            if file.is_file()
        ]
            
    def deleteFile(self):
        pass
    def move_files(self,target):
        allfiles = self.listFiles(target)
        if len(allfiles)<=0:
            print(f"No files present in {target} folder to be organized" )
        for file in allfiles:
            if file.is_dir():
                continue

            extension = file.suffix.lstrip(".").lower()
            destination_folder = self.BASEPATH / target/extension
            destination_folder.mkdir(exist_ok=True)
            destination = destination_folder /file.name
            shutil.move(str(file),str(destination))
            print(f"{file} has been moved to {destination_folder}")

