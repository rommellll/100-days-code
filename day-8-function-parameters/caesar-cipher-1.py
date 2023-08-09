alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(message,shift_amount,action):
    cipher_text = []
    for letter in message:
        if action == "encode":
            position = (alphabet.index(letter) + shift_amount ) % 26
            message_action = "encoded"
        elif action == "decode":
            position = (alphabet.index(letter) - shift_amount ) % 26
            message_action = "decoded"
        else:
            exit("Wrong option.")
        cipher_text.append(alphabet[position])
        cipher_text = ("".join(cipher_text))
        print(f"Your {message_action} message is {cipher_text}")

# def encrypt(plain_text,shift_amount):
#   for letter in plain_text:
#     position = (alphabet.index(letter) + shift_amount ) % 26
#     #solution 2
#     # position = 26 - alphabet.index(letter)
#     # shifted_position = shift - position
#     encoded_text.append(alphabet[position])
#   cipher_text = ("".join(encoded_text))
#   print(f"The encoded text is {cipher_text}")

# def decrypt(encoded_message,shift_amount):
#   for letter in encoded_message:
#     position = (alphabet.index(letter) - shift_amount ) % 26
#     #solution 2
#     # position = 26 - alphabet.index(letter)
#     # shifted_position = shift - position
#     encoded_text.append(alphabet[position])
#   cipher_text = ("".join(encoded_text))
#   print(f"You decoded text is {cipher_text}")
    
  
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
caesar(message=text,shift_amount=shift,action=direction)