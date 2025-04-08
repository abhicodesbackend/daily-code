"""
Raghuram 16-06-2019
Invoke thread from function
"""
import threading
import time
print("\nMulti Threading example")
count = 1
def gen(delay=35):
    global count
    time.sleep(1)
    while count < delay:
        time.sleep(1)
        print("\ngenThread - Count = ", count)
        count = count + 1
    print("\ngen-Thread Stopped")
def alm():
    global count
    while count < 31:
        #time.sleep(0.8)
        if((count % 10) == 0):
            print(f"\nalmThread - Count-{count} is multiple of 10")
    print("\nalm-Thread Stopped")
if __name__ == '__main__':
    genThread = threading.Thread(target=gen, args=())
    almThread = threading.Thread(target=alm, args=())
    print("\nStarting Thread genThread")
    genThread.start()
    print("\nStarting Thread almThread")
    almThread.start()
    """
    while genThread.is_alive():
        pass
    print("\ngenThread Stopped")
    while almThread.is_alive():
        pass
    print("\nalmThread Stopped")
    """
    genThread.join()
    almThread.join()
    
    print("Exiting main thread...")



    


