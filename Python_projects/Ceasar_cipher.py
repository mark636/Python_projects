alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode to encrpyt, type decode to 'decode' to decrpyt:\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number\n"))

def encrpyt(text, shift):
    cipher_text = ""
    for letter in text:
        shifted_position = alpha.index(letter) + shift
        shifted_position %= len(alpha) 
        cipher_text += alpha[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")



encrpyt(text, shift)