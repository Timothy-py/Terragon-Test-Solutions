# CEASER CYPHER
# Uppercase letters are shifted 5 letters to the right
# Lowercase letters are shifted 3 letters to the left
# The use of different shift patterns for uppercase and lowercase
# letters is to limit brute forece attack

while True:

    text = input("Enter message here: ")    # prompt the user to enter the text message and save in the variable 'text'

    cipher = ''                             # create a variable named 'cipher' to store the text that will be encrypted

    for char in text:                       # take the characters in the text one-by-one and check for
                                            # the following if conditions
        if char == ' ' or char.isdigit():
            continue                        # ignore spaces and digits characters in the message text

        if char.isalpha():                  # check if the character is a capital letter
            code = ord(char) + 5            # convert the character to ASCII code and add 5 to it to shift the
                                            # character 5 places to the right
            if ord(char) > ord('U'):        # check if the addition of 5 to the ASCII code result in an integer
                                            # greater than 90(i.e Z)
                code = ord(char) - 21       # deduct 21 from the ASCII code of such character so that it can start from A

        if char.islower():                  # check if the character is a lower case letter
            code = ord(char) - 3            # convert the character to ASCII code and deduct 3 from it to shift
                                            # the character 3 places to the left
            if ord(char) < ord('d'):        # check if the deduction of 3 from the ASCII code result in an
                                            # integer lesser than 97(i.e a)
                code = ord(char) + 23       # add 21 to the ASCII code of such character so that it can start from z

        cipher += chr(code)                 # convert the ASCII code back to alphabet and store it in the cipher variable
    print(cipher)                           # output the encrypted text message

# SAMPLE OUTPUT
>>	Enter message here: ADEYEYE Timothy sent 28 lines of codes to ARO Ayomide
>>	FIJDJDJYfjlqevpbkqifkbplczlabpqlFWTFvljfab


