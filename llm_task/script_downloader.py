import requests
from pathlib import Path

# List of (URL, local filename) pairs
files_to_download = [
    (
        "https://raw.githubusercontent.com/mcoffman1/ROB-144/refs/heads/main/llm_task/download_model.py",
        "download_model.py"
    ),
    (
        "https://raw.githubusercontent.com/mcoffman1/ROB-144/refs/heads/main/llm_task/index.html",
        "index.html"
    ),
    (
        "https://raw.githubusercontent.com/mcoffman1/ROB-144/refs/heads/main/llm_task/index.js",
        "index.js"
    )
]

# Loop through each file and download if not already present
for url, filename in files_to_download:
    file_path = Path(filename)

    if file_path.is_file():
        print(f"{filename} already exists")
    else:
        print(f"Downloading {filename}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            file_path.write_bytes(response.content)
            print(f"Downloaded {filename} successfully")
        except requests.RequestException as e:
            print(f"Failed to download {filename}: {e}")
