def client():
    string1 = open('C:/Users/HP/Desktop/the louvre/staffs.txt',).read()
    string2 = [line.strip() for line in open('C:/Users/HP/Desktop/the louvre/staffs.txt')]
    client = input('enter the name of the client: ')
    while client not in string2:
        if client not in string2:
            print ('the name you entered does not exist!\n please enter the right client\n>>')
            break
    else:
        print('welcome to the louvre', client)


def main ():
    string3 = 0
    print('how can i help you:\n ')

    while string3==0:
        string3 = eval(input("1.age\n2.occupation\n3.allergies\n4.email\n5.address\n6.phone_no\n>>"))

        if string3 == 1:
            age()
        elif string3 == 2:
            occupation()
        elif string3 == 3:
            allergies()
        elif string3 == 4:
            email()
        elif string3 == 5:
            address()
        elif string3== 6:
            phone_no()
        elif (string3 < 1 or string3 > 6):  # Validating User Option
            print("Please Enter Valid Option")  # Error Message

        else:
            print('incorrect')

def runAgain():  # Making Runable Problem1353
     runAgn = input("\nwant To Run Again Y/n: ")
     if (runAgn.lower() == 'y'):
      print(client())
     else:
        main() # Print GoodBye Message And Exit The Program

print()

def age():
    print('The name of the client in the system: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/age.txt').read()
    print(client1,'\n')

    returnn = eval(input('press 0 to go to main menu\n:'))

    while returnn !=0:
        returnn = eval(input('press 0 to go to main menu\n:'))
    else:
        main()

def occupation():
    print('The name of the client in the system: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/occupation.txt').read()
    print(client1,'\n')

    returnn = eval(input('press 0 to go to main menu\n:'))

    while returnn !=0:
        returnn = eval(input('press 0 to go to main menu\n:'))
    else:
        main()
def allergies():
    print('The name of the client in the system: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/allergies.txt').read()
    print(client1,'\n')

    returnn = eval(input('press 0 to go to main menu\n:'))

    while returnn !=0:
        returnn = eval(input('press 0 to go to main menu\n:'))
    else:
        main()
def email():
    print('The name of the client in the system: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/email.txt').read()
    print(client1,'\n')

    returnn = eval(input('press 0 to go to main menu\n:'))

    while returnn !=0:
        returnn = eval(input('press 0 to go to main menu\n:'))
    else:
        main()
def address():
    print('The name of the client in the system: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/address.txt').read()
    print(client1,'\n')

    returnn = eval(input('press 0 to go to main menu\n:'))

    while returnn !=0:
        returnn = eval(input('press 0 to go to main menu\n:'))
    else:
        main()
def phone_no():
    print('The name of the client in the system: ')
    client1 = open('C:/Users/HP/Desktop/the louvre/phone no.txt').read()
    print(client1,'\n')

    returnn = eval(input('press 0 to go to main menu\n:'))

    while returnn !=0:
        returnn = eval(input('press 0 to go to main menu\n:'))
    else:
        main()



print ('welcome to the lourve')
client()
main()
runAgain()


# brought to you by code-projects.or





