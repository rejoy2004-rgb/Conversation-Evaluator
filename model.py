from transformers import pipeline, GenerationConfig
import os

# suppress uneccesary warnings
#Keeps console output clean during execution
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

#Initialize text generation pipeline with Qwen2-1.5B-Instruct model
generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2-1.5B-Instruct"
)

#Define generation configuration
#max_new_tokens: limit response length
#do_sample=False: deterministic output (important for evaluation consistency)
gen_config = GenerationConfig(
    max_new_tokens=80,
    do_sample=False
)

def generate(prompt):
    """
    Generate model response for a given prompt.

    Input:
    - prompt: text prompt sent to the LLM

    Output:
    - generated text (model response only, without input prompt)
    """

    
    #Run inference using the pipeline 
    output = generator(
        prompt,
        generation_config=gen_config,
        return_full_text=False #return only generated response
    )
    return output[0]["generated_text"]
from transformers import pipeline, GenerationConfig
import os

# suppress uneccesary warnings
#Keeps console output clean during execution
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

#Initialize text generation pipeline with Qwen2-1.5B-Instruct model
generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2-1.5B-Instruct"
)

#Define generation configuration
#max_new_tokens: limit response length
#do_sample=False: deterministic output (important for evaluation consistency)
gen_config = GenerationConfig(
    max_new_tokens=80,
    do_sample=False
)

def generate(prompt):
    """
    Generate model response for a given prompt.

    Input:
    - prompt: text prompt sent to the LLM

    Output:
    - generated text (model response only, without input prompt)
    """

    
    #Run inference using the pipeline 
    output = generator(
        prompt,
        generation_config=gen_config,
        return_full_text=False #return only generated response
    )
    return output[0]["generated_text"]