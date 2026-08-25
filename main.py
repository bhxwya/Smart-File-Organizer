from organizer import FileOrganizer


def main():
    folder_path = input("Enter the folder path: ")
    
    try:
        organizer = FileOrganizer(folder_path)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    print(f"Folder selected: {organizer.folder_path}")
    organizer.organize()

if __name__ == "__main__":
    main()
