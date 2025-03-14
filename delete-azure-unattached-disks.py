# Author Matt Brady
# 3-14-25 
# This worked today. Success. 

import subprocess
import pandas as pd
#from openpyxl import load_workbook

# Load the Excel file (Modify this for your actual file and sheet)
# file_path = "azure_disks.xlsx"
# sheet_name = "Sheet1"  # Change if needed
# column_name = "DiskName"  # The column containing disk names

#Azure Resource Group
resource_group = "cre-s4-pce-canadacentral" 

# Load the Excel file containing the volume IDs (disk IDs in this case)
file_path = "azure_cre_pce_unattached_volumes_2025_02_28.xlsx"
sheet_name = "azure_cre_pce_unattached_volume"
column_name = 'VOLUME_NAME'

# Read the disk names from the Excel file
df = pd.read_excel(file_path, sheet_name)

# Convert column values to a list (Remove empty values)
disk_names = df[column_name].dropna().tolist()

# Loop through each disk name and delete it using Azure CLI
for disk_name in disk_names:
    print(f"Deleting disk: {disk_name}...")
    
    # Construct the Azure CLI delete command
    command = f"az disk delete --resource-group {resource_group} --name {disk_name} --yes"
    
    # Execute the command
    subprocess.run(command, shell=True, check=True)

print("All disks processed.")
