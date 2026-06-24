# morse_code_simple.py

def get_morse_code():
    return {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
        'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
        'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
        'U': '..-', 'V': '...-','W': '.--',  'X': '-..-',
        'Y': '-.--','Z': '--..',
        '0': '-----','1': '.----','2': '..---','3': '...--',
        '4': '....-','5': '.....','6': '-....','7': '--...',
        '8': '---..','9': '----.'
    }


def text_to_morse(text):
    morse_dict = get_morse_code()
    result = ""

    for ch in text.upper():
        if ch == ' ':
            result += "/ "
        elif ch in morse_dict:
            result += morse_dict[ch] + " "

    return result.strip()


def morse_to_text(morse):
    morse_dict = get_morse_code()
    reverse_dict = {}

    for key in morse_dict:
        reverse_dict[morse_dict[key]] = key

    words = morse.split(" / ")
    final_text = ""

    for word in words:
        letters = word.split()
        for letter in letters:
            final_text += reverse_dict.get(letter, "")
        final_text += " "

    return final_text.strip()


def main():
    print("\nMORSE CODE TRANSLATOR")
    print("1. Text to Morse")
    print("2. Morse to Text")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        text = input("Enter text: ")
        print("Morse Code:", text_to_morse(text))

    elif choice == "2":
        morse = input("Enter morse (. - /): ")
        print("Decoded Text:", morse_to_text(morse))

    else:
        print("Invalid choice")


main()
