import math
import numpy as np
import matplotlib.pyplot as plt

print("Select an op: ")
print("1. Natural log")
print("2. log(a) to base b")
print("3. Antilog")
print("4. Exponential")
operation1 = input()

def natural_log():
    print("Select one option")
    print("1. Single digit input")
    print("2. array Input")
    operation2 = input()
    if operation2 == "1":
        x = int(input("Enter the value of x"))
        out1 = np.log(x)
        print("Natural log i.e., log(exp(x)) = ",out1)
    elif operation2 == "2":
        lst = []
        x1 = int(input("Enter the values of x: "))
        for i in range(0,x1):
            ele = int(input())
            lst.append(ele)
        print("Natural Log values are : ", np.log(lst))
        plt.plot(lst, lst, color = 'blue', marker = "*")
        plt.plot(np.log(lst), lst, color = 'red', marker = "o")
        plt.title("numpy.log()")
        plt.xlabel("Output")
        plt.ylabel("Input")
        plt.show()
    else:
        print("Syntax error/Invalid entry")

def logr():
    y = int(input("Enter Base value: "))
    y1 = int(input("Enter actual value: "))
    out2 = math.log(y1,y)
    print("logy(y1) = ",out2)

def Antilog():
    print("Select one option")
    print("1. ln(x)")
    print("2. logb(x)")
    operation3 = input
    if operation3 == "1":
        z = (input("Enter value: "))
        out3 = math.pow(10,z)
        print("Antilog = ", out3)
    elif operation3 == "2":
        z = (input("Enter value: "))
        out4 = math.exp(z)
        print("Antilog = ", out4)
    else:
        print("Syntax error or Invalid entry")

def expo():
    print("Select one option")
    print("1. exponential graph")
    print("2. exponential value")
    operation4 = input()
    if operation4 == "2":
        a = input("Enter the value: ")
        out5 = math.exp(a)
        if (out5 > 1):
            print("Growing exponential")
            print("Exponential value = ",out5)
        elif (out5 > 0 and out5 < 1):
            print("Decaying exponential")
            print("Exponential value = ",out5)
        else:
            print("Syntax error or Invalid entry")
    elif operation4 == "1":
        b = int(input("Enter start value for the graph: "))
        c = int(input("Enter stop value for the graph: "))
        d = input("Enter the constant for amplitude: ")
        time1 = np.arange(b,c,0.0001)
        amplitude_g = d * np.exp(time1)
        amplitude_d = d * np.exp(-time1)
        plt.plot(time1, amplitude_g, time, amplitude_d)
        plt.title('Exponential Curve', color = 'b')
        plt.xlabel('Time'+r'$\rightarraw$')
        plt.ylabel('Amplitude'+r'$\rightarrow')
        plt.legend(['Growing exponential, Decaying Exponential'])
        plt.grid()
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()

if operation1 == "1":
    natural_log()
elif operation1 == "2":
    logr()
elif operation1 == "3":
    Antilog()
elif operation1 == "4":
    expo()
else:
    print("Invalid entry")