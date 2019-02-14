#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Thu Feb 14 13:55:42 2019
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
psychopyVersion = '3.0.3'
expName = 'part1_subjective_segmentation'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexreblando/Documents/GitHub/ebs/part1_subjective_segmentation_lastrun.py',
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

# Initialize components for Routine "intro"
introClock = core.Clock()
welcome_2 = visual.TextStim(win=win, name='welcome_2',
    text='default text',
    font='Arial',
    pos=(0, .7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
timer = core.Clock()
image_10 = visual.ImageStim(
    win=win, name='image_10',
    image='sin', mask=None,
    ori=0, pos=(0, -.3), size=[1.5, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "shows_jobs"
shows_jobsClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);


# Initialize components for Routine "intro_2"
intro_2Clock = core.Clock()
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
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);


# Initialize components for Routine "just_perspective_2"
just_perspective_2Clock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='default text',
    font='Arial',
    pos=(-.4, .25), height=0.1, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_9 = visual.ImageStim(
    win=win, name='image_9',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

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
    pos=(-.4, .25), height=0.1, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.75, 0.75),
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
    pos=(-.4, .25), height=0.1, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_6 = visual.ImageStim(
    win=win, name='image_6',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.75, 0.75),
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
    pos=(-.4, .25), height=0.1, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_7 = visual.ImageStim(
    win=win, name='image_7',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.75, 0.75),
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
    pos=(-.4, .25), height=0.1, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_8 = visual.ImageStim(
    win=win, name='image_8',
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "intro_practicetest"
intro_practicetestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='indicate the order in which the questions appeared:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "test"
testClock = core.Clock()

question1_2 = visual.TextStim(win=win, name='question1_2',
    text='default text',
    font='Arial',
    pos=(0, .60), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
question2_2 = visual.TextStim(win=win, name='question2_2',
    text='default text',
    font='Arial',
    pos=(0, .35), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
question3_2 = visual.TextStim(win=win, name='question3_2',
    text='default text',
    font='Arial',
    pos=(0, .12), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
question4_2 = visual.TextStim(win=win, name='question4_2',
    text='default text',
    font='Arial',
    pos=(0, -.12), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
question5_2 = visual.TextStim(win=win, name='question5_2',
    text='default text',
    font='Arial',
    pos=(0, -.35), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
question6_2 = visual.TextStim(win=win, name='question6_2',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=(0, -.85), size=(0.25, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "final_test_intro"
final_test_introClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Final Tests',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "final_test_i"
final_test_iClock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "test3"
test3Clock = core.Clock()

question1_3 = visual.TextStim(win=win, name='question1_3',
    text='default text',
    font='Arial',
    pos=(0, .60), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
question2_3 = visual.TextStim(win=win, name='question2_3',
    text='default text',
    font='Arial',
    pos=(0, .35), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
question3_3 = visual.TextStim(win=win, name='question3_3',
    text='default text',
    font='Arial',
    pos=(0, .12), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
question4_3 = visual.TextStim(win=win, name='question4_3',
    text='default text',
    font='Arial',
    pos=(0, -.12), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
question5_3 = visual.TextStim(win=win, name='question5_3',
    text='default text',
    font='Arial',
    pos=(0, -.35), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
question6_3 = visual.TextStim(win=win, name='question6_3',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0, -.85), size=(0.25, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "segmentation_instructions"
segmentation_instructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);


# Initialize components for Routine "end_of_intro"
end_of_introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='end of introduction',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions.xlsx'),
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
    
    # ------Prepare to start Routine "intro"-------
    t = 0
    introClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    welcome_2.setText(instruct_text)
    key_resp_8 = event.BuilderKeyResponse()
    
    image_10.setImage(this_pic)
    # keep track of which components have finished
    introComponents = [welcome_2, key_resp_8, image_10]
    for thisComponent in introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_2* updates
        if t >= 0.0 and welcome_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            welcome_2.tStart = t
            welcome_2.frameNStart = frameN  # exact frame index
            welcome_2.setAutoDraw(True)
        
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
        if event.getKeys(['q']):
            trials_2.finished = True
            continueRoutine=False
        
        # *image_10* updates
        if t >= 0.0 and image_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_10.tStart = t
            image_10.frameNStart = frameN  # exact frame index
            image_10.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys=None
    trials_2.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials_2.addData('key_resp_8.rt', key_resp_8.rt)
    
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('jobsPics.xlsx'),
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
    
    # ------Prepare to start Routine "shows_jobs"-------
    t = 0
    shows_jobsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(rolePic)
    key_resp_2 = event.BuilderKeyResponse()
    text_2.setText(job
)
    
    # keep track of which components have finished
    shows_jobsComponents = [image, key_resp_2, text_2]
    for thisComponent in shows_jobsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "shows_jobs"-------
    while continueRoutine:
        # get current time
        t = shows_jobsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
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
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        if event.getKeys(['q']):
            trials_4.finished = True
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in shows_jobsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "shows_jobs"-------
    for thisComponent in shows_jobsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    trials_4.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_4.addData('key_resp_2.rt', key_resp_2.rt)
    
    # the Routine "shows_jobs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
loop3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions2.xlsx'),
    seed=None, name='loop3')
thisExp.addLoop(loop3)  # add the loop to the experiment
thisLoop3 = loop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
if thisLoop3 != None:
    for paramName in thisLoop3:
        exec('{} = thisLoop3[paramName]'.format(paramName))

for thisLoop3 in loop3:
    currentLoop = loop3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
    if thisLoop3 != None:
        for paramName in thisLoop3:
            exec('{} = thisLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro_2"-------
    t = 0
    intro_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    welcome.setText(instruct_text)
    key_resp_6 = event.BuilderKeyResponse()
    text_12.setText(instruct_text2
)
    
    # keep track of which components have finished
    intro_2Components = [welcome, key_resp_6, text_12]
    for thisComponent in intro_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "intro_2"-------
    while continueRoutine:
        # get current time
        t = intro_2Clock.getTime()
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
        if event.getKeys(['q']):
            loop3.finished = True
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intro_2"-------
    for thisComponent in intro_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    loop3.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        loop3.addData('key_resp_6.rt', key_resp_6.rt)
    
    # the Routine "intro_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop3'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
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
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=5, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        
        # ------Prepare to start Routine "just_perspective_2"-------
        t = 0
        just_perspective_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_18.setText(roleName)
        image_9.setImage(rolePic)
        key_resp_14 = event.BuilderKeyResponse()
        # keep track of which components have finished
        just_perspective_2Components = [text_18, image_9, key_resp_14]
        for thisComponent in just_perspective_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "just_perspective_2"-------
        while continueRoutine:
            # get current time
            t = just_perspective_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_18* updates
            if t >= 0.0 and text_18.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_18.tStart = t
                text_18.frameNStart = frameN  # exact frame index
                text_18.setAutoDraw(True)
            
            # *image_9* updates
            if t >= 0.0 and image_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_9.tStart = t
                image_9.frameNStart = frameN  # exact frame index
                image_9.setAutoDraw(True)
            
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in just_perspective_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "just_perspective_2"-------
        for thisComponent in just_perspective_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_14.keys in ['', [], None]:  # No response was made
            key_resp_14.keys=None
        trials.addData('key_resp_14.keys',key_resp_14.keys)
        if key_resp_14.keys != None:  # we had a response
            trials.addData('key_resp_14.rt', key_resp_14.rt)
        # the Routine "just_perspective_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q1"-------
        t = 0
        q1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_8.setText(('A: ' + Q1)



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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
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
        trials.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            trials.addData('key_resp_10.rt', key_resp_10.rt)
        # the Routine "q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q2"-------
        t = 0
        q2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_10.setText(('B: ' + Q2)



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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
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
        trials.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            trials.addData('key_resp_11.rt', key_resp_11.rt)
        # the Routine "q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q3"-------
        t = 0
        q3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_13.setText(('C: ' + Q3)



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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in q3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
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
        trials.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            trials.addData('key_resp_12.rt', key_resp_12.rt)
        # the Routine "q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q4"-------
        t = 0
        q4Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_15.setText(('D: ' + Q4)



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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in q4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
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
        trials.addData('key_resp_13.keys',key_resp_13.keys)
        if key_resp_13.keys != None:  # we had a response
            trials.addData('key_resp_13.rt', key_resp_13.rt)
        # the Routine "q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "intro_practicetest"-------
        t = 0
        intro_practicetestClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4 = event.BuilderKeyResponse()
        # keep track of which components have finished
        intro_practicetestComponents = [text_5, key_resp_4]
        for thisComponent in intro_practicetestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "intro_practicetest"-------
        while continueRoutine:
            # get current time
            t = intro_practicetestClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if t >= 0.0 and text_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_5.tStart = t
                text_5.frameNStart = frameN  # exact frame index
                text_5.setAutoDraw(True)
            
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intro_practicetestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intro_practicetest"-------
        for thisComponent in intro_practicetestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys=None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
        # the Routine "intro_practicetest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "test"-------
        t = 0
        testClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        from psychopy import visual, core, event
        
        Q = np.array([Q1, Q2, Q3, Q4, D1, D2])
        correct = np.array([1,2,3,4,0,0], dtype=int)
        randperm = np.random.permutation(6) 
        Q = Q[randperm] 
        correct = correct[randperm]
        
        text1 = "1: " + Q[0]
        text2 = "2: " + Q[1]
        text3 = "3: " + Q[2]
        text4 = "4: " + Q[3]
        text5 = "5: " + Q[4]
        text6 = "6: " + Q[5]
        
        this_image = 'bar1.png'
        
        
        
        check = visual.ImageStim(win, 'checkmark.png')
        redx = visual.ImageStim(win, 'redx.png')
        
        thumbsup = visual.ImageStim(win, 'thumbsup.png')
        
        
        
        checkCount = 0
        test1 = 0
        test2 = 0
        test3 = 0
        test4 = 0
        test5 = 0
        test6 = 0
        
        
        question1_2.setText(text1)
        question2_2.setText(text2
)
        question3_2.setText(text3)
        question4_2.setText(text4)
        question5_2.setText(text5
)
        question6_2.setText(text6)
        
        # keep track of which components have finished
        testComponents = [question1_2, question2_2, question3_2, question4_2, question5_2, question6_2, image_3]
        for thisComponent in testComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "test"-------
        while continueRoutine:
            # get current time
            t = testClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *question1_2* updates
            if t >= 0.0 and question1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                question1_2.tStart = t
                question1_2.frameNStart = frameN  # exact frame index
                question1_2.setAutoDraw(True)
            
            # *question2_2* updates
            if t >= 0.0 and question2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                question2_2.tStart = t
                question2_2.frameNStart = frameN  # exact frame index
                question2_2.setAutoDraw(True)
            
            # *question3_2* updates
            if t >= 0.0 and question3_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                question3_2.tStart = t
                question3_2.frameNStart = frameN  # exact frame index
                question3_2.setAutoDraw(True)
            
            # *question4_2* updates
            if t >= 0.0 and question4_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                question4_2.tStart = t
                question4_2.frameNStart = frameN  # exact frame index
                question4_2.setAutoDraw(True)
            
            # *question5_2* updates
            if t >= 0.0 and question5_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                question5_2.tStart = t
                question5_2.frameNStart = frameN  # exact frame index
                question5_2.setAutoDraw(True)
            
            # *question6_2* updates
            if t >= 0.0 and question6_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                question6_2.tStart = t
                question6_2.frameNStart = frameN  # exact frame index
                question6_2.setAutoDraw(True)
            if this_image == 'bar5.jpeg':
                thumbsup.draw()
                win.flip()
                core.wait(1.5)
                trials.finished= True 
                continueRoutine = False
            #key press 1 
            if event.getKeys(['1']):
                if correct[0] == (checkCount + 1):
                    if test1 == 0:
                        test1 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #keypress 2
            if event.getKeys(['2']):
                if correct[1] == (checkCount + 1):
                    if test2 == 0:
                        test2 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #key press 3 
            if event.getKeys(['3']):
                if correct[2] == (checkCount + 1):
                    if test3 == 0:
                        test3 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #keypress 4
            if event.getKeys(['4']):
                if correct[3] == (checkCount + 1):
                    if test4 == 0:
                        test4 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #key press 5 
            if event.getKeys(['5']):
                if correct[4] == (checkCount + 1):
                    if test5 == 0:
                        test5 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #keypress 6
            if event.getKeys(['6']):
                if correct[5] == (checkCount + 1):
                    if test6 == 0:
                        test6 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
                    
            
            if event.getKeys(['q']):
                trials.finished = True
                trials_3.finished = True
                continueRoutine=False
            if checkCount == 4:
                this_image = 'bar5.jpeg'
            
            if checkCount == 1:
                this_image = 'bar2.png'
            if checkCount == 2: 
                this_image = 'bar3.jpeg'
            if checkCount == 3:
                this_image = 'bar4.png'
            
            # *image_3* updates
            if t >= 0.0 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:  # only update if drawing
                image_3.setImage(this_image, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
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
        
    # completed 5 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "final_test_intro"-------
t = 0
final_test_introClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
final_test_introComponents = [text_3]
for thisComponent in final_test_introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "final_test_intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = final_test_introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_test_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_test_intro"-------
for thisComponent in final_test_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('whichRole.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_7 = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_7')
    thisExp.addLoop(trials_7)  # add the loop to the experiment
    thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    for thisTrial_7 in trials_7:
        currentLoop = trials_7
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
        if thisTrial_7 != None:
            for paramName in thisTrial_7:
                exec('{} = thisTrial_7[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "final_test_i"-------
        t = 0
        final_test_iClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_2.setImage(rolePic)
        key_resp_3 = event.BuilderKeyResponse()
        text_4.setText(roleName
)
        # keep track of which components have finished
        final_test_iComponents = [image_2, key_resp_3, text_4]
        for thisComponent in final_test_iComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "final_test_i"-------
        while continueRoutine:
            # get current time
            t = final_test_iClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            
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
            
            # *text_4* updates
            if t >= 0.0 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in final_test_iComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "final_test_i"-------
        for thisComponent in final_test_iComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys=None
        trials_7.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_7.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "final_test_i" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "test3"-------
        t = 0
        test3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        from psychopy import visual, core, event
        
        Q = np.array([Q1, Q2, Q3, Q4, D1, D2])
        correct = np.array([1,2,3,4,0,0], dtype=int)
        randperm = np.random.permutation(6) 
        Q = Q[randperm] 
        correct = correct[randperm]
        
        text1 = "1: " + Q[0]
        text2 = "2: " + Q[1]
        text3 = "3: " + Q[2]
        text4 = "4: " + Q[3]
        text5 = "5: " + Q[4]
        text6 = "6: " + Q[5]
        
        this_image = 'bar1.png'
        
        
        
        check = visual.ImageStim(win, 'checkmark.png')
        redx = visual.ImageStim(win, 'redx.png')
        
        thumbsup = visual.ImageStim(win, 'thumbsup.png')
        
        
        
        checkCount = 0
        test1 = 0
        test2 = 0
        test3 = 0
        test4 = 0
        test5 = 0
        test6 = 0
        
        
        question1_3.setText(text1)
        question2_3.setText(text2
)
        question3_3.setText(text3)
        question4_3.setText(text4)
        question5_3.setText(text5
)
        question6_3.setText(text6)
        
        # keep track of which components have finished
        test3Components = [question1_3, question2_3, question3_3, question4_3, question5_3, question6_3, image_4]
        for thisComponent in test3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "test3"-------
        while continueRoutine:
            # get current time
            t = test3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *question1_3* updates
            if t >= 0.0 and question1_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                question1_3.tStart = t
                question1_3.frameNStart = frameN  # exact frame index
                question1_3.setAutoDraw(True)
            
            # *question2_3* updates
            if t >= 0.0 and question2_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                question2_3.tStart = t
                question2_3.frameNStart = frameN  # exact frame index
                question2_3.setAutoDraw(True)
            
            # *question3_3* updates
            if t >= 0.0 and question3_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                question3_3.tStart = t
                question3_3.frameNStart = frameN  # exact frame index
                question3_3.setAutoDraw(True)
            
            # *question4_3* updates
            if t >= 0.0 and question4_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                question4_3.tStart = t
                question4_3.frameNStart = frameN  # exact frame index
                question4_3.setAutoDraw(True)
            
            # *question5_3* updates
            if t >= 0.0 and question5_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                question5_3.tStart = t
                question5_3.frameNStart = frameN  # exact frame index
                question5_3.setAutoDraw(True)
            
            # *question6_3* updates
            if t >= 0.0 and question6_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                question6_3.tStart = t
                question6_3.frameNStart = frameN  # exact frame index
                question6_3.setAutoDraw(True)
            if this_image == 'bar5.jpeg':
                thumbsup.draw()
                win.flip()
                core.wait(1.5)
                trials.finished= True 
                continueRoutine = False
            #key press 1 
            if event.getKeys(['1']):
                if correct[0] == (checkCount + 1):
                    if test1 == 0:
                        test1 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #keypress 2
            if event.getKeys(['2']):
                if correct[1] == (checkCount + 1):
                    if test2 == 0:
                        test2 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                elif correct[1] == 0:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #key press 3 
            if event.getKeys(['3']):
                if correct[2] == (checkCount + 1):
                    if test3 == 0:
                        test3 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #keypress 4
            if event.getKeys(['4']):
                if correct[3] == (checkCount + 1):
                    if test4 == 0:
                        test4 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #key press 5 
            if event.getKeys(['5']):
                if correct[4] == (checkCount + 1):
                    if test5 == 0:
                        test5 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
            
            #keypress 6
            if event.getKeys(['6']):
                if correct[5] == (checkCount + 1):
                    if test6 == 0:
                        test6 = 1
                        checkCount += 1
                        check.draw()
                        win.flip()
                        core.wait(.15)
                else:
                    redx.draw()
                    win.flip()
                    core.wait(1)
                    continueRoutine = False
                    
            
            if event.getKeys(['q']):
                trials_7.finished = True
                trials_5.finished = True
                continueRoutine=False
            if checkCount == 4:
                this_image = 'bar5.jpeg'
                trials_7.finished = True
            
            if checkCount == 1:
                this_image = 'bar2.png'
            if checkCount == 2: 
                this_image = 'bar3.jpeg'
            if checkCount == 3:
                this_image = 'bar4.png'
            
            # *image_4* updates
            if t >= 0.0 and image_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_4.tStart = t
                image_4.frameNStart = frameN  # exact frame index
                image_4.setAutoDraw(True)
            if image_4.status == STARTED:  # only update if drawing
                image_4.setImage(this_image, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "test3"-------
        for thisComponent in test3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # the Routine "test3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5 repeats of 'trials_7'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions_segment.xlsx'),
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8:
        exec('{} = thisTrial_8[paramName]'.format(paramName))

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "segmentation_instructions"-------
    t = 0
    segmentation_instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()
    text_6.setText(instructText)
    
    # keep track of which components have finished
    segmentation_instructionsComponents = [key_resp_5, text_6]
    for thisComponent in segmentation_instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "segmentation_instructions"-------
    while continueRoutine:
        # get current time
        t = segmentation_instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        if event.getKeys(['q']):
            trials_8.finished = True
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in segmentation_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "segmentation_instructions"-------
    for thisComponent in segmentation_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    trials_8.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials_8.addData('key_resp_5.rt', key_resp_5.rt)
    
    # the Routine "segmentation_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_8'


# set up handler to look after randomisation of conditions etc
trials_9 = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_9')
thisExp.addLoop(trials_9)  # add the loop to the experiment
thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
if thisTrial_9 != None:
    for paramName in thisTrial_9:
        exec('{} = thisTrial_9[paramName]'.format(paramName))

for thisTrial_9 in trials_9:
    currentLoop = trials_9
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "end_of_intro"-------
    t = 0
    end_of_introClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7 = event.BuilderKeyResponse()
    instructions_time = timer.getTime()
    thisExp.addData('instructions time', instructions_time)
    # keep track of which components have finished
    end_of_introComponents = [text, key_resp_7]
    for thisComponent in end_of_introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "end_of_intro"-------
    while continueRoutine:
        # get current time
        t = end_of_introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
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
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_7.keys = theseKeys[-1]  # just the last key pressed
                key_resp_7.rt = key_resp_7.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        if event.getKeys(['escape']):
            core.quit()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_of_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_of_intro"-------
    for thisComponent in end_of_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys=None
    trials_9.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        trials_9.addData('key_resp_7.rt', key_resp_7.rt)
    
    # the Routine "end_of_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials_9'










# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
