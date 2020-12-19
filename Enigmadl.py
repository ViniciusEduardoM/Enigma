# Importando as bibliotecas necessárioas
# Nós precisamos da biblioteca ascii_lowercase para puxar uma lista com alfabeto ingles
from string import ascii_lowercase

class enigma:
    def __init__(self, plugboard = {" ":" "}, alpha=None, beta=None, gama=None):
            
        ''' Setando as configurações do enigma antes da encriptação '''
        
        # Criando a lista do alfabeto
        self.alphabet = list(ascii_lowercase)

        '''
            Plugboard é um sistema de soquetes que era usado conectando pares de letras que eram 
            trocadas na entrada do primeiro rotor
        '''
        
        self.plugboard = plugboard
        
        if alpha != None and beta != None and gama != None and plugboard != None:
            ''' Aqui testamos se os valores do plugboard são letras e 
                setemos os valores dos rotores para aquilo que o construtor receber  '''
            if type(plugboard) is not dict:
                self.plugboard = {" " : " "}
            self.alpha = alpha
            self.beta = beta
            self.gama = gama
        
        # Aqui verificamos se a letra a ser encriptada está no plugboard, e assim duplicamos seu par
        for letter in list(self.plugboard.keys()):
            print(str(plugboard))
            if letter in self.alphabet:
                self.plugboard.update({self.plugboard[letter]:letter})
                print(str(plugboard))
        
        '''Aqui setamos o refletor que pega uma letra, e reflete sua posição no alfabeto, 
            como um a, invertido vira z e assim por diante'''
        self.reflector = [leter for leter in reversed(self.alphabet)]
        
    def shift(self, rotor):
        ''' Aqui criamos a primeira função do Enigma, essa função 'roda o alfabeto' 
            dependendo das configuraçoes setadas nos rotores '''
        shift_alphabet = ''.join(self.alphabet)
        shift_alphabet = list(shift_alphabet)
        for iter in range(rotor):
            shift_alphabet.insert(0, shift_alphabet[-1])
            shift_alphabet.pop(-1)
        #print(self.alphabet)
        #print('Separa')
        #print(shift_alphabet)
        return shift_alphabet
    def shift_reverso(self, rotor):
        ''' Esta função tem a mesma lógica da função anterior, 
            mas fazendo o caminho invertido para frente  '''
        shift_alphabet = ''.join(self.alphabet)
        shift_alphabet = list(shift_alphabet)
        for iter in range(rotor):
            shift_alphabet.append(shift_alphabet[0])
            shift_alphabet.pop(0)
        #print(self.alphabet)
        #print(shift_alphabet)
        return shift_alphabet

    def encrypt_text(self, text):
        ''' Esta é a função principal da classe, 
            ela chama todas as outras funcões de forma lógica para encriptar a mensagem '''
            
        encrypted_text = []
        # Processando o texto recebido
        text = text.lower() # Transformamos o texto totalmente em minusculo
        text.split() # 'Splitamos' o texto, ou seja, o cortamos, deixando cada letra ser um objeto numa lista
        
        # Aqui começa a encriptação letra por letra
        for letter in text:
            # Checamos se a letra está no plugboard
                if letter in self.plugboard:
                # Se a letra está, a encriptamos com seu par
                    
                    letter = self.plugboard[letter]
                    print('Está no plugboard -> ' + letter)
                ''' Aqui testamos se o caracter é um espaço, se for, 
                    o adicionamos no final do texto final e seguimos para outra letra'''
                if letter == ' ':
                    encrypted_text.append(' ')
                
                else:
                
                    # Aqui temos a letra sendo ecriptada pelo primeiro rotor
                    temp_letter = self.shift(self.alpha)[self.alphabet.index(letter)]
                    print("alpha - {}".format(temp_letter))
                    # Aqui temos a letra sendo ecriptada pelo segundo rotor
                    temp_letter = self.shift(self.beta)[self.alphabet.index(temp_letter)]
                    print("beta - {}".format(temp_letter))
                    # Aqui temos a letra sendo ecriptada pelo terceiro rotor
                    temp_letter = self.shift(self.gama)[self.alphabet.index(temp_letter)]
                    print("gama - {}".format(temp_letter))
                
                    # Aqui chamamos o refletor, para refletir a letra encriptada no alfabeto
                    print(temp_letter)
                    temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                    print("reflector - > {}".format(temp_letter))
                
                    ''' Caminho de volta ''' 
                    
                    # Aqui temos a letra sendo ecriptada pelo primeiro rotor reverso
                    temp_letter = self.shift_reverso(self.gama)[self.alphabet.index(temp_letter)]
                    #print('Reversed')
                    print("gama - {}".format(temp_letter))
                    # Aqui temos a letra sendo ecriptada pelo segundo rotor reverso
                    temp_letter = self.shift_reverso(self.beta)[self.alphabet.index(temp_letter)]
                    #print('Reversed')
                    print("beta - {}".format(temp_letter))
                    # Aqui temos a letra sendo ecriptada pelo terceiro rotor reverso
                    temp_letter = self.shift_reverso(self.alpha)[self.alphabet.index(temp_letter)]
                    #print('Reversed')
                    print("alpha - {}".format(temp_letter))
                    print('Letra final codificada -> ' + temp_letter)
                    
                    if temp_letter in self.plugboard:
                        temp_letter = self.plugboard[temp_letter]
                        print('Está na saida plugboard, virou -> ' + temp_letter)
        
                    encrypted_text.append(temp_letter) # Juntamos a letra temporaria ao texto encriptado e a printamos
                    
                    # Rodando os rotores * Explicado com detalhes na documentação * 
                    self.alpha += 1
                    if self.alpha % len(self.alphabet) == 0:
                        self.beta += 1
                        self.alpha = 0
                    if self.beta % len(self.alphabet) == 0 and self.alpha % len(self.alphabet) != 0 and self.beta >= len(
                        self.alphabet) - 1:
                        self.gama += 1
                        self.beta = 1
                    print('Valor do rotor beta - {}'.format(self.beta)) # Setamos o novo valor de Beta
                    print('Valor do rotor alpha - {}'.format(self.alpha))# Setamos o novo valor de Alpha
                
                    print('Fim encriptação da letra')
                    print('------------------------------------ \n')
        print('Mensagem encriptada/decriptada:\n')
        return ''.join(encrypted_text) # Depois de todo loop de encriptação feito, mostramos a mensagem
        
alpha = int(input('Digite aqui o valor do Primeiro Rotor: ')) # Setando o valor do primeiro rotor
beta = int(input('Digite aqui o valor do Segundo Rotor: ')) # Setando o valor do segundo rotor
gama = int(input('Digite aqui o valor do Terceiro Rotor: ')) # Setando o valor do terceiro rotor

crypttxt = input('Digite aqui a mensagem a ser encriptada: ') # Recebendo a mensagem para ser encriptada

Enigma = enigma({'f':'g','d':'y','h':'b'}, alpha = alpha, beta = beta, gama = gama)

print(Enigma.encrypt_text(crypttxt))
