letters_numbers = {
    "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22,
    "n": 23, "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30, "v": 31, "w": 32, "x": 33, "y": 34, "z": 35
}

bad_use = False
bad_base_use = False

base = int(input("give me base: "))
number = input("Give me a number: ")

if base > 36 or base < 2:
    bad_base_use = True

summation = int()
i = len(number)

if base <= 10:
 for digit in number:
   if digit >= str(base):
       bad_use = True
   else:
     i -= 1
     summation = summation + int(digit)*(base**(i))

if base > 10:
    for digit in number:
        if digit.lower() in letters_numbers:
            if letters_numbers[digit.lower()] >= base:
                bad_use = True
            else:
                i -= 1
                summation = summation + int(letters_numbers[digit.lower()])*(base**i)
        else:
           i -= 1
           summation = summation + int(digit)*(base**(i))

if bad_use == False and bad_base_use == False:
    print(f"Your number converted to base 10 is {summation}")
elif bad_use == True and bad_base_use == False:
    print("You can't use the base or higher as a number, try again")
elif bad_use == False and bad_base_use == True:
    print("The limit for the base is between 36 and 2, sorry guy")
else:
    print("You are a completely dumb")
