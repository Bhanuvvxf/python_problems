#Command Parser (with guard)

list = [input("Enter the command : "), input("Enter the file name : ")]

match list:
    case ["load",filename]:
        if filename[-1] == "t" and filename[-2] == "x":
            if filename [-3] == "t" and filename[-4] == ".":
                print("Loading a text file . ")
        else:
            print("loading file . ")
        
    case ["save",filename]:
        print("Saving file . ")
    case ["exit"]:
        print("Exiting")
    case _ :
        print("Unkown command")