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

