import random
import time
import datetime

nameLog = "Audit Log.txt"
nameBase = "Base.txt"
nameFileBase = "Base2.txt"
nameSymbolFile = "Symbol.txt"
symbols = "qwertyuiop[]asdfghjkl;'\zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&()_+"
banWord = "cancel"
globalFlag = False
secretFile = "SECRET.txt"
nonSecFile = "NONSEC.txt"
gameExe = "GAME.exe"
newSecretFile = "NewSecretFile.txt"


class User:
    def __init__(self, name, passw, access,roles):
        self.name = name
        self.passw = passw
        self.access = access
        self.roles = roles

    def write(self, user):
        f = open(nameBase, 'a')
        f.write(user.name + '\t' + user.passw + '\t' + user.access + '\t' + user.roles + '\n')
        f.close()
        return 0


class File:
    def __init__(self, name, access):
        self.name = name
        self.access = access


def readFileBase():
    array2 = []
    f = open(nameFileBase, 'r')
    while True:  # цикл чтения данных из файла
        line = f.readline()  # читаем строчку
        if not line:  # если строка пустая - файл закончился, выходим из цикла
            break
        line = line.split('\t')  # преобразование строчки в массив значений - разделителем является '\t'

        objectFile = File(line[0], line[1][:1])
        array2.append(objectFile)
    f.close()
    return array2


def coding(msg):
    size = len(msg)
    msg2 = str(size) + "*" + msg
    size = len(msg2)
    if size % 6 == 0:
        count = int(size / 6)
    else:
        count = int(size / 6 + 1)
    result = ""
    it = 0
    for i in range(0, count):
        matrix = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        for j in range(0, 3):
            for k in range(0, 3):
                random.seed()
                matrix[j][k] = random.choice(symbols)
        if it < len(msg2):
            matrix[2][2] = msg2[it]
            it += 1
        if it < len(msg2):
            matrix[1][2] = msg2[it]
            it += 1
        if it < len(msg2):
            matrix[0][2] = msg2[it]
            it += 1
        if it < len(msg2):
            matrix[0][1] = msg2[it]
            it += 1
        if it < len(msg2):
            matrix[0][0] = msg2[it]
            it += 1
        if it < len(msg2):
            matrix[1][1] = msg2[it]
            it += 1
        for j in range(0, 3):
            for k in range(0, 3):
                result += str(matrix[j][k])
    return result


def encoding(msg):
    res = ""
    for it in range(0, int(len(msg) / 9)):
        matrix = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        tmp = msg[it * 9:it * 9 + 9]
        it2 = 0
        for i in range(0, 3):
            for j in range(0, 3):
                matrix[i][j] = tmp[it2]
                it2 += 1
        res += str(matrix[2][2])
        res += str(matrix[1][2])
        res += str(matrix[0][2])
        res += str(matrix[0][1])
        res += str(matrix[0][0])
        res += str(matrix[1][1])
    it2 = 0
    for a in res:
        if a == '*':
            break
        it2 += 1
    res = res[it2 + 1:it2 + 1 + int(res[0:it2])]
    return res


def readBase():
    array = []
    try:
        f = open(nameBase, 'r')
    except (OSError, IOError):
        f = open(nameBase, 'w')
        name = str(input("Введите имя для первого пользователя: "))
        while True:
            passw = str(input(
                "Введите пароль для первого пользователя. Пароль должен содержать 8 символов : "))
            if not checkPass(passw):
                print("Добро пожаловать!")
                f.write(name + '\t' + coding(passw) + '\t' + "9" + '\t' + "")
                array.append(User(name, coding(passw), "9"))
                f.close()
                f = open(nameBase, 'r')
                global globalFlag
                globalFlag = True
                break
    while True:  # цикл чтения данных из файла
        line = f.readline()  # читаем строчку
        if not line:  # если строка пустая - файл закончился, выходим из цикла
            break
        line = line.split('\t')  # преобразование строчки в массив значений - разделителем является '\t'
        user = User(line[0], line[1], line[2], line[3])
        array.append(user)
    f.close()
    return array


