#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Wed Feb 13 12:49:17 2019
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
expName = 'body_behavioural'  # from the Builder filename that created this script
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
    originPath='/Users/alexreblando/Documents/GitHub/ebs/body_behavioural_lastrun.py',
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

# Initialize components for Routine "storycount"
storycountClock = core.Clock()
text_38 = visual.TextStim(win=win, name='text_38',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_39 = visual.TextStim(win=win, name='text_39',
    text='Story     out of 8',
    font='Arial',
    pos=(0.03, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
timer = core.Clock()

# Initialize components for Routine "ask_to_assume"
ask_to_assumeClock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='PLEASE ASSUME THE ROLE OF:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


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
other_perspectives = []

for i in range(0,16):
    if order_perspectives[i] == 'Social':
        other_pespectives = other_perspectives.append('Location')
    else:
        other_pespectives = other_perspectives.append('Social')

thisExp.addData('order of stories', order_stories)
thisExp.addData('order of perspectives', order_perspectives)
thisExp.addData('participant 2 order - stories', run2)
thisExp.addData('participant 2 order  - schemas types', order_run2)













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

# Initialize components for Routine "intro_test"
intro_testClock = core.Clock()
text_37 = visual.TextStim(win=win, name='text_37',
    text='indicate the order in which the questions appeared:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "perspective_test"
perspective_testClock = core.Clock()

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

image_15 = visual.ImageStim(
    win=win, name='image_15',
    image='sin', mask=None,
    ori=0, pos=(0, -.85), size=(0.25, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

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
other_perspectives = []

for i in range(0,16):
    if order_perspectives[i] == 'Social':
        other_pespectives = other_perspectives.append('Location')
    else:
        other_pespectives = other_perspectives.append('Social')

thisExp.addData('order of stories', order_stories)
thisExp.addData('order of perspectives', order_perspectives)
thisExp.addData('participant 2 order - stories', run2)
thisExp.addData('participant 2 order  - schemas types', order_run2)













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

text_34 = visual.TextStim(win=win, name='text_34',
    text="Press '9' if you think this sentence is the beginning of a new 'part' of the story",
    font='Arial',
    pos=(.8, -.6), height=0.05, wrapWidth=.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_35 = visual.TextStim(win=win, name='text_35',
    text="Press '1' if you think this sentence is in the same 'part' of the story as the previous sentence. ",
    font='Arial',
    pos=(-.8, -.6), height=0.05, wrapWidth=.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "RECALL_BREAK"
RECALL_BREAKClock = core.Clock()
text_45 = visual.TextStim(win=win, name='text_45',
    text='RECALL TASK',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


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

# Initialize components for Routine "recallcount_2"
recallcount_2Clock = core.Clock()
text_41 = visual.TextStim(win=win, name='text_41',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='Recall     out of 8',
    font='Arial',
    pos=(0.02, 0), height=0.1, wrapWidth=None, ori=0, 
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

# Initialize components for Routine "questions_task"
questions_taskClock = core.Clock()
text_46 = visual.TextStim(win=win, name='text_46',
    text='QUESTIONS TASK\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


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

# Initialize components for Routine "questioncount"
questioncountClock = core.Clock()
text_43 = visual.TextStim(win=win, name='text_43',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_44 = visual.TextStim(win=win, name='text_44',
    text='Question Set     out of 8',
    font='Arial',
    pos=(-0.06, 0), height=0.1, wrapWidth=None, ori=0, 
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
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_3 = visual.Line(
    win=win, name='right_line_3',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_3 = visual.Line(
    win=win, name='left_line_3',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
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
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_4 = visual.Line(
    win=win, name='right_line_4',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_4 = visual.Line(
    win=win, name='left_line_4',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
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
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_5 = visual.Line(
    win=win, name='right_line_5',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_5 = visual.Line(
    win=win, name='left_line_5',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
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
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_6 = visual.Line(
    win=win, name='right_line_6',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_6 = visual.Line(
    win=win, name='left_line_6',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question5"
question5Clock = core.Clock()

text_25 = visual.TextStim(win=win, name='text_25',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_11 = visual.ImageStim(
    win=win, name='image_11',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_7 = visual.Line(
    win=win, name='polygon_7',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_7 = visual.Line(
    win=win, name='bottom_line_7',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_7 = visual.Line(
    win=win, name='right_line_7',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_7 = visual.Line(
    win=win, name='left_line_7',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question6"
question6Clock = core.Clock()

text_27 = visual.TextStim(win=win, name='text_27',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_12 = visual.ImageStim(
    win=win, name='image_12',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_8 = visual.Line(
    win=win, name='polygon_8',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_8 = visual.Line(
    win=win, name='bottom_line_8',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_8 = visual.Line(
    win=win, name='right_line_8',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_8 = visual.Line(
    win=win, name='left_line_8',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question7"
question7Clock = core.Clock()

text_29 = visual.TextStim(win=win, name='text_29',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_13 = visual.ImageStim(
    win=win, name='image_13',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_9 = visual.Line(
    win=win, name='polygon_9',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_9 = visual.Line(
    win=win, name='bottom_line_9',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_9 = visual.Line(
    win=win, name='right_line_9',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_9 = visual.Line(
    win=win, name='left_line_9',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question8"
question8Clock = core.Clock()

text_31 = visual.TextStim(win=win, name='text_31',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_14 = visual.ImageStim(
    win=win, name='image_14',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_10 = visual.Line(
    win=win, name='polygon_10',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_10 = visual.Line(
    win=win, name='bottom_line_10',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.3),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_10 = visual.Line(
    win=win, name='right_line_10',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_10 = visual.Line(
    win=win, name='left_line_10',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.2125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "end_of_questions"
end_of_questionsClock = core.Clock()
text_47 = visual.TextStim(win=win, name='text_47',
    text='END OF QUESTIONS\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "end_of_task"
end_of_taskClock = core.Clock()
text_36 = visual.TextStim(win=win, name='text_36',
    text='end of task',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count_8.xlsx'),
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
    
    # ------Prepare to start Routine "storycount"-------
    t = 0
    storycountClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_38.setText((count + 1))
    key_resp_8 = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    storycountComponents = [text_38, key_resp_8, text_39]
    for thisComponent in storycountComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "storycount"-------
    while continueRoutine:
        # get current time
        t = storycountClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_38* updates
        if t >= 0.0 and text_38.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_38.tStart = t
            text_38.frameNStart = frameN  # exact frame index
            text_38.setAutoDraw(True)
        
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
        
        # *text_39* updates
        if t >= 0.0 and text_39.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_39.tStart = t
            text_39.frameNStart = frameN  # exact frame index
            text_39.setAutoDraw(True)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in storycountComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "storycount"-------
    for thisComponent in storycountComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys=None
    trials.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials.addData('key_resp_8.rt', key_resp_8.rt)
    
    # the Routine "storycount" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ask_to_assume"-------
    t = 0
    ask_to_assumeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    ask_to_assumeComponents = [text_33, key_resp_5]
    for thisComponent in ask_to_assumeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ask_to_assume"-------
    while continueRoutine:
        # get current time
        t = ask_to_assumeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_33* updates
        if t >= 0.0 and text_33.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_33.tStart = t
            text_33.frameNStart = frameN  # exact frame index
            text_33.setAutoDraw(True)
        
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
        for key in event.getKeys():
            if key in ['q']: 
                trials.finished = 1
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ask_to_assumeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ask_to_assume"-------
    for thisComponent in ask_to_assumeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    
    # the Routine "ask_to_assume" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_7 = data.TrialHandler(nReps=5, method='sequential', 
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
            question1 = 'How does the person who is initiating the breakup feel before they do it?'
            question2 ='Why does the initiator want to break up?'
            question3 ='How does the person being broken up with respond?'
            question4 = 'Do the partners leave on good terms?'
            question5 = 'Does the person being broken up with expect that this is coming?'
            question6 = 'For how long has the initiator been wanting to break up?'
        if this_perspective == 'Restaurant Critic':
            display_pic = 'jobphotos/restaurant_critic.jpg'
            question1 = 'How is the restaurant decorated?'
            question2 ='What are the menus like?'
            question3 = 'What do the clients order?' 
            question4 = 'How do the clients like the food?'
            question5 = 'What meal is being served?'
            question6 = 'How old is the waiter?'
        if this_perspective == 'Airport Customer Experience Manager':
            display_pic = 'jobphotos/acem.jpg'
            question1 = 'When the travelers arrive at the airport, how much time do they have to go through the airport?'
            question2 ='What do the travelers have to do at security to comply with the security check?'
            question3 ='How do the travelers feel when they are  walking to the gates?'
            question4 ='Where does each traveler sit on the plane?' 
            question5 = 'Are the security guides friendly or rude?'
            question6 = 'Are the airport restrooms clean?'
        if this_perspective == 'Grocery Store Customer Experience Manager':
            display_pic = 'jobphotos/gscem.jpg'
            question1 = 'What is the grocery store like upon entering?'
            question2 ='What items do the clients pick out?'
            question3 ='How is the checkout line and how long do the clients wait in line?'
            question4 = 'How much are the groceries and what method of payment do the clients use?'
            question5 = 'How long does it take for the cashier to scan all of the customers’ groceries?'
            question6 = 'What type of grocery bags do the clients use?'
        if this_perspective == 'Dean of Academic Studies':
            display_pic ='jobphotos/dean.jpg'
            question1 = 'What is the lecture hall like?'
            question2 ='What class are the students  in and what is the day’s lecture about?'
            question3 ='What is something taught in lecture?'
            question4 = 'When is the next assessment in the class?'
            question5 = 'Are the students paying attention?'
            question6 = 'Are the desks comfortable?'
        if this_perspective == 'Wedding Planner':
            display_pic = 'jobphotos/weddingplanner.jpg'
            question1 = 'How does the person who proposed feel before proposing?'
            question2 ='What is the ring like?'
            question3 ='Does anyone help with the proposal?'
            question4 = 'Who witnessed the “yes”?'
            question5 = 'Is anyone taking pictures of the proposal?'
            question6 = 'How long does the proposal take?'
        if this_perspective == 'Business Reporter':
            display_pic = 'jobphotos/business_reporter.jpg'
            question1 = 'What industry are the business people in?'
            question2 = 'What is being negotiated and how much money is at stake?'
            question3 = 'What is the response to the proposed deal?'
            question4 =  'What comes about from the business proposal?'
            question5 = 'Is the deal fair?'
            question6 =  'How long does it take to make the deal?'
        if this_perspective == 'Matchmaker':
            display_pic = 'jobphotos/matchmaker.jpg'
            question1 = 'Who notices who first and why do they notice the other?' 
            question2 ='How does the couple start talking?'
            question3 ='Which of the people proposes going on an actual date and what do they propose?'
            question4 = 'Who leaves first and why do they have to go?'
            question5 = 'Is the couple going to get married?'
            question6 = 'Who shows more interest?'
        
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in perspectiveComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "perspective"-------
        for thisComponent in perspectiveComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "perspective" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "intro_test"-------
        t = 0
        intro_testClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_7 = event.BuilderKeyResponse()
        # keep track of which components have finished
        intro_testComponents = [text_37, key_resp_7]
        for thisComponent in intro_testComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "intro_test"-------
        while continueRoutine:
            # get current time
            t = intro_testClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_37* updates
            if t >= 0.0 and text_37.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_37.tStart = t
                text_37.frameNStart = frameN  # exact frame index
                text_37.setAutoDraw(True)
            
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intro_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intro_test"-------
        for thisComponent in intro_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys=None
        trials_7.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_7.addData('key_resp_7.rt', key_resp_7.rt)
        # the Routine "intro_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "perspective_test"-------
        t = 0
        perspective_testClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        from psychopy import visual, core, event
        
        event.clearEvents()
        Q = np.array([question1, question2, question3, question4, question5, question6])
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
        perspective_testComponents = [question1_2, question2_2, question3_2, question4_2, question5_2, question6_2, image_15]
        for thisComponent in perspective_testComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "perspective_test"-------
        while continueRoutine:
            # get current time
            t = perspective_testClock.getTime()
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
                trials_7.finished= True 
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
                trials_7.finished = True
                continueRoutine=False
            if checkCount == 4:
                this_image = 'bar5.jpeg'
            
            if checkCount == 1:
                this_image = 'bar2.png'
            if checkCount == 2: 
                this_image = 'bar3.jpeg'
            if checkCount == 3:
                this_image = 'bar4.png'
            
            # *image_15* updates
            if t >= 0.0 and image_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_15.tStart = t
                image_15.frameNStart = frameN  # exact frame index
                image_15.setAutoDraw(True)
            if image_15.status == STARTED:  # only update if drawing
                image_15.setImage(this_image, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in perspective_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "perspective_test"-------
        for thisComponent in perspective_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # the Routine "perspective_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5 repeats of 'trials_7'
    
    
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
        question1 = 'How does the person who is initiating the breakup feel before they do it?'
        question2 ='Why does the initiator want to break up?'
        question3 ='How does the person being broken up with respond?'
        question4 = 'Do the partners leave on good terms?'
        question5 = 'Does the person being broken up with expect that this is coming?'
        question6 = 'For how long has the initiator been wanting to break up?'
    if this_perspective == 'Restaurant Critic':
        display_pic = 'jobphotos/restaurant_critic.jpg'
        question1 = 'How is the restaurant decorated?'
        question2 ='What are the menus like?'
        question3 = 'What do the clients order?' 
        question4 = 'How do the clients like the food?'
        question5 = 'What meal is being served?'
        question6 = 'How old is the waiter?'
    if this_perspective == 'Airport Customer Experience Manager':
        display_pic = 'jobphotos/acem.jpg'
        question1 = 'When the travelers arrive at the airport, how much time do they have to go through the airport?'
        question2 ='What do the travelers have to do at security to comply with the security check?'
        question3 ='How do the travelers feel when they are  walking to the gates?'
        question4 ='Where does each traveler sit on the plane?' 
        question5 = 'Are the security guides friendly or rude?'
        question6 = 'Are the airport restrooms clean?'
    if this_perspective == 'Grocery Store Customer Experience Manager':
        display_pic = 'jobphotos/gscem.jpg'
        question1 = 'What is the grocery store like upon entering?'
        question2 ='What items do the clients pick out?'
        question3 ='How is the checkout line and how long do the clients wait in line?'
        question4 = 'How much are the groceries and what method of payment do the clients use?'
        question5 = 'How long does it take for the cashier to scan all of the customers’ groceries?'
        question6 = 'What type of grocery bags do the clients use?'
    if this_perspective == 'Dean of Academic Studies':
        display_pic ='jobphotos/dean.jpg'
        question1 = 'What is the lecture hall like?'
        question2 ='What class are the students  in and what is the day’s lecture about?'
        question3 ='What is something taught in lecture?'
        question4 = 'When is the next assessment in the class?'
        question5 = 'Are the students paying attention?'
        question6 = 'Are the desks comfortable?'
    if this_perspective == 'Wedding Planner':
        display_pic = 'jobphotos/weddingplanner.jpg'
        question1 = 'How does the person who proposed feel before proposing?'
        question2 ='What is the ring like?'
        question3 ='Does anyone help with the proposal?'
        question4 = 'Who witnessed the “yes”?'
        question5 = 'Is anyone taking pictures of the proposal?'
        question6 = 'How long does the proposal take?'
    if this_perspective == 'Business Reporter':
        display_pic = 'jobphotos/business_reporter.jpg'
        question1 = 'What industry are the business people in?'
        question2 = 'What is being negotiated and how much money is at stake?'
        question3 = 'What is the response to the proposed deal?'
        question4 =  'What comes about from the business proposal?'
        question5 = 'Is the deal fair?'
        question6 =  'How long does it take to make the deal?'
    if this_perspective == 'Matchmaker':
        display_pic = 'jobphotos/matchmaker.jpg'
        question1 = 'Who notices who first and why do they notice the other?' 
        question2 ='How does the couple start talking?'
        question3 ='Which of the people proposes going on an actual date and what do they propose?'
        question4 = 'Who leaves first and why do they have to go?'
        question5 = 'Is the couple going to get married?'
        question6 = 'Who shows more interest?'
    
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in perspectiveComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
        trialComponents = [text, story_presses, image_2, text_34, text_35]
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
            for key in event.getKeys():
                if key in ['q']: 
                    trials_2.finished = 1
                    continueRoutine = False
            
            # *text_34* updates
            if t >= 0.0 and text_34.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_34.tStart = t
                text_34.frameNStart = frameN  # exact frame index
                text_34.setAutoDraw(True)
            
            # *text_35* updates
            if t >= 0.0 and text_35.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_35.tStart = t
                text_35.frameNStart = frameN  # exact frame index
                text_35.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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


# ------Prepare to start Routine "RECALL_BREAK"-------
t = 0
RECALL_BREAKClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
story_time = timer.getTime()
thisExp.addData('story time', story_time)
# keep track of which components have finished
RECALL_BREAKComponents = [text_45, key_resp_6]
for thisComponent in RECALL_BREAKComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "RECALL_BREAK"-------
while continueRoutine:
    # get current time
    t = RECALL_BREAKClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_45* updates
    if t >= 0.0 and text_45.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_45.tStart = t
        text_45.frameNStart = frameN  # exact frame index
        text_45.setAutoDraw(True)
    
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
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RECALL_BREAKComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RECALL_BREAK"-------
for thisComponent in RECALL_BREAKComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()

# the Routine "RECALL_BREAK" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recall_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
    trialList=data.importConditions('count_8.xlsx'),
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
    
    # ------Prepare to start Routine "recallcount_2"-------
    t = 0
    recallcount_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_41.setText((count + 1))
    key_resp_10 = event.BuilderKeyResponse()
    # keep track of which components have finished
    recallcount_2Components = [text_41, key_resp_10, text_42]
    for thisComponent in recallcount_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "recallcount_2"-------
    while continueRoutine:
        # get current time
        t = recallcount_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_41* updates
        if t >= 0.0 and text_41.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_41.tStart = t
            text_41.frameNStart = frameN  # exact frame index
            text_41.setAutoDraw(True)
        
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
        
        # *text_42* updates
        if t >= 0.0 and text_42.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_42.tStart = t
            text_42.frameNStart = frameN  # exact frame index
            text_42.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallcount_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recallcount_2"-------
    for thisComponent in recallcount_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys=None
    trials_4.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        trials_4.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "recallcount_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recall_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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


# ------Prepare to start Routine "questions_task"-------
t = 0
questions_taskClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()
recall_time = timer.getTime()
thisExp.addData('recall time', recall_time)
# keep track of which components have finished
questions_taskComponents = [text_46, key_resp_12]
for thisComponent in questions_taskComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "questions_task"-------
while continueRoutine:
    # get current time
    t = questions_taskClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_46* updates
    if t >= 0.0 and text_46.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_46.tStart = t
        text_46.frameNStart = frameN  # exact frame index
        text_46.setAutoDraw(True)
    
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
    for thisComponent in questions_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "questions_task"-------
for thisComponent in questions_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys=None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()

# the Routine "questions_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questions_instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
    trials_5.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_5.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "questions_instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count_8.xlsx'),
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
    
    # ------Prepare to start Routine "questioncount"-------
    t = 0
    questioncountClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_43.setText((count + 1))
    key_resp_11 = event.BuilderKeyResponse()
    # keep track of which components have finished
    questioncountComponents = [text_43, key_resp_11, text_44]
    for thisComponent in questioncountComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "questioncount"-------
    while continueRoutine:
        # get current time
        t = questioncountClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_43* updates
        if t >= 0.0 and text_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_43.tStart = t
            text_43.frameNStart = frameN  # exact frame index
            text_43.setAutoDraw(True)
        
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
        
        # *text_44* updates
        if t >= 0.0 and text_44.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_44.tStart = t
            text_44.frameNStart = frameN  # exact frame index
            text_44.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questioncountComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questioncount"-------
    for thisComponent in questioncountComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys=None
    trials_6.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        trials_6.addData('key_resp_11.rt', key_resp_11.rt)
    # the Routine "questioncount" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_22* updates
        if t >= 0.0 and text_22.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_22.tStart = t
            text_22.frameNStart = frameN  # exact frame index
            text_22.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in story_imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "story_image"-------
    for thisComponent in story_imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "story_image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question1"-------
    t = 0
    question1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    event.clearEvents()
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
    
    this_perspective = storyDict.get(order_stories[count], {}).get(order_perspectives[count])
    other_perspective = storyDict.get(order_stories[count], {}).get(other_perspectives[count])
    #set questions
    if value < .5:
        question_order = 'primed first'
        this_perspective = storyDict.get(order_stories[count], {}).get(order_perspectives[count])
        if this_perspective == 'Couples Therapist':
            pic1 = 'jobphotos/couples.jpg'
            question1 = 'How does the person who is initiating the breakup feel before they do it?'
            question2 ='Why does the initiator want to break up?'
            question3 ='How does the person being broken up with respond?'
            question4 = 'Do the partners leave on good terms?'
        if this_perspective == 'Restaurant Critic':
            pic1 = 'jobphotos/restaurant_critic.jpg'
            question1 = 'How is the restaurant decorated?'
            question2 ='What are the menus like?'
            question3 = 'What do the clients order?' 
            question4 = 'How do the clients like the food?'
        if this_perspective == 'Airport Customer Experience Manager':
            pic1 = 'jobphotos/acem.jpg'
            question1 = 'When the clients arrive at the airport, how much time do they have to go through?'
            question2 ='What do the clients have do at security to comply with the security check?'
            question3 ='How do the clients feel when they are  walking to the gates?'
            question4 ='Where does each client sit on the plane?' 
        if this_perspective == 'Grocery Store Customer Experience Manager':
            pic1 = 'jobphotos/gscem.jpg'
            question1 = 'What is the grocery store like upon entering?'
            question2 ='What items do the clients pick out?'
            question3 ='How is the checkout line and how long do the clients wait in line?'
            question4 = 'How much are the groceries and what method of payment do the clients use?'
        if this_perspective == 'Dean of Academic Studies':
            pic1 ='jobphotos/dean.jpg'
            question1 = 'What is the lecture hall like?'
            question2 ='What class are the students  in and what is the day’s lecture about?'
            question3 ='What is something taught in lecture?'
            question4 = 'When is the next assessment in the class?'
        if this_perspective == 'Wedding Planner':
            pic1 = 'jobphotos/weddingplanner.jpg'
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
            pic1 = 'jobphotos/matchmaker.jpg'
            question1 = 'Who notices who first and why do they notice the other?' 
            question2 ='How does the couple start talking?'
            question3 ='Which of the people proposes going on an actual date and what do they propose?'
            question4 = 'Who leaves first and why do they have to go?'
    
        if other_perspective == 'Couples Therapist':
            pic2 = 'jobphotos/couples.jpg'
            question5 = 'How does the person who is initiating the breakup feel before they do it?'
            question6 ='Why does the initiator want to break up?'
            question7 ='How does the person being broken up with respond?'
            question8 = 'Do the partners leave on good terms?'
        if other_perspective == 'Restaurant Critic':
            pic2 = 'jobphotos/restaurant_critic.jpg'
            question5 = 'How is the restaurant decorated?'
            question6 ='What are the menus like?'
            question7 = 'What do the clients order?'
            question8 = 'How do the clients like the food?'
        if other_perspective == 'Airport Customer Experience Manager':
            pic2 = 'jobphotos/acem.jpg'
            question5 = 'When the clients arrive at the airport, how much time do they have to go through?'
            question6 ='What do the clients have do at security to comply with the security check?'
            question7 ='How do the clients feel when they are  walking to the gates?'
            question8 ='Where does each client sit on the plane?' 
        if other_perspective == 'Grocery Store Customer Experience Manager':
            pic2 = 'jobphotos/gscem.jpg'
            question5 = 'What is the grocery store like upon entering?'
            question6 ='What items do the clients pick out?'
            question7 ='How is the checkout line and how long do the clients wait in line?'
            question8 = 'How much are the groceries and what method of payment do the clients use?'
        if other_perspective == 'Dean of Academic Studies':
            pic2 ='jobphotos/dean.jpg'
            question5 = 'What is the lecture hall like?'
            question6 ='What class are the students  in and what is the day’s lecture about?'
            question7 ='What is something taught in lecture?'
            question8 = 'When is the next assessment in the class?'
        if other_perspective == 'Wedding Planner':
            pic2 = 'jobphotos/weddingplanner.jpg'
            question5 = 'How does the person who proposed feel before proposing?'
            question6 ='What is the ring like?'
            question7 ='Does anyone help with the proposal?'
            question8 = 'Who witnessed the “yes”?'
        if other_perspective == 'Business Reporter':
            pic2 = 'jobphotos/business_reporter.jpg'
            question5 = 'What industry are the business people in?'
            question6 = 'What is being negotiated and how much money is at stake?'
            question7 = 'What is the response to the proposed deal?'
            question8 =  'What comes about from the business proposal?'
        if other_perspective == 'Matchmaker':
            pic2 = 'jobphotos/matchmaker.jpg'
            question5 = 'Who notices who first and why do they notice the other?'
            question6 ='How does the couple start talking?'
            question7 ='Which of the people proposes going on an actual date and what do they propose?'
            question8 = 'Who leaves first and why do they have to go?'
    else:
        question_order = 'non-primed first'
        if other_perspective == 'Couples Therapist':
            pic1 = 'jobphotos/couples.jpg'
            question1 = 'How does the person who is initiating the breakup feel before they do it?'
            question2 ='Why does the initiator want to break up?'
            question3 ='How does the person being broken up with respond?'
            question4 = 'Do the partners leave on good terms?'
        if other_perspective == 'Restaurant Critic':
            pic1 = 'jobphotos/restaurant_critic.jpg'
            question1 = 'How is the restaurant decorated?'
            question2 ='What are the menus like?'
            question3 = 'What do the clients order?'
            question4 = 'How do the clients like the food?'
        if other_perspective == 'Airport Customer Experience Manager':
            pic1 = 'jobphotos/acem.jpg'
            question1 = 'When the clients arrive at the airport, how much time do they have to go through?'
            question2 ='What do the clients have do at security to comply with the security check?'
            question3 ='How do the clients feel when they are  walking to the gates?'
            question4 ='Where does each client sit on the plane?' 
        if other_perspective == 'Grocery Store Customer Experience Manager':
            pic1 = 'jobphotos/gscem.jpg'
            question1 = 'What is the grocery store like upon entering?'
            question2 ='What items do the clients pick out?'
            question3 ='How is the checkout line and how long do the clients wait in line?'
            question4 = 'How much are the groceries and what method of payment do the clients use?'
        if other_perspective == 'Dean of Academic Studies':
            pic1 ='jobphotos/dean.jpg'
            question1 = 'What is the lecture hall like?'
            question2 ='What class are the students  in and what is the day’s lecture about?'
            question3 ='What is something taught in lecture?'
            question4 = 'When is the next assessment in the class?'
        if other_perspective == 'Wedding Planner':
            pic1 = 'jobphotos/weddingplanner.jpg'
            question1 = 'How does the person who proposed feel before proposing?'
            question2 ='What is the ring like?'
            question3 ='Does anyone help with the proposal?'
            question4 = 'Who witnessed the “yes”?'
        if other_perspective == 'Business Reporter':
            pic1 = 'jobphotos/business_reporter.jpg'
            question1 = 'What industry are the business people in?'
            question2 = 'What is being negotiated and how much money is at stake?'
            question3 = 'What is the response to the proposed deal?'
            question4 =  'What comes about from the business proposal?'
        if other_perspective == 'Matchmaker':
            pic1 = 'jobphotos/matchmaker.jpg'
            question1 = 'Who notices who first and why do they notice the other?'
            question2 ='How does the couple start talking?'
            question3 ='Which of the people proposes going on an actual date and what do they propose?'
            question4 = 'Who leaves first and why do they have to go?'
    
        if this_perspective == 'Couples Therapist':
            pic2 = 'jobphotos/couples.jpg'
            question5 = 'How does the person who is initiating the breakup feel before they do it?'
            question6 ='Why does the initiator want to break up?'
            question7 ='How does the person being broken up with respond?'
            question8 = 'Do the partners leave on good terms?'
        if this_perspective == 'Restaurant Critic':
            pic2 = 'jobphotos/restaurant_critic.jpg'
            question5 = 'How is the restaurant decorated?'
            question6 ='What are the menus like?'
            question7 = 'What do the clients order?'
            question8 = 'How do the clients like the food?'
        if this_perspective == 'Airport Customer Experience Manager':
            pic2 = 'jobphotos/acem.jpg'
            question5 = 'When the clients arrive at the airport, how much time do they have to go through?'
            question6 ='What do the clients have do at security to comply with the security check?'
            question7 ='How do the clients feel when they are  walking to the gates?'
            question8 ='Where does each client sit on the plane?' 
        if this_perspective == 'Grocery Store Customer Experience Manager':
            pic2 = 'jobphotos/gscem.jpg'
            question5 = 'What is the grocery store like upon entering?'
            question6 ='What items do the clients pick out?'
            question7 ='How is the checkout line and how long do the clients wait in line?'
            question8 = 'How much are the groceries and what method of payment do the clients use?'
        if this_perspective == 'Dean of Academic Studies':
            pic2 ='jobphotos/dean.jpg'
            question5 = 'What is the lecture hall like?'
            question6 ='What class are the students  in and what is the day’s lecture about?'
            question7 ='What is something taught in lecture?'
            question8 = 'When is the next assessment in the class?'
        if this_perspective == 'Wedding Planner':
            pic2 = 'jobphotos/weddingplanner.jpg'
            question5 = 'How does the person who proposed feel before proposing?'
            question6 ='What is the ring like?'
            question7 ='Does anyone help with the proposal?'
            question8 = 'Who witnessed the “yes”?'
        if this_perspective == 'Business Reporter':
            pic2 = 'jobphotos/business_reporter.jpg'
            question5 = 'What industry are the business people in?'
            question6 = 'What is being negotiated and how much money is at stake?'
            question7 = 'What is the response to the proposed deal?'
            question8 =  'What comes about from the business proposal?'
        if this_perspective == 'Matchmaker':
            pic2 = 'jobphotos/matchmaker.jpg'
            question5 = 'Who notices who first and why do they notice the other?'
            question6 ='How does the couple start talking?'
            question7 ='Which of the people proposes going on an actual date and what do they propose?'
            question8 = 'Who leaves first and why do they have to go?'
    
    
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question1"-------
    for thisComponent in question1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question1_answer', captured_string)
    thisExp.addData('order of question', question_order)
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question2"-------
    for thisComponent in question2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question2_answer', captured_string)
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question3"-------
    for thisComponent in question3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question3_answer', captured_string)
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question4"-------
    for thisComponent in question4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question4_answer', captured_string)
    # the Routine "question4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question5"-------
    t = 0
    question5Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_26.alignHoriz ='left'
    text_26.alignVert = 'top'
    text_26.wrapWidth = 1.8
    text_26.height = .05
    
    
    text_25.setText(question5)
    image_11.setImage(this_recall_pic)
    # keep track of which components have finished
    question5Components = [text_25, text_26, image_11, polygon_7, bottom_line_7, right_line_7, left_line_7]
    for thisComponent in question5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question5"-------
    while continueRoutine:
        # get current time
        t = question5Clock.getTime()
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
        
        # *text_25* updates
        if t >= 0.0 and text_25.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_25.tStart = t
            text_25.frameNStart = frameN  # exact frame index
            text_25.setAutoDraw(True)
        
        # *text_26* updates
        if t >= 0.0 and text_26.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_26.tStart = t
            text_26.frameNStart = frameN  # exact frame index
            text_26.setAutoDraw(True)
        if text_26.status == STARTED:  # only update if drawing
            text_26.setText(captured_string, log=False)
        
        # *image_11* updates
        if t >= 0.0 and image_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_11.tStart = t
            image_11.frameNStart = frameN  # exact frame index
            image_11.setAutoDraw(True)
        
        # *polygon_7* updates
        if t >= 0.0 and polygon_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_7.tStart = t
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.setAutoDraw(True)
        
        # *bottom_line_7* updates
        if t >= 0.0 and bottom_line_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_7.tStart = t
            bottom_line_7.frameNStart = frameN  # exact frame index
            bottom_line_7.setAutoDraw(True)
        
        # *right_line_7* updates
        if t >= 0.0 and right_line_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_7.tStart = t
            right_line_7.frameNStart = frameN  # exact frame index
            right_line_7.setAutoDraw(True)
        
        # *left_line_7* updates
        if t >= 0.0 and left_line_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_7.tStart = t
            left_line_7.frameNStart = frameN  # exact frame index
            left_line_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question5"-------
    for thisComponent in question5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question5_answer', captured_string)
    # the Routine "question5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question6"-------
    t = 0
    question6Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_28.alignHoriz ='left'
    text_28.alignVert = 'top'
    text_28.wrapWidth = 1.8
    text_28.height = .05
    
    
    text_27.setText(question6)
    image_12.setImage(this_recall_pic)
    # keep track of which components have finished
    question6Components = [text_27, text_28, image_12, polygon_8, bottom_line_8, right_line_8, left_line_8]
    for thisComponent in question6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question6"-------
    while continueRoutine:
        # get current time
        t = question6Clock.getTime()
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
        
        # *text_27* updates
        if t >= 0.0 and text_27.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_27.tStart = t
            text_27.frameNStart = frameN  # exact frame index
            text_27.setAutoDraw(True)
        
        # *text_28* updates
        if t >= 0.0 and text_28.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_28.tStart = t
            text_28.frameNStart = frameN  # exact frame index
            text_28.setAutoDraw(True)
        if text_28.status == STARTED:  # only update if drawing
            text_28.setText(captured_string, log=False)
        
        # *image_12* updates
        if t >= 0.0 and image_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_12.tStart = t
            image_12.frameNStart = frameN  # exact frame index
            image_12.setAutoDraw(True)
        
        # *polygon_8* updates
        if t >= 0.0 and polygon_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_8.tStart = t
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.setAutoDraw(True)
        
        # *bottom_line_8* updates
        if t >= 0.0 and bottom_line_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_8.tStart = t
            bottom_line_8.frameNStart = frameN  # exact frame index
            bottom_line_8.setAutoDraw(True)
        
        # *right_line_8* updates
        if t >= 0.0 and right_line_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_8.tStart = t
            right_line_8.frameNStart = frameN  # exact frame index
            right_line_8.setAutoDraw(True)
        
        # *left_line_8* updates
        if t >= 0.0 and left_line_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_8.tStart = t
            left_line_8.frameNStart = frameN  # exact frame index
            left_line_8.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question6"-------
    for thisComponent in question6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question6_answer', captured_string)
    # the Routine "question6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question7"-------
    t = 0
    question7Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_30.alignHoriz ='left'
    text_30.alignVert = 'top'
    text_30.wrapWidth = 1.8
    text_30.height = .05
    
    
    text_29.setText(question7
)
    image_13.setImage(this_recall_pic)
    # keep track of which components have finished
    question7Components = [text_29, text_30, image_13, polygon_9, bottom_line_9, right_line_9, left_line_9]
    for thisComponent in question7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question7"-------
    while continueRoutine:
        # get current time
        t = question7Clock.getTime()
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
        
        # *text_29* updates
        if t >= 0.0 and text_29.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_29.tStart = t
            text_29.frameNStart = frameN  # exact frame index
            text_29.setAutoDraw(True)
        
        # *text_30* updates
        if t >= 0.0 and text_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_30.tStart = t
            text_30.frameNStart = frameN  # exact frame index
            text_30.setAutoDraw(True)
        if text_30.status == STARTED:  # only update if drawing
            text_30.setText(captured_string, log=False)
        
        # *image_13* updates
        if t >= 0.0 and image_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_13.tStart = t
            image_13.frameNStart = frameN  # exact frame index
            image_13.setAutoDraw(True)
        
        # *polygon_9* updates
        if t >= 0.0 and polygon_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_9.tStart = t
            polygon_9.frameNStart = frameN  # exact frame index
            polygon_9.setAutoDraw(True)
        
        # *bottom_line_9* updates
        if t >= 0.0 and bottom_line_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_9.tStart = t
            bottom_line_9.frameNStart = frameN  # exact frame index
            bottom_line_9.setAutoDraw(True)
        
        # *right_line_9* updates
        if t >= 0.0 and right_line_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_9.tStart = t
            right_line_9.frameNStart = frameN  # exact frame index
            right_line_9.setAutoDraw(True)
        
        # *left_line_9* updates
        if t >= 0.0 and left_line_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_9.tStart = t
            left_line_9.frameNStart = frameN  # exact frame index
            left_line_9.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question7"-------
    for thisComponent in question7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question7_answer', captured_string)
    # the Routine "question7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question8"-------
    t = 0
    question8Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cursorCounter=0
    cursorVariable='|'
    captured_string=''
    subject_response_finished=False
    shift_flag = False
    text_32.alignHoriz ='left'
    text_32.alignVert = 'top'
    text_32.wrapWidth = 1.8
    text_32.height = .05
    
    
    text_31.setText(question8)
    image_14.setImage(this_recall_pic)
    # keep track of which components have finished
    question8Components = [text_31, text_32, image_14, polygon_10, bottom_line_10, right_line_10, left_line_10]
    for thisComponent in question8Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "question8"-------
    while continueRoutine:
        # get current time
        t = question8Clock.getTime()
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
        
        # *text_31* updates
        if t >= 0.0 and text_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_31.tStart = t
            text_31.frameNStart = frameN  # exact frame index
            text_31.setAutoDraw(True)
        
        # *text_32* updates
        if t >= 0.0 and text_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_32.tStart = t
            text_32.frameNStart = frameN  # exact frame index
            text_32.setAutoDraw(True)
        if text_32.status == STARTED:  # only update if drawing
            text_32.setText(captured_string, log=False)
        
        # *image_14* updates
        if t >= 0.0 and image_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_14.tStart = t
            image_14.frameNStart = frameN  # exact frame index
            image_14.setAutoDraw(True)
        
        # *polygon_10* updates
        if t >= 0.0 and polygon_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_10.tStart = t
            polygon_10.frameNStart = frameN  # exact frame index
            polygon_10.setAutoDraw(True)
        
        # *bottom_line_10* updates
        if t >= 0.0 and bottom_line_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottom_line_10.tStart = t
            bottom_line_10.frameNStart = frameN  # exact frame index
            bottom_line_10.setAutoDraw(True)
        
        # *right_line_10* updates
        if t >= 0.0 and right_line_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_line_10.tStart = t
            right_line_10.frameNStart = frameN  # exact frame index
            right_line_10.setAutoDraw(True)
        
        # *left_line_10* updates
        if t >= 0.0 and left_line_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_line_10.tStart = t
            left_line_10.frameNStart = frameN  # exact frame index
            left_line_10.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question8"-------
    for thisComponent in question8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('question8_answer', captured_string)
    # the Routine "question8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_6'


# ------Prepare to start Routine "end_of_questions"-------
t = 0
end_of_questionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()
questions_time = timer.getTime()
thisExp.addData('questions time', questions_time)
# keep track of which components have finished
end_of_questionsComponents = [text_47, key_resp_13]
for thisComponent in end_of_questionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_of_questions"-------
while continueRoutine:
    # get current time
    t = end_of_questionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_47* updates
    if t >= 0.0 and text_47.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_47.tStart = t
        text_47.frameNStart = frameN  # exact frame index
        text_47.setAutoDraw(True)
    
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
    for thisComponent in end_of_questionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_of_questions"-------
for thisComponent in end_of_questionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys=None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()

# the Routine "end_of_questions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "end_of_task"-------
    t = 0
    end_of_taskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    end_of_taskComponents = [text_36]
    for thisComponent in end_of_taskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "end_of_task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_of_taskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_36* updates
        if t >= 0.0 and text_36.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_36.tStart = t
            text_36.frameNStart = frameN  # exact frame index
            text_36.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_36.status == STARTED and t >= frameRemains:
            text_36.setAutoDraw(False)
        for key in event.getKeys():
            if key in ['escape']: 
                core.quit()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_of_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_of_task"-------
    for thisComponent in end_of_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials_8'






















# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
