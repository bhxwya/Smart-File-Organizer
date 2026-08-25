import organizer.logger
from organizer.organizer import FileOrganizer
from organizer.utils import display_title, display_success

import logging
logger = logging.getLogger(__name__)


def main():
    display_title()
    folder_path = input("Enter the folder path: ")

    try:
        organizer = FileOrganizer(folder_path)
    except ValueError as e:
        print(f"Error: {e}")
        logger.error(f"Invalid folder path provided: {folder_path}")
        return
    
    print()
    print(f"Folder selected: {organizer.folder_path}")
    print()
    
    preview_files = organizer.organize(preview=True)

    if not preview_files:
        print("No available files to organize.")
        return

    print("Files available to organize:")

    for file in preview_files:
        print(file)
    print()

    while True:
        choice = input("Do you want to organize these files? (y/n): ").lower()

        if choice == "y":
            count = organizer.organize()
            display_success(count)
            break

        elif choice == "n":
            print("Organization cancelled.")
            break

        else:
            print("Please enter y or n.")


if __name__ == "__main__":
    main()
