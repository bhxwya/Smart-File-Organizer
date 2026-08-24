from pathlib import Path
from categories import CATEGORIES


class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def get_category(self, item):
        for category, extensions in CATEGORIES.items():
            if item.suffix in extensions:
                return category
        return "Others"

    def organize(self):
        for item in self.folder_path.iterdir():
            if item.is_file():
                category = self.get_category(item)
                destination = self.folder_path / category
                destination.mkdir(exist_ok=True)
                put_files = destination / item.name
                item.rename(put_files)
                
        print("Files organized successfully!")
