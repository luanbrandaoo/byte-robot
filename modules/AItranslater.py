from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

if __name__ == "__main__":
    cache_dir='.cache/'
else:
    cache_dir='modules/.cache/'

tokenizerToEN = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-roa-en", cache_dir=cache_dir)
modelToEN = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-roa-en", cache_dir=cache_dir)

tokenizerFromEN = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-mul", cache_dir=cache_dir)
modelFromEN = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-mul", cache_dir=cache_dir)
tokenizerFromEN.dest_lang = 'pt'

def translateToEN(input):
    inputs = tokenizerToEN.encode(input, return_tensors="pt")
    outputs = modelToEN.generate(inputs, num_beams=None, early_stopping=True)
    return tokenizerToEN.decode(outputs[0]).replace('<pad>','').strip()

def translateFromEN(input):
    input = ">>por<< "+input
    inputs = tokenizerFromEN.encode(input, return_tensors="pt")
    outputs = modelFromEN.generate(inputs, num_beams=None, early_stopping=True)
    return tokenizerFromEN.decode(outputs[0]).replace('<pad>','').strip()
