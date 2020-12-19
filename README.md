#Enigma Machine

Enigma was an encryption machine invented by Arthur Scherbius, used by the Germans in World War II to send secret codes between the German navy. In short, Enigma was based on a more complex replacement chipher. Looking like a typewriter, when one letter was a keyboard, it would return another letter, any letter of the alphabet, except itself, but given its functioning, it would never return the same letter in the code, and in the vast majority of times that it wrote, it would receive a code entirely differently, a much more elaborate version than Caesar's key.

#Components

Rotors

Rotors were mechanical mechanisms used to replace letters
In which specific values were defined that would represent the number of shifts that the letter would do in the alphabet order
The machine had 3 of these that encrypted the letter in sequence respectively connected to the reflector, and made another round on the rotors in reverse order

This Python component is separated into 2 functions, shift and shift_reverse
The first one substitutes clockwise, as an argument the value passed for each rotor, and the second function performs counterclockwise

    def shift(self, rotor):
       
        shift_alphabet = ''.join(self.alphabet)
        shift_alphabet = list(shift_alphabet)
        for iter in range(rotor):
            shift_alphabet.insert(0, shift_alphabet[-1])
            shift_alphabet.pop(-1)
        return shift_alphabet
    def shift_reverso(self, rotor):
        
        shift_alphabet = ''.join(self.alphabet)
        shift_alphabet = list(shift_alphabet)
        for iter in range(rotor):
            shift_alphabet.append(shift_alphabet[0])
            shift_alphabet.pop(0)
        return shift_alphabet

The reflector

The reflector is the simplest part of the code, it takes the initial position of the letter passed to it and inverts its position in the alphabet, returning the letter in this position, for example an A becomes a Z, a B an Y.

    self.reflector = [leter for leter in reversed(self.alphabet)]

Plugboard

The plugboard is the most interesting part of Enigma, as it multiplies billions of times the complexity of encryption.

If it consists of forming pairs of letters, for example 'AG' and these will be exchanged in encryption, before and after encryption with their respective pair
Your logic is present throughout the code, so check the .py file

The Encryptation

Finally we come to the main function of the code: Encryption. We start by receiving the text typed by the user, and the value of the alpha, beta and gamma rotors. We split the text to become a list of letters and create a for function to scroll through that list.

Encryption is done letter by letter, so first we test if the letter has a pair on the plugboard, if yes, we replace it with its pair and we start the encryption, if not, this step is not performed

Then, the letter passes 1 time for each rotor in the hourly function, so 3 rounds, with rotor, alpha, beta and gamma, goes through the reflector, and is encrypted again in the counterclockwise direction, by the gamma, beta and alpha rotor. At the end, the letter obtained is concatenated at the end of a string. The values ​​of the slowest rotors are changed, based on the fastest rotors, the alpha will always change its value with each letter, the beta will only change when the alpha takes a complete turn in itself, and the gamma only when beta gives a complete turn in itself.

    def encrypt_text(self, text):


            encrypted_text = []

            text = text.lower() 
            text.split() 


            for letter in text:
                # Check if latter it in plugboard
                    if letter in self.plugboard:
                    # Se a letra está, a encriptamos com seu par

                        letter = self.plugboard[letter]
                        print('Está no plugboard -> ' + letter)

                    if letter == ' ':
                        encrypted_text.append(' ')

                    else:


                        temp_letter = self.shift(self.alpha)[self.alphabet.index(letter)]
                        print("alpha - {}".format(temp_letter))

                        temp_letter = self.shift(self.beta)[self.alphabet.index(temp_letter)]
                        print("beta - {}".format(temp_letter))

                        temp_letter = self.shift(self.gama)[self.alphabet.index(temp_letter)]
                        print("gama - {}".format(temp_letter))


                        print(temp_letter)
                        temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                        print("reflector - > {}".format(temp_letter))

                        ''' Reverse ''' 


                        temp_letter = self.shift_reverso(self.gama)[self.alphabet.index(temp_letter)]

                        print("gama - {}".format(temp_letter))

                        temp_letter = self.shift_reverso(self.beta)[self.alphabet.index(temp_letter)]

                        print("beta - {}".format(temp_letter))

                        temp_letter = self.shift_reverso(self.alpha)[self.alphabet.index(temp_letter)]

                        print("alpha - {}".format(temp_letter))
                        print('Final latter encrypt  -> ' + temp_letter)

                        if temp_letter in self.plugboard:
                            temp_letter = self.plugboard[temp_letter]
                            print('Está na saida plugboard, virou -> ' + temp_letter)

                        encrypted_text.append(temp_letter) 

                        # Rodando os rotores * Explicado com detalhes na documentação * 
                        self.alpha += 1
                        if self.alpha % len(self.alphabet) == 0:
                            self.beta += 1
                            self.alpha = 0
                        if self.beta % len(self.alphabet) == 0 and self.alpha % len(self.alphabet) != 0 and self.beta >= len(
                            self.alphabet) - 1:
                            self.gama += 1
                            self.beta = 1
                        print('Value of beta rotor  - {}'.format(self.beta)) # Set new value for Beta
                        print('Value of alpha rotor - {}'.format(self.alpha))# Set new valuw for Alpha

                        print('Fim encriptação da letra')
                        print('------------------------------------ \n')
            print('Message encypt/decrypt:\n')
            return ''.join(encrypted_text) # After loop ends, show the message
