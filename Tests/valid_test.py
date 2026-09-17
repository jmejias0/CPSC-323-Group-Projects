while(True):
    
    text = input("Enter characters: ") 

    valid_text = ""

    for character in text:
        if character.isalpha():  # Check if the input is alphabetic character
            valid_text += character  # Append valid characters to the valid_text string
        else:
            break

    print(valid_text)  # Print the valid characters to the console