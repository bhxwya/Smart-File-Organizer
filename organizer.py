from pathlib import Path


class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def organize(self):
        for item in self.folder_path.iterdir():
            if item.is_file():
                print(item)
