import os
import time
import pyautogui

def clear():
    os.system('clear')

def header():
    clear()
    print ("  ###  #     ###    ###  #  #")
    print (" #     #      #    #     # # ")
    print ("#      #      #   #      ## ")
    print (" #     #      #    #     # # ")
    print ("  ###  ####  ###    ###  #  #")
    print ("     by SeekerRook20485 ")
    print("")


def Click():

    try:
        header()    
        f = float(input('Enter Desired Click Delay in seconds(0 for as fast as posible):'))
        header()
        n = int(input('Enter Number of Clicks(0 for Infinite):'))
        header()
        print("")  
        print ("CAUTION: You are strongly recomended to make this window always visible.")
        input ('Place Cursor in Desired Position and press ENTER to start:')
        
        if (n != 0):
            for i in range(n):
                print('click')
                pyautogui.click()                
                time.sleep(f)
                selector()
        else :
            while True:
                print('click')
                pyautogui.click()                
                time.sleep(f)

    
    except KeyboardInterrupt:
        selector()  

def Show(): 
    try:
        while True:
         header()            
         x,y = pyautogui.position()   
         print ('X: '+str(x),flush=True)
         print ('Y: '+str(y),flush=True)
         time.sleep(0.1)
    except  KeyboardInterrupt:
        selector()    
   
            

        

def Trace():
    try:
        header()
        while True:                            
            x,y = pyautogui.position()   
            print ('X: '+str(x)+' Y: '+str(y),flush=True)            
            time.sleep(0.1)
    except  KeyboardInterrupt:
        selector()        


def Quit():
    print()


def selector():
    print("")    
    c = input("Enter Command (Q/S/L/C): ")
    if selectorback(c) == False:
        print ("Invalid Choice")
        selector()
    

def selectorback(c):
    if c == 's' or c == 'S' :
        Show()
        return True
    elif  c == 'c' or c == 'C':
        Click()
        return True
    elif c ==  'l' or c == 'L':
        Trace()
        return True
    elif  c == 'q' or c == 'Q':
        Quit()
        return True
    else :return False



def Start():
    header()
    print ("Welcome To Click !!!")
    print ("You can use one of the following options:")
    print("") 
    print ("   (C)lick Mode: put cursor in desired position and  start clicking")
    print("") 
    print ("   (S)how Mode: show coordinates of cursor")
    print("") 
    print ("   (L)og Mode: print all the coordinates the cursor passes from")
    print("") 
    print ("   (Q)uit: terminates the application")
    print("") 
    print ("To Stop a Function press 'Ctrl'+'C'")
    print("")
    print("")  
    print ("CAUTION: You are strongly recomended to make this window always visible especially in Clicker Mode.")

    
    selector()


Start()
