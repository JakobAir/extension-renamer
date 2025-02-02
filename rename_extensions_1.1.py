import os

def batch_rename_extensions():
    """Renames file extensions and handles original file saving/deletion (in the same directory)."""

    source_extension = input("Enter the current file extension (e.g., .txt): ").lower()
    target_extension = input("Enter the desired file extension (e.g., .pdf): ").lower()

    if not source_extension.startswith("."):
        source_extension = "." + source_extension
    if not target_extension.startswith("."):
        target_extension = "." + target_extension

    print(f"Changing files with extension '{source_extension}' to '{target_extension}' in the current directory.")

    save_originals = input("Do you want to save the original files with a different name? (yes/no): ").lower()

    try:
        for filename in os.listdir():
            if filename.lower().endswith(source_extension):
                new_filename = filename[:-len(source_extension)] + target_extension

                if save_originals == "yes":
                    original_filename_no_ext = filename[:-len(source_extension)]  # Filename without extension
                    original_backup_filename = original_filename_no_ext + "_original" + source_extension # Append "_original"
                    os.rename(filename, original_backup_filename) # Rename the original

                    os.rename(original_backup_filename, new_filename) # Rename the copy

                    print(f"Renamed: {filename} to {new_filename} (Original saved as {original_backup_filename})")

                elif save_originals == "no":
                    os.rename(filename, new_filename)
                    print(f"Renamed: {filename} to {new_filename} (Original deleted)")
                else:
                    print("Invalid input for saving originals. Assuming 'no'.")
                    os.rename(filename, new_filename)
                    print(f"Renamed: {filename} to {new_filename} (Original deleted)")

        print("Renaming complete.")

    except FileNotFoundError:
        print("No files with that extension were found in this directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    batch_rename_extensions()
