def code():
    string1 = open('C:/Users/HP/Desktop/the louvre/codes.txt',).read()
    string2 = [line.strip() for line in open('C:/Users/HP/Desktop/the louvre/codes.txt')]
    code = input('enter the your code: ')
    while code not in string2:
        print ('the code you entered does not exist!\nplease enter the right code:')

    else:
        print('welcome to the louvre: ',code)


def main ():
    string3 = 0
    print('How can i help you:',)
    print()

    while string3==0:
        string3 = eval(input("1.stakehold1\n2.stakehold2\n3.stakehold3\n4.stakehold4\n5.stakehold5\n6.stakehold6\n>> "))

        if string3 == 1:
            stakehold1()
        elif string3 == 2:
            stakehold2()
        elif string3 == 3:
            stakehold3()
        elif string3 == 4:
            stakehold4()
        elif string3 == 5:
            stakehold5()
        elif string3 == 6:
            stakehold6()
    else:
            goback1 = eval(input("invalid response!... press 0 to go back:"))
            if goback1 == 0:
                main()

    ''''else:
        print('you made an error.')
        print()'''

def stakehold1():
    print('The details of the client in the system are: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/obinna.txt').read()
    print(client1,)

    request = eval(input('press 0 to go to main menu\n>>'))
    while request != 0:
      request = eval(input('press 0 to go to main menu\n>>'))
    else:
        main()


def stakehold2():
    print('The details of the client in the system are: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/mandy.txt').read()
    print(client1)

    request = eval(input('press 0 to go to main menu\n>>'))

    while request!=0:
        request = eval(input('press 0 to go to main menu\n>>'))
    else:
        main()

def stakehold3():
    print('The details of the client in the system are: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/martin.txt').read()
    print(client1)

    request = eval(input('press 0 to go to main menu\n>>'))

    while request!=0:
        request= eval(input('press 0 to go to main menu\n>>'))
    else:
        main()
def stakehold4():
    print('The details of the client in the system are: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/william.txt').read()
    print(client1)

    request = eval(input('press 0 to go to main menu:\n>>'))

    while request!=0:
        request = eval(input('press 0 to go to main menu\n>>'))
    else:
        main()
def stakehold5():
    print('The details of the client in the system are: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/ayo.txt').read()
    print(client1)

    request = eval(input('press 0 to go to main menu\>>:'))

    while request!=0:
        request = eval(input('press 0 to go to main menu\n>>'))
    else:
        main()
def stakehold6():
    print('The details of the client in the system are: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/chidi.txt').read()
    print(client1)

    request = eval(input('press 0 to go to main menu\n>>'))

    while request!=0:
        request = eval(input('press 0 to go to main menu\n>>'))
    else:
        main()

print(" ------------------------------------------------------")
print("|======== WELCOME TO THE LOUVRE ========|")
print("|======================================================|")
print('Greetings')
print()
main()







