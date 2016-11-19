import random
import time

def main():
    introduction()
    # give the player some starting loot
    loot = 5
    
    cavenumber = choosecave()
 
    print(cavenumber)
    if(cavenumber == 1):
        loot = friendly(loot)
    elif(cavenumber == 2):
        loot= dangerouscave(loot)
    elif(cavenumber == 2):
        loot= waterlesscave(loot)
    elif(cavenumber == -1):
        print("What! Quiting? No guts! No glory!")
    else:
        print("error: not a valid cave number\n")

    if(loot >= 0):
        print("you now have " + str(loot) + " gold coins!")
    else:
        print("sorry that you died in the game!")
                
def friendly(loot):
    #cavenumber == 1
    print ("You have encountered...")
    time.sleep(3)
    print("...the friendly dragon!")
    print("She has given you treasure!")
    loot= loot + 10
    #remove before turning in 
    print ("and you now have " + str(loot)+ " gold coins!")
    return(loot)

def dangerouscave(loot):
    #cavenumber=2
    print("You enter the cave...")
    time.sleep(1)
    print("You see a large dragon lurking in the shadows...")
    time.sleep(1)
    print("The dragon jumps in front of you and...")
    time.sleep(2)

    taken = 10
    loot=(loot-taken)
    if(loot<=0):
        print("Eats you!!!")
    else:
        print("Takes "+str(taken)+" of gold coins from your treasure!!!")
        print("Total Treasure ="+str(loot))
    return(loot)
 
def waterlesscave(loot):
    #cave 3 
    hoursTrapped = random.randint(1, 4)
    print("You enter the cave...")
    time.sleep(1)
    print("You find that you are trapped for " + str(hoursTrapped) + " hours")
    time.sleep(1)
    print("and there's no water...")
    time.sleep(2)

    print("You can buy water for 10 gold coins, enough for an hour")
    taken = 10*hoursTrapped
    loot=(loot-taken)
    if(loot<=0):
        print("You die of thirst!!!")
    else:
        print("This takes "+str(taken)+" of gold coins from your treasure!!!")
        print("Total Treasure ="+str(loot))
    return(loot)

def introduction():
    print("Welcome: To DO write instructions")

def choosecave():
    choice=input("Do you dare enter this cave [y/n]?")
    if(choice == 'n'):
        cave = -1         #-1 cave means quit
    else:
        cave = randomcave()
    return cave

def randomcave():
    cavenumber = random.randint(1, 3)
    return cavenumber


main()
