# imports random module
import random


# Opening a file
file = open("full_data.txt","rt")
counter_test = 0
counter_train = 0

f_train = open("train_CM.txt", "w")
f_test = open("test_CM.txt", "w")

for x in file:
    ss = x.isspace()
    if(not ss and counter_train<30000): 
        f_train.write(x)
        counter_train+=1
    elif(not ss and counter_test<10000):
        f_test.write(x)
        counter_test+=1

