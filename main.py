morse_codes = {
    'A': '.-', 'N': '-.', '0': '-----',
    'B': '-...', 'O': '---', '1': '.----',
    'C': '-.-.', 'P': '.--.', '2': '..---',
    'D': '-..', 'Q': '--.-', '3': '...--',
    'E': '.', 'R': '.-.', '4': '....-',
    'F': '..-.', 'S': '...', '5': '.....',
    'G': '--.', 'T': '-', '6': '-....',
    'H': '....', 'U': '..-', '7': '--...',
    'I': '..', 'V': '...-', '8': '---..',
    'J': '.---', 'W': '.--', '9': '----.',
    'K': '-.-', 'X': '-..-',
    'L': '.-..', 'Y': '-.--',
    'M': '--', 'Z': '--..'
}
data = input("Please Enter your String :")


def encode(input_string):
    encoded_string = [morse_codes.get(letter.upper()) for letter in input_string]
    print(" ".join(encoded_string))


encode(data)
