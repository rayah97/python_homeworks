#qani chi mutqagrvel stop bary, mutqagrvac bolor tvery piti lcne filei mej dasavorvac achman kargov

numbers = []
while True:
    mstr = input("Please input a value or type 'stop' to exit: ")
    while mstr.lower() == "stop":
        try:
            ch=int(mstr)
            div= 100/ch
            numbers.append(str(div)).sort()
            
        except ZeroDivisionError:
            print("can not be 0")
            pass
        except ValueError:
            pass
    






