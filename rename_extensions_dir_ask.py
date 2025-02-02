import os

def batch_rename_extensions():
    """Renames file extensions in a user-specified directory (without tkinter)."""

    folder_path = input("Enter the full path to the folder containing the files: ")

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist. Exiting.")
        return

    source_extension = input("Enter the current file extension (e.g., .txt): ").lower()
    target_extension = input("Enter the desired file extension (e.g., .pdf): ").lower()

    if not source_extension.startswith("."):
        source_extension = "." + source_extension
    if not target_extension.startswith("."):
        target_extension = "." + target_extension

    print(f"Changing files with extension '{source_extension}' to '{target_extension}' in folder: {folder_path}")

    save_originals = input("Do you want to save the original files with a different name? (yes/no): ").lower()

    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(source_extension):
                filepath = os.path.join(folder_path, filename)
                new_filename = filename[:-len(source_extension)] + target_extension
                new_filepath = os.path.join(folder_path, new_filename)

                if save_originals == "yes":
                    original_filename_no_ext = filename[:-len(source_extension)]
                    original_backup_filename = original_filename_no_ext + "_original" + source_extension
                    original_backup_filepath = os.path.join(folder_path, original_backup_filename)

                    os.rename(filepath, original_backup_filepath)
                    os.rename(original_backup_filepath, new_filepath)
                    print(f"Renamed: {filename} to {new_filename} (Original saved as {original_backup_filename})")

                elif save_originals == "no":
                    os.rename(filepath, new_filepath)
                    print(f"Renamed: {filename} to {new_filename} (Original deleted)")
                else:
                    print("Invalid input for saving originals. Assuming 'no'.")
                    os.rename(filepath, new_filepath)
                    print(f"Renamed: {filename} to {new_filename} (Original deleted)")

        print("Renaming complete.")

    except FileNotFoundError:
        print("No files with that extension were found in the selected folder.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    batch_rename_extensions()
