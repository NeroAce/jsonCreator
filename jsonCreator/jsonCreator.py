def  main():
   pass

def createJson(dic,fileName,path=""):
    strDict = str(dic)

    if (len(path)!=0):
        if path[len(path)-1]!="/":
            path = path+"/"

    if (type(dic)!= dict):
        print(f'<Failed create> InputError: {dic} is {type(dic)} not dict')
        return "Failed"
    try:

        strDict  = strDict.replace("'",'"')

        with open(f"{path}{fileName}.json","w") as files:
            files.write(strDict)
            print(f"<Done create>:{path}{fileName}.json")

    except FileNotFoundError:
        print(f"<Failed create> No such directory: {path}")


if __name__=="__main__":
    main()
