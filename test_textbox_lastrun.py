#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Tue Jan 22 13:43:54 2019
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
expName = 'test_textbox'  # from the Builder filename that created this script
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
    originPath='/Users/alexreblando/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/ebs/test_textbox_lastrun.py',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
import numpy as np

a = np.zeros(shape = [4, 4], dtype = int)

s_order = np.array([10, 20, 30, 40], dtype = int)

l_order = np.array([1,2,3,4], dtype = int)


np.random.shuffle(s_order)
np.random.shuffle(l_order)

a[0] += s_order[0]
a[1] += s_order[1]
a[2] += s_order[2]
a[3] += s_order[3]

a[:,0] += l_order[0]
a[:,1] += l_order[1]
a[:, 2] += l_order[2]
a[:, 3] += l_order[3]

run1 = np.array([a[0,0], a[1,1], a[2,0], a[3,1], a[0,2], a[1,3], a[2,2], a[3,3]]) 
run2 = np.array([a[0,1], a[1,0], a[2,1], a[3,0], a[0,3], a[1,2], a[2,3], a[3,2]]) 
order_run1 = np.array(['Location', 'Location', 'Social', 'Social', 'Social', 'Social', 'Location', 'Location'])
order_run2 = np.array(['Location', 'Location', 'Social', 'Social', 'Social', 'Social', 'Location', 'Location'])

randperm1 = np.random.permutation(8)
randperm2 = np.random.permutation(8)

run1 = run1[randperm1]
run2 = run2[randperm2]
order_run1 = order_run1[randperm1]
order_run2 = order_run2[randperm2]



#create a dictionary for all the stories and their values

storyDict = {11: {'name':'Restaurant Breakup', 'Social': 'Couples Therapist', 'Location':'Restaurant Critic', 'pic':'storypics/11_storypic', 'storyFile': 'story_xlsx_files/11.xlsx'},
             12: {'name':'Airport Breakup', 'Social': 'Couples Therapist', 'Location':'Airport Customer Experience Manager', 'pic':'storypics/12_storypic', 'storyFile': 'story_xlsx_files/12.xlsx'},
             13: {'name':'Grocery Shopping- Break up', 'Social':'Couples Therapist', 'Location': 'Grocery Store Customer Experience Manager', 'pic':'storypics/13_storypic', 'storyFile': 'story_xlsx_files/13.xlsx'},
             14: {'name':'Attending a Lecture-Breakup', 'Social':'Couples Therapist', 'Location': 'Dean of Academic Studies', 'pic':'storypics/14_storypic', 'storyFile': 'story_xlsx_files/14.xlsx'},
             21: {'name':'Restaurant Proposal', 'Social': 'Wedding Planner', 'Location': 'Restaurant Critic', 'pic':'storypics/21_storypic', 'storyFile': 'story_xlsx_files/21.xlsx'},
             22: {'name':'Airport Proposal', 'Social': 'Wedding Planner', 'Location':'Airport Customer Experience Manager', 'pic':'storypics/22_storypic', 'storyFile': 'story_xlsx_files/22.xlsx'},
             23: {'name':'Grocery Shopping- Proposal', 'Social': 'Wedding Planner', 'Location':'Grocery Store Customer Experience Manager', 'pic':'storypics/23_storypic', 'storyFile': 'story_xlsx_files/23.xlsx'},
             24: {'name':'Attending a Lecture-Proposal', 'Social': 'Wedding Planner', 'Location': 'Dean of Academic Studies', 'pic':'storypics/24_storypic', 'storyFile': 'story_xlsx_files/24.xlsx'},
             31: {'name':'Restaurant Business Deal', 'Social':'Business Reporter', 'Location':'Restaurant Critic', 'pic':'storypics/31_storypic', 'storyFile': 'story_xlsx_files/31.xlsx'},
             32: {'name':'Airport Business Deal', 'Social':'Business Reporter', 'Location':'Airport Customer Experience Manager', 'pic':'storypics/32_storypic', 'storyFile': 'story_xlsx_files/32.xlsx'},
             33: {'name':'Grocery Shopping- Business Deal', 'Social':'Business Reporter', 'Location':'Grocery Store Customer Experience Manager', 'pic':'storypics/33_storypic', 'storyFile': 'story_xlsx_files/33.xlsx'},
             34: {'name':'Attending a Lecture-Business Deal', 'Social':'Business Reporter', 'Location':'Dean of Academic Studies', 'pic':'storypics/34_storypic', 'storyFile': 'story_xlsx_files/34.xlsx'},
             41: {'name':'Restaurant Meet Cute', 'Social': 'Matchmaker', 'Location':'Restaurant Critic', 'pic':'storypics/41_storypic', 'storyFile': 'story_xlsx_files/41.xlsx'},
             42: {'name':'Airport Meet Cute', 'Social': 'Matchmaker', 'Location':'Airport Customer Experience Manager', 'pic':'storypics/42_storypic', 'storyFile': 'story_xlsx_files/42.xlsx'},
             43: {'name':'Grocery Shopping- Meet Cute', 'Social':'Matchmaker', 'Location': 'Grocery Store Customer Experience Manager', 'pic':'storypics/43_storypic', 'storyFile': 'story_xlsx_files/43.xlsx'},
             44: {'name':'Attending a Lecture-Meet Cute', 'Social':'Matchmaker', 'Location': 'Dean of Academic Studies', 'pic':'storypics/44_storypic', 'storyFile': 'story_xlsx_files/44.xlsx'}}