def checkPass(passw):
    if len(passw) < 8 or (len(passw) % 2 == 0):
        print("Неправильный пароль (Длина пароля меньше 8 символов или остаток от деления на три не равен нулю)")
        return 1
    digitA = passw[0::2]
    dog = passw[1::2]
    global mainSymbol
    for j in dog:
        if j != mainSymbol:
            print("Использован неверный символ")
            return 1
    if digitA.isdigit():
        return 0
    else:
        print("Неправильный пароль (Содержит неверные символы или неправильную последовательность)")
        return 1


def printInfo():
    print("Информация о всех пользователях системы: ")
    f = open(nameBase, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        print(line)


def fileChoice():
    global currentFile
    global currentRole
    while True:
        array2 = readFileBase()
        fileFlag = False
        fileFlag2 = False
        print("Доступные файлы: ")
        for i in array2:
            if currentRole == "Manager":
                if int(i.access) == 8 and currentUser.access == '8':
                    print(i.name)
                elif int(i.access) == 5 and currentUser.access == '5':
                    print(i.name)
                elif (int(i.access) == 5 or int(i.access) == 8) and currentUser.access == '9':
                    print(i.name)
            elif currentRole == "Worker":
                if 6 <= int(i.access) < 8 and currentUser.access == '8':
                    print(i.name)
                elif currentUser.access == '6' and int(i.access) == 6:
                    print(i.name)
                elif currentUser.access == '5' and int(i.access) == 5:
                    print(i.name)
                elif currentUser.access == '3' and int(i.access) == 3:
                    print(i.name)
                elif currentUser.access == '2' and int(i.access) == 2:
                    print(i.name)
                elif currentUser.access == '9' and ((3 <= int(i.access) <= 4) or (6 <= int(i.access) <= 7)):
                    print(i.access)
            elif currentRole == "Admin":
                if int(i.access) == 9:
                    print(i.name)
        while True:
            print("Введите название файла: ")
            fileName = str(input())
            for tmp2 in array2:
                if tmp2.name == fileName:
                    fileFlag = True
                    currentFile = tmp2
                    if currentRole == "Manager":
                        if int(currentFile.access) == 8 and currentUser.access == '8':
                            fileFlag2 = True
                        elif int(currentFile.access) == 5 and currentUser.access == '5':
                            fileFlag2 = True
                        elif (int(currentFile.access) == 5 or int(currentFile.access) == 8) and currentUser.access == '9':
                            fileFlag2 = True
                    elif currentRole == "Worker":
                        if 6 <= int(currentFile.access) < 8 and currentUser.access == '8':
                            fileFlag2 = True
                        elif currentUser.access == '6' and int(currentFile.access) == 6:
                            fileFlag2 = True
                        elif currentUser.access == '5' and int(currentFile.access) == 5:
                            fileFlag2 = True
                        elif currentUser.access == '3' and int(currentFile.access) == 3:
                            fileFlag2 = True
                        elif currentUser.access == '2' and int(currentFile.access) == 2:
                            fileFlag2 = True
                        elif currentUser.access == '9' and ((3 <= int(currentFile.access) <= 4) or (6 <= int(currentFile.access) <= 7)):
                            fileFlag2 = True
                    elif currentRole == "Admin":
                        if int(currentFile.access) == 9:
                            fileFlag2 = True
                    if not fileFlag2:
                        print("У вас неподходящий уровень допуска, повторите попытку")
                        continue
            if not fileFlag:
                print("Неверное имя файла, повторите попытку")
            if fileFlag:
                break
        break
    return currentFile


def userMenu():
    global currentRole
    while True:
        currentRole = str(input(f"Выберите роль из списка: {currentUser.roles}"))
        print(f"Вы выбрали роль {currentRole}!")
        print("1 - Работа с файлами")
        print("exit - Выйти с данной учетной записи")
        menu = input()
        if menu == '1':
            currentFile = fileChoice()
            print("1 - Записать информацию в файл")
            print("2 - Прочитать информацию из файла")
            print("cancel - Вернуться в главное меню")
            menu2 = input()
            if menu2 == '1':
                f = open(currentFile.name, 'w')
                print("Введите строку в файл: ")
                str1 = str(input())
                f.write(str1)
                f.close()
            elif menu2 == '2':
                f = open(currentFile.name, 'r')
                while True:
                    line = f.readline()
                    print(line)
                    if not line:
                        break
                f.close()
            elif menu2 == 'cancel':
                if currentUser.access == '9':
                    return
                continue
        elif menu == 'exit':
            return

# main interface
print("Добро пожаловать!")
try:
    x = open(nameSymbolFile, 'r')
    mainSymbol = x.readline()
except(OSError, IOError):
    mainSymbol = " "

while True:
    array = readBase()
    array2 = readFileBase()
    currentUser = User
    if not globalFlag:
        while True:
            name = str(input("Введите логин: "))
            flag = False
            flag2 = False
            for tmp in array:
                if tmp.name == name:
                    while True:
                        password = str(input("Введите пароль: "))
                        if password == encoding(tmp.passw):
                            flag = True
                            currentUser = tmp
                            break
                        else:
                            print("Неверный пароль")
                            print("Повторите попытку через 3...")
                            time.sleep(1)
                            print("2...")
                            time.sleep(1)
                            print("1...")
                            time.sleep(1)
                if flag:
                    flag2 = True
                    break
            if flag2:
                break
            print("Неверный логин")
    else:
        globalFlag = False
        currentUser = array[0]
    print("Успешный вход")

    try:
        al = open(nameLog, 'a')
    except (OSError, IOError):
        al = open(nameLog, 'w')
    time1 = datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    al.write(currentUser.name + '\t' + time1 + '\t')
    al.close()

    while True:
        if currentUser.access == "9":
            print("Вы являетесь админинстратором.")
            print("0 - добавить нового пользователя.")
            print("1 - изменить пользователя.")
            print("2 - показать информацию о всех пользователях.")
            print("3 - работа с файлами.")
            print("Сменить пользователя или выйти - любое другое число")
            var = input()
            if var == '0':
                while True:
                    exit = False
                    while True:
                        name = str(input("Для выхода напишите {banWord}. Введите логин: "))
                        if name == banWord:
                            exit = True
                            break
                        repeat = False
                        for tmp in array:
                            if tmp.name == name:
                                print("Логин используется")
                                repeat = True
                                break
                        if repeat:
                            continue
                        else:
                            break
                    if exit:
                        break
                    while True:
                        password = str(input("Для выхода напишите {banWord}. Введите пароль: "))
                        if password == banWord:
                            exit = True
                            break
                        if checkPass(password):
                            continue
                        else:
                            break
                    if exit:
                        break
                    access = str(input("Введите уровень доступа: "))
                    user = User(name, coding(password), access)
                    res = currentUser.write(user)
                    if res == 0:
                        print("Удачно")
                        array.append(user)
                        break
                    else:
                        print("Ошибка записи в файл")
            elif var == '1':
                while True:
                    exit = False
                    name = str(input("Для выхода напишите {banWord}. Введите имя пользователя для изменения:\n"))
                    if name == banWord:
                        break
                    i = 0
                    while i < len(array):
                        if name == array[i].name:
                            print("Для выхода напишите {banWord}. Введите новый уровень допуска:")
                            while True:
                                newss = input()
                                if newss == banWord:
                                    break
                                if newss == 'su' or newss == 'u':
                                    array[i].access = newss
                                    break
                                else:
                                    print('Введен неправильный тип допуска, повторите попытку.')
                            if newss == banWord:
                                break
                            f = open(nameBase, 'w')
                            for user in array:
                                f.write(user.name + '\t' + user.passw + '\t' + user.access + '\n')
                            f.close()
                            print('Успешное изменение.')
                            exit = True
                            break
                        i += 1
                    if exit:
                        break
                    print("Пользователь не найден.")
            elif var == '2':
                printInfo()
            elif var == '3':
                userMenu()
            else:
                break
        elif currentUser.access == '3':
            userMenu()
            break
        elif currentUser.access == '4':
            userMenu()
            break
        elif currentUser.access == '5':
            userMenu()
            break
        elif currentUser.access == '6':
            userMenu()
            break
        elif currentUser.access == '7':
            userMenu()
            break
        elif currentUser.access == '8':
            userMenu()
            break
    time2 = datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    al = open(nameLog, 'a')
    al.write(time2 + '\n')
    al.close()
    menu = int(input("Введите 1 - для выхода, 0 - для смены пользователя. "))
    if menu == 1:
        break
