Welcome = 0
Numbers = []
try:
 Welcome = int(input("Welcome to my Calculator of Statistics, how many numbers you need: "))

 print("Write each one of the numbers...")

 for number in range(Welcome):
    Numbers.append(int(input("Number " + str(int(number) + 1) + ": ")))

except:
    print("Invalid input")

Counted = []
Repetitions = []
Summation = float()
i = -1
Index_mode = []
mode_number = []

for number in Numbers:
    if not(number in Counted):
       Repetitions.append(Numbers.count(number))
       Counted.append(number)

if Repetitions.count(max(Repetitions)) == 1:
    mode_number = Counted[Repetitions.index(max(Repetitions))]
else:
    for number in Repetitions:
        i = i + 1
        if number == max(Repetitions):
            Index_mode.append(i)

number_of_modes = len(Index_mode)

if number_of_modes == 0:
    number_of_modes = 1

for index in Index_mode:
    mode_number.append(Counted[index])

if number_of_modes > 1:
  print("We got " + str(number_of_modes) + " modes, which they are: " + str(mode_number))
else:
    print("Your mode is " + str(mode_number))

if max(Repetitions) == 1 and number_of_modes > 1:
     print("Each one of the modes repeats 1 time")
elif number_of_modes > 1:
    print("Each one of the modes repeats " + str(max(Repetitions)) + " times")

if number_of_modes == 1 and max(Repetitions) == 1:
    print("Your mode repeats 1 time")
elif number_of_modes == 1 and max(Repetitions) > 1:
    print("Your mode repeats " + str(max(Repetitions)) + " times")

# Here we start to get the average

for number in Numbers:
    Summation = Summation + number

average = Summation/Welcome

print(f"Your average is {average}")

# Here we start to get the median number
Median = []
Rep = []
Median_number = 0
r = 0

for count in range(len(Numbers)):
  r = 0
  for count2 in range(len(Numbers)):
      if Numbers[count] > Numbers[count2]:
         r = r + 1
      if count2 == (len(Numbers) - 1):
          Rep.append(r)

for countt in range(len(Rep)):
    if Rep.count(countt) == 1:
        Median.append(Numbers[Rep.index(countt)])
    if Rep.count(countt) > 1:
        for number in range(Rep.count(countt)):
            Median.append(Numbers[Rep.index(countt)])

if len(Numbers) % 2 == 1:
   Median_number = Median[int((len(Numbers) - 1)/2)]

if len(Numbers) % 2 == 0:
    Median_number = (Median[int((len(Numbers))/2) - 1] + Median[int((len(Numbers))/2)])/2

print(f"Your median is {Median_number}!")
print(Median)
# Deviation mean
Sum_deviation = 0
deviation_mean = 0

for number in Numbers:
  Sum_deviation = Sum_deviation + abs(average - number)

deviation_mean = Sum_deviation / Welcome
print(f"Your deviation mean is {deviation_mean}")
# Standard deviation
Sum_standard = 0
for number in Numbers:
    Sum_standard = Sum_standard + (abs(average - number))**2

Variance = Sum_standard / Welcome
deviation_standard = (Variance)**(1/2)

print(f"Your Variance is {Variance}")
print(f"Your Standard deviation is {deviation_standard}")
