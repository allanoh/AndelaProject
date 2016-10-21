import time, sys
import progressbar

def progress_bar(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    block = int(round(barLength*progress))
    text = "\rLoading application data:[{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
print ("")
for i in range(100):
    time.sleep(0.1)
    progress_bar(i/100.0)

