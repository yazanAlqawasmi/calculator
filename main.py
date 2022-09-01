#                          #                              اضافة مدخلات

print(9)
print(10/2)
name = input("entr your name :")
ege = input("entr your age :")
print("haloo "+ name)
print("your age :" +ege)
# _______________________________________________________________________________________
#                         جمع المدخلات ك text وليس ك رقم


nambar = input ("entr your farst nambar :")
nambr2 = input("iner your scand namber : ")
man = nambar+nambr2
print(man)
# -----------------------------------------------------------------------------------------
#                                         جمع مدخلا ك ارقام

nambr = input("intr your nambr : ")
nambr2 = input("intr your nambr : ")
lo = int (nambr)+int (nambr2)
print(lo)
# --------------------------------------------------------------------------------------------
#  عوده ...
#
opration=input("select the operation")
print(type(opration))
first_num=input("pleass enter first numer : ")
secandNum=input("pleass enter scnde numer : ")
output=0
match  opration :
    case '+':
            output = int(first_num) + int(secandNum)
    case '-':
            output = int(first_num) - int(secandNum)
    case '*':
            output = int(first_num) * int(secandNum)

    case '/':
            output = int(first_num) / int(secandNum)
    case _:
        print("error opration")
print(output)
# ______________________________________________________________________________________________________________


# ____________________________________________________________________________________________
#                            جمع المدخلات ك ارقام صحيحة وغير صحيحه


