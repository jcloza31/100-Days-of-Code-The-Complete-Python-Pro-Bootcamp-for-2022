alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  if shift_amount >= 26:
      shift_amount = shift_amount % 26
  for char in start_text:
    if char not in alphabet:
        end_text += char
    else:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  
from art import logo
print(logo)

program_is_on = True
while program_is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no' ").lower()
    if play_again == "no":
        program_is_on = False
        print("Goodbye! Thanks for using our Caesar Cipher.")
    
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

