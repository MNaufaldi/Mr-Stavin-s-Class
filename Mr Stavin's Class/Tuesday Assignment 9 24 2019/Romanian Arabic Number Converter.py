#Arabic Converter
def ArabicToRomanian(num):
    list_roman = ["I","V","X"]
    romanic_num = " "
    #X net
    romanic_num = (romanic_num + (list_roman[2] * (num // 10)))
    #V net
    romanic_num = (romanic_num + (list_roman[1] * ((num % 10) // 5)))
    #I net
    romanic_num = (romanic_num + (list_roman[0] * (num % 5)))
    #IV net and IX net(Cleanup)
    if "IIII" in (romanic_num):
        if "V" in (romanic_num):
           romanic_num = romanic_num.replace("VIIII","IX")
        else:
           romanic_num = romanic_num.replace("IIII","IV")
    return romanic_num
#Romanian Converter
def RomanianToArabic(num):
    arabic_num = " "
    #Specials net(Priority)
    num = num.replace("IX","9+")
    num = num.replace("IV","4+")
    #X net
    num = num.replace("X","10+")
    #V net
    num = num.replace("V","5+")
    #I net
    num = num.replace("I","1+")
    num = num + "0"
    arabic_num = eval(num)
    return arabic_num
