from transformers import AutoModelForCausalLM, AutoTokenizer

if __name__ == "__main__":
    cache_dir='.cache/'
else:
    cache_dir='modules/.cache/'

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large", cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large", cache_dir=cache_dir)

def dialoGPT(inputMsg):
    new_user_input_ids = tokenizer.encode(str(inputMsg) + tokenizer.eos_token, return_tensors='pt')
    chat_history_ids = model.generate(new_user_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id).to('cuda')
    return str(tokenizer.decode(chat_history_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True))

if __name__ == "__main__":
    while 1:
        print(dialoGPT(input('Usuário: ')))