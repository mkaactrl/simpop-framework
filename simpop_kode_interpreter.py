import os
import shutil
import zipfile

# Function for cracking ZIP files
def crack_zip(filename, dictionary):
    if not zipfile.is_zipfile(filename):
        print("Not a valid ZIP file.")
        return
    
    print(f"Attempting to crack '{filename}' with passwords from '{dictionary}'...")
    with zipfile.ZipFile(filename) as zf:
        with open(dictionary, 'r') as pwd_file:
            for password in pwd_file:
                password = password.strip()
                try:
                    zf.extractall(pwd=password.encode('utf-8'))
                    print(f"Success! Password: '{password}'")
                    return
                except Exception:
                    continue  # Wrong password, continue
    print("Failed to crack the file. Password not found.")

# Simpop Kode Interpreter
def simpop_kode_interpreter():
    print("Welcome to Simpop Kode!")
    multiline_buffer = []  # Buffer for multiline input
    in_multiline_mode = False  # Flag for system block mode

    while True:
        prompt = "> " if in_multiline_mode else "$ "
        command = input(prompt)

        # Enter Multiline Mode
        if command.startswith("$op.sys()"):
            print("Entering multiline mode... Type $opend.fin() to finish.")
            in_multiline_mode = True
            multiline_buffer = []

        # Finish Multiline Mode
        elif command.startswith("$opend.fin()") and in_multiline_mode:
            print("Executing block...")
            block_code = "\n".join(multiline_buffer)
            try:
                exec(block_code)  # Execute the buffered code
            except Exception as e:
                print(f"Error in code block: {e}")
            in_multiline_mode = False

        # Multiline Buffering
        elif in_multiline_mode:
            multiline_buffer.append(command)

        # Crack ZIP File
        elif command.startswith("$crack.zip"):
            print("Crack mode activated for ZIP files.")

        elif command.startswith("func crack"):
            parts = command.split()
            if len(parts) >= 3:
                filename = parts[2]
                dictionary = "passwords.txt"  # Default dictionary
                if os.path.exists(dictionary):
                    crack_zip(filename, dictionary)
                else:
                    print(f"Dictionary file '{dictionary}' not found.")
            else:
                print("Usage: func crack <filename>")

        # Create File
        elif command.startswith("func createfile"):
            
