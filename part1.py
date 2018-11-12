#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Thu Nov  8 17:52:37 2018
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
expName = 'part1'  # from the Builder filename that created this script
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
    originPath='/Users/alexreblando/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/ebs/part1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "q1"
q1Clock = core.Clock()
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

# Initialize components for Routine "q2"
q2Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    pos=(0, -.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='default text',
    font='Arial',
    pos=(-.25, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_6 = visual.ImageStim(
    win=win, name='image_6',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "q3"
q3Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='default text',
    font='Arial',
    pos=(0, -.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='default text',
    font='Arial',
    pos=(-.25, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_7 = visual.ImageStim(
    win=win, name='image_7',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "q4"
q4Clock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='default text',
    font='Arial',
    pos=(0, -.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='default text',
    font='Arial',
    pos=(-.25, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_8 = visual.ImageStim(
    win=win, name='image_8',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "test"
testClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='couples.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('whichRole.xlsx'),
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
    
    # ------Prepare to start Routine "q1"-------
    t = 0
    q1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_8.setText(Q1



)
    text_9.setText(roleName)
    image_5.setImage(rolePic)
    key_resp_10 = event.BuilderKeyResponse()
    # keep track of which components have finished
    q1Components = [text_8, text_9, image_5, key_resp_10]
    for thisComponent in q1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "q1"-------
    while continueRoutine:
        # get current time
        t = q1Clock.getTime()
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
        for thisComponent in q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "q1"-------
    for thisComponent in q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys=None
    trials_3.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        trials_3.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "q2"-------
    t = 0
    q2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_10.setText(Q2



)
    text_11.setText(roleName)
    image_6.setImage(rolePic)
    key_resp_11 = event.BuilderKeyResponse()
    # keep track of which components have finished
    q2Components = [text_10, text_11, image_6, key_resp_11]
    for thisComponent in q2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "q2"-------
    while continueRoutine:
        # get current time
        t = q2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        
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
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "q2"-------
    for thisComponent in q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys=None
    trials_3.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        trials_3.addData('key_resp_11.rt', key_resp_11.rt)
    # the Routine "q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "q3"-------
    t = 0
    q3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_13.setText(Q3



)
    text_14.setText(roleName)
    image_7.setImage(rolePic)
    key_resp_12 = event.BuilderKeyResponse()
    # keep track of which components have finished
    q3Components = [text_13, text_14, image_7, key_resp_12]
    for thisComponent in q3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "q3"-------
    while continueRoutine:
        # get current time
        t = q3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        
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
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "q3"-------
    for thisComponent in q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys=None
    trials_3.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        trials_3.addData('key_resp_12.rt', key_resp_12.rt)
    # the Routine "q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "q4"-------
    t = 0
    q4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_15.setText(Q4



)
    text_16.setText(roleName)
    image_8.setImage(rolePic)
    key_resp_13 = event.BuilderKeyResponse()
    # keep track of which components have finished
    q4Components = [text_15, text_16, image_8, key_resp_13]
    for thisComponent in q4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "q4"-------
    while continueRoutine:
        # get current time
        t = q4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        
        # *image_8* updates
        if t >= 0.0 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        
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
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "q4"-------
    for thisComponent in q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys=None
    trials_3.addData('key_resp_13.keys',key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        trials_3.addData('key_resp_13.rt', key_resp_13.rt)
    # the Routine "q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test"-------
    t = 0
    testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    from psychopy import visual, core, event
    
    Q = np.array([Q1, Q2, Q3, Q4, D1, D2])
    correct = np.array([1,1,1,1,0,0], dtype=bool)
    randperm = np.random.permutation(6)
    Q = Q[randperm]
    correct = correct[randperm]
    
    
    
    check = visual.ImageStim(win, 'checkmark.png')
    
    checkCount = 0
    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    test5 = 0
    test6 = 0
    test7 = 0
    
    text.setText(Q[0])
    # keep track of which components have finished
    testComponents = [text]
    for thisComponent in testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test"-------
    while continueRoutine:
        # get current time
        t = testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if event.getKeys(['1']):
            check.draw()  
            core.wait(1)
        if event.getKeys(['5']):
           continueRoutine=False
        if checkCount == 4:
            continueRoutine = False
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials_3'


# ------Prepare to start Routine "feedback"-------
t = 0
feedbackClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
feedbackComponents = [image]
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "feedback"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feedbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image.status == STARTED and t >= frameRemains:
        image.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
