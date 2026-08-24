from organizer import FileOrganizer


def main():
    folder_path = input("Enter the folder path: ")

    organizer = FileOrganizer(folder_path)
    print(f"Folder selected: {organizer.folder_path}")

    organizer.organize()

if __name__ == "__main__":
    main()
