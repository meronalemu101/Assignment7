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
#-create a dialogue box that will collect current participant number, age, gender, handedness
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
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
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

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    print('Welcome to Block' + thisBlock)
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(catmings)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        print('Trials' + str(thisTrial+1))
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #wait .5 seconds
        #-draw stimulus
        my_image.draw()
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()
#-quit experiment