order_stories = np.concatenate((run1, run2), axis =None)
order_perspectives = np.concatenate((order_run1, order_run2), axis = None)

#create complementary perspectives list for non-primed questions
other_perspectives = []

for i in range(0,16):
    if order_perspectives[i] == 'Social':
        other_pespectives = other_perspectives.append('Location')
    else:
        other_pespectives = other_perspectives.append('Social')

thisExp.addData('order of stories', order_stories)
thisExp.addData('order of perspectives', order_perspectives)














# Initialize components for Routine "recall"
recallClock = core.Clock()

text_9 = visual.TextStim(win=win, name='text_9',
    text='Type everything you recall here (press return to submit your response):',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon = visual.Line(
    win=win, name='polygon',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line = visual.Line(
    win=win, name='bottom_line',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.975),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_2 = visual.Line(
    win=win, name='right_line_2',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.55),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line = visual.Line(
    win=win, name='left_line',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.55),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
trialComponents = []
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count.xlsx'),
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
    
    # ------Prepare to start Routine "recall"-------
    t = 0
    recallClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=10
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = True
    text_10.alignHoriz ='left'
    text_10.alignVert = 'top'
    text_10.wrapWidth = 1.8
    text_10.height = .05
    
    this_recall_pic = storyDict.get(order_stories[count], {}).get('pic')
    
    image_4.setImage(this_recall_pic)
    # keep track of which components have finished
    recallComponents = [text_9, text_10, image_4, polygon, bottom_line, right_line_2, left_line]
    for thisComponent in recallComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "recall"-------
    while continueRoutine:
        # get current time
        t = recallClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if subject_response_finished:
            final_response=captured_string
            continueRoutine=False
        for key in event.getKeys():
            if key in ['tab']:
                trials_4.finished = 1
                continueRoutine = False
            if key in ['escape']: 
                core.quit()
            elif key in ['delete','backspace']:
                captured_string = captured_string[:-1] 
            elif key in ['return']:
                thisExp.addData('recall', captured_string)
                subject_response_finished=True
            elif key in ['space']:
                captured_string = captured_string+' '
            elif key in ['period']:
                captured_string = captured_string+'.'
            elif key in ['dollar']:
                captured_string = captured_string + '$'
            elif key in ['exclamation']:
                captured_string = captured_string + '!'
            elif key in ['lshift', 'rshift']:
                shift_flag = True
            elif key in ['comma']:
                captured_string = captured_string+','
            elif key in ['apostrophe']:
                captured_string = captured_string+"'"
            elif key in ['slash']:
                captured_string = captured_string+'/'
            elif key in ['semicolon']:
                captured_string = captured_string + ';'
            elif key in ['option']:
                captured_string = captured_string
            elif key in ['lshift','rshift']:
                shift_flag = True
                captured_string = captured_string + ' '
            elif key in ['minus']:
                captured_string = captured_string+'-'
            elif key in ['up','down','left','right','return']:
                pass
            else: 
                captured_string = captured_string+key
            # this next line formats the output. you can remove or modify as necessary
            captured_string=captured_string.capitalize()
        
        # *text_9* updates
        if t >= 0.0 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        
        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:  # only update if drawing
            text_10.setText(captured_string, log=False)
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        
        # *bottom_line* updates
        if t >= 0.0 and bottom_line.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line.tStart = t
            bottom_line.frameNStart = frameN  # exact frame index
            bottom_line.setAutoDraw(True)
        
        # *right_line_2* updates
        if t >= 0.0 and right_line_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_2.tStart = t
            right_line_2.frameNStart = frameN  # exact frame index
            right_line_2.setAutoDraw(True)
        
        # *left_line* updates
        if t >= 0.0 and left_line.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line.tStart = t
            left_line.frameNStart = frameN  # exact frame index
            left_line.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recall"-------
    for thisComponent in recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
