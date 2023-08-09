from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(message,shift_amount,action):
    cipher_text = []
    for letter in message:
        if letter.isalpha():
            if action == "encode":
                position = (alphabet.index(letter) + shift_amount ) % 26
            elif action == "decode":
                position = (alphabet.index(letter) - shift_amount ) % 26
            else:
                exit("Wrong option.")
            cipher_text.append(alphabet[position])
        else:
            cipher_text.append(letter)
    cipher_text = ("".join(cipher_text))
    print(f"Your {action}d message is {cipher_text}")


continue_cipher = True  

while continue_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    caesar(message=text,shift_amount=shift,action=direction)
    answer = input("Do you want to continue encoding and decoding messages? Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if answer == "no":
        continue_cipher = False
        print("Bye")