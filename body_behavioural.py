#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Fri Jan 18 13:31:23 2019
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
expName = 'body_behavioural'  # from the Builder filename that created this script
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
    originPath='/Users/alexreblando/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/ebs/body_behavioural.py',
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
other_perspectives = np.array([])

for i in range(0,15):
    if order_perspectives[i] == 'Social':
        np.append(other_perspectives, 'Location')
    else:
        np.append(other_perspectives, 'Social')

thisExp.addData('order of stories', order_stories)
thisExp.addData('order of perspectives', order_perspectives)













text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='(press space to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

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

# Initialize components for Routine "recall_instructions"
recall_instructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='(press space to continue)',
    font='Arial',
    pos=(0, -.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "recall_3"
recall_3Clock = core.Clock()

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

# Initialize components for Routine "questions_instructions2"
questions_instructions2Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='(press space to continue)',
    font='Arial',
    pos=(0, -.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "story_image"
story_imageClock = core.Clock()

image_10 = visual.ImageStim(
    win=win, name='image_10',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_22 = visual.TextStim(win=win, name='text_22',
    text='(press space to continue)',
    font='Arial',
    pos=(0, -.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "question1"
question1Clock = core.Clock()

text_14 = visual.TextStim(win=win, name='text_14',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_6 = visual.ImageStim(
    win=win, name='image_6',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_3 = visual.Line(
    win=win, name='polygon_3',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_3 = visual.Line(
    win=win, name='bottom_line_3',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.5),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_3 = visual.Line(
    win=win, name='right_line_3',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_3 = visual.Line(
    win=win, name='left_line_3',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question2"
question2Clock = core.Clock()

text_16 = visual.TextStim(win=win, name='text_16',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_7 = visual.ImageStim(
    win=win, name='image_7',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_4 = visual.Line(
    win=win, name='polygon_4',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_4 = visual.Line(
    win=win, name='bottom_line_4',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.5),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_4 = visual.Line(
    win=win, name='right_line_4',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_4 = visual.Line(
    win=win, name='left_line_4',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question3"
question3Clock = core.Clock()

text_18 = visual.TextStim(win=win, name='text_18',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_8 = visual.ImageStim(
    win=win, name='image_8',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_5 = visual.Line(
    win=win, name='polygon_5',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_5 = visual.Line(
    win=win, name='bottom_line_5',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.5),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_5 = visual.Line(
    win=win, name='right_line_5',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_5 = visual.Line(
    win=win, name='left_line_5',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question4"
question4Clock = core.Clock()

text_20 = visual.TextStim(win=win, name='text_20',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_9 = visual.ImageStim(
    win=win, name='image_9',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_6 = visual.Line(
    win=win, name='polygon_6',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_6 = visual.Line(
    win=win, name='bottom_line_6',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.5),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_6 = visual.Line(
    win=win, name='right_line_6',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_6 = visual.Line(
    win=win, name='left_line_6',
    start=(-(.375, 1)[0]/2.0, 0), end=(+(.375, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.3125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

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
        display_pic = 'jobphotos/couples.jpg'
    if this_perspective == 'Restaurant Critic':
        display_pic = 'jobphotos/restaurant_critic.jpg'
    if this_perspective == 'Airport Customer Experience Manager':
        display_pic = 'jobphotos/acem.jpg'
    if this_perspective == 'Grocery Store Customer Experience Manager':
        display_pic = 'jobphotos/gscem.jpg'
    if this_perspective == 'Dean of Academic Studies':
        display_pic ='jobphotos/dean.jpg'
    if this_perspective == 'Wedding Planner':
        display_pic = 'jobphotos/weddingplanner.jpg'
    if this_perspective == 'Business Reporter':
        display_pic = 'jobphotos/business_reporter.jpg'
    if this_perspective == 'Matchmaker':
        display_pic = 'jobphotos/matchmaker.jpg'
    
    #set the story file and picture
    
    this_story_file = storyDict.get(order_stories[count], {}).get('storyFile')
    this_story_pic = storyDict.get(order_stories[count], {}).get('pic')
    
    text_4.setText(this_perspective)
    image.setImage(display_pic)
    # keep track of which components have finished
    perspectiveComponents = [text_4, image, text_5]
    for thisComponent in perspectiveComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "perspective"-------
    while continueRoutine:
        # get current time
        t = perspectiveClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        for key in event.getKeys():
            if key in ['space']: 
                continueRoutine = False
            if key in ['q']: 
                trials.finished = 1
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
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        
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
    
    # the Routine "perspective" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(this_story_file),
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
        story_presses = event.BuilderKeyResponse()
        image_2.setImage(this_story_pic)
        # keep track of which components have finished
        trialComponents = [text, story_presses, image_2]
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
            
            # *story_presses* updates
            if t >= 0.0 and story_presses.status == NOT_STARTED:
                # keep track of start time/frame for later
                story_presses.tStart = t
                story_presses.frameNStart = frameN  # exact frame index
                story_presses.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(story_presses.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if story_presses.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '9'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if story_presses.keys == []:  # then this was the first keypress
                        story_presses.keys = theseKeys[0]  # just the first key pressed
                        story_presses.rt = story_presses.clock.getTime()
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
        if story_presses.keys in ['', [], None]:  # No response was made
            story_presses.keys=None
        trials_2.addData('story_presses.keys',story_presses.keys)
        if story_presses.keys != None:  # we had a response
            trials_2.addData('story_presses.rt', story_presses.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('recall_instructions.xlsx'),
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
    
    # ------Prepare to start Routine "recall_instructions"-------
    t = 0
    recall_instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()
    text_6.setText(instructText)
    # keep track of which components have finished
    recall_instructionsComponents = [key_resp_2, text_6, text_24]
    for thisComponent in recall_instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "recall_instructions"-------
    while continueRoutine:
        # get current time
        t = recall_instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # *text_24* updates
        if t >= 0.0 and text_24.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_24.tStart = t
            text_24.frameNStart = frameN  # exact frame index
            text_24.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recall_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recall_instructions"-------
    for thisComponent in recall_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    trials_3.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_3.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "recall_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count.xlsx'),
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
    
    # ------Prepare to start Routine "recall_3"-------
    t = 0
    recall_3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_10.alignHoriz ='left'
    text_10.alignVert = 'top'
    text_10.wrapWidth = 1.8
    text_10.height = .05
    
    this_recall_pic = storyDict.get(order_stories[count], {}).get('pic')
    
    image_4.setImage(this_recall_pic)
    # keep track of which components have finished
    recall_3Components = [text_9, text_10, image_4, polygon, bottom_line, right_line_2, left_line]
    for thisComponent in recall_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "recall_3"-------
    while continueRoutine:
        # get current time
        t = recall_3Clock.getTime()
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
            elif key in ['minus']:
                captured_string = captured_string+'-'
            elif key in ['lshift','rshift','up','down','left','right','return']:
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
        for thisComponent in recall_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recall_3"-------
    for thisComponent in recall_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "recall_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('question_instructions.xlsx'),
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
    
    # ------Prepare to start Routine "questions_instructions2"-------
    t = 0
    questions_instructions2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3 = event.BuilderKeyResponse()
    text_13.setText(instructText)
    # keep track of which components have finished
    questions_instructions2Components = [key_resp_3, text_13, text_23]
    for thisComponent in questions_instructions2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "questions_instructions2"-------
    while continueRoutine:
        # get current time
        t = questions_instructions2Clock.getTime()
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
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        
        # *text_23* updates
        if t >= 0.0 and text_23.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_23.tStart = t
            text_23.frameNStart = frameN  # exact frame index
            text_23.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questions_instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questions_instructions2"-------
    for thisComponent in questions_instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.nextEntry()
    # the Routine "questions_instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count.xlsx'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "story_image"-------
    t = 0
    story_imageClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    this_recall_pic = storyDict.get(order_stories[count], {}).get('pic')
    image_10.setImage(this_recall_pic)
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    story_imageComponents = [image_10, key_resp_4, text_22]
    for thisComponent in story_imageComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "story_image"-------
    while continueRoutine:
        # get current time
        t = story_imageClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *image_10* updates
        if t >= 0.0 and image_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_10.tStart = t
            image_10.frameNStart = frameN  # exact frame index
            image_10.setAutoDraw(True)
        
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
        
        # *text_22* updates
        if t >= 0.0 and text_22.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_22.tStart = t
            text_22.frameNStart = frameN  # exact frame index
            text_22.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in story_imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "story_image"-------
    for thisComponent in story_imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
    trials_6.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_6.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "story_image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question1"-------
    t = 0
    question1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_15.alignHoriz ='left'
    text_15.alignVert = 'top'
    text_15.wrapWidth = 1.8
    text_15.height = .05
    
    #flip coin
    value = random()
    
    
    #if value < .5:
    
    #set questions
    this_perspective = storyDict.get(order_stories[count], {}).get(other_perspectives[count])
    if this_perspective == 'Couples Therapist':
        question1 = 'How does the person who is initiating the breakup feel before they do it?'
        question2 ='Why does the initiator want to break up?'
        question3 ='How does the person being broken up with respond?'
        question4 = 'Do the partners leave on good terms?'
    if this_perspective == 'Restaurant Critic':
        question1 = 'How is the restaurant decorated?'
        question2 ='What are the menus like?'
        question3 = 'What do the clients order?'
        question4 = 'How do the clients like the food?'
    if this_perspective == 'Airport Customer Experience Manager':
        question1 = 'When the clients arrive at the airport, how much time do they have to go through?'
        question2 ='What do the clients have do at security to comply with the security check?'
        question3 ='How do the clients feel when they are  walking to the gates?'
        question4 ='Where does each client sit on the plane?' 
    if this_perspective == 'Grocery Store Customer Experience Manager':
        question1 = 'What is the grocery store like upon entering?'
        question2 ='What items do the clients pick out?'
        question3 ='How is the checkout line and how long do the clients wait in line?'
        question4 = 'How much are the groceries and what method of payment do the clients use?'
    if this_perspective == 'Dean of Academic Studies':
        question1 = 'What is the lecture hall like?'
        question2 ='What class are the students  in and what is the day’s lecture about?'
        question3 ='What is something taught in lecture?'
        question4 = 'When is the next assessment in the class?'
    if this_perspective == 'Wedding Planner':
        question1 = 'How does the person who proposed feel before proposing?'
        question2 ='What is the ring like?'
        question3 ='Does anyone help with the proposal?'
        question4 = 'Who witnessed the “yes”?'
    if this_perspective == 'Business Reporter':
        question1 = 'What industry are the business people in?'
        question2 = 'What is being negotiated and how much money is at stake?'
        question3 = 'What is the response to the proposed deal?'
        question4 =  'What comes about from the business proposal?'
    if this_perspective == 'Matchmaker':
        question1 = 'Who notices who first and why do they notice the other?'
        question2 ='How does the couple start talking?'
        question3 ='Which of the people proposes going on an actual date and what do they propose?'
        question4 = 'Who leaves first and why do they have to go?'
    
    
    text_14.setText(question1)
    image_6.setImage(this_recall_pic)
    # keep track of which components have finished
    question1Components = [text_14, text_15, image_6, polygon_3, bottom_line_3, right_line_3, left_line_3]
    for thisComponent in question1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question1"-------
    while continueRoutine:
        # get current time
        t = question1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if subject_response_finished:
            final_response=captured_string
            continueRoutine=False
        for key in event.getKeys():
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
            elif key in ['comma']:
                captured_string = captured_string+','
            elif key in ['apostrophe']:
                captured_string = captured_string+"'"
            elif key in ['slash']:
                captured_string = captured_string+'/'
            elif key in ['dollar']:
                captured_string = captured_string + '$'
            elif key in ['exclamation']:
                captured_string = captured_string + '!'
            elif key in ['semicolon']:
                captured_string = captured_string + ';'
            elif key in ['option']:
                captured_string = captured_string
            elif key in ['minus']:
                captured_string = captured_string+'-'
            elif key in ['lshift','rshift','up','down','left','right','return']:
                pass
            else: 
                captured_string = captured_string+key
            # this next line formats the output. you can remove or modify as necessary
            captured_string=captured_string.capitalize()
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        if text_15.status == STARTED:  # only update if drawing
            text_15.setText(captured_string, log=False)
        
        # *image_6* updates
        if t >= 0.0 and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
        
        # *polygon_3* updates
        if t >= 0.0 and polygon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_3.tStart = t
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.setAutoDraw(True)
        
        # *bottom_line_3* updates
        if t >= 0.0 and bottom_line_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_3.tStart = t
            bottom_line_3.frameNStart = frameN  # exact frame index
            bottom_line_3.setAutoDraw(True)
        
        # *right_line_3* updates
        if t >= 0.0 and right_line_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_3.tStart = t
            right_line_3.frameNStart = frameN  # exact frame index
            right_line_3.setAutoDraw(True)
        
        # *left_line_3* updates
        if t >= 0.0 and left_line_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_3.tStart = t
            left_line_3.frameNStart = frameN  # exact frame index
            left_line_3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question1"-------
    for thisComponent in question1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question1_correct_perspective', captured_string)
    
    # the Routine "question1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question2"-------
    t = 0
    question2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_17.alignHoriz ='left'
    text_17.alignVert = 'top'
    text_17.wrapWidth = 1.8
    text_17.height = .05
    
    
    text_16.setText(question2
)
    image_7.setImage(this_recall_pic)
    # keep track of which components have finished
    question2Components = [text_16, text_17, image_7, polygon_4, bottom_line_4, right_line_4, left_line_4]
    for thisComponent in question2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question2"-------
    while continueRoutine:
        # get current time
        t = question2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if subject_response_finished:
            final_response=captured_string
            continueRoutine=False
        for key in event.getKeys():
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
            elif key in ['minus']:
                captured_string = captured_string+'-'
            elif key in ['lshift','rshift','up','down','left','right','return']:
                pass
            else: 
                captured_string = captured_string+key
            # this next line formats the output. you can remove or modify as necessary
            captured_string=captured_string.capitalize()
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        
        # *text_17* updates
        if t >= 0.0 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:  # only update if drawing
            text_17.setText(captured_string, log=False)
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        
        # *polygon_4* updates
        if t >= 0.0 and polygon_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_4.tStart = t
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.setAutoDraw(True)
        
        # *bottom_line_4* updates
        if t >= 0.0 and bottom_line_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_4.tStart = t
            bottom_line_4.frameNStart = frameN  # exact frame index
            bottom_line_4.setAutoDraw(True)
        
        # *right_line_4* updates
        if t >= 0.0 and right_line_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_4.tStart = t
            right_line_4.frameNStart = frameN  # exact frame index
            right_line_4.setAutoDraw(True)
        
        # *left_line_4* updates
        if t >= 0.0 and left_line_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_4.tStart = t
            left_line_4.frameNStart = frameN  # exact frame index
            left_line_4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question2"-------
    for thisComponent in question2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question2_correct_perspective', captured_string)
    # the Routine "question2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question3"-------
    t = 0
    question3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_19.alignHoriz ='left'
    text_19.alignVert = 'top'
    text_19.wrapWidth = 1.8
    text_19.height = .05
    
    
    text_18.setText(question3
)
    image_8.setImage(this_recall_pic)
    # keep track of which components have finished
    question3Components = [text_18, text_19, image_8, polygon_5, bottom_line_5, right_line_5, left_line_5]
    for thisComponent in question3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question3"-------
    while continueRoutine:
        # get current time
        t = question3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if subject_response_finished:
            final_response=captured_string
            continueRoutine=False
        for key in event.getKeys():
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
            elif key in ['dollar']:
                captured_string = captured_string + '$'
            elif key in ['exclamation']:
                captured_string = captured_string + '!'
            elif key in ['minus']:
                captured_string = captured_string+'-'
            elif key in ['lshift','rshift','up','down','left','right','return']:
                pass
            else: 
                captured_string = captured_string+key
            # this next line formats the output. you can remove or modify as necessary
            captured_string=captured_string.capitalize()
        
        # *text_18* updates
        if t >= 0.0 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        
        # *text_19* updates
        if t >= 0.0 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        if text_19.status == STARTED:  # only update if drawing
            text_19.setText(captured_string, log=False)
        
        # *image_8* updates
        if t >= 0.0 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        
        # *polygon_5* updates
        if t >= 0.0 and polygon_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_5.tStart = t
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.setAutoDraw(True)
        
        # *bottom_line_5* updates
        if t >= 0.0 and bottom_line_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_5.tStart = t
            bottom_line_5.frameNStart = frameN  # exact frame index
            bottom_line_5.setAutoDraw(True)
        
        # *right_line_5* updates
        if t >= 0.0 and right_line_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_5.tStart = t
            right_line_5.frameNStart = frameN  # exact frame index
            right_line_5.setAutoDraw(True)
        
        # *left_line_5* updates
        if t >= 0.0 and left_line_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_5.tStart = t
            left_line_5.frameNStart = frameN  # exact frame index
            left_line_5.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question3"-------
    for thisComponent in question3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question3_correct_perspective', captured_string)
    # the Routine "question3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question4"-------
    t = 0
    question4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_21.alignHoriz ='left'
    text_21.alignVert = 'top'
    text_21.wrapWidth = 1.8
    text_21.height = .05
    
    
    text_20.setText(question4)
    image_9.setImage(this_recall_pic)
    # keep track of which components have finished
    question4Components = [text_20, text_21, image_9, polygon_6, bottom_line_6, right_line_6, left_line_6]
    for thisComponent in question4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question4"-------
    while continueRoutine:
        # get current time
        t = question4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if subject_response_finished:
            final_response=captured_string
            continueRoutine=False
        for key in event.getKeys():
            if key in ['escape']: 
                core.quit()
            elif key in ['delete','backspace']:
                captured_string = captured_string[:-1] 
            elif key in ['return']:
                thisExp.addData('recall', captured_string)
                subject_response_finished=True
            elif key in ['space']:
                captured_string = captured_string+' '
            elif key in ['dollar']:
                captured_string = captured_string + '$'
            elif key in ['exclamation']:
                captured_string = captured_string + '!'
            elif key in ['period']:
                captured_string = captured_string+'.'
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
            elif key in ['minus']:
                captured_string = captured_string+'-'
            elif key in ['lshift','rshift','up','down','left','right','return']:
                pass
            else: 
                captured_string = captured_string+key
            # this next line formats the output. you can remove or modify as necessary
            captured_string=captured_string.capitalize()
        
        # *text_20* updates
        if t >= 0.0 and text_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_20.tStart = t
            text_20.frameNStart = frameN  # exact frame index
            text_20.setAutoDraw(True)
        
        # *text_21* updates
        if t >= 0.0 and text_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_21.tStart = t
            text_21.frameNStart = frameN  # exact frame index
            text_21.setAutoDraw(True)
        if text_21.status == STARTED:  # only update if drawing
            text_21.setText(captured_string, log=False)
        
        # *image_9* updates
        if t >= 0.0 and image_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_9.tStart = t
            image_9.frameNStart = frameN  # exact frame index
            image_9.setAutoDraw(True)
        
        # *polygon_6* updates
        if t >= 0.0 and polygon_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_6.tStart = t
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.setAutoDraw(True)
        
        # *bottom_line_6* updates
        if t >= 0.0 and bottom_line_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_6.tStart = t
            bottom_line_6.frameNStart = frameN  # exact frame index
            bottom_line_6.setAutoDraw(True)
        
        # *right_line_6* updates
        if t >= 0.0 and right_line_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_6.tStart = t
            right_line_6.frameNStart = frameN  # exact frame index
            right_line_6.setAutoDraw(True)
        
        # *left_line_6* updates
        if t >= 0.0 and left_line_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_6.tStart = t
            left_line_6.frameNStart = frameN  # exact frame index
            left_line_6.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question4"-------
    for thisComponent in question4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question4_correct_perspective', captured_string)
    # the Routine "question4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_6'








# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
