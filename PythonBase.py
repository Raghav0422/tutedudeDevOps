file = open("file.txt",'r')
content =file.read()
print("content in file is: ",content)
file.close()

'''dic={}
n=0
while(n<4):
    n=int(input("Select the Option \n 1. Add a new student and grade \n 2. Update an existing student's grade. \n 3. Print all student Grade \n 4. exit \n\n"))
    if n==1:
        name=input("enter the name of student: ")
        grade=input("Enter Grade, (A/B/C/D/F): ")
        dic.update({name:grade})
        print("\n\n---------------------------------- \n new student grade added in system: \n ------------------------------------ \n\n")
    elif n==2:
        print("List of student in system, enter the name which need to update \n", dic)
        name=input("Enter the name of student which Grade to be updated: ")
        grade=input("Enter Grade, (A/B/C/D/F): ")
        dic[name]=grade
        print("\n\n---------------------------------- \n student grade  is updated \n ------------------------------------ \n\n\n")
    elif n==3:
        print("\n\n ---------------------------------\n Here is the list of all students \n", dic, "\n -------------------------------------\n\n")
    else:
        pass
        

'''
