###1)

from psychopy import visual, monitors, event, core
import os

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=31.4, distance=60)
mon.setSizePix([1280,800])
win = visual.Window(monitor=mon) #define a window
my_image = visual.ImageStim(win, units = 'pix', size=(400,400))

#set durations
fix_dur = 0.2 #200 ms
image_dur = 0.1 #100 ms
text_dur = 0.2 #200 ms

refresh=1.0/59.20 #single frame duration in seconds

#set frame counts
fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

fix = visual.TextStim(win, text='+')

nBlocks=3
nTrials=4

main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg']

for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        
        my_image.image = os.path.join(image_dir,stims[trial])
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames): #for the whole trial...
            #-draw stimulus
            if 0 <= frameN <= fix_frames: #number of frames for fixation      
                fix.draw() #draw
                win.flip() #show
                
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
                    
            #number of frames for image after fixation
            if fix_frames < frameN <= (fix_frames+image_frames):      
                my_image.draw() #draw image
                fix.draw() #draw
                win.flip() #show 
                
                if frameN == (fix_frames+image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number  
                    
            #number of frames for the final text stimulus    
            if (fix_frames+image_frames) < frameN < total_frames:  
                fix.draw() #draw
                win.flip() #show  
                
                if frameN == (total_frames-1): #last frame for the text
                    print("End text frame =", frameN) #print frame number    
                
win.close()    

###2)

from psychopy import visual, monitors, event, core, logging
import os

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=31.4, distance=60)
mon.setSizePix([1280,800])
win = visual.Window(monitor=mon) #define a window

refresh = 1.0/59.20

#set durations
fix_dur = 0.2 #200 ms
image_dur = 0.1 #100 ms
text_dur = 0.2 #200 ms

#set frame counts
fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

fix = visual.TextStim(win, text='+')

nBlocks=2
nTrials=4

#add information to record dropped frames
win.recordFrameIntervals = True #record frames
#give the monitor refresh rate plus a few ms tolerance (usually 4ms)
win.refreshThreshold = 1.0/59.20 + 0.004

# Set the log module to report warnings to the standard output window 
#(default is errors only).
logging.console.setLevel(logging.WARNING)

my_image = visual.ImageStim(win, units = 'pix', size=(400,400))
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg','face02.jpg','face03.jpg', 'face04.jpg']

for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        my_image.image = os.path.join(image_dir,stims[trial])
        #-set stimuli and stimulus properties for the current trial
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames): #for the whole trial...
            #-draw stimulus
            if 0 <= frameN <= fix_frames: #number of frames for fixation      
                fix.draw() #draw
                win.flip() #show
                    
            #number of frames for image after fixation
            if fix_frames < frameN <= (fix_frames+image_frames):      
                my_image.draw() #draw image
                fix.draw() #draw
                win.flip() #show  
                    
            #number of frames for the final text stimulus    
            if (fix_frames+image_frames) < frameN < total_frames:  
                fix.draw() #draw
                win.flip() #show          

        #this will print total number of frames dropped following every trial
        print('Overall, %i frames were dropped.' % win.nDroppedFrames)

win.close()  
