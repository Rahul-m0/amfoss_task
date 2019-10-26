str_1=input("Enter the time which has to be converted (hh:mm:ssAM or hh:mm:ssPM ) :")
def convertTime(str_1):
    if str_1[-2:]=='PM' and str_1[:2]=="12":
        return "00"+str_1[:-2]
    elif str_1[-2:]=="AM":
        return str_1[:-2]
    elif str_1[-2:]=="PM" and str_1[:2]=='12':
        return str_1[:-2]
    else:
        return str(int(str_1[:2])+12)+str_1[2:8]
print(convertTime(str_1))

