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

    @property
    def parameters(self):
        return {
            "target": {"type": "string", "description": "Folder name"},
            "action": {"type": "string", "enum": ["move", "delete"]},
        }

    def execute(self, target, action):
        if action == "move":
            self.file_service.move_files(target)
        return "success..!"
