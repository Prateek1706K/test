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
    except (shutil.Error, OSError) as error:  # Catching specific exceptions
        print(f"Backup failed: {error}")

if __name__ == "__main__":
    SOURCE = r"D:\Python For Devops"  # UPPER_CASE for constants
    DESTINATION = r"D:\Python For Devops\backups"

    backup_files(SOURCE, DESTINATION)
