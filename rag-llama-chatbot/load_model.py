from llama_cpp import Llama

llama = Llama(
    model_path="./models/llama-3-8b-q4.gguf",
    n_ctx=4096,
    n_threads=8,
    n_gpu_layers=40,  # set to 0 if CPU only
    verbose=False
)
