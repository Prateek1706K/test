"""
Backup Utility Script

This script allows users to create compressed backups of files.
"""

import shutil
import datetime
import os

def backup_files(source: str, destination: str) -> None:
    """
    Creates a compressed backup of the source directory.

    :param source: The source directory to back up.
    :param destination: The directory where the backup will be stored.
    """
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")
    
    try:
        shutil.make_archive(backup_file_name, 'gztar', source)
        print(f"Backup successfully created at {backup_file_name}.tar.gz")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    source = r"D:\Python For Devops"  # Use raw strings to avoid escape issues
    destination = r"D:\Python For Devops\backups"

    backup_files(source, destination)
