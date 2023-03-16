input = "Hello!"
list_of_letters = list(input)
print(list_of_letters)

cipher_codes = []
for letter in list_of_letters:
  cipher_codes.append(ord(letter))
print('Here is my message', cipher_codes)


raw_codes = [72, 101, 108, 108, 111, 33]
converted_letters = []
for i in raw_codes:
  converted_letters.append(chr(i))

decrypted_message = "".join(str(i) for i in converted_letters)
print(decrypted_message)

def encrypt_message(string):
    
    list_of_letters = list(string)
    
    cipher_codes = []
    for letter in list_of_letters:
        cipher_codes.append(ord(letter))
    
    return cipher_codes

    
print(encrypt_message("Hello"))