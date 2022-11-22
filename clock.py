#1)
from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=31.4, distance=60)
mon.setSizePix([1280,800])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win,text='+')
my_image = visual.ImageStim(win)

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show  
nTrials=3
wait_timer = core.Clock()

for trial in range(nTrials):
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    my_image.draw()
    win.flip()
    imgStartTime = wait_timer.getTime()
    core.wait(1)
    
    fix_text.draw()
    imgEndTime = wait_timer.getTime()
    win.flip()
    core.wait(.5)
    
    print("Image Duration (s) was {} seconds".format(imgEndTime - imgStartTime))
win.close()
