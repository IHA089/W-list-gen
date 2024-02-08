import sys

def home_logo():
    print("""
        ####   ##     ##      ###        #####      #######     ####### 
         ##    ##     ##     ## ##      ##   ##    ##     ##   ##     ##
         ##    ##     ##    ##   ##    ##     ##   ##     ##   ##     ##
         ##    #########   ##     ##   ##     ##    #######     ########
         ##    ##     ##   #########   ##     ##   ##     ##          ##
         ##    ##     ##   ##     ##    ##   ##    ##     ##   ##     ##
        ####   ##     ##   ##     ##     #####      #######     #######
    
IHA089: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.
    """)

def single_combo(name, characters, file, total, flag):
    for char in characters:
        cpass1=name+char
        if flag == True:
            cpass2=char+name
            file.write(cpass1+"\n"+cpass2+"\n")
            total+1
        else:
            file.write(cpass1+"\n")
        total=total+1
    return total

def double_combo(name, characters, file, total, flag):
    for char1 in characters:
        for char2 in characters:
            cpass1=name+char1+char2
            if flag == True:
                cpass2=char1+char2+name
                file.write(cpass1+"\n"+cpass2+"\n")
                total = total+1
            else:
                file.write(cpass1+"\n")
            total=total+1
    return total

def triple_combo(name, characters, file, total, flag):
    for char1 in characters:
        for char2 in characters:
            for char3 in characters:
                cpass1=name+char1+char2+char3
                if flag == True:
                    cpass2=char1+char2+char3+name
                    file.write(cpass1+"\n"+cpass2+"\n")
                    total=total+1
                else:
                    file.write(cpass1+"\n")
                total=total+1
    return total

def fourth_combo(name, characters, file, total, flag):
    for char1 in characters:
        for char2 in characters:
            for char3 in characters:
                for char4 in characters:
                    cpass1=name+char1+char2+char3+char4
                    if flag == True:
                        cpass2=char1+char2+char3+char4+name
                        file.write(cpass1+"\n"+cpass2+"\n")
                        total=total+1
                    else:
                        file.write(cpass1+"\n")
                    total=total+1
    return total

def fifth_combo(name, characters, file, total, flag):
    for char1 in characters:
        for char2 in characters:
            for char3 in characters:
                for char4 in characters:
                    for char5 in characters:
                        cpass1=name+char1+char2+char3+char4+char5
                        if flag == True:
                            cpass2=char1+char2+char3+char4+char5+name
                            file.write(cpass1+"\n"+cpass2+"\n")
                            total=total+1
                        else:
                            file.write(cpass1+"\n")
                        total=total+1
                        
    return total

def Main():
    try:
        name = input("Enter target name(Ex. john) :::")
        name = name[0].lower() + name[1:]
        try:
            name = int(name)
            print("Please enter string not integer")
            sys.exit()
        except ValueError:
            pass

        wordlist_name = input("Enter wordlist name ::: ")
        Name=name.capitalize()


        characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$']
        print("Char List ::: ", end="")
        for c in characters:
            print("{} ".format(c), end="")
        print()
        check = input("Do you want to add more characters in char List[y/n] ::: ")
        if check == "y" or check == "Y":
            more_char = input("Enter characters by commas(Ex. : ^,&,*,) ::: ")
            if "," not in more_char and len(more_char) > 1:
                print("Please enter comma between each character")
                sys.exit()
            else:
                chars = more_char.split(",")
                for cc in chars:
                    if cc not in characters:
                        characters.append(cc)
                print("New Char List ::: ", end="")
                for c in characters:
                    print("{} ".format(c), end="")
                print()
        else:
            pass

        check = input("Do you want to remove characters from char list[y/n] ::: ")
        if check == "y" or check == "Y":
            rm_char = input("Enter characters by commas(Ex. : 1,2,@,#) ::: ")
            if "," not in rm_char and len(rm_char) > 1:
                print("Please enter comma between each character")
                sys.exit()
            else:
                chars = rm_char.split(",")
                for cc in chars:
                    if cc in characters:
                        characters.remove(cc)
                print("New Char List ::: ", end="")
                for c in characters:
                    print("{} ".format(c), end="")
                print()
        else:
            pass
        check = input("Do you want to use special characters before target name[y/n] ::: ")
        if check == "y" or check == "Y":
            flag = True
        else:
            flag = False
    except KeyboardInterrupt:
        print("\nExit by user....")
        sys.exit()            

    file = open(wordlist_name, 'w')
    i=0
    i=single_combo(name, characters, file, i, flag)
    i=single_combo(Name, characters, file, i, flag)

    i=double_combo(name, characters, file, i, flag)
    i=double_combo(Name, characters, file, i, flag)

    i=triple_combo(name, characters, file, i, flag)
    i=triple_combo(Name, characters, file, i, flag)

    i=fourth_combo(name, characters, file, i, flag)
    i=fourth_combo(Name, characters, file, i, flag)

    i=fifth_combo(name, characters, file, i, flag)
    i=fifth_combo(Name, characters, file, i, flag)
    file.close()

    print("Total Password generated ::: {}".format(i))

if __name__ == "__main__":
    home_logo()
    Main()
