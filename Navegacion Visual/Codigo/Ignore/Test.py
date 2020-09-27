import threading 
  
def gfg(): 
    print("GeeksforGeeks\n") 
  
timer = threading.Timer(5.0, gfg) 
timer.start() 

print(timer)

print("Done")