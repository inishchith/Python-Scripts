#To Add : Check for valid url (https :) convert to lower and then store/access
#To Add : Saving Current Browers Tabs

import webbrowser

f=open('Test.txt','a') # can use 'w' etc.

choice = input("Do you want to add links (y/n) ? \n")
if choice=='y' :
    while 1:
        f.write(str(input("Enter TagName under which you want to add links : \n")) + ' ')
        while 1 :
            f.write(str(input('Enter link :\n ')) +' ' )
            choice = input("Still want to add links (y/n) :\n ")
            if choice=='n':
                f.write('\n')
                break
        choice = input('Still want to add Tags (y/n) : \n')
        if choice=='n':
            break
    print("Done Adding")

choice = input("Do you wish to open some links under some tags ? (y/n) : \n")
if choice=='n':
    quit()
while 1 :
    tagname=input('Enter TagName to browse : \n')
    flag=0
    with open('Test.txt') as f:
        for line in f:
            lines= line.split()
            if tagname in lines :
                flag=1
                print(lines)
                for link in range(1,len(lines)):
                    webbrowser.open(lines[link])
    if flag==0 :
        print('Tag does not exist \n')
        choice = input('Still want to browse some tags ? (y/n) :\n')
        if choice=='n':
            print('Thanks , Bye!')
            f.close()
            quit()