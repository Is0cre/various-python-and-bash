import subprocess

def nmap_wizard():
  # Prompt the user for the target IP address or hostname
  target = input("Enter the target IP address or hostname: ")

  # Prompt the user for the ports to scan
  ports = input("Enter the ports to scan (e.g. 80,443,1-65535): ")

  # Prompt the user for whether to use a silent scan
  silent = input("Silent scan (y/n)? ")

  # Set the nmap options
  options = f"-sV -p {ports}"
  if silent.lower() == "y":
    options += " -T4"

  # Call nmap and store the output in a variable
  result = subprocess.run(["nmap", options, target], capture_output=True)

  # Print the output
  print(result.stdout)

# Run the nmap wizard
nmap_wizard()
