#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Thu Jan  3 11:54:58 2019
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
expName = 'body_updated'  # from the Builder filename that created this script
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
    originPath='/Users/alexreblando/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/ebs/body_updated_lastrun.py',
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

# Initialize components for Routine "perspective"
perspectiveClock = core.Clock()
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

storyDict = {11: {'name':'Restaurant Breakup', 'Social': 'Couples Therapist', 'Location':'Restaurant Critic'},
             12: {'name':'Airport Breakup', 'Social': 'Couples Therapist', 'Location':'Airport Customer Experience Manager'},
             13: {'name':'Grocery Shopping- Break up', 'Social':'Couples Therapist', 'Location': 'Grocery Store Customer Experience Manager'},
             14: {'name':'Attending a Lecture-Breakup', 'Social':'Couples Therapist', 'Location': 'Dean of Academic Studies'},
             21: {'name':'Restaurant Proposal', 'Social': 'Wedding Planner', 'Location': 'Restaurant Critic'},
             22: {'name':'Airport Proposal', 'Social': 'Wedding Planner', 'Location':'Airport Customer Experience Manager'},
             23: {'name':'Grocery Shopping- Proposal', 'Social': 'Wedding Planner', 'Location':'Grocery Store Customer Experience Manager'},
             24: {'name':'Attending a Lecture-Proposal', 'Social': 'Wedding Planner', 'Location': 'Dean of Academic Studies'},
             31: {'name':'Restaurant Business Deal', 'Social':'Business Reporter', 'Location':'Restaurant Critic'},
             32: {'name':'Airport Business Deal', 'Social':'Business Reporter', 'Location':'Airport Customer Experience Manager'},
             33: {'name':'Grocery Shopping- Business Deal', 'Social':'Business Reporter', 'Location':'Grocery Store Customer Experience Manager'},
             34: {'name':'Attending a Lecture-Business Deal', 'Social':'Business Reporter', 'Location':'Dean of Academic Studies'},
             41: {'name':'Restaurant Meet Cute', 'Social': 'Matchmaker', 'Location':'Restaurant Critic'},
             42: {'name':'Airport Meet Cute', 'Social': 'Matchmaker', 'Location':'Airport Customer Experience Manager'},
             43: {'name':'Grocery Shopping- Meet Cute', 'Social':'Matchmaker', 'Location': 'Grocery Store Customer Experience Manager'},
             44: {'name':'Attending a Lecture-Meet Cute', 'Social':'Matchmaker', 'Location': 'Dean of Academic Studies'}}

order_stories = np.concatenate((run1, run2), axis =None)
order_perspectives = np.concatenate((order_run1, order_run2), axis = None)

thisExp.addData('order of stories', order_stories)
thisExp.addData('order of perspectives', order_perspectives)













text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, -.5), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, .4), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
    
    # ------Prepare to start Routine "perspective"-------
    t = 0
    perspectiveClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    #set the perspective
    this_perspective = storyDict.get(order_stories[count], {}).get(order_perspectives[count])
    if this_perspective == 'Couples Therapist':
        display_pic = 'couples.jpg'
    if this_perspective == 'Restaurant Critic':
        display_pic = 'restaurant_critic.jpg'
    if this_perspective == 'Airport Customer Experience Manager':
        display_pic = 'acem.jpg'
    if this_perspective == 'Grocery Store Customer Experience Manager':
        display_pic = 'gscem.jpg'
    if this_perspective == 'Dean of Academic Studies':
        display_pic = 'dean.jpg'
    if this_perspective == 'Wedding Planner':
        display_pic = 'weddingplanner.jpg'
    if this_perspective == 'Business Reporter':
        display_pic = 'business_reporter.jpg'
    if this_perspective == 'Matchmaker':
        display_pic = 'matchmaker.jpg'
    
    #set the story text
    this_story = order_stories[count]
    
    if this_story == 11:
        story_file = '11.xlsx'
        this_story_pic = '11_faces.jpg'
    if this_story == 12:
        story_file = '12.xlsx'
        this_story_pic = '12_faces.jpg'
    if this_story == 13:
        story_file = '13.xlsx'
        this_story_pic = '13_faces.jpg'
    if this_story == 14:
        story_file = '14.xlsx'
        this_story_pic = '14_faces.jpg'
    if this_story == 21:
        story_file = '21.xlsx'
        this_story_pic = '21_faces.jpg'
    if this_story == 22:
        story_file = '22.xlsx'
        this_story_pic = '22_faces.jpg'
    if this_story == 23:
        story_file = '23.xlsx'
        this_story_pic = '23_faces.jpg'
    if this_story == 24:
        story_file = '24.xlsx'
        this_story_pic = '24_faces.jpg'
    if this_story == 31:
        story_file = '31.xlsx'
        this_story_pic = '31_faces.jpg'
    if this_story == 32:
        story_file = '32.xlsx'
        this_story_pic = '32_faces.jpg'
    if this_story == 33:
        story_file = '33.xlsx'
        this_story_pic = '33_faces.jpg'
    if this_story == 34:
        story_file = '34.xlsx'
        this_story_pic = '34_faces.jpg'
    if this_story == 41:
        story_file = '41.xlsx'
        this_story_pic = '41_faces.jpg'
    if this_story == 42:
        story_file = '42.xlsx'
        this_story_pic = '42_faces.jpg'
    if this_story == 43:
        story_file = '43.xlsx'
        this_story_pic = '43_faces.jpg'
    if this_story == 44:
        story_file = '44.xlsx'
        this_story_pic = '44_faces.jpg'
    
    
    
    
    key_resp_3 = event.BuilderKeyResponse()
    text_4.setText(this_perspective)
    image.setImage(display_pic)
    # keep track of which components have finished
    perspectiveComponents = [key_resp_3, text_4, image]
    for thisComponent in perspectiveComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "perspective"-------
    while continueRoutine:
        # get current time
        t = perspectiveClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
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
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
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
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in perspectiveComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "perspective"-------
    for thisComponent in perspectiveComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "perspective" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(story_file),
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
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(storyText

)
        key_resp_2 = event.BuilderKeyResponse()
        image_2.setImage(this_story_pic)
        # keep track of which components have finished
        trialComponents = [text, key_resp_2, image_2]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            
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
                theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
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
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys=None
        trials_2.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials_2.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
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
