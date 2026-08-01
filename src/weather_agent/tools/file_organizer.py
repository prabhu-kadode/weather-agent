from .file_actions import File_Services
class File_Organizer:
    def __init__(self):
        self.file_service = File_Services()
    @property
    def name(self):
        return "fileorganizer"
    @property
    def description(self):
        return "Tool to organize files in download folder"
    
    def execute(self,target,action):
        print(target,action)
        if action=='move':
            self.file_service.move_files(target)
        return "success..!"



    