import random


class Word():
    def __init__(self, txt, rare):
        self.eng = txt[0]
        self.hun = txt[1]
        self.rare = rare
def importFromFile():
    temp_list = []
    f = open('bank.txt', 'r', encoding='utf8')
    lines = f.read().split("\n")
    f.close

    for i in lines:
        temp_list.append(Word(i.split(":"), 3))

    return temp_list
def printList(list, leng):
    if leng == "hun":
        for i in range(len(list)):
            print(f"{list[i].hun}:{list[i].eng}")
        return 0
    for i in range(len(list)):
            print(f"{list[i].eng}:{list[i].hun}")
    return 0
def countMissing(list):
    temp = 0
    for i in range(len(list)):
        temp += list[i].rare
    return temp
def findWord(list):
    i = len(list)-1
    while True:
        j = random.randint(0, i)
        if list[j].rare != 0:
            return j
def checkWord(obj, leng):
    if leng == "hun":
        answ = input(f"{obj.hun} = ")
        if answ == obj.eng:
            obj.rare -= 1
            print(f":D")
            return obj
        obj.rare += 1
        print(f"X {obj.eng}")
        return obj
    answ = input(f"{obj.eng} = ")
    if answ == obj.hun:
        obj.rare -= 1
        print(f":D")
        return obj
    obj.rare += 1
    print(f"X {obj.hun}")
    return obj
def askQ(list, leng):
    missing = countMissing(list)
    while missing != 0:
        tempWord = findWord(list)
        list[tempWord] = checkWord(list[tempWord], leng)
        missing = countMissing(list)
        print(f"{len(list)*3}/{missing}")
def main():
    main_list = importFromFile()
    askQ(main_list, "hun")



main()