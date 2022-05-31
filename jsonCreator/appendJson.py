def appendJson(dic,fileName,path=""):
    y =[]

    if (len(path)!=0):
        if path[len(path)-1]!="/":
            path = path+"/"

    if (type(dic) == dict):
        # try to get file with spacified path and name
        try:
        # if file found then open file in read mode
            with open(f"{path}{fileName}.json","r") as files:
               for file in files:
                   y.append(file)

            #check if file is not empty, if empty return error
            if len(y)==0:
                print(f"<Failed append> File is Empty:{path}{fileName}.json")
                return("<Failed append>")

            y = "".join(y).replace("[","").replace("]","")
            y = "["+y+","+str(dic)+"]"
            y = y.replace("'",'"')

            # write appended list to file
            with open(f"{path}{fileName}.json","w") as files:
                files.write(y)
            print(f"<Done append>:{path}{fileName}.json")

        # if file not found, return Error
        except FileNotFoundError:
            print(f"<Failed append> File Not Found : {path}{fileName}.json")

    # if input data type is not dict type return error
    else:
        print(f'<Failed append> InputError: {dic} is {type(dic)} not dict')
        return("InputError")