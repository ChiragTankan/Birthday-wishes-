import time

from random import randint

for i in range(1,100):

    print('  ')

space='  '

for i in range(1,1000):

    count=randint(1,99)

    while(count>0):

        space+=' '

        count-=1

    if(i%10==0):

         print(space+ 'Happy Birthday!')

    elif(i%9==0):

         print(space+'🎊Happy Birthday Chirag tankan')

    elif(i%8==0):

         print(space+'🎂')

    elif(i%7==0):

         print(space+'🥞Happy Birthday Chirag tankan')

    elif(i%6==0):

         print(space+'Happy Birthday Chirag tankan 🍩')

    elif(i%5==0):

         print(space+'🍰')

    elif(i%4==0):

         print(space+'🍫')

    elif(i%3==0):

         print(space+'🥧')

    elif(i%2==0):

         print(space+'Happy Birthday Chirag tankan🧁')

    elif(i%1==0):

         print(space+'🍨')

    space='  '

    time.sleep(0.2)
