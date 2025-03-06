def getinput():
    number = int(input("please input the number of times to print\n"))
    language = input("please input the Language (among English, Chinese and Russian)\n")
    return number,language

def printout(number,language):
    if language == 'English':
        for i in range(number):
            print("Hello World")
    elif language == 'Chinese':
        for i in range(number):
            print("你好世界")
    elif language == 'Russian': 
        for i in range(number):
            print("Привет мир")

def main():
    number,language = getinput()
    printout(number,language)

main()