# Create your tests here.

# from https://github.com/abetlen/llama-cpp-python demo usage
from llama_cpp import Llama

llm = Llama(
    model_path="deep4/reflect/ml_models/for_codellamacpp/codellama-7b.Q5_0.gguf",
    n_gpu_layers=-1,  # Uncomment to use GPU acceleration
    # seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)
output = []
for i in range(0, 5):
    output.append(
        llm.create_chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": "Q: Write a simple list comprehension in Python  A:",
                }
            ],
            max_tokens=80,
            temperature=0.5 * i,
        )
    )  # Generate a completion, can also call create_completion
for i in range(0, 5):
    print(0.5 * i, output[i]["choices"][0]["message"]["content"])
