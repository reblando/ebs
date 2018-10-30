#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Mon Oct 29 14:14:25 2018
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
expName = 'try1'  # from the Builder filename that created this script
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
    originPath='/Users/alexreblando/Documents/GitHub/ebs/try1_lastrun.py',
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
    text='Welcome to the Role Assumption Task!\n\n(press the space bar to continue)',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rb_opening"
rb_openingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='you will assume 8 different roles today while reading various stories. \n\nThese roles will be: \n\n\n\n\n\n(press the space bar to continue)\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "restaurant_critic"
restaurant_criticClock = core.Clock()


# Initialize components for Routine "airport_customer_experience_manager_2"
airport_customer_experience_manager_2Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win, name='image_6',
    image='/Users/alexreblando/Documents/GitHub/ebs/acem.jpg', mask=None,
    ori=0, pos=(0, .1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='Airport Customer Experience Manager\n',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Grocery_Store_Customer_Experience_Manager"
Grocery_Store_Customer_Experience_ManagerClock = core.Clock()


# Initialize components for Routine "Couples_Therapist"
Couples_TherapistClock = core.Clock()
image_9 = visual.ImageStim(
    win=win, name='image_9',
    image='/Users/alexreblando/Documents/GitHub/ebs/couples.jpg', mask=None,
    ori=0, pos=(0, .1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='Couples Therapist\n\n',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Wedding_Planner"
Wedding_PlannerClock = core.Clock()
image_10 = visual.ImageStim(
    win=win, name='image_10',
    image='/Users/alexreblando/Documents/GitHub/ebs/weddingplanner.jpg', mask=None,
    ori=0, pos=(0, .1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_12 = visual.TextStim(win=win, name='text_12',
    text='Wedding Planner\n',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "MatchMaker"
MatchMakerClock = core.Clock()
image_12 = visual.ImageStim(
    win=win, name='image_12',
    image='/Users/alexreblando/Documents/GitHub/ebs/matchmaker.jpg', mask=None,
    ori=0, pos=(0, .1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_14 = visual.TextStim(win=win, name='text_14',
    text='Matchmaker\n',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Business_Reporter"
Business_ReporterClock = core.Clock()
image_11 = visual.ImageStim(
    win=win, name='image_11',
    image='/Users/alexreblando/Documents/GitHub/ebs/business_reporter.jpg', mask=None,
    ori=0, pos=(0, .1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_13 = visual.TextStim(win=win, name='text_13',
    text='Business Reporter',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Dean_of_Academic_Studies"
Dean_of_Academic_StudiesClock = core.Clock()
image_8 = visual.ImageStim(
    win=win, name='image_8',
    image='/Users/alexreblando/Documents/GitHub/ebs/dean.jpg', mask=None,
    ori=0, pos=(0, .1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_10 = visual.TextStim(win=win, name='text_10',
    text='Dean of Academic Studies\n',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "routine_1"
routine_1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_2"
routine_2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='When Sadie entered, she found him deep in thought on a bench by the door.',
    font='Arial',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='/Users/alexreblando/Documents/GitHub/ebs/AB.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "routine_3"
routine_3Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='/Users/alexreblando/Documents/GitHub/ebs/AB.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='The restaurant had a kitschy charm, and was reminiscent of a diner from the 70’s. ',
    font='Arial',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "routine_4"
routine_4Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='When Thomas noticed Sadie, he jumped up and gave her a side hug.',
    font='Arial',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='/Users/alexreblando/Documents/GitHub/ebs/AB_3.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
introComponents = [welcome, key_resp_6]
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

# ------Prepare to start Routine "rb_opening"-------
t = 0
rb_openingClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
rb_openingComponents = [text, key_resp_7]
for thisComponent in rb_openingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "rb_opening"-------
while continueRoutine:
    # get current time
    t = rb_openingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rb_openingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rb_opening"-------
for thisComponent in rb_openingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "rb_opening" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "restaurant_critic"-------
t = 0
restaurant_criticClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scale = 0.7

from psychopy import visual, core, event
win = visual.Window(fullscr=True)
faceRGB = visual.ImageStim(win, 'restaurant_critic.jpg')
faceRGB.pos += (0, .25)
txt = visual.TextStim(win, text = 'restaurant critic')
txt.pos += (0, -.75)
faceRGB.size *= scale * 1.5  # scale the image relative to initial size


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
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
airport_customer_experience_manager_2Components = [key_resp_10, image_6, text_8]
for thisComponent in airport_customer_experience_manager_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "airport_customer_experience_manager_2"-------
while continueRoutine:
    # get current time
    t = airport_customer_experience_manager_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    
    # *image_6* updates
    if t >= 0.0 and image_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_6.tStart = t
        image_6.frameNStart = frameN  # exact frame index
        image_6.setAutoDraw(True)
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    
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
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
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
win = visual.Window(fullscr=True)
txt = visual.TextStim(win, text='Grocery Store Costumer Experience Manager') 
txt.pos += (0, -.5)
faceRGB = visual.ImageStim(win, 'gscem.jpg')
faceRGB.pos += (0, .25)
faceRGB.size *= scale  # scale the image relative to initial size

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
key_resp_13 = event.BuilderKeyResponse()
# keep track of which components have finished
Couples_TherapistComponents = [key_resp_13, image_9, text_11]
for thisComponent in Couples_TherapistComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Couples_Therapist"-------
while continueRoutine:
    # get current time
    t = Couples_TherapistClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_13.keys = theseKeys[-1]  # just the last key pressed
            key_resp_13.rt = key_resp_13.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_9* updates
    if t >= 0.0 and image_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_9.tStart = t
        image_9.frameNStart = frameN  # exact frame index
        image_9.setAutoDraw(True)
    
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
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys=None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
# the Routine "Couples_Therapist" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Wedding_Planner"-------
t = 0
Wedding_PlannerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_14 = event.BuilderKeyResponse()
# keep track of which components have finished
Wedding_PlannerComponents = [key_resp_14, image_10, text_12]
for thisComponent in Wedding_PlannerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Wedding_Planner"-------
while continueRoutine:
    # get current time
    t = Wedding_PlannerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_14* updates
    if t >= 0.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_14.keys = theseKeys[-1]  # just the last key pressed
            key_resp_14.rt = key_resp_14.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_10* updates
    if t >= 0.0 and image_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_10.tStart = t
        image_10.frameNStart = frameN  # exact frame index
        image_10.setAutoDraw(True)
    
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
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys=None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.nextEntry()
# the Routine "Wedding_Planner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MatchMaker"-------
t = 0
MatchMakerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_16 = event.BuilderKeyResponse()
# keep track of which components have finished
MatchMakerComponents = [key_resp_16, image_12, text_14]
for thisComponent in MatchMakerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "MatchMaker"-------
while continueRoutine:
    # get current time
    t = MatchMakerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_16* updates
    if t >= 0.0 and key_resp_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_16.tStart = t
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_16.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_16.keys = theseKeys[-1]  # just the last key pressed
            key_resp_16.rt = key_resp_16.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_12* updates
    if t >= 0.0 and image_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_12.tStart = t
        image_12.frameNStart = frameN  # exact frame index
        image_12.setAutoDraw(True)
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
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
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys=None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.nextEntry()
# the Routine "MatchMaker" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Business_Reporter"-------
t = 0
Business_ReporterClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()
# keep track of which components have finished
Business_ReporterComponents = [key_resp_15, image_11, text_13]
for thisComponent in Business_ReporterComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Business_Reporter"-------
while continueRoutine:
    # get current time
    t = Business_ReporterClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_15* updates
    if t >= 0.0 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_15.keys = theseKeys[-1]  # just the last key pressed
            key_resp_15.rt = key_resp_15.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_11* updates
    if t >= 0.0 and image_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_11.tStart = t
        image_11.frameNStart = frameN  # exact frame index
        image_11.setAutoDraw(True)
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    
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
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys=None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.nextEntry()
# the Routine "Business_Reporter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Dean_of_Academic_Studies"-------
t = 0
Dean_of_Academic_StudiesClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()
# keep track of which components have finished
Dean_of_Academic_StudiesComponents = [key_resp_12, image_8, text_10]
for thisComponent in Dean_of_Academic_StudiesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Dean_of_Academic_Studies"-------
while continueRoutine:
    # get current time
    t = Dean_of_Academic_StudiesClock.getTime()
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_12.keys = theseKeys[-1]  # just the last key pressed
            key_resp_12.rt = key_resp_12.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_8* updates
    if t >= 0.0 and image_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_8.tStart = t
        image_8.frameNStart = frameN  # exact frame index
        image_8.setAutoDraw(True)
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
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
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys=None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "Dean_of_Academic_Studies" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_1"-------
t = 0
routine_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
text_2.setText('Thomas got to the restaurant early, dreading the conversation he was about to have. \n')
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
routine_1Components = [text_2, key_resp_2]
for thisComponent in routine_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "routine_1"-------
while continueRoutine:
    # get current time
    t = routine_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_1"-------
for thisComponent in routine_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "routine_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_2"-------
t = 0
routine_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()

# keep track of which components have finished
routine_2Components = [text_3, key_resp_3, image_2]
for thisComponent in routine_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "routine_2"-------
while continueRoutine:
    # get current time
    t = routine_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_2* updates
    if t >= 0.0 and image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_2.tStart = t
        image_2.frameNStart = frameN  # exact frame index
        image_2.setAutoDraw(True)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_2"-------
for thisComponent in routine_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()

# the Routine "routine_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_3"-------
t = 0
routine_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
routine_3Components = [image_3, key_resp_4, text_4]
for thisComponent in routine_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "routine_3"-------
while continueRoutine:
    # get current time
    t = routine_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if t >= 0.0 and image_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_3.tStart = t
        image_3.frameNStart = frameN  # exact frame index
        image_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_3"-------
for thisComponent in routine_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "routine_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_4"-------
t = 0
routine_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
routine_4Components = [text_5, key_resp_5, image_4]
for thisComponent in routine_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "routine_4"-------
while continueRoutine:
    # get current time
    t = routine_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_4* updates
    if t >= 0.0 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_4"-------
for thisComponent in routine_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "routine_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
