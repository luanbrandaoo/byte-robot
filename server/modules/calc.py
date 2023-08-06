from text_to_num import alpha2digit

operator_text = ['mais','menos','dividido','multiplicado','somado','diminuido','dividir','multiplica','com','sem','divisão','vezes','soma','tira','somado','subtraido','divisao','elevado','sobre','X','x','−','×','^','√','raizquadrada','raizcubica','∛']
operator_simb = ['+','-','/','*','+','-','/','*','+','-','/','*','+','-','+','-','/','**','/','*','*','-','*','**','raizquadrada','raizquadrada','raizcubica','raizquadrada','raizcubica']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','  ','ç','~','^','ã','ê','á','à','`','õ','ô','â','é','?','!']
calc_list = ['mais','menos','dividido','multiplicado','somado','diminuido','dividir','multiplica','com','sem','divisão','vezes','soma','tira','somado','subtraido','divisao','elevado','sobre','+','-','/','*','**',' x ','×','^','√','∛','raizcubica','raizquadrada']

def detect_calc(input):
    if input.startswith('quanto') or input.startswith('calcule'):
        print('quanto detected')
        print(input)
        for word in calc_list:
            if word in input:
                print(word+' detected')
                return True
        return False
    else:
        return False

def calc_voice(input):
    output = input.replace('**',' elevado à ').replace('/',' dividido pra ').replace('*',' vezes ').replace('=',' igual à ')
    return output

def calc(input):
    input = input.lower().strip().replace('tres','três').replace('milhao','milhão').replace('milhoes','milhões').replace('bilhao','bilhão').replace('bilhoes','bilhões').replace('bilhao','bilhão').replace('trilhoes','trilhões')
    input = alpha2digit(input, "pt")
    input = input.replace(' ','').replace('  ','')+'a'
    for x in range(len(operator_text)):
        x=x-1
        input = input.replace(operator_text[x],operator_simb[x])
    t=0
    while 1:
        t = t+1
        if 'raizquadrada' in input:
            end_position = input.find('raizquadrada')+12
            while 1:
                if input[end_position].isnumeric() == True:
                    while 1:
                        if input[end_position].isnumeric() == False:
                            break
                        else:
                           end_position = end_position+1 
                    break
                else:
                    end_position = end_position+1
            input = input[0:end_position]+'**0.5'+input[end_position:]
            input = input.replace('raizquadrada','')
        elif 'raizcubica' in input:
            end_position = input.find('raizcubica')+10
            while 1:
                if input[end_position].isnumeric() == True:
                    while 1:
                        if input[end_position].isnumeric() == False:
                            break
                        else:
                           end_position = end_position+1 
                    break
                else:
                    end_position = end_position+1
            input = input[0:end_position]+'**(1/3)'+input[end_position:]
            input = input.replace('raizcubica','')
        else:
            break
    for x in letters:
        input = input.replace(x,'')
    input = input.replace(',','.')
    result = eval(input)
    if result % 1 == 0:
        result = int(result)
    return '{}= {}'.format(input,result)

if __name__ == '__main__':
    print(calc(input('digite: ')))