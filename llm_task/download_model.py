import urllib.request
import os

MODEL_URL = "https://huggingface.co/google/gemma-2b-it-GGUF/resolve/main/gemma-2b-it-gpu-int4.bin"
MODEL_NAME = "gemma-2b-it-gpu-int4.bin"

def download_model():
    if os.path.exists(MODEL_NAME):
        print(f"{MODEL_NAME} already exists. Skipping download.")
        return

    print(f"Downloading {MODEL_NAME}...")
    try:
        urllib.request.urlretrieve(MODEL_URL, MODEL_NAME)
        print("Download complete.")
    except Exception as e:
        print(f"Download failed: {e}")

if __name__ == "__main__":
    download_model()
