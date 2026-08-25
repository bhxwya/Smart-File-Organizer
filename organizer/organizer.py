from pathlib import Path
from organizer.categories import CATEGORIES
import logging

logger = logging.getLogger(__name__)


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

    def organize(self, preview=False):
        count = 0
        preview_files = []

        for item in self.folder_path.iterdir():
            if item.is_file():
                category = self.get_category(item)

                if preview:
                    preview_files.append(f"{item.name} → {category}")
                    count += 1
                    continue

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
                    logger.info(
                        f"Duplicate detected: {item.name} → renamed to {changed_name} to prevent overwrite.")

                count += 1
                logger.info(f"Moved {put_files.name} → {category}")
                
        if preview:
            return preview_files
        
        return count
