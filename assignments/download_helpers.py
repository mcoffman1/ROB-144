import requests
from pathlib import Path

# download helper functions if it doesn't exist
if Path("helper_functions.py").is_file():
  print("helper_functions.py already exists")
else:
  print("Downloading helper_functions.py")
  request = requests.get("https://raw.githubusercontent.com/mcoffman1/ROB-144/refs/heads/main/assignments/helper_functions.py")
  with open("helper_functions.py", "wb") as f:
    f.write(request.content)
