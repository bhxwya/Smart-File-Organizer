import organizer.logger
from organizer.organizer import FileOrganizer

import logging
logger = logging.getLogger(__name__)


def main():
    folder_path = input("Enter the folder path: ")
    
    try:
        organizer = FileOrganizer(folder_path)
    except ValueError as e:
        print(f"Error: {e}")
        logger.error(f"ERROR - Invalid folder path provided: {folder_path}")
        return
    
    print(f"Folder selected: {organizer.folder_path}")
    organizer.organize()

if __name__ == "__main__":
    main()
