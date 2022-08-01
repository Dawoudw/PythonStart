import random

rand = random.randint(0,10);
isCorrect =False

while isCorrect !=True:
    val = input("Please guess number between 0 to 10:  ")
    if int(val)==rand:
        print("your guess is right , the correct number is {} ".format(val))
        isCorrect=True
    else:
        print("wrong guess, please guess aonther number")


for i in range(1,11):
    print(i)