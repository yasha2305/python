import os
import shutil
import hashlib
import time

# Generate file hash
def get_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()

# Synchronize folders
def sync_folders(source, backup):

    if not os.path.exists(backup):
        os.makedirs(backup)

    copied = 0

    for root, dirs, files in os.walk(source):

        relative_path = os.path.relpath(
            root,
            source
        )

        backup_root = os.path.join(
            backup,
            relative_path
        )

        os.makedirs(
            backup_root,
            exist_ok=True
        )

        for file in files:

            source_file = os.path.join(
                root,
                file
            )

            backup_file = os.path.join(
                backup_root,
                file
            )

            copy_required = False

            if not os.path.exists(
                backup_file
            ):
                copy_required = True

            else:

                source_hash = get_hash(
                    source_file
                )

                backup_hash = get_hash(
                    backup_file
                )

                if source_hash != backup_hash:
                    copy_required = True

            if copy_required:

                shutil.copy2(
                    source_file,
                    backup_file
                )

                copied += 1

                print(
                    f"Copied: {source_file}"
                )

    print(
        f"\nSynchronization Complete!"
    )

    print(
        f"Files Updated: {copied}"
    )

# Main
def main():

    source = input(
        "Source Folder: "
    )

    backup = input(
        "Backup Folder: "
    )

    if not os.path.exists(source):

        print(
            "Source folder not found."
        )

        return

    sync_folders(
        source,
        backup
    )

if __name__ == "__main__":
    main()