#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Mon Nov  5 16:48:15 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'try2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexreblando/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/ebs/try2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='iMac', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "intro"
introClock = core.Clock()
welcome = visual.TextStim(win=win, name='welcome',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='default text',
    font='Arial',
    pos=(0, -.25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "restaurant_critic"
restaurant_criticClock = core.Clock()


# Initialize components for Routine "airport_customer_experience_manager_2"
airport_customer_experience_manager_2Clock = core.Clock()


# Initialize components for Routine "Grocery_Store_Customer_Experience_Manager"
Grocery_Store_Customer_Experience_ManagerClock = core.Clock()


# Initialize components for Routine "Couples_Therapist"
Couples_TherapistClock = core.Clock()


# Initialize components for Routine "Wedding_Planner"
Wedding_PlannerClock = core.Clock()


# Initialize components for Routine "MatchMaker"
MatchMakerClock = core.Clock()


# Initialize components for Routine "Business_Reporter"
Business_ReporterClock = core.Clock()


# Initialize components for Routine "Dean_of_Academic_Studies"
Dean_of_Academic_StudiesClock = core.Clock()


# Initialize components for Routine "intro_questions"
intro_questionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "role_questions"
role_questionsClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='default text',
    font='Arial',
    pos=(0, -.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='default text',
    font='Arial',
    pos=(-.25, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "narrative_intro"
narrative_introClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Questions:\n1. How does the person who is initiating the breakup feel before they do it? \n 2. Why does the initiator want to break up?  3. How does the person being broken up with respond?  4. Do the partners leave on good terms? ',
    font='Arial',
    pos=(0, -.25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_6 = visual.ImageStim(
    win=win, name='image_6',
    image='couples.jpg', mask=None,
    ori=0, pos=(.25, .3), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='Role:  Couples Therapist',
    font='Arial',
    pos=(-.25, .3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "RB_story"
RB_storyClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, -.25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win, name='image',
    image='AB_3.jpg', mask=None,
    ori=0, pos=(0, .25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
welcome.setText(instruct_text)
key_resp_6 = event.BuilderKeyResponse()
text_12.setText(instruct_text2
)
# keep track of which components have finished
introComponents = [welcome, key_resp_6, text_12]
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    if t >= 0.0 and welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome.tStart = t
        welcome.frameNStart = frameN  # exact frame index
        welcome.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "restaurant_critic"-------
t = 0
restaurant_criticClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event

faceRGB = visual.ImageStim(win, 'restaurant_critic.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'Restaurant Critic')
txt.pos += (0, -.25)
faceRGB.size *= scale * 1.75  # scale the image relative to initial size


win.mouseVisible = False

txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False

# keep track of which components have finished
restaurant_criticComponents = []
for thisComponent in restaurant_criticComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "restaurant_critic"-------
while continueRoutine:
    # get current time
    t = restaurant_criticClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restaurant_criticComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "restaurant_critic"-------
for thisComponent in restaurant_criticComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "restaurant_critic" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "airport_customer_experience_manager_2"-------
t = 0
airport_customer_experience_manager_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event

faceRGB = visual.ImageStim(win, 'acem.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'Airport Customer Experience Manager')
txt.pos += (0, -.25)
faceRGB.size *= scale * 1.5  # scale the image relative to initial size


win.mouseVisible = False

txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False

key_resp_12 = event.BuilderKeyResponse()
# keep track of which components have finished
airport_customer_experience_manager_2Components = [key_resp_12]
for thisComponent in airport_customer_experience_manager_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "airport_customer_experience_manager_2"-------
while continueRoutine:
    # get current time
    t = airport_customer_experience_manager_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_12.keys = theseKeys[-1]  # just the last key pressed
            key_resp_12.rt = key_resp_12.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in airport_customer_experience_manager_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "airport_customer_experience_manager_2"-------
for thisComponent in airport_customer_experience_manager_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys=None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "airport_customer_experience_manager_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Grocery_Store_Customer_Experience_Manager"-------
t = 0
Grocery_Store_Customer_Experience_ManagerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
trialClock = core.Clock()
scale = 0.7

from psychopy import visual, core, event

txt = visual.TextStim(win, text='Grocery Store Costumer Experience Manager') 
txt.pos += (0, -.25)
faceRGB = visual.ImageStim(win, 'gscem.jpg')
faceRGB.pos += (0, .25)
faceRGB.size *= scale  * 1.75 # scale the image relative to initial size

win.mouseVisible = False
txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False


# keep track of which components have finished
Grocery_Store_Customer_Experience_ManagerComponents = []
for thisComponent in Grocery_Store_Customer_Experience_ManagerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Grocery_Store_Customer_Experience_Manager"-------
while continueRoutine:
    # get current time
    t = Grocery_Store_Customer_Experience_ManagerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Grocery_Store_Customer_Experience_ManagerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Grocery_Store_Customer_Experience_Manager"-------
for thisComponent in Grocery_Store_Customer_Experience_ManagerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Grocery_Store_Customer_Experience_Manager" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Couples_Therapist"-------
t = 0
Couples_TherapistClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event

faceRGB = visual.ImageStim(win, 'couples.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'Couples Therapist')
txt.pos += (0, -.25)
faceRGB.size *= scale * 1  # scale the image relative to initial size


win.mouseVisible = False

txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False

# keep track of which components have finished
Couples_TherapistComponents = []
for thisComponent in Couples_TherapistComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Couples_Therapist"-------
while continueRoutine:
    # get current time
    t = Couples_TherapistClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Couples_TherapistComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Couples_Therapist"-------
for thisComponent in Couples_TherapistComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Couples_Therapist" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Wedding_Planner"-------
t = 0
Wedding_PlannerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event

faceRGB = visual.ImageStim(win, 'weddingplanner.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'Wedding Planner')
txt.pos += (0, -.25)
faceRGB.size *= scale * .3  # scale the image relative to initial size


win.mouseVisible = False

txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False

# keep track of which components have finished
Wedding_PlannerComponents = []
for thisComponent in Wedding_PlannerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Wedding_Planner"-------
while continueRoutine:
    # get current time
    t = Wedding_PlannerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wedding_PlannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wedding_Planner"-------
for thisComponent in Wedding_PlannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Wedding_Planner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MatchMaker"-------
t = 0
MatchMakerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event

faceRGB = visual.ImageStim(win, 'matchmaker.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'Matchmaker')
txt.pos += (0, -.25)
faceRGB.size *= scale * 1.5  # scale the image relative to initial size


win.mouseVisible = False

txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False

# keep track of which components have finished
MatchMakerComponents = []
for thisComponent in MatchMakerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "MatchMaker"-------
while continueRoutine:
    # get current time
    t = MatchMakerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MatchMakerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MatchMaker"-------
for thisComponent in MatchMakerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "MatchMaker" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Business_Reporter"-------
t = 0
Business_ReporterClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event

faceRGB = visual.ImageStim(win, 'business_reporter.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'Business Reporter')
txt.pos += (0, -.25)
faceRGB.size *= scale * 1.5  # scale the image relative to initial size


win.mouseVisible = False

txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False

# keep track of which components have finished
Business_ReporterComponents = []
for thisComponent in Business_ReporterComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Business_Reporter"-------
while continueRoutine:
    # get current time
    t = Business_ReporterClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Business_ReporterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Business_Reporter"-------
for thisComponent in Business_ReporterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Business_Reporter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Dean_of_Academic_Studies"-------
t = 0
Dean_of_Academic_StudiesClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event

faceRGB = visual.ImageStim(win, 'dean.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'Dean of Academic Studies')
txt.pos += (0, -.25)
faceRGB.size *= scale * 1.75  # scale the image relative to initial size


win.mouseVisible = False

txt.draw()
faceRGB.draw()
win.flip()
event.waitKeys(keyList=['space'])
continueRoutine = False

# keep track of which components have finished
Dean_of_Academic_StudiesComponents = []
for thisComponent in Dean_of_Academic_StudiesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Dean_of_Academic_Studies"-------
while continueRoutine:
    # get current time
    t = Dean_of_Academic_StudiesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Dean_of_Academic_StudiesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Dean_of_Academic_Studies"-------
for thisComponent in Dean_of_Academic_StudiesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Dean_of_Academic_Studies" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro_questions"-------
    t = 0
    intro_questionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_6.setText(instruct_text
)
    key_resp_8 = event.BuilderKeyResponse()
    # keep track of which components have finished
    intro_questionsComponents = [text_6, key_resp_8]
    for thisComponent in intro_questionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "intro_questions"-------
    while continueRoutine:
        # get current time
        t = intro_questionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                key_resp_8.rt = key_resp_8.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro_questionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intro_questions"-------
    for thisComponent in intro_questionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys=None
    trials.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials.addData('key_resp_8.rt', key_resp_8.rt)
    # the Routine "intro_questions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('whichRole.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(thisRole),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "role_questions"-------
        t = 0
        role_questionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_8.setText(thisQuestion


)
        text_9.setText(roleName)
        image_5.setImage(rolePic)
        key_resp_10 = event.BuilderKeyResponse()
        # keep track of which components have finished
        role_questionsComponents = [text_8, text_9, image_5, key_resp_10]
        for thisComponent in role_questionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "role_questions"-------
        while continueRoutine:
            # get current time
            t = role_questionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_8* updates
            if t >= 0.0 and text_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_8.tStart = t
                text_8.frameNStart = frameN  # exact frame index
                text_8.setAutoDraw(True)
            
            # *text_9* updates
            if t >= 0.0 and text_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_9.tStart = t
                text_9.frameNStart = frameN  # exact frame index
                text_9.setAutoDraw(True)
            
            # *image_5* updates
            if t >= 0.0 and image_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_5.tStart = t
                image_5.frameNStart = frameN  # exact frame index
                image_5.setAutoDraw(True)
            
            # *key_resp_10* updates
            if t >= 0.0 and key_resp_10.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_10.tStart = t
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_10.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_10.rt = key_resp_10.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in role_questionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "role_questions"-------
        for thisComponent in role_questionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys=None
        trials_3.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            trials_3.addData('key_resp_10.rt', key_resp_10.rt)
        # the Routine "role_questions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "narrative_intro"-------
t = 0
narrative_introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
narrative_introComponents = [text_10, image_6, key_resp_11, text_11]
for thisComponent in narrative_introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "narrative_intro"-------
while continueRoutine:
    # get current time
    t = narrative_introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # *image_6* updates
    if t >= 0.0 and image_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_6.tStart = t
        image_6.frameNStart = frameN  # exact frame index
        image_6.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in narrative_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "narrative_intro"-------
for thisComponent in narrative_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys=None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "narrative_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('story1.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RB_story"-------
    t = 0
    RB_storyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_7.setText(storyText
)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    RB_storyComponents = [text_7, image, key_resp_9]
    for thisComponent in RB_storyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "RB_story"-------
    while continueRoutine:
        # get current time
        t = RB_storyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *key_resp_9* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys = theseKeys[-1]  # just the last key pressed
                key_resp_9.rt = key_resp_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RB_storyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RB_story"-------
    for thisComponent in RB_storyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys=None
    trials_2.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials_2.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "RB_story" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'









# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
