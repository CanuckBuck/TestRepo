import time as t
import matplotlib.pyplot as plt

print("")
print("This program will test your typing speed and accuracy")
print("You will be prompted to type a word five times in a row.")
print("When you are done the program will report your number of")
print("mistakes and the time taken to type the word each time")
print("")

print('Type the word "Programming" five times as quickly as you can')
input("Press Any key to continue")

print("Start typing in...")
for x in range (3, 0, -1):  
    print(str(x) + "...")
    t.sleep(1)

print("")
print("Start!")
print("")

times = []
mistakes = 0

while len(times) < 5:
    starttime = t.time()
    entry = input(str(len(times) + 1) + ": ")
    endtime = t.time()
    times.append(endtime - starttime)
    if (entry != "Programming"):
        mistakes += 1

print("You made " + str(mistakes) + " mistake(s).")
print("")
print("Here's a graph showing your typing times.")
t.sleep(2)

x = ('1', '2', '3', '4', '5')
y = times
plt.plot(x,y)
plt.xlabel("Attempts")
plt.ylabel("seconds")
plt.title("Typing times")
plt.show()