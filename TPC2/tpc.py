import sys

#def read_input():
#    """Função para ler o texto do canal de entrada."""
#    return sys.stdin.read()
#
#def parse_input(text):
#    """Função para extrair as sequências de dígitos do texto."""
#    result = 0
#    in_number = False
#    current_number = ""
#    for char in text:
#        if char.isdigit():
#            in_number = True
#            current_number += char
#        else:
#            if in_number:
#                result += int(current_number)
#                current_number = ""
#                in_number = False
#            if char.lower() == 'o':
#                if text.lower().startswith("off", pos):
#                    break
#            elif char.lower() == 'o':
#                if text.lower().startswith("on", pos):
#                    in_number = True
#                    pos += 1
#    return result
#
#def main():
#    in_sum = True
#    flag = True
#    while flag:
#        text = read_input()
#        if not text:
#            break
#        if not in_sum:
#            if "on" in text.lower():
#                in_sum = True
#            continue
#        result = parse_input(text)
#        if "=" in text:
#            print(result)
#            flag = False
#        if "off" in text.lower():
#            in_sum = False
#

#for line in sys.stdin:
#    print(line)

def reader():
     
    a_somar = True
    numero = ""
    resultado = 0
    pos = 0
    in_number = False

    for line in sys.stdin:
        pos = 0
        if line.lower().strip() == 'quit':
            break

        for char in line:
            
            if char.isdigit():
                numero += char
                in_number = True
            else :
                if a_somar and in_number:
                    resultado += int(numero)
                    numero = ""
                
                if char == '=':
                    print("Resultado = " + str(resultado))

                elif char.lower() == 'o':
                    if line.lower().startswith("off", pos):
                        a_somar = False
                        numero = ''

                    elif line.lower().startswith("on", pos):
                        a_somar = True
                        numero = ''
                in_number = False
            pos += 1
        


def main():
    reader()

if __name__ == "__main__":
    main()