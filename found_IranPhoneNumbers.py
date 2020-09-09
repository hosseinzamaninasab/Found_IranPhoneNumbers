# determine Iran phone_numbers in text or anywhere : 09xxxxxxxxx

def is_phone_number(text):
    if len(text) != 11:
        return False  # not PhoneNumber-sized
    for index in range(0, 11):
        if not text[index].isdecimal():
            return False  # make sure about having numbers
    for index in range(0, 2):
        if not text[0] == '0':
            return False
        elif not text[1] == '9':
            return False  # we must have numbers with '09' at the start
    return True


# print(is_phone_number('09111111111')) # just for find out that our program work's fine!

message = input("Give me the text & I'll give you the numbers:\n")
found_number = False
for i in range(len(message)):
    digit = message[i: i+11]  # slicing the number from our text
    if is_phone_number(digit):
        print("Found number: ", digit)
        found_number = True
if not found_number:
    print("sorry, i didn't find any numbers")
