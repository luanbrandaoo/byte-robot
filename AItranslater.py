from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-roa-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-roa-en")

def ptToEn(input):
    inputs = tokenizer.encode(input, return_tensors="pt")
    outputs = model.generate(inputs, num_beams=None, early_stopping=True)
    return tokenizer.decode(outputs[0]).replace('<pad>','').strip()