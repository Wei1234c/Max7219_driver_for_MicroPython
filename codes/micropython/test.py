import time
from time import sleep 
import max_matrix  
mm = max_matrix.MaxMatrix() 
 
def show_second_run():
    while True:
        current_time = time.localtime()
        year, month, day, hour, minute, second, _, _ = current_time        
        mm.showString('{0:02d}'.format(second), fixed_width = 4, left_padding = 2, right_padding = 2,) 
        sleep(1)         
        
def main():
    show_second_run()

main()    