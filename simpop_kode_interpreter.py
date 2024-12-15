# Define the function to simulate 'print' in Simpop Kode
def prn(message):
    print(message)

# Define the system behavior (boot and flash)
class Sys:
    def __init__(self):
        self.sys_op_boot = 0  # Boot state (0 = not booted, 1 = booted)
    
    def boot_flash(self):
        # Simulate flashing the system
        prn("Flashing system boot... GUI initialized.")
    
    def config_flshbt(self):
        # Simulate configuring the system
        prn("System configuration updated.")
    
    def set_boot_state(self, state):
        self.sys_op_boot = state

# Initialize the Sys class to handle boot and configuration
sys = Sys()

# This function simulates the behavior of interpreting Simpop Kode
def interpret_simpop_code(code):
    lines = code.splitlines()
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("prn"):
            # Print command
            message = line[5:-1]  # Extract message from prn("message")
            prn(message)
        
        elif line.startswith("$sys.boot.flash"):
            # Flash boot
            sys.boot_flash()
        
        elif line.startswith("$sys.config.Flshbt"):
            # Configure system
            sys.config_flshbt()
        
        elif line.startswith("var sys_op_boot"):
            # Set system boot state
            state = int(line.split("=")[1].strip())
            sys.set_boot_state(state)
        
        elif line.startswith("if sys_op_boot == 1"):
            # Boot condition check
            if sys.sys_op_boot == 1:
                prn("Successful Boot")
                sys.boot_flash()  # Flash boot for GUI
            else:
                prn("Boot failed")
                sys.set_boot_state(0)  # Set boot state to 0 if it fails

# Example of Simpop Kode input
simpop_code = """
prn("Starting system operations...")
var sys_op_boot = 1
if sys_op_boot == 1
    prn("Successful Boot")
    $sys.boot.flash
else
    prn("Boot failed")
    var sys_op_boot = 0
$sys.config.Flshbt
"""

# Interpret and execute the Simpop Kode
interpret_simpop_code(simpop_code)
