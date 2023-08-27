import sys
print("Welcome to my geometric and arithmetic series")
decision = input("Arithmetic or Geometric series(Enter 1 for Arithmetic and 2 for Geometric): ")
summation = 0

if decision == "2":

 try:
  firstElement = float(input("Enter the first number of your set: "))
  r = float(input("Tell me the reason(r) for this set of numbers(not 1): "))
  numbers = int(input("Tell me how many numbers you want to add(integer): "))
 except:
    sys.exit("It looks like you didn't put a number")

 for i in range(numbers):
    summation = summation + firstElement*(r**(i))
 print(f"Your summation is {summation}!")

elif decision == "1":

    try:
        firstElement = float(input("Enter the first number of your set: "))
        d = float(input("Tell me the difference(d) for this set of numbers(not 0): "))
        numbers = int(input("Tell me how many numbers you want to add(integer): "))
    except:
        sys.exit("It looks like you didn't put a number")

    for i in range(numbers):
     summation = summation + firstElement + i*d

    print(f"Your summation is {summation}!")

else:
    print("You didn't choose 1 or 2, try again")
