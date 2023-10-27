#c = (x -n)%26

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

text = input("Enter the text: ")
shift = int(input("Enter the shift: "))
print("The cipher text is: ")
print("the encrypted text is: ",encrypt(text, shift))