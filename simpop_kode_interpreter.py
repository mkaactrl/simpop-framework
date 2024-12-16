import os
import shutil
import zipfile  # For cracking ZIP files

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

def simpop_kode_interpreter():
    print("Welcome to Simpop Kode!")
    multiline_buffer = []
    in_multiline_mode = False

    while True:
        prompt = "> " if in_multiline_mode else "$ "
        command = input(prompt)

        # Multiline mode
        if command.startswith("$op.sys()"):
            print("Entering multiline mode... Type $opend.fin() to finish.")
            in_multiline_mode = True
            multiline_buffer = []
        elif command.startswith("$opend.fin()") and in_multiline_mode:
            print("Executing block...")
            block_code = "\n".join(multiline_buffer)
            try:
                exec(block_code)
            except Exception as e:
                print(f"Error in code block: {e}")
            in_multiline_mode = False
        elif in_multiline_mode:
            multiline_buffer.append(command)

        # Crack ZIP File
        elif command.startswith("$crack.zip"):
            print("Crack mode activated for ZIP files.")

        elif command.startswith("func crack"):
            parts = command.split()
            if len(parts) >= 3:
                filename = parts[2]
                dictionary = "passwords.txt"  # Default password dictionary file
                if os.path.exists(dictionary):
                    crack_zip(filename, dictionary)
                else:
                    print(f"Dictionary file '{dictionary}' not found.")
            else:
                print("Usage: func crack <filename>")

        # Create File
        elif command.startswith("func createfile"):
            parts = command.split()
            if len(parts) >= 3:
                filename = parts[2]
                try:
                    with open(filename, "w") as f:
                        print(f"File '{filename}' created successfully!")
                except Exception as e:
                    print(f"Error creating file: {e}")
            else:
                print("Usage: func createfile <filename>")

        # Print Command
        elif command.startswith("prn"):
            text = command.split("prn")[1].strip('()" ')
            print(text)

        # Exit
        elif command == "exit":
            print("Exiting Simpop Kode. Goodbye!")
            break
        else:
            print("Unknown command:", command)


# Run the interpreter
simpop_kode_interpreter()
