### For the sake of the small additions made I will give the entire code per question.

###1)
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
    imgEndTime = wait_timer.getTime()
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    print("Image Duration (s) was {} seconds".format(imgEndTime - imgStartTime))
win.close()

## The core.wait is pretty percise, marking times at 0.999.. seconds.

###2)
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
waitTimer = core.Clock() #meta timer for stimuli
stimTimer = core.Clock() # added stim timer to time stimuli

for trial in range(nTrials):
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    stimTimer.reset()
    imgStartTime = waitTimer.getTime()
    
    while stimTimer.getTime() <= 1: #added while loop
        my_image.draw()
        win.flip()
    imgEndTime = waitTimer.getTime()
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    print("Image Duration (s) was {} seconds".format(imgEndTime - imgStartTime))
win.close()

## With while loop we also have same level of percision at 0.999... seconds.

###3)

### Added more images for countdown timer. Still percise in recording countdown.

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

stims = ['face01.jpg','face02.jpg','face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg'] #create a list if images to show  
nTrials= len(stims)
waitTimer = core.Clock() #meta timer for stimuli
stimTimer = core.CountdownTimer() # added stim timer to time stimuli

for trial in range(nTrials):
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    stimTimer.reset()
    stimTimer.add(1)
    imgStartTime = waitTimer.getTime()
    
    while stimTimer.getTime() > 0: #added while loop
        my_image.draw()
        win.flip()
    imgEndTime = waitTimer.getTime()
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    print("Image Duration (s) was {} seconds".format(imgEndTime - imgStartTime))
win.close()

###4)

##Editing script as directed from previous level.

#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist

print(os.getcwd())
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
data_dir = os.path.join(main_dir,'data')

if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_dir):
    os.path.mkdir(data_dir)

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
cats = ['faces']*10
imgs = ['im1.png', 'im2.png', 'im3.png','im4.png','im5.png','im6.png','im7.png','im8.png','im9.png','im10.png']
catimgs = list(zip(cats,imgs))

#-stimulus properties like size, orientation, location, duration *
stimSize = [200, 200];
stimDur = 1;
stimOrien = [10];
#-start message text *
startMessage ("Welcome to the experiement, press any key to begin")
#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
pics = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']

'face' + str(number) + '.jpg'
ims_in_dir = sorted(os.listdir(images_dir))
if not pics == ims_in_dir:
    raise Exception("This image list do not match up!")
#-create counterbalanced list of all conditions *
catmings = list(zip(cats,imgs))
#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is 
    #correct") *
corrResp = [];
corrResp = np.zeros(20);

#-create an empty list for participant responses (e.g., "on this trial, response was a #X") *
corrResp = np.zeros(20);
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
corrResp = np.zeros(20);
#-create an empty list for response time collection *
corrResp = np.zeros(20);
#-create an empty list for recording the order of stimulus identities *
corrResp = np.zeros(20);
#-create an empty list for recording the order of stimulus properties *
corrResp = np.zeros(20);
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

blockTimer = core.Clock()
trialTimer = core.Clock()
stimTimer = core.Clock()
respTimer = core.Clock()
#=====================
#BLOCK SEQUENCE
#=====================
for thisBlock in range(nBlocks):
    blockTimer.reset()
    blockStart = blockTimer.getTime()
    #-present block start message
    #-randomize order of trials here *
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials)
        trialTimer.reset()
        trialStart = trialTimer.getTime()
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        stimTimer.reset()
        while stimTimer <= 1:
            fix_text.draw()#-draw fixation
            win.flip()#-flip window
        
        stimTimer.reset()
        respTimer.reset()
        while stimTimer <= .5:
            my_image.draw()#-draw stimulus
            win.flip()#-flip window
        
        #-draw stimulus
        #-...
        stimTimer.reset()
        while stimTimer <= 1:
            fix_text.draw()#-draw fixation
            win.flip()#-flip window
        
        event.waitKeys()
        RTrespTimer.getTime()
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        trialEnd = trialTimer.getTime()
        
    blockEnd = blockTimer.getTime()
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
win.close() #-close window
#-quit experiment
