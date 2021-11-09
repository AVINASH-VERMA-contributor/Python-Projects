import random
while(True):
    print("Press 'r' to roll or 'q' to quit")
    commnad=input()
    result=random.randint(1,6)
    if(commnad=='r'):
        print("The Number on dice comes out to be: ")
        print(result)
    else:
        break


