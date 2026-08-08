#the function that allows the encoding of messages.
def encode(message: str, shift: int) -> str:
    encodedmessage = [] #the (initially empty) list where the encoded message is temporarily transported to later on.
    for character in message: #loops every character in the message being asked to be encoded, in order to encode said character.
        if character.isupper(): #checks whether the character is uppercase (uppercase and lowercase letters have different (ord) integer values.)
            newcharacter = chr((ord(character) - ord('A') + shift) % 26 + ord('A'))
            #Turns the character being focused on into an integer through (ord), and then removes the integer associated with the
            #first capital letter 'A', in order to get the character's integer down to 0 for the next step (otherwise the integers for the letters
            #would start at 65). Then the shift is added, before a modulo function is used to check whether the character will wrap
            #around the alphabet or not: if not, the modulo won't do anything and it'll be unaffected, but if the shift goes past 26, then the
            #remainder is used to determine which new character it's wrapped around to. Then the number is moved back to where it was by adding 'A'
            #(the reason it was subtracted was for the modulo to work) and then it's turned back into the encoded character.
            encodedmessage.append(newcharacter) #the character is added to the list.
        elif character.islower(): #checks whether the character is lowercase.
            newcharacter = chr((ord(character) - ord('a') + shift) % 26 + ord('a')) #does the same as the uppercase, but 'A' is replaced with 'a'.
            encodedmessage.append(newcharacter) #the character is added to the list.
        else: #if the character is not a letter at all:
            encodedmessage.append(character) #just adds it without uselessly encoding it.
    joinedmessage = "".join(encodedmessage) #joins every character in the list thus far into a single string, completing the encryption.
    print(joinedmessage) #prints the encryption.
    return(joinedmessage) #finishes the function.
 
def decode(message: str, shift: int) -> str: #the function that allows the decryption of messages.
    return encode(message, -shift) #this refers back to the encryption lines of code, but just removes the shift to decrypt it.

encode('xyz', 3)