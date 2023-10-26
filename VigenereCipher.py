class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alpha = alphabet
        
    
    def encode(self, text):
        encodedList = []
        keyIndexList = []
        # For each character in the text, rotate through the letters of the key
        # and make a list of their indexes in the alphabet.  Wrap around to the 
        # first letter of the key if the key is shorter than the text.
        for i in range(len(text)):
            keyIndexList.append(self.alpha.index(self.key[i % len(self.key)]))

        # For each character in the text, find the index in the alphabet and add
        # to it the corresponding index from the key index list...     
        for i, char in enumerate(text):
            # unless the current character is not in the alphabet, then append it
            # directly to the output list without encoding.
            if char not in self.alpha:
                encodedList.append(char)
            else:
                encodeIndex = (self.alpha.index(char) + keyIndexList[i]) % len(self.alpha)
                # Find the character of the new index, and append it to the output list
                encodedList.append(self.alpha[encodeIndex])

        return ''.join(encodedList)

    
    def decode(self, text):
        decodedList = []
        keyIndexList = []
        # For each character in the text, rotate through the letters of the key
        # and make a list of their indexes in the alphabet.  Wrap around to the 
        # first letter of the key if the key is shorter than the text.
        for i in range(len(text)):
            keyIndexList.append(self.alpha.index(self.key[i % len(self.key)]))

        # For each character in the text, find the index in the alphabet and
        # subtract from it the corresponding index from the key index list...               
        for i, char in enumerate(text):
            # unless the current character is not in the alphabet, then append it 
            # directly to the output list without decoding.            
            if char not in self.alpha:
                decodedList.append(char)
            else:
                decodeIndex = self.alpha.index(char) - keyIndexList[i]
                # Find the character of the new index, and append it to the output list                
                decodedList.append(self.alpha[decodeIndex])

        return ''.join(decodedList)
