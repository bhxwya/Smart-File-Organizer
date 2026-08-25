# Smart File Organizer

A modular CLI file organization application built with Python.

A command-line tool that automatically organizes files into categorized folders based on their file extensions, with duplicate handling, preview mode, input validation, logging, and a structured package architecture.

## Features

- Automatic file organization by extension
- Categorization of images, documents, audio, video, code, and other files
- Automatic creation of category folders
- Duplicate filename handling with automatic renaming
- Preview mode before organizing files
- User confirmation with `y/n` validation
- Folder path validation
- File organization count
- Logging of file movements and duplicate handling
- Modular package architecture

## Tech & Concepts

**Python · OOP · Modules & Packages · pathlib · File I/O · Dictionaries · Loops · Exception Handling · Logging · CLI · Git/GitHub**

## Project Structure

```text
Smart-File-Organizer/
├── organizer/
│   ├── __init__.py
│   ├── organizer.py
│   ├── categories.py
│   ├── utils.py
│   └── logger.py
│
├── logs/
│   └── log.log
│
├── test folder/
│
├── main.py
├── .gitignore
└── README.md
```

## Run

Make sure Python is installed, then run:

```bash
python -m main
```

Enter the path of the folder you want to organize.

The program will first preview the files and their target categories:

```text
Files available to organize:

resume.pdf → Documents
photo.jpg → Images
song.mp3 → Audio

Do you want to organize these files? (y/n):
```

Enter y to organize the files or n to cancel.

## Duplicate Handling

If a file with the same name already exists in the destination folder, the organizer automatically renames the new file:

```text
sample.py
sample_1.py
sample_2.py
```
This prevents existing files from being overwritten.

## Logging
The application records file organization events and duplicate handling in the log file:
logs/log.log

Example:

```text
2026-08-25 13:32:03,506 - organizer.organizer - INFO - Moved resume.pdf → Documents
```

## Version

v1.0.0