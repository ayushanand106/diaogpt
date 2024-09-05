from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling 
from torch.utils.data import Dataset, DataLoader 
import torch

model = AutoModelForCausalLM.from_pretrained("./fine-tuned-dialoGPT") 
tokenizer = AutoTokenizer.from_pretrained("./fine-tuned-dialoGPT")

def get_response(input_text):
    print(input_text)
    # Tokenize the input text and append the end-of-sequence token
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")

    # Generate the output using the model
    output_ids = model.generate(input_ids, max_length=100)

    # Decode the output to get the response text
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return response
