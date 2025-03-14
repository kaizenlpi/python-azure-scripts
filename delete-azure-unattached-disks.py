Author: Matt Brady

import subprocess

# List of Azure Resource Groups (If needed, match each disk to its group)
resource_groups = [
    "CRE-S4-PCE-CUSTOMER0039",
    "CRE-S4-PCE-CANADAEAST-MANAGEMENT",
    "CRE-S4-PCE-CUSTOMER0050",
    "CRE-S4-PCE-SUPPORT0012",
    "CRE-S4-PCE-CUSTOMER0020",
    "CRE-S4-PCE-CUSTOMER0031",
    "CRE-S4-PCE-CUSTOMER0526",
    "CRE-S4-PCE-CUSTOMER0057",
    "CRE-S4-PCE-CUSTOMER0039",
    "CRE-S4-PCE-CUSTOMER0557"
]

# File containing disk IDs (each disk ID should be on a new line)
file_path = "disk-ids.azure.txt"

# Read disk IDs from the file and clean them
with open(file_path, "r") as file:
    disk_ids = [line.strip() for line in file if line.strip()]  # Remove spaces & empty lines

# Check if there are disks to delete
if not disk_ids:
    print("No disks found in the file.")
    exit()

# Convert disk IDs into a space-separated string for Azure CLI
disk_ids_string = " ".join(disk_ids)

# Construct and run the Azure CLI delete command
command = f"az disk delete --ids {disk_ids_string} --yes"
print(f"Running command: {command}")  # Debugging output

result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Print the command output
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

# Check for errors
if result.returncode != 0:
    print(f"Error deleting disks: {result.stderr}")
else:
    print("All specified disks have been deleted successfully.")
