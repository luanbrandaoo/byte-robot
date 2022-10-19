from text_to_num import alpha2digit

operator_text = ['mais','menos','dividido','multiplicado','somado','diminuido','dividir','multiplica','com','sem','divisão','vezes','soma','tira','somado','subtraido','divisao','elevado','sobre']
operator_simb = ['+','-','/','*','+','-','/','*','+','-','/','*','+','-','+','-','/','**','/']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','  ','ç','~','^','ã','ê','á','à','`','õ','ô','â','é','?','!']

def calc(input):
    input = input.lower().strip().replace('tres','três').replace('milhao','milhão').replace('milhoes','milhões').replace('bilhao','bilhão').replace('bilhoes','bilhões').replace('bilhao','bilhão').replace('trilhoes','trilhões')
    input = alpha2digit(input, "pt")
    input = input.replace('raiz quadrada','raiz').replace('raiz quadrada de ','raiz').replace('raiz de','raiz').replace('de','').replace(' ','').replace('  ','')+'a'
    while 1:
        if 'raiz' in input:
            end_position = input.find('raiz')+5
            while 1:
                if input[end_position].isnumeric() == False:
                    break
                else:
                    end_position = end_position+1
            input = input[0:end_position]+'**0.5'+input[end_position:]
            input = input.replace('raiz','')
        else:
            break
    input = input.replace(',','.')
    for x in range(len(operator_text)):
        x=x-1
        input = input.replace(operator_text[x],operator_simb[x])
    for x in letters:
        input = input.replace(x,'')
    result = eval(input)
    if result % 1 == 0:
        result = int(result)
    return '{}= {}'.format(input,result)

if __name__ == '__main__':
    print(calc(input('digite: ')))