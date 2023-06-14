alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    alphabet_index = alphabet.index(letter)
    if (alphabet_index + shift_amount) > (len(alphabet) - 1):
      alphabet_index = alphabet_index - len(alphabet)

    cipher_text += alphabet[alphabet_index+shift_amount]

  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  cipher_text = ""
  for letter in plain_text:
    alphabet_index = alphabet.index(letter)
    if (alphabet_index-shift_amount) < 0:
      alphabet_index = (len(alphabet) -1) + (alphabet_index-shift_amount)
    else:
      alphabet_index = alphabet_index - shift_amount

    cipher_text += alphabet[alphabet_index]

  print(f"The decoded text is {cipher_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction.lower() == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction.lower() == "decode":
  decrypt(plain_text=text, shift_amount=shift)
else:
  print("Type a valid direction encode/decode")