#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.1),
    on Sun Jan 26 23:54:37 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.1'
expName = 'training_fmri'  # from the Builder filename that created this script
expInfo = {'participant': 'alex', 'sA': '0', 'sB': '1', 'lA': '0', 'lB': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='/Users/alexreblando/Documents/GitHub/ebs/fMRI experiment/psychopy code/training_fmri.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Dict = {}

#Dict[0] entry for sA
if int(expInfo['sA']) == 0:
    Dict[0] = 'intro_roles/s0.xlsx'
elif int(expInfo['sA']) == 1:
    Dict[0] = 'intro_roles/s1.xlsx'
if int(expInfo['sA']) == 2:
    Dict[0] = 'intro_roles/s2.xlsx'
elif int(expInfo['sA']) == 3:
    Dict[0] = 'intro_roles/s3.xlsx'

#Dict[1] entry for sB
if int(expInfo['sB']) == 0:
    Dict[1] = 'intro_roles/s0.xlsx'
if int(expInfo['sB']) == 1:
    Dict[1] = 'intro_roles/s1.xlsx'
if int(expInfo['sB']) == 2:
    Dict[1] = 'intro_roles/s2.xlsx'
if int(expInfo['sB']) == 3:
    Dict[1] = 'intro_roles/s3.xlsx'

#Dict[2] entry for lA
if int(expInfo['lA']) == 0:
    Dict[2] = 'intro_roles/l0.xlsx'
elif int(expInfo['lA']) == 1:
    Dict[2] = 'intro_roles/l1.xlsx'
if int(expInfo['lA']) == 2:
    Dict[2] = 'intro_roles/l2.xlsx'
elif int(expInfo['lA']) == 3:
    Dict[2] = 'intro_roles/l3.xlsx'

#Dict[3] entry for lB
if int(expInfo['lB']) == 0:
    Dict[3] = 'intro_roles/l0.xlsx'
if int(expInfo['lB']) == 1:
    Dict[3] = 'intro_roles/l1.xlsx'
if int(expInfo['lB']) == 2:
    Dict[3] = 'intro_roles/l2.xlsx'
if int(expInfo['lB']) == 3:
    Dict[3] = 'intro_roles/l3.xlsx'

# Initialize components for Routine "intro"
introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "intro_pic"
intro_picClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='jobphotos/restaurant_critic.jpg', mask=None,
    ori=0, pos=(0, -.3), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "intro"
introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "intro1"
intro1Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='For example, 2 of the questions associated with the restaurant critic may be "What are the menus like?" and "What does each client order?"',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='jobphotos/restaurant_critic.jpg', mask=None,
    ori=0, pos=(0, -.3), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "intro2"
intro2Clock = core.Clock()
key_resp_6 = keyboard.Keyboard()
text_12 = visual.TextStim(win=win, name='text_12',
    text='For each story, an image with the title of the story, character names, and character images, like the one below, will be presented on the screen while you hear it being played.',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='icon/intro_faces.jpg', mask=None,
    ori=0, pos=(0, -.5), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "intro"
introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "show_jobs"
show_jobsClock = core.Clock()
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_17 = visual.TextStim(win=win, name='text_17',
    text='default text',
    font='Arial',
    pos=(0, -.7), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "perspective_only"
perspective_onlyClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='default text',
    font='Arial',
    pos=(-.5, .25), height=0.15, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "q1"
q1Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='default text',
    font='Arial',
    pos=(-.5, .25), height=0.15, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "q2"
q2Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='default text',
    font='Arial',
    pos=(-.5, .25), height=0.15, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "q3"
q3Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='default text',
    font='Arial',
    pos=(-.5, .25), height=0.15, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "q4"
q4Clock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='default text',
    font='Arial',
    pos=(-.5, .25), height=0.15, wrapWidth=.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='sin', mask=None,
    ori=0, pos=(.25, .25), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "intro_practicetest"
intro_practicetestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Please indicate the order in which the questions appear in the following quiz:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "test"
testClock = core.Clock()
question1_2 = visual.TextStim(win=win, name='question1_2',
    text='default text',
    font='Arial',
    pos=(0, .70), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
question2_2 = visual.TextStim(win=win, name='question2_2',
    text='default text',
    font='Arial',
    pos=(0, .45), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
question3_2 = visual.TextStim(win=win, name='question3_2',
    text='default text',
    font='Arial',
    pos=(0, .16), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
question4_2 = visual.TextStim(win=win, name='question4_2',
    text='default text',
    font='Arial',
    pos=(0, -.12), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
question5_2 = visual.TextStim(win=win, name='question5_2',
    text='default text',
    font='Arial',
    pos=(0, -.35), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
question6_2 = visual.TextStim(win=win, name='question6_2',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
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
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, -.7), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "test3"
test3Clock = core.Clock()
question1_3 = visual.TextStim(win=win, name='question1_3',
    text='default text',
    font='Arial',
    pos=(0, .70), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
question2_3 = visual.TextStim(win=win, name='question2_3',
    text='default text',
    font='Arial',
    pos=(0, .45), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
question3_3 = visual.TextStim(win=win, name='question3_3',
    text='default text',
    font='Arial',
    pos=(0, .16), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
question4_3 = visual.TextStim(win=win, name='question4_3',
    text='default text',
    font='Arial',
    pos=(0, -.12), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
question5_3 = visual.TextStim(win=win, name='question5_3',
    text='default text',
    font='Arial',
    pos=(0, -.35), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
question6_3 = visual.TextStim(win=win, name='question6_3',
    text='default text',
    font='Arial',
    pos=(0, -.6), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, -.85), size=(0.25, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='end of training',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = []
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instruct1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fmri_instruct1.xlsx'),
    seed=None, name='instruct1')
thisExp.addLoop(instruct1)  # add the loop to the experiment
thisInstruct1 = instruct1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruct1.rgb)
if thisInstruct1 != None:
    for paramName in thisInstruct1:
        exec('{} = thisInstruct1[paramName]'.format(paramName))

for thisInstruct1 in instruct1:
    currentLoop = instruct1
    # abbreviate parameter names if possible (e.g. rgb = thisInstruct1.rgb)
    if thisInstruct1 != None:
        for paramName in thisInstruct1:
            exec('{} = thisInstruct1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro"-------
    # update component parameters for each repeat
    text.setText(instruct_text)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    introComponents = [text, key_resp]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    instruct1.addData('text.started', text.tStartRefresh)
    instruct1.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    instruct1.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        instruct1.addData('key_resp.rt', key_resp.rt)
    instruct1.addData('key_resp.started', key_resp.tStartRefresh)
    instruct1.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instruct1'


# set up handler to look after randomisation of conditions etc
instruct2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fmri_instruct2.xlsx'),
    seed=None, name='instruct2')
thisExp.addLoop(instruct2)  # add the loop to the experiment
thisInstruct2 = instruct2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruct2.rgb)
if thisInstruct2 != None:
    for paramName in thisInstruct2:
        exec('{} = thisInstruct2[paramName]'.format(paramName))

for thisInstruct2 in instruct2:
    currentLoop = instruct2
    # abbreviate parameter names if possible (e.g. rgb = thisInstruct2.rgb)
    if thisInstruct2 != None:
        for paramName in thisInstruct2:
            exec('{} = thisInstruct2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro_pic"-------
    # update component parameters for each repeat
    text_6.setText(instruct_text)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    intro_picComponents = [text_6, key_resp_2, image]
    for thisComponent in intro_picComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intro_picClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intro_pic"-------
    while continueRoutine:
        # get current time
        t = intro_picClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intro_picClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro_picComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intro_pic"-------
    for thisComponent in intro_picComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instruct2.addData('text_6.started', text_6.tStartRefresh)
    instruct2.addData('text_6.stopped', text_6.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    instruct2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        instruct2.addData('key_resp_2.rt', key_resp_2.rt)
    instruct2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    instruct2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    instruct2.addData('image.started', image.tStartRefresh)
    instruct2.addData('image.stopped', image.tStopRefresh)
    # the Routine "intro_pic" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instruct2'


# set up handler to look after randomisation of conditions etc
instruct3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fmri_instruct3.xlsx'),
    seed=None, name='instruct3')
thisExp.addLoop(instruct3)  # add the loop to the experiment
thisInstruct3 = instruct3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruct3.rgb)
if thisInstruct3 != None:
    for paramName in thisInstruct3:
        exec('{} = thisInstruct3[paramName]'.format(paramName))

for thisInstruct3 in instruct3:
    currentLoop = instruct3
    # abbreviate parameter names if possible (e.g. rgb = thisInstruct3.rgb)
    if thisInstruct3 != None:
        for paramName in thisInstruct3:
            exec('{} = thisInstruct3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro"-------
    # update component parameters for each repeat
    text.setText(instruct_text)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    introComponents = [text, key_resp]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    instruct3.addData('text.started', text.tStartRefresh)
    instruct3.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    instruct3.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        instruct3.addData('key_resp.rt', key_resp.rt)
    instruct3.addData('key_resp.started', key_resp.tStartRefresh)
    instruct3.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instruct3'


# ------Prepare to start Routine "intro1"-------
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
# keep track of which components have finished
intro1Components = [text_7, image_10, key_resp_5]
for thisComponent in intro1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "intro1"-------
while continueRoutine:
    # get current time
    t = intro1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_5.keys = theseKeys.name  # just the last key pressed
            key_resp_5.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro1"-------
for thisComponent in intro1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('image_10.started', image_10.tStartRefresh)
thisExp.addData('image_10.stopped', image_10.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instruct4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fmri_instruct4.xlsx'),
    seed=None, name='instruct4')
thisExp.addLoop(instruct4)  # add the loop to the experiment
thisInstruct4 = instruct4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruct4.rgb)
if thisInstruct4 != None:
    for paramName in thisInstruct4:
        exec('{} = thisInstruct4[paramName]'.format(paramName))

for thisInstruct4 in instruct4:
    currentLoop = instruct4
    # abbreviate parameter names if possible (e.g. rgb = thisInstruct4.rgb)
    if thisInstruct4 != None:
        for paramName in thisInstruct4:
            exec('{} = thisInstruct4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro"-------
    # update component parameters for each repeat
    text.setText(instruct_text)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    introComponents = [text, key_resp]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    instruct4.addData('text.started', text.tStartRefresh)
    instruct4.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    instruct4.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        instruct4.addData('key_resp.rt', key_resp.rt)
    instruct4.addData('key_resp.started', key_resp.tStartRefresh)
    instruct4.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instruct4'


# ------Prepare to start Routine "intro2"-------
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
intro2Components = [key_resp_6, text_12, image_11]
for thisComponent in intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "intro2"-------
while continueRoutine:
    # get current time
    t = intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro2"-------
for thisComponent in intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('image_11.started', image_11.tStartRefresh)
thisExp.addData('image_11.stopped', image_11.tStopRefresh)
# the Routine "intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instruct5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fmri_instruct5.xlsx'),
    seed=None, name='instruct5')
thisExp.addLoop(instruct5)  # add the loop to the experiment
thisInstruct5 = instruct5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruct5.rgb)
if thisInstruct5 != None:
    for paramName in thisInstruct5:
        exec('{} = thisInstruct5[paramName]'.format(paramName))

for thisInstruct5 in instruct5:
    currentLoop = instruct5
    # abbreviate parameter names if possible (e.g. rgb = thisInstruct5.rgb)
    if thisInstruct5 != None:
        for paramName in thisInstruct5:
            exec('{} = thisInstruct5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro"-------
    # update component parameters for each repeat
    text.setText(instruct_text)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    introComponents = [text, key_resp]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    instruct5.addData('text.started', text.tStartRefresh)
    instruct5.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    instruct5.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        instruct5.addData('key_resp.rt', key_resp.rt)
    instruct5.addData('key_resp.started', key_resp.tStartRefresh)
    instruct5.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instruct5'


# set up handler to look after randomisation of conditions etc
count_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count_0123.xlsx'),
    seed=None, name='count_4')
thisExp.addLoop(count_4)  # add the loop to the experiment
thisCount_4 = count_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCount_4.rgb)
if thisCount_4 != None:
    for paramName in thisCount_4:
        exec('{} = thisCount_4[paramName]'.format(paramName))

for thisCount_4 in count_4:
    currentLoop = count_4
    # abbreviate parameter names if possible (e.g. rgb = thisCount_4.rgb)
    if thisCount_4 != None:
        for paramName in thisCount_4:
            exec('{} = thisCount_4[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Dict[count]),
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
        
        # ------Prepare to start Routine "show_jobs"-------
        # update component parameters for each repeat
        image_12.setImage(rolePic)
        text_17.setText(roleName)
        key_resp_7.keys = []
        key_resp_7.rt = []
        # keep track of which components have finished
        show_jobsComponents = [image_12, text_17, key_resp_7]
        for thisComponent in show_jobsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        show_jobsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "show_jobs"-------
        while continueRoutine:
            # get current time
            t = show_jobsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=show_jobsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_12* updates
            if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                image_12.setAutoDraw(True)
            
            # *text_17* updates
            if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_17.frameNStart = frameN  # exact frame index
                text_17.tStart = t  # local t and not account for scr refresh
                text_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                text_17.setAutoDraw(True)
            
            # *key_resp_7* updates
            waitOnFlip = False
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_7.keys = theseKeys.name  # just the last key pressed
                    key_resp_7.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in show_jobsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "show_jobs"-------
        for thisComponent in show_jobsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('image_12.started', image_12.tStartRefresh)
        trials_5.addData('image_12.stopped', image_12.tStopRefresh)
        trials_5.addData('text_17.started', text_17.tStartRefresh)
        trials_5.addData('text_17.stopped', text_17.tStopRefresh)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_5.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_5.addData('key_resp_7.rt', key_resp_7.rt)
        trials_5.addData('key_resp_7.started', key_resp_7.tStartRefresh)
        trials_5.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
        # the Routine "show_jobs" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_5'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'count_4'


# set up handler to look after randomisation of conditions etc
instruct6 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fmri_instruct6.xlsx'),
    seed=None, name='instruct6')
thisExp.addLoop(instruct6)  # add the loop to the experiment
thisInstruct6 = instruct6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruct6.rgb)
if thisInstruct6 != None:
    for paramName in thisInstruct6:
        exec('{} = thisInstruct6[paramName]'.format(paramName))

for thisInstruct6 in instruct6:
    currentLoop = instruct6
    # abbreviate parameter names if possible (e.g. rgb = thisInstruct6.rgb)
    if thisInstruct6 != None:
        for paramName in thisInstruct6:
            exec('{} = thisInstruct6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intro"-------
    # update component parameters for each repeat
    text.setText(instruct_text)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    introComponents = [text, key_resp]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    instruct6.addData('text.started', text.tStartRefresh)
    instruct6.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    instruct6.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        instruct6.addData('key_resp.rt', key_resp.rt)
    instruct6.addData('key_resp.started', key_resp.tStartRefresh)
    instruct6.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instruct6'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count_0123.xlsx'),
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
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=7, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Dict[count]),
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
        
        # ------Prepare to start Routine "perspective_only"-------
        # update component parameters for each repeat
        text_18.setText(roleName)
        image_9.setImage(rolePic)
        key_resp_14.keys = []
        key_resp_14.rt = []
        # keep track of which components have finished
        perspective_onlyComponents = [text_18, image_9, key_resp_14]
        for thisComponent in perspective_onlyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        perspective_onlyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "perspective_only"-------
        while continueRoutine:
            # get current time
            t = perspective_onlyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=perspective_onlyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_18* updates
            if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_18.frameNStart = frameN  # exact frame index
                text_18.tStart = t  # local t and not account for scr refresh
                text_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
                text_18.setAutoDraw(True)
            
            # *image_9* updates
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                image_9.setAutoDraw(True)
            
            # *key_resp_14* updates
            waitOnFlip = False
            if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_14.frameNStart = frameN  # exact frame index
                key_resp_14.tStart = t  # local t and not account for scr refresh
                key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                key_resp_14.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_14.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_14.keys = theseKeys.name  # just the last key pressed
                    key_resp_14.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in perspective_onlyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "perspective_only"-------
        for thisComponent in perspective_onlyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('text_18.started', text_18.tStartRefresh)
        trials_2.addData('text_18.stopped', text_18.tStopRefresh)
        trials_2.addData('image_9.started', image_9.tStartRefresh)
        trials_2.addData('image_9.stopped', image_9.tStopRefresh)
        # check responses
        if key_resp_14.keys in ['', [], None]:  # No response was made
            key_resp_14.keys = None
        trials_2.addData('key_resp_14.keys',key_resp_14.keys)
        if key_resp_14.keys != None:  # we had a response
            trials_2.addData('key_resp_14.rt', key_resp_14.rt)
        trials_2.addData('key_resp_14.started', key_resp_14.tStartRefresh)
        trials_2.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
        # the Routine "perspective_only" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q1"-------
        # update component parameters for each repeat
        text_8.setText(('A: ' + Q1)



)
        text_9.setText(roleName)
        image_5.setImage(rolePic)
        key_resp_10.keys = []
        key_resp_10.rt = []
        # keep track of which components have finished
        q1Components = [text_8, text_9, image_5, key_resp_10]
        for thisComponent in q1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "q1"-------
        while continueRoutine:
            # get current time
            t = q1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=q1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                text_9.setAutoDraw(True)
            
            # *image_5* updates
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                image_5.setAutoDraw(True)
            
            # *key_resp_10* updates
            waitOnFlip = False
            if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_10.keys = theseKeys.name  # just the last key pressed
                    key_resp_10.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_2.addData('text_8.started', text_8.tStartRefresh)
        trials_2.addData('text_8.stopped', text_8.tStopRefresh)
        trials_2.addData('text_9.started', text_9.tStartRefresh)
        trials_2.addData('text_9.stopped', text_9.tStopRefresh)
        trials_2.addData('image_5.started', image_5.tStartRefresh)
        trials_2.addData('image_5.stopped', image_5.tStopRefresh)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys = None
        trials_2.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            trials_2.addData('key_resp_10.rt', key_resp_10.rt)
        trials_2.addData('key_resp_10.started', key_resp_10.tStartRefresh)
        trials_2.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
        # the Routine "q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q2"-------
        # update component parameters for each repeat
        text_10.setText(('B: ' + Q2)



)
        text_11.setText(roleName)
        image_6.setImage(rolePic)
        key_resp_11.keys = []
        key_resp_11.rt = []
        # keep track of which components have finished
        q2Components = [text_10, text_11, image_6, key_resp_11]
        for thisComponent in q2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "q2"-------
        while continueRoutine:
            # get current time
            t = q2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=q2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_10* updates
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                text_10.setAutoDraw(True)
            
            # *text_11* updates
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                text_11.setAutoDraw(True)
            
            # *image_6* updates
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                image_6.setAutoDraw(True)
            
            # *key_resp_11* updates
            waitOnFlip = False
            if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_11.keys = theseKeys.name  # just the last key pressed
                    key_resp_11.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_2.addData('text_10.started', text_10.tStartRefresh)
        trials_2.addData('text_10.stopped', text_10.tStopRefresh)
        trials_2.addData('text_11.started', text_11.tStartRefresh)
        trials_2.addData('text_11.stopped', text_11.tStopRefresh)
        trials_2.addData('image_6.started', image_6.tStartRefresh)
        trials_2.addData('image_6.stopped', image_6.tStopRefresh)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        trials_2.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            trials_2.addData('key_resp_11.rt', key_resp_11.rt)
        trials_2.addData('key_resp_11.started', key_resp_11.tStartRefresh)
        trials_2.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
        # the Routine "q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q3"-------
        # update component parameters for each repeat
        text_13.setText(('C: ' + Q3)



)
        text_14.setText(roleName)
        image_7.setImage(rolePic)
        key_resp_12.keys = []
        key_resp_12.rt = []
        # keep track of which components have finished
        q3Components = [text_13, text_14, image_7, key_resp_12]
        for thisComponent in q3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "q3"-------
        while continueRoutine:
            # get current time
            t = q3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=q3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_13* updates
            if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_13.frameNStart = frameN  # exact frame index
                text_13.tStart = t  # local t and not account for scr refresh
                text_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                text_13.setAutoDraw(True)
            
            # *text_14* updates
            if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                text_14.setAutoDraw(True)
            
            # *image_7* updates
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                image_7.setAutoDraw(True)
            
            # *key_resp_12* updates
            waitOnFlip = False
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_12.keys = theseKeys.name  # just the last key pressed
                    key_resp_12.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_2.addData('text_13.started', text_13.tStartRefresh)
        trials_2.addData('text_13.stopped', text_13.tStopRefresh)
        trials_2.addData('text_14.started', text_14.tStartRefresh)
        trials_2.addData('text_14.stopped', text_14.tStopRefresh)
        trials_2.addData('image_7.started', image_7.tStartRefresh)
        trials_2.addData('image_7.stopped', image_7.tStopRefresh)
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        trials_2.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            trials_2.addData('key_resp_12.rt', key_resp_12.rt)
        trials_2.addData('key_resp_12.started', key_resp_12.tStartRefresh)
        trials_2.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
        # the Routine "q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "q4"-------
        # update component parameters for each repeat
        text_15.setText(('D: ' + Q4)



)
        text_16.setText(roleName)
        image_8.setImage(rolePic)
        key_resp_13.keys = []
        key_resp_13.rt = []
        # keep track of which components have finished
        q4Components = [text_15, text_16, image_8, key_resp_13]
        for thisComponent in q4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "q4"-------
        while continueRoutine:
            # get current time
            t = q4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=q4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_15* updates
            if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_15.frameNStart = frameN  # exact frame index
                text_15.tStart = t  # local t and not account for scr refresh
                text_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                text_15.setAutoDraw(True)
            
            # *text_16* updates
            if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_16.frameNStart = frameN  # exact frame index
                text_16.tStart = t  # local t and not account for scr refresh
                text_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
                text_16.setAutoDraw(True)
            
            # *image_8* updates
            if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                image_8.setAutoDraw(True)
            
            # *key_resp_13* updates
            waitOnFlip = False
            if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_13.frameNStart = frameN  # exact frame index
                key_resp_13.tStart = t  # local t and not account for scr refresh
                key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                key_resp_13.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_13.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_13.keys = theseKeys.name  # just the last key pressed
                    key_resp_13.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_2.addData('text_15.started', text_15.tStartRefresh)
        trials_2.addData('text_15.stopped', text_15.tStopRefresh)
        trials_2.addData('text_16.started', text_16.tStartRefresh)
        trials_2.addData('text_16.stopped', text_16.tStopRefresh)
        trials_2.addData('image_8.started', image_8.tStartRefresh)
        trials_2.addData('image_8.stopped', image_8.tStopRefresh)
        # check responses
        if key_resp_13.keys in ['', [], None]:  # No response was made
            key_resp_13.keys = None
        trials_2.addData('key_resp_13.keys',key_resp_13.keys)
        if key_resp_13.keys != None:  # we had a response
            trials_2.addData('key_resp_13.rt', key_resp_13.rt)
        trials_2.addData('key_resp_13.started', key_resp_13.tStartRefresh)
        trials_2.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
        # the Routine "q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "intro_practicetest"-------
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        # keep track of which components have finished
        intro_practicetestComponents = [text_5, key_resp_4]
        for thisComponent in intro_practicetestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intro_practicetestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "intro_practicetest"-------
        while continueRoutine:
            # get current time
            t = intro_practicetestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intro_practicetestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_4.keys = theseKeys.name  # just the last key pressed
                    key_resp_4.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_2.addData('text_5.started', text_5.tStartRefresh)
        trials_2.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials_2.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials_2.addData('key_resp_4.rt', key_resp_4.rt)
        trials_2.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        trials_2.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        # the Routine "intro_practicetest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "test"-------
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
        
        this_image = 'icon/bar1.png'
        
        
        
        check = visual.ImageStim(win, 'icon/checkmark.png')
        redx = visual.ImageStim(win, 'icon/redx.png')
        
        thumbsup = visual.ImageStim(win, 'icon/thumbsup.png')
        
        
        
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "test"-------
        while continueRoutine:
            # get current time
            t = testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question1_2* updates
            if question1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question1_2.frameNStart = frameN  # exact frame index
                question1_2.tStart = t  # local t and not account for scr refresh
                question1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question1_2, 'tStartRefresh')  # time at next scr refresh
                question1_2.setAutoDraw(True)
            
            # *question2_2* updates
            if question2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question2_2.frameNStart = frameN  # exact frame index
                question2_2.tStart = t  # local t and not account for scr refresh
                question2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question2_2, 'tStartRefresh')  # time at next scr refresh
                question2_2.setAutoDraw(True)
            
            # *question3_2* updates
            if question3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question3_2.frameNStart = frameN  # exact frame index
                question3_2.tStart = t  # local t and not account for scr refresh
                question3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question3_2, 'tStartRefresh')  # time at next scr refresh
                question3_2.setAutoDraw(True)
            
            # *question4_2* updates
            if question4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question4_2.frameNStart = frameN  # exact frame index
                question4_2.tStart = t  # local t and not account for scr refresh
                question4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question4_2, 'tStartRefresh')  # time at next scr refresh
                question4_2.setAutoDraw(True)
            
            # *question5_2* updates
            if question5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question5_2.frameNStart = frameN  # exact frame index
                question5_2.tStart = t  # local t and not account for scr refresh
                question5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question5_2, 'tStartRefresh')  # time at next scr refresh
                question5_2.setAutoDraw(True)
            
            # *question6_2* updates
            if question6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question6_2.frameNStart = frameN  # exact frame index
                question6_2.tStart = t  # local t and not account for scr refresh
                question6_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question6_2, 'tStartRefresh')  # time at next scr refresh
                question6_2.setAutoDraw(True)
            if this_image == 'icon/bar5.jpg':
                thumbsup.draw()
                win.flip()
                core.wait(1.5)
                trials_2.finished= True 
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
                trials_2.finished = True
                continueRoutine=False
            if checkCount == 4:
                this_image = 'icon/bar5.jpg'
            
            if checkCount == 1:
                this_image = 'icon/bar2.png'
            if checkCount == 2: 
                this_image = 'icon/bar3.jpg'
            if checkCount == 3:
                this_image = 'icon/bar4.png'
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:  # only update if drawing
                image_3.setImage(this_image, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_2.addData('question1_2.started', question1_2.tStartRefresh)
        trials_2.addData('question1_2.stopped', question1_2.tStopRefresh)
        trials_2.addData('question2_2.started', question2_2.tStartRefresh)
        trials_2.addData('question2_2.stopped', question2_2.tStopRefresh)
        trials_2.addData('question3_2.started', question3_2.tStartRefresh)
        trials_2.addData('question3_2.stopped', question3_2.tStopRefresh)
        trials_2.addData('question4_2.started', question4_2.tStartRefresh)
        trials_2.addData('question4_2.stopped', question4_2.tStopRefresh)
        trials_2.addData('question5_2.started', question5_2.tStartRefresh)
        trials_2.addData('question5_2.stopped', question5_2.tStopRefresh)
        trials_2.addData('question6_2.started', question6_2.tStartRefresh)
        trials_2.addData('question6_2.stopped', question6_2.tStopRefresh)
        trials_2.addData('image_3.started', image_3.tStartRefresh)
        trials_2.addData('image_3.stopped', image_3.tStopRefresh)
        # the Routine "test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 7 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "final_test_intro"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
final_test_introComponents = [text_3]
for thisComponent in final_test_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
final_test_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "final_test_intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = final_test_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=final_test_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count_0123.xlsx'),
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
    trials_3 = data.TrialHandler(nReps=7, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Dict[count]),
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
        
        # ------Prepare to start Routine "final_test_i"-------
        # update component parameters for each repeat
        image_2.setImage(rolePic)
        key_resp_3.keys = []
        key_resp_3.rt = []
        text_4.setText(roleName
)
        # keep track of which components have finished
        final_test_iComponents = [image_2, key_resp_3, text_4]
        for thisComponent in final_test_iComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        final_test_iClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "final_test_i"-------
        while continueRoutine:
            # get current time
            t = final_test_iClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=final_test_iClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_3.keys = theseKeys.name  # just the last key pressed
                    key_resp_3.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_3.addData('image_2.started', image_2.tStartRefresh)
        trials_3.addData('image_2.stopped', image_2.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_3.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_3.addData('key_resp_3.rt', key_resp_3.rt)
        trials_3.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        trials_3.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        trials_3.addData('text_4.started', text_4.tStartRefresh)
        trials_3.addData('text_4.stopped', text_4.tStopRefresh)
        # the Routine "final_test_i" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "test3"-------
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
        
        this_image = 'icon/bar1.png'
        
        
        
        check = visual.ImageStim(win, 'icon/checkmark.png')
        redx = visual.ImageStim(win, 'icon/redx.png')
        
        thumbsup = visual.ImageStim(win, 'icon/thumbsup.png')
        
        
        
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        test3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "test3"-------
        while continueRoutine:
            # get current time
            t = test3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=test3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question1_3* updates
            if question1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question1_3.frameNStart = frameN  # exact frame index
                question1_3.tStart = t  # local t and not account for scr refresh
                question1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question1_3, 'tStartRefresh')  # time at next scr refresh
                question1_3.setAutoDraw(True)
            
            # *question2_3* updates
            if question2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question2_3.frameNStart = frameN  # exact frame index
                question2_3.tStart = t  # local t and not account for scr refresh
                question2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question2_3, 'tStartRefresh')  # time at next scr refresh
                question2_3.setAutoDraw(True)
            
            # *question3_3* updates
            if question3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question3_3.frameNStart = frameN  # exact frame index
                question3_3.tStart = t  # local t and not account for scr refresh
                question3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question3_3, 'tStartRefresh')  # time at next scr refresh
                question3_3.setAutoDraw(True)
            
            # *question4_3* updates
            if question4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question4_3.frameNStart = frameN  # exact frame index
                question4_3.tStart = t  # local t and not account for scr refresh
                question4_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question4_3, 'tStartRefresh')  # time at next scr refresh
                question4_3.setAutoDraw(True)
            
            # *question5_3* updates
            if question5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question5_3.frameNStart = frameN  # exact frame index
                question5_3.tStart = t  # local t and not account for scr refresh
                question5_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question5_3, 'tStartRefresh')  # time at next scr refresh
                question5_3.setAutoDraw(True)
            
            # *question6_3* updates
            if question6_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question6_3.frameNStart = frameN  # exact frame index
                question6_3.tStart = t  # local t and not account for scr refresh
                question6_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question6_3, 'tStartRefresh')  # time at next scr refresh
                question6_3.setAutoDraw(True)
            if this_image == 'icon/bar5.jpg':
                thumbsup.draw()
                win.flip()
                core.wait(1.5)
                trials_3.finished= True 
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
                trials_3.finished = True
                continueRoutine=False
            if checkCount == 4:
                this_image = 'icon/bar5.jpg'
                trials_7.finished = True
            
            if checkCount == 1:
                this_image = 'icon/bar2.png'
            if checkCount == 2: 
                this_image = 'icon/bar3.jpg'
            if checkCount == 3:
                this_image = 'icon/bar4.png'
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                image_4.setAutoDraw(True)
            if image_4.status == STARTED:  # only update if drawing
                image_4.setImage(this_image, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_3.addData('question1_3.started', question1_3.tStartRefresh)
        trials_3.addData('question1_3.stopped', question1_3.tStopRefresh)
        trials_3.addData('question2_3.started', question2_3.tStartRefresh)
        trials_3.addData('question2_3.stopped', question2_3.tStopRefresh)
        trials_3.addData('question3_3.started', question3_3.tStartRefresh)
        trials_3.addData('question3_3.stopped', question3_3.tStopRefresh)
        trials_3.addData('question4_3.started', question4_3.tStartRefresh)
        trials_3.addData('question4_3.stopped', question4_3.tStopRefresh)
        trials_3.addData('question5_3.started', question5_3.tStartRefresh)
        trials_3.addData('question5_3.stopped', question5_3.tStopRefresh)
        trials_3.addData('question6_3.started', question6_3.tStartRefresh)
        trials_3.addData('question6_3.stopped', question6_3.tStopRefresh)
        trials_3.addData('image_4.started', image_4.tStartRefresh)
        trials_3.addData('image_4.stopped', image_4.tStopRefresh)
        # the Routine "test3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 7 repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "end"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_2]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
