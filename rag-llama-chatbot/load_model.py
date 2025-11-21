from llama_cpp import Llama
import os

# Path to your model
MODEL_PATH = "./models/Meta-Llama-3.1-8B-Instruct-IQ2_M.gguf"

# Check if model exists
if not os.path.isfile(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

# Configuration
CTX_SIZE = 4096
N_THREADS = 8

# Number of layers to offload to GPU (set 0 for CPU-only)
N_GPU_LAYERS = 0  # adjust according to your GPU memory

# Create Llama instance
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=CTX_SIZE,
    n_threads=N_THREADS,
    n_gpu_layers=N_GPU_LAYERS,  # set 0 for CPU-only
    verbose=True
)

print(f"Loaded model: {MODEL_PATH}")
