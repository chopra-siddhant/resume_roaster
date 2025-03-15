from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load your fine-tuned model; adjust the path as needed.
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('path_to_your_finetuned_model')

def generate_roast(resume_text):
    input_text = f"Roast this resume humorously: {resume_text}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    outputs = model.generate(
        input_ids, 
        max_length=200, 
        num_return_sequences=1, 
        do_sample=True, 
        temperature=0.9
    )
    roast = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return roast

def generate_improvements(resume_text):
    input_text = f"Suggest creative improvements for this resume: {resume_text}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    outputs = model.generate(
        input_ids,
        max_length=200,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.9
    )
    improvements = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return improvements

def generate_professional_improvements(resume_text):
    input_text = f"Provide professional improvement suggestions for this resume: {resume_text}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    outputs = model.generate(
        input_ids,
        max_length=200,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7  # Slightly less randomness for professional tone
    )
    improvements = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return improvements
