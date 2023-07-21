from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

if __name__ == "__main__":
    cache_dir='.cache/'
else:
    cache_dir='modules/.cache/'

model_name = 'facebook/blenderbot-400M-distill'
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def blenderbot(inputMsg):
  inputs = tokenizer(inputMsg, return_tensors="pt")
  result = model.generate(**inputs).to('cuda')
  return str(tokenizer.decode(result[0])).replace('<s>','').replace('</s>','')
