#Continous Additions
def addition(num_1, num_2):
    flag = True
    result = int(num_1) + int(num_2)
    additionalNum = ""
    while flag == True:
        additionalNum = (input("Enter another number: "))
        if additionalNum != "end":
            result = result + eval(additionalNum)
        else:
            flag == False
            print(result)
            break
addition(10,20)
#%%
# Task - create the remaining functions for substraction, multiplication and division
#Substraction
firstNum = input("Enter the first number: ")
secNum = input("Enter the second number: ")
def substract(num_1, num_2):
    return int(num_1) - int(num_2)
print (substract(firstNum,secNum))
#Multiplication
def multiplicate(num_1, num_2):
    return int(num_1) * int(num_2)
print(multiplicate(firstNum,secNum))
#Division
def divide(num_1, num_2):
    return float(num_1) / float(num_2)
print(divide(firstNum,secNum))