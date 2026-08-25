from pathlib import Path
from categories import CATEGORIES


class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        
        if not self.folder_path.exists() or not self.folder_path.is_dir():
            raise ValueError("Invalid folder path.")
          

    def get_category(self, item):
        for category, extensions in CATEGORIES.items():
            if item.suffix in extensions:
                return category
        return "Others"

    def organize(self):
        count = 0

        for item in self.folder_path.iterdir():
            if item.is_file():
                category = self.get_category(item)
                destination = self.folder_path / category
                destination.mkdir(exist_ok=True)

                put_files = destination / item.name

                try:
                    item.rename(put_files)

                except FileExistsError:
                    number = 1

                    while put_files.exists():
                        changed_name = item.stem + "_" + \
                            str(number) + item.suffix
                        put_files = destination / changed_name
                        number += 1

                    item.rename(put_files)

                count += 1

        print("Files organized successfully!")
        print(f"{count} files organized.")
