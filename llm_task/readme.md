# Local LLM Inference Web Demo

This project runs a local Large Language Model (LLM) entirely in your browser using MediaPipe's GenAI Tasks. It uses a `.bin` model file for offline inference — no server-side processing or internet connection is required after setup.

## Files

- `index.html`: Web interface with input/output text areas.
- `index.js`: Loads the model and runs inference using MediaPipe.
- `gemma-2b-it-gpu-int4.bin`: Local LLM model file (must be in the same directory).

## How to Use

1. **Ensure all files are in the same folder**:
   - `index.html`
   - `index.js`

2. **Download the model file** (if not already present):
   - Run the following in your terminal:
     ```bash
     python download_model.py
     ```
   - This will download `gemma-2b-it-gpu-int4.bin` to the current folder.

3. **Start a local web server** from that folder:
   ```bash
   python -m http.server 8000


4. **Open your browser and go to:**
http://localhost:8000/index.html