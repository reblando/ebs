#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.1),
    on Wed Feb  5 11:48:08 2020
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
expName = 'body_behavioural'  # from the Builder filename that created this script
expInfo = {'participant': '', 'sA': '0', 'sB': '1', 'lA': '0', 'lB': '1', 'block_struct': '1', 'random_seed': '2'}
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
    originPath='/Users/alexreblando/Documents/GitHub/ebs/fMRI experiment/psychopy code/short_answer.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
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

# Initialize components for Routine "startup"
startupClock = core.Clock()
import numpy as np
import random 

timer = core.Clock()

#iterating through the question sets
set_count = 0

#basic matrix of all stories
story_matrix = np.zeros(shape = [4, 4], dtype = int)

s_order = np.array([10, 20, 30, 40], dtype = int)

l_order = np.array([1,2,3,4], dtype = int)

story_matrix[0] += s_order[0]
story_matrix[1] += s_order[1]
story_matrix[2] += s_order[2]
story_matrix[3] += s_order[3]

story_matrix[:,0] += l_order[0]
story_matrix[:,1] += l_order[1]
story_matrix[:, 2] += l_order[2]
story_matrix[:, 3] += l_order[3]

#constructing the action matrix based on the inputted social and location perspectives
action_matrix = np.zeros(shape = [4, 4], dtype = int)
these_social_ps = [int(expInfo['sA']), int(expInfo['sB'])] 
these_location_ps = [int(expInfo['lA']), int(expInfo['lB'])]

for i in range(2):
    action_matrix[these_social_ps[i],:] += 1
    action_matrix[:,these_location_ps[i]] += 2
    
action_matrix[action_matrix == 0] = 4

#block molds
block_mold1 = np.array([[0, 1, 0, 1], [1,0,1,0],[0,1,0,1], [1,0,1,0]])
block_mold2 = np.array([[1,0,1,0],[0,1,0,1], [1,0,1,0],[0, 1, 0, 1]])

#selecting a mold for the first half of the presented stories

if int(expInfo['block_struct']) == 0:
    action_matrix_block1 = np.multiply(action_matrix, block_mold1)
    action_matrix_block2 = np.multiply(action_matrix, block_mold2)
    story_matrix_block1 = np.multiply(story_matrix, block_mold1)
    story_matrix_block2 = np.multiply(story_matrix, block_mold2)
else:
    action_matrix_block1 = np.multiply(action_matrix, block_mold2)
    action_matrix_block2 = np.multiply(action_matrix, block_mold1)
    story_matrix_block1 = np.multiply(story_matrix, block_mold2)
    story_matrix_block2 = np.multiply(story_matrix, block_mold1)

#shuffling the story and action lists
randperm1 = np.random.RandomState(seed=int(expInfo['random_seed'])).permutation(8)
randperm2 = np.random.RandomState(seed= (int(expInfo['random_seed']) + 1)).permutation(8)

#block1
#turning matrices into lists and removing zeros
action_list_block1 = list(action_matrix_block1.flatten())
action_list_block1 = np.asarray([x for x in action_list_block1 if x != 0])
story_list_block1 = list(story_matrix_block1.flatten())
story_list_block1 = np.asarray([x for x in story_list_block1 if x != 0])
#shuffling
action_list_block1 = action_list_block1[randperm1]
story_list_block1 = story_list_block1[randperm1]
#saving data
thisExp.addData('story_list_block1', story_list_block1)
thisExp.addData('action_list_block1', action_list_block1)
#printing
print(story_list_block1)

#block2
#turning matrices into lists and removing zeros
action_list_block2 = list(action_matrix_block2.flatten())
action_list_block2 = np.asarray([x for x in action_list_block2 if x != 0])
story_list_block2 = list(story_matrix_block2.flatten())
story_list_block2 = np.asarray([x for x in story_list_block2 if x != 0])
#shuffling
action_list_block2 = action_list_block2[randperm2]
story_list_block2 = story_list_block2[randperm2]
#saving data
thisExp.addData('story_list_block2', story_list_block2)
thisExp.addData('action_list_block2', action_list_block2)
#printing
print(story_list_block2)

#concatenating the story and action lists
all_stories = np.concatenate((story_list_block1,story_list_block2), axis = None)
all_actions = np.concatenate((action_list_block1,action_list_block2), axis = None)

print(all_stories)
print(all_actions)



#dictionary for all the stories and their values
storyDict = {11: {'name':'Restaurant Breakup', 1: 'Couples Therapist', 2:'Restaurant Critic', 'pic':'storypics/11_storypic.jpg', 'storyFile': 'audio_excel_sheets/11_audio.xlsx'},
             12: {'name':'Airport Breakup', 1: 'Couples Therapist', 2:'Airport Customer Experience Manager', 'pic':'storypics/12_storypic.jpg', 'storyFile': 'audio_excel_sheets/12_audio.xlsx'},
             13: {'name':'Grocery Shopping- Break up', 1:'Couples Therapist', 2: 'Grocery Store Customer Experience Manager', 'pic':'storypics/13_storypic.jpg', 'storyFile': 'audio_excel_sheets/13_audio.xlsx'},
             14: {'name':'Attending a Lecture-Breakup', 1:'Couples Therapist', 2: 'Dean of Academic Studies', 'pic':'storypics/14_storypic.jpg', 'storyFile': 'audio_excel_sheets/14_audio.xlsx'},
             21: {'name':'Restaurant Proposal', 1: 'Wedding Planner', 2: 'Restaurant Critic', 'pic':'storypics/21_storypic.jpg', 'storyFile': 'audio_excel_sheets/21_audio.xlsx'},
             22: {'name':'Airport Proposal', 1: 'Wedding Planner', 2:'Airport Customer Experience Manager', 'pic':'storypics/22_storypic.jpg', 'storyFile': 'audio_excel_sheets/22_audio.xlsx'},
             23: {'name':'Grocery Shopping- Proposal', 1: 'Wedding Planner', 2:'Grocery Store Customer Experience Manager', 'pic':'storypics/23_storypic.jpg', 'storyFile': 'audio_excel_sheets/23_audio.xlsx'},
             24: {'name':'Attending a Lecture-Proposal', 1: 'Wedding Planner', 2: 'Dean of Academic Studies', 'pic':'storypics/24_storypic.jpg', 'storyFile': 'audio_excel_sheets/24_audio.xlsx'},
             31: {'name':'Restaurant Business Deal', 1:'Business Reporter', 2:'Restaurant Critic', 'pic':'storypics/31_storypic.jpg', 'storyFile': 'audio_excel_sheets/31_audio.xlsx'},
             32: {'name':'Airport Business Deal', 1:'Business Reporter', 2:'Airport Customer Experience Manager', 'pic':'storypics/32_storypic.jpg', 'storyFile': 'audio_excel_sheets/32_audio.xlsx'},
             33: {'name':'Grocery Shopping- Business Deal', 1:'Business Reporter', 2:'Grocery Store Customer Experience Manager', 'pic':'storypics/33_storypic.jpg', 'storyFile': 'audio_excel_sheets/33_audio.xlsx'},
             34: {'name':'Attending a Lecture-Business Deal', 1:'Business Reporter', 2:'Dean of Academic Studies', 'pic':'storypics/34_storypic.jpg', 'storyFile': 'audio_excel_sheets/34_audio.xlsx'},
             41: {'name':'Restaurant Meet Cute', 1: 'Matchmaker', 2:'Restaurant Critic', 'pic':'storypics/41_storypic.jpg', 'storyFile': 'audio_excel_sheets/41_audio.xlsx'},
             42: {'name':'Airport Meet Cute', 1: 'Matchmaker', 2:'Airport Customer Experience Manager', 'pic':'storypics/42_storypic.jpg', 'storyFile': 'audio_excel_sheets/42_audio.xlsx'},
             43: {'name':'Grocery Shopping- Meet Cute', 1:'Matchmaker', 2: 'Grocery Store Customer Experience Manager', 'pic':'storypics/43_storypic.jpg', 'storyFile': 'audio_excel_sheets/43_audio.xlsx'},
             44: {'name':'Attending a Lecture-Meet Cute', 1:'Matchmaker', 2: 'Dean of Academic Studies', 'pic':'storypics/44_storypic.jpg', 'storyFile': 'audio_excel_sheets/44_audio.xlsx'}}


# Initialize components for Routine "questions_instructions2"
questions_instructions2Clock = core.Clock()
key_resp_3 = keyboard.Keyboard()
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

# Initialize components for Routine "check_played_story"
check_played_storyClock = core.Clock()

# Initialize components for Routine "questioncount"
questioncountClock = core.Clock()
text_43 = visual.TextStim(win=win, name='text_43',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_11 = keyboard.Keyboard()
text_44 = visual.TextStim(win=win, name='text_44',
    text='Question Set     out of 12',
    font='Arial',
    pos=(-0.06, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "story_image"
story_imageClock = core.Clock()
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_4 = keyboard.Keyboard()
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
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_3 = visual.Line(
    win=win, name='polygon_3',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_3 = visual.Line(
    win=win, name='bottom_line_3',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_3 = visual.Line(
    win=win, name='right_line_3',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_3 = visual.Line(
    win=win, name='left_line_3',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question2"
question2Clock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_4 = visual.Line(
    win=win, name='polygon_4',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_4 = visual.Line(
    win=win, name='bottom_line_4',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_4 = visual.Line(
    win=win, name='right_line_4',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_4 = visual.Line(
    win=win, name='left_line_4',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question3"
question3Clock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_5 = visual.Line(
    win=win, name='polygon_5',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_5 = visual.Line(
    win=win, name='bottom_line_5',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_5 = visual.Line(
    win=win, name='right_line_5',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_5 = visual.Line(
    win=win, name='left_line_5',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question4"
question4Clock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_6 = visual.Line(
    win=win, name='polygon_6',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_6 = visual.Line(
    win=win, name='bottom_line_6',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_6 = visual.Line(
    win=win, name='right_line_6',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_6 = visual.Line(
    win=win, name='left_line_6',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question5"
question5Clock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_7 = visual.Line(
    win=win, name='polygon_7',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_7 = visual.Line(
    win=win, name='bottom_line_7',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_7 = visual.Line(
    win=win, name='right_line_7',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_7 = visual.Line(
    win=win, name='left_line_7',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question6"
question6Clock = core.Clock()
text_27 = visual.TextStim(win=win, name='text_27',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_8 = visual.Line(
    win=win, name='polygon_8',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_8 = visual.Line(
    win=win, name='bottom_line_8',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_8 = visual.Line(
    win=win, name='right_line_8',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_8 = visual.Line(
    win=win, name='left_line_8',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question7"
question7Clock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_9 = visual.Line(
    win=win, name='polygon_9',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_9 = visual.Line(
    win=win, name='bottom_line_9',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_9 = visual.Line(
    win=win, name='right_line_9',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_9 = visual.Line(
    win=win, name='left_line_9',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "question8"
question8Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='default text',
    font='Arial',
    pos=[0, -.2], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='default text',
    font='Arial',
    pos=[-.9, -0.55], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_10 = visual.Line(
    win=win, name='polygon_10',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.525),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_10 = visual.Line(
    win=win, name='bottom_line_10',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.7),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_10 = visual.Line(
    win=win, name='right_line_10',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_10 = visual.Line(
    win=win, name='left_line_10',
    start=(-(.175, 1)[0]/2.0, 0), end=(+(.175, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.6125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "end_of_task"
end_of_taskClock = core.Clock()
text_36 = visual.TextStim(win=win, name='text_36',
    text='End of task',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "startup"-------
# update component parameters for each repeat
# keep track of which components have finished
startupComponents = []
for thisComponent in startupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "startup"-------
while continueRoutine:
    # get current time
    t = startupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startupClock)
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
    for thisComponent in startupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startup"-------
for thisComponent in startupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "startup" was not non-slip safe, so reset the non-slip timer
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
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    text_13.setText(instructText)
    # keep track of which components have finished
    questions_instructions2Components = [key_resp_3, text_13, text_23]
    for thisComponent in questions_instructions2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questions_instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "questions_instructions2"-------
    while continueRoutine:
        # get current time
        t = questions_instructions2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questions_instructions2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        key_resp_3.keys = None
    trials_5.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_5.addData('key_resp_3.rt', key_resp_3.rt)
    trials_5.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials_5.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    trials_5.addData('text_13.started', text_13.tStartRefresh)
    trials_5.addData('text_13.stopped', text_13.tStopRefresh)
    trials_5.addData('text_23.started', text_23.tStartRefresh)
    trials_5.addData('text_23.stopped', text_23.tStopRefresh)
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
    
    # ------Prepare to start Routine "check_played_story"-------
    # update component parameters for each repeat
    if all_actions[count] == 3:
        played_story = 0
    else:
        played_story = 1
    # keep track of which components have finished
    check_played_storyComponents = []
    for thisComponent in check_played_storyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    check_played_storyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "check_played_story"-------
    while continueRoutine:
        # get current time
        t = check_played_storyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=check_played_storyClock)
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
        for thisComponent in check_played_storyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "check_played_story"-------
    for thisComponent in check_played_storyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "check_played_story" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=played_story, method='sequential', 
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
        
        # ------Prepare to start Routine "questioncount"-------
        # update component parameters for each repeat
        set_count += 1
        text_43.setText((set_count))
        key_resp_11.keys = []
        key_resp_11.rt = []
        # keep track of which components have finished
        questioncountComponents = [text_43, key_resp_11, text_44]
        for thisComponent in questioncountComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        questioncountClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "questioncount"-------
        while continueRoutine:
            # get current time
            t = questioncountClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=questioncountClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_43* updates
            if text_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_43.frameNStart = frameN  # exact frame index
                text_43.tStart = t  # local t and not account for scr refresh
                text_43.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
                text_43.setAutoDraw(True)
            
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
            
            # *text_44* updates
            if text_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_44.frameNStart = frameN  # exact frame index
                text_44.tStart = t  # local t and not account for scr refresh
                text_44.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_44, 'tStartRefresh')  # time at next scr refresh
                text_44.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('text_43.started', text_43.tStartRefresh)
        trials.addData('text_43.stopped', text_43.tStopRefresh)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        trials.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            trials.addData('key_resp_11.rt', key_resp_11.rt)
        trials.addData('key_resp_11.started', key_resp_11.tStartRefresh)
        trials.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
        trials.addData('text_44.started', text_44.tStartRefresh)
        trials.addData('text_44.stopped', text_44.tStopRefresh)
        # the Routine "questioncount" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "story_image"-------
        # update component parameters for each repeat
        this_recall_pic = storyDict.get(all_stories[count], {}).get('pic')
        image_10.setImage(this_recall_pic)
        key_resp_4.keys = []
        key_resp_4.rt = []
        # keep track of which components have finished
        story_imageComponents = [image_10, key_resp_4, text_22]
        for thisComponent in story_imageComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        story_imageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "story_image"-------
        while continueRoutine:
            # get current time
            t = story_imageClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=story_imageClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_10* updates
            if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                image_10.setAutoDraw(True)
            
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
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_22* updates
            if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_22.frameNStart = frameN  # exact frame index
                text_22.tStart = t  # local t and not account for scr refresh
                text_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
                text_22.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('image_10.started', image_10.tStartRefresh)
        trials.addData('image_10.stopped', image_10.tStopRefresh)
        trials.addData('text_22.started', text_22.tStartRefresh)
        trials.addData('text_22.stopped', text_22.tStopRefresh)
        # the Routine "story_image" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "question1"-------
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
        values = [1,2]
        random.shuffle(values)
        
        #questions from one schema
        this_perspective = storyDict.get(all_stories[count], {}).get(values[0])
        print(this_perspective)
        #questions from other schema
        other_perspective = storyDict.get(all_stories[count], {}).get(values[1])
        print(other_perspective)
        if this_perspective == 'Couples Therapist':
            pic1 = 'jobphotos/couples.jpg'
            question1 = 'For how long has the initiator of the breakup been thinking about breaking up with his/her partner?'
            question2 ='What is the initial reason stated by the initiator for why he/she is breaking up?'
            question3 ='Does the person who is being broken up with want to break up, and what’s the reason stated by them for this?'
            question4 = 'Who wants what items back as a result of the breakup?'
        if this_perspective == 'Restaurant Critic':
            pic1 = 'jobphotos/restaurant_critic.jpg'
            question1 = 'How is the restaurant decorated?'
            question2 ='What are the menus like?'
            question3 = 'What does each client order?' 
            question4 = 'How do the clients like the food?'
        if this_perspective == 'Airport Customer Experience Manager':
            pic1 = 'jobphotos/acem.jpg'
            question1 = 'When the clients arrive at the airport, how much time do they have until their flight departs?'
            question2 ='What is the reason for the hold-up at security?'
            question3 ='Toward which gate are the clients walking?'
            question4 ='What section and seat does each client sit in on the plane?'
        if this_perspective == 'Grocery Store Customer Experience Manager':
            pic1 = 'jobphotos/gscem.jpg'
            question1 = 'What is the grocery store like upon entering?'
            question2 ='What items do the clients pick out to buy?'
            question3 ='How many checkout lanes are open, and which one do the clients step into?'
            question4 = 'How much are the groceries, and what method of payment do the clients use?'
        if this_perspective == 'Dean of Academic Studies':
            pic1 ='jobphotos/dean.jpg'
            question1 = 'What is the lecture hall like?'
            question2 ='What class are the students in, and what is the day’s lecture about?'
            question3 ='What is something taught in lecture?'
            question4 = 'What is the next assessment/assignment for the class, and when is it scheduled/due?'
        if this_perspective == 'Wedding Planner':
            pic1 = 'jobphotos/weddingplanner.jpg'
            question1 = 'For how long has the couple been dating?'
            question2 ='How many diamonds are on the ring, and what is the diamond color?'
            question3 ='In/on what item is the ring presented?'
            question4 = 'Who does the new fiancee text first?'
        if this_perspective == 'Business Reporter':
            pic1 = 'jobphotos/business_reporter.jpg'
            question1 = 'What is each business person’s job title?'
            question2 = 'How much money is at stake in the initial offer made?'
            question3 = 'What is the name of the other industry competitor? '
            question4 =  'With what gesture do the business partners secure the deal?'
        if this_perspective == 'Matchmaker':
            pic1 = 'jobphotos/matchmaker.jpg'
            question1 = 'What object is the initiator of the interaction holding when he/she first notices the other person?' 
            question2 ='What is the initial question that begins the conversation between the couple?'
            question3 ='When will be the next time the couple meets and for what occasion?'
            question4 = 'What time is it when the couple parts?'
        
        if other_perspective == 'Couples Therapist':
            pic2 = 'jobphotos/couples.jpg'
            question5 = 'For how long has the initiator of the breakup been thinking about breaking up with his/her partner?'
            question6 ='What is the initial reason stated by the initiator for why he/she is breaking up?'
            question7 ='Does the person who is being broken up with want to break up, and what’s the reason stated by them for this?'
            question8 = 'Who wants what items back as a result of the breakup?'
        if other_perspective == 'Restaurant Critic':
            pic2 = 'jobphotos/restaurant_critic.jpg'
            question5 = 'How is the restaurant decorated?'
            question6 ='What are the menus like?'
            question7 = 'What does each client order?'
            question8 = 'How do the clients like the food?'
        if other_perspective == 'Airport Customer Experience Manager':
            pic2 = 'jobphotos/acem.jpg'
            question5 = 'When the clients arrive at the airport, how much time do they have until their flight departs?'
            question6 ='What is the reason for the hold-up at security?'
            question7 ='Toward which gate are the clients walking?'
            question8 ='What section and seat does each client sit in on the plane?' 
        if other_perspective == 'Grocery Store Customer Experience Manager':
            pic2 = 'jobphotos/gscem.jpg'
            question5 = 'What is the grocery store like upon entering?'
            question6 ='What items do the clients pick out to buy?'
            question7 ='How many checkout lanes are open, and which one do the clients step into?'
            question8 = 'How much are the groceries, and what method of payment do the clients use?'
        if other_perspective == 'Dean of Academic Studies':
            pic2 ='jobphotos/dean.jpg'
            question5 = 'What is the lecture hall like?'
            question6 ='What class are the students in, and what is the day’s lecture about?'
            question7 ='What is something taught in lecture?'
            question8 = 'What is the next assessment/assignment for the class, and when is it scheduled/due?'
        if other_perspective == 'Wedding Planner':
            pic2 = 'jobphotos/weddingplanner.jpg'
            question5 = 'For how long has the couple been dating?'
            question6 ='How many diamonds are on the ring, and what is the diamond color?'
            question7 ='In/on what item is the ring presented?'
            question8 = 'Who does the new fiancee text first?'
        if other_perspective == 'Business Reporter':
            pic2 = 'jobphotos/business_reporter.jpg'
            question5 = 'What is each business person’s job title?'
            question6 = 'How much money is at stake in the initial offer made?'
            question7 = 'What is the name of the other industry competitor? '
            question8 =  'With what gesture do the business partners secure the deal?'
        if other_perspective == 'Matchmaker':
            pic2 = 'jobphotos/matchmaker.jpg'
            question5 = 'What object is the initiator of the interaction holding when he/she first notices the other person?' 
            question6 ='What is the initial question that begins the conversation between the couple?'
            question7 ='When will be the next time the couple meets and for what occasion?'
            question8 = 'What time is it when the couple parts?'
        
        text_14.setText(question1)
        image_6.setImage(this_recall_pic)
        # keep track of which components have finished
        question1Components = [text_14, text_15, image_6, polygon_3, bottom_line_3, right_line_3, left_line_3]
        for thisComponent in question1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "question1"-------
        while continueRoutine:
            # get current time
            t = question1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
            if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                text_14.setAutoDraw(True)
            
            # *text_15* updates
            if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_15.frameNStart = frameN  # exact frame index
                text_15.tStart = t  # local t and not account for scr refresh
                text_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                text_15.setAutoDraw(True)
            if text_15.status == STARTED:  # only update if drawing
                text_15.setText(captured_string, log=False)
            
            # *image_6* updates
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                image_6.setAutoDraw(True)
            
            # *polygon_3* updates
            if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_3.frameNStart = frameN  # exact frame index
                polygon_3.tStart = t  # local t and not account for scr refresh
                polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(True)
            
            # *bottom_line_3* updates
            if bottom_line_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_line_3.frameNStart = frameN  # exact frame index
                bottom_line_3.tStart = t  # local t and not account for scr refresh
                bottom_line_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_line_3, 'tStartRefresh')  # time at next scr refresh
                bottom_line_3.setAutoDraw(True)
            
            # *right_line_3* updates
            if right_line_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_line_3.frameNStart = frameN  # exact frame index
                right_line_3.tStart = t  # local t and not account for scr refresh
                right_line_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_line_3, 'tStartRefresh')  # time at next scr refresh
                right_line_3.setAutoDraw(True)
            
            # *left_line_3* updates
            if left_line_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_line_3.frameNStart = frameN  # exact frame index
                left_line_3.tStart = t  # local t and not account for scr refresh
                left_line_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_line_3, 'tStartRefresh')  # time at next scr refresh
                left_line_3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        thisExp.addData('order of question', values)
        trials.addData('text_14.started', text_14.tStartRefresh)
        trials.addData('text_14.stopped', text_14.tStopRefresh)
        trials.addData('text_15.started', text_15.tStartRefresh)
        trials.addData('text_15.stopped', text_15.tStopRefresh)
        trials.addData('image_6.started', image_6.tStartRefresh)
        trials.addData('image_6.stopped', image_6.tStopRefresh)
        trials.addData('polygon_3.started', polygon_3.tStartRefresh)
        trials.addData('polygon_3.stopped', polygon_3.tStopRefresh)
        trials.addData('bottom_line_3.started', bottom_line_3.tStartRefresh)
        trials.addData('bottom_line_3.stopped', bottom_line_3.tStopRefresh)
        trials.addData('right_line_3.started', right_line_3.tStartRefresh)
        trials.addData('right_line_3.stopped', right_line_3.tStopRefresh)
        trials.addData('left_line_3.started', left_line_3.tStartRefresh)
        trials.addData('left_line_3.stopped', left_line_3.tStopRefresh)
        # the Routine "question1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "question2"-------
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "question2"-------
        while continueRoutine:
            # get current time
            t = question2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
            if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_16.frameNStart = frameN  # exact frame index
                text_16.tStart = t  # local t and not account for scr refresh
                text_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
                text_16.setAutoDraw(True)
            
            # *text_17* updates
            if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_17.frameNStart = frameN  # exact frame index
                text_17.tStart = t  # local t and not account for scr refresh
                text_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                text_17.setAutoDraw(True)
            if text_17.status == STARTED:  # only update if drawing
                text_17.setText(captured_string, log=False)
            
            # *image_7* updates
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                image_7.setAutoDraw(True)
            
            # *polygon_4* updates
            if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_4.frameNStart = frameN  # exact frame index
                polygon_4.tStart = t  # local t and not account for scr refresh
                polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(True)
            
            # *bottom_line_4* updates
            if bottom_line_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_line_4.frameNStart = frameN  # exact frame index
                bottom_line_4.tStart = t  # local t and not account for scr refresh
                bottom_line_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_line_4, 'tStartRefresh')  # time at next scr refresh
                bottom_line_4.setAutoDraw(True)
            
            # *right_line_4* updates
            if right_line_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_line_4.frameNStart = frameN  # exact frame index
                right_line_4.tStart = t  # local t and not account for scr refresh
                right_line_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_line_4, 'tStartRefresh')  # time at next scr refresh
                right_line_4.setAutoDraw(True)
            
            # *left_line_4* updates
            if left_line_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_line_4.frameNStart = frameN  # exact frame index
                left_line_4.tStart = t  # local t and not account for scr refresh
                left_line_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_line_4, 'tStartRefresh')  # time at next scr refresh
                left_line_4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('text_16.started', text_16.tStartRefresh)
        trials.addData('text_16.stopped', text_16.tStopRefresh)
        trials.addData('text_17.started', text_17.tStartRefresh)
        trials.addData('text_17.stopped', text_17.tStopRefresh)
        trials.addData('image_7.started', image_7.tStartRefresh)
        trials.addData('image_7.stopped', image_7.tStopRefresh)
        trials.addData('polygon_4.started', polygon_4.tStartRefresh)
        trials.addData('polygon_4.stopped', polygon_4.tStopRefresh)
        trials.addData('bottom_line_4.started', bottom_line_4.tStartRefresh)
        trials.addData('bottom_line_4.stopped', bottom_line_4.tStopRefresh)
        trials.addData('right_line_4.started', right_line_4.tStartRefresh)
        trials.addData('right_line_4.stopped', right_line_4.tStopRefresh)
        trials.addData('left_line_4.started', left_line_4.tStartRefresh)
        trials.addData('left_line_4.stopped', left_line_4.tStopRefresh)
        # the Routine "question2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "question3"-------
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "question3"-------
        while continueRoutine:
            # get current time
            t = question3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
            if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_18.frameNStart = frameN  # exact frame index
                text_18.tStart = t  # local t and not account for scr refresh
                text_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
                text_18.setAutoDraw(True)
            
            # *text_19* updates
            if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_19.frameNStart = frameN  # exact frame index
                text_19.tStart = t  # local t and not account for scr refresh
                text_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
                text_19.setAutoDraw(True)
            if text_19.status == STARTED:  # only update if drawing
                text_19.setText(captured_string, log=False)
            
            # *image_8* updates
            if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                image_8.setAutoDraw(True)
            
            # *polygon_5* updates
            if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_5.frameNStart = frameN  # exact frame index
                polygon_5.tStart = t  # local t and not account for scr refresh
                polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
                polygon_5.setAutoDraw(True)
            
            # *bottom_line_5* updates
            if bottom_line_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_line_5.frameNStart = frameN  # exact frame index
                bottom_line_5.tStart = t  # local t and not account for scr refresh
                bottom_line_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_line_5, 'tStartRefresh')  # time at next scr refresh
                bottom_line_5.setAutoDraw(True)
            
            # *right_line_5* updates
            if right_line_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_line_5.frameNStart = frameN  # exact frame index
                right_line_5.tStart = t  # local t and not account for scr refresh
                right_line_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_line_5, 'tStartRefresh')  # time at next scr refresh
                right_line_5.setAutoDraw(True)
            
            # *left_line_5* updates
            if left_line_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_line_5.frameNStart = frameN  # exact frame index
                left_line_5.tStart = t  # local t and not account for scr refresh
                left_line_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_line_5, 'tStartRefresh')  # time at next scr refresh
                left_line_5.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('text_18.started', text_18.tStartRefresh)
        trials.addData('text_18.stopped', text_18.tStopRefresh)
        trials.addData('text_19.started', text_19.tStartRefresh)
        trials.addData('text_19.stopped', text_19.tStopRefresh)
        trials.addData('image_8.started', image_8.tStartRefresh)
        trials.addData('image_8.stopped', image_8.tStopRefresh)
        trials.addData('polygon_5.started', polygon_5.tStartRefresh)
        trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
        trials.addData('bottom_line_5.started', bottom_line_5.tStartRefresh)
        trials.addData('bottom_line_5.stopped', bottom_line_5.tStopRefresh)
        trials.addData('right_line_5.started', right_line_5.tStartRefresh)
        trials.addData('right_line_5.stopped', right_line_5.tStopRefresh)
        trials.addData('left_line_5.started', left_line_5.tStartRefresh)
        trials.addData('left_line_5.stopped', left_line_5.tStopRefresh)
        # the Routine "question3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "question4"-------
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "question4"-------
        while continueRoutine:
            # get current time
            t = question4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
            if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_20.frameNStart = frameN  # exact frame index
                text_20.tStart = t  # local t and not account for scr refresh
                text_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
                text_20.setAutoDraw(True)
            
            # *text_21* updates
            if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_21.frameNStart = frameN  # exact frame index
                text_21.tStart = t  # local t and not account for scr refresh
                text_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
                text_21.setAutoDraw(True)
            if text_21.status == STARTED:  # only update if drawing
                text_21.setText(captured_string, log=False)
            
            # *image_9* updates
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                image_9.setAutoDraw(True)
            
            # *polygon_6* updates
            if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_6.frameNStart = frameN  # exact frame index
                polygon_6.tStart = t  # local t and not account for scr refresh
                polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                polygon_6.setAutoDraw(True)
            
            # *bottom_line_6* updates
            if bottom_line_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_line_6.frameNStart = frameN  # exact frame index
                bottom_line_6.tStart = t  # local t and not account for scr refresh
                bottom_line_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_line_6, 'tStartRefresh')  # time at next scr refresh
                bottom_line_6.setAutoDraw(True)
            
            # *right_line_6* updates
            if right_line_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_line_6.frameNStart = frameN  # exact frame index
                right_line_6.tStart = t  # local t and not account for scr refresh
                right_line_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_line_6, 'tStartRefresh')  # time at next scr refresh
                right_line_6.setAutoDraw(True)
            
            # *left_line_6* updates
            if left_line_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_line_6.frameNStart = frameN  # exact frame index
                left_line_6.tStart = t  # local t and not account for scr refresh
                left_line_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_line_6, 'tStartRefresh')  # time at next scr refresh
                left_line_6.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('text_20.started', text_20.tStartRefresh)
        trials.addData('text_20.stopped', text_20.tStopRefresh)
        trials.addData('text_21.started', text_21.tStartRefresh)
        trials.addData('text_21.stopped', text_21.tStopRefresh)
        trials.addData('image_9.started', image_9.tStartRefresh)
        trials.addData('image_9.stopped', image_9.tStopRefresh)
        trials.addData('polygon_6.started', polygon_6.tStartRefresh)
        trials.addData('polygon_6.stopped', polygon_6.tStopRefresh)
        trials.addData('bottom_line_6.started', bottom_line_6.tStartRefresh)
        trials.addData('bottom_line_6.stopped', bottom_line_6.tStopRefresh)
        trials.addData('right_line_6.started', right_line_6.tStartRefresh)
        trials.addData('right_line_6.stopped', right_line_6.tStopRefresh)
        trials.addData('left_line_6.started', left_line_6.tStartRefresh)
        trials.addData('left_line_6.stopped', left_line_6.tStopRefresh)
        # the Routine "question4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "question5"-------
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "question5"-------
        while continueRoutine:
            # get current time
            t = question5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
            if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_25.frameNStart = frameN  # exact frame index
                text_25.tStart = t  # local t and not account for scr refresh
                text_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
                text_25.setAutoDraw(True)
            
            # *text_26* updates
            if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_26.frameNStart = frameN  # exact frame index
                text_26.tStart = t  # local t and not account for scr refresh
                text_26.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
                text_26.setAutoDraw(True)
            if text_26.status == STARTED:  # only update if drawing
                text_26.setText(captured_string, log=False)
            
            # *image_11* updates
            if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                image_11.setAutoDraw(True)
            
            # *polygon_7* updates
            if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_7.frameNStart = frameN  # exact frame index
                polygon_7.tStart = t  # local t and not account for scr refresh
                polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
                polygon_7.setAutoDraw(True)
            
            # *bottom_line_7* updates
            if bottom_line_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_line_7.frameNStart = frameN  # exact frame index
                bottom_line_7.tStart = t  # local t and not account for scr refresh
                bottom_line_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_line_7, 'tStartRefresh')  # time at next scr refresh
                bottom_line_7.setAutoDraw(True)
            
            # *right_line_7* updates
            if right_line_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_line_7.frameNStart = frameN  # exact frame index
                right_line_7.tStart = t  # local t and not account for scr refresh
                right_line_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_line_7, 'tStartRefresh')  # time at next scr refresh
                right_line_7.setAutoDraw(True)
            
            # *left_line_7* updates
            if left_line_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_line_7.frameNStart = frameN  # exact frame index
                left_line_7.tStart = t  # local t and not account for scr refresh
                left_line_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_line_7, 'tStartRefresh')  # time at next scr refresh
                left_line_7.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('text_25.started', text_25.tStartRefresh)
        trials.addData('text_25.stopped', text_25.tStopRefresh)
        trials.addData('text_26.started', text_26.tStartRefresh)
        trials.addData('text_26.stopped', text_26.tStopRefresh)
        trials.addData('image_11.started', image_11.tStartRefresh)
        trials.addData('image_11.stopped', image_11.tStopRefresh)
        trials.addData('polygon_7.started', polygon_7.tStartRefresh)
        trials.addData('polygon_7.stopped', polygon_7.tStopRefresh)
        trials.addData('bottom_line_7.started', bottom_line_7.tStartRefresh)
        trials.addData('bottom_line_7.stopped', bottom_line_7.tStopRefresh)
        trials.addData('right_line_7.started', right_line_7.tStartRefresh)
        trials.addData('right_line_7.stopped', right_line_7.tStopRefresh)
        trials.addData('left_line_7.started', left_line_7.tStartRefresh)
        trials.addData('left_line_7.stopped', left_line_7.tStopRefresh)
        # the Routine "question5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "question6"-------
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "question6"-------
        while continueRoutine:
            # get current time
            t = question6Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question6Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
            if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_27.frameNStart = frameN  # exact frame index
                text_27.tStart = t  # local t and not account for scr refresh
                text_27.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
                text_27.setAutoDraw(True)
            
            # *text_28* updates
            if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_28.frameNStart = frameN  # exact frame index
                text_28.tStart = t  # local t and not account for scr refresh
                text_28.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
                text_28.setAutoDraw(True)
            if text_28.status == STARTED:  # only update if drawing
                text_28.setText(captured_string, log=False)
            
            # *image_12* updates
            if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                image_12.setAutoDraw(True)
            
            # *polygon_8* updates
            if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_8.frameNStart = frameN  # exact frame index
                polygon_8.tStart = t  # local t and not account for scr refresh
                polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
                polygon_8.setAutoDraw(True)
            
            # *bottom_line_8* updates
            if bottom_line_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_line_8.frameNStart = frameN  # exact frame index
                bottom_line_8.tStart = t  # local t and not account for scr refresh
                bottom_line_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_line_8, 'tStartRefresh')  # time at next scr refresh
                bottom_line_8.setAutoDraw(True)
            
            # *right_line_8* updates
            if right_line_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_line_8.frameNStart = frameN  # exact frame index
                right_line_8.tStart = t  # local t and not account for scr refresh
                right_line_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_line_8, 'tStartRefresh')  # time at next scr refresh
                right_line_8.setAutoDraw(True)
            
            # *left_line_8* updates
            if left_line_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_line_8.frameNStart = frameN  # exact frame index
                left_line_8.tStart = t  # local t and not account for scr refresh
                left_line_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_line_8, 'tStartRefresh')  # time at next scr refresh
                left_line_8.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('text_27.started', text_27.tStartRefresh)
        trials.addData('text_27.stopped', text_27.tStopRefresh)
        trials.addData('text_28.started', text_28.tStartRefresh)
        trials.addData('text_28.stopped', text_28.tStopRefresh)
        trials.addData('image_12.started', image_12.tStartRefresh)
        trials.addData('image_12.stopped', image_12.tStopRefresh)
        trials.addData('polygon_8.started', polygon_8.tStartRefresh)
        trials.addData('polygon_8.stopped', polygon_8.tStopRefresh)
        trials.addData('bottom_line_8.started', bottom_line_8.tStartRefresh)
        trials.addData('bottom_line_8.stopped', bottom_line_8.tStopRefresh)
        trials.addData('right_line_8.started', right_line_8.tStartRefresh)
        trials.addData('right_line_8.stopped', right_line_8.tStopRefresh)
        trials.addData('left_line_8.started', left_line_8.tStartRefresh)
        trials.addData('left_line_8.stopped', left_line_8.tStopRefresh)
        # the Routine "question6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "question7"-------
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
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "question7"-------
        while continueRoutine:
            # get current time
            t = question7Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question7Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
            if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_29.frameNStart = frameN  # exact frame index
                text_29.tStart = t  # local t and not account for scr refresh
                text_29.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
                text_29.setAutoDraw(True)
            
            # *text_30* updates
            if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_30.frameNStart = frameN  # exact frame index
                text_30.tStart = t  # local t and not account for scr refresh
                text_30.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
                text_30.setAutoDraw(True)
            if text_30.status == STARTED:  # only update if drawing
                text_30.setText(captured_string, log=False)
            
            # *image_13* updates
            if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_13.frameNStart = frameN  # exact frame index
                image_13.tStart = t  # local t and not account for scr refresh
                image_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
                image_13.setAutoDraw(True)
            
            # *polygon_9* updates
            if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_9.frameNStart = frameN  # exact frame index
                polygon_9.tStart = t  # local t and not account for scr refresh
                polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
                polygon_9.setAutoDraw(True)
            
            # *bottom_line_9* updates
            if bottom_line_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_line_9.frameNStart = frameN  # exact frame index
                bottom_line_9.tStart = t  # local t and not account for scr refresh
                bottom_line_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_line_9, 'tStartRefresh')  # time at next scr refresh
                bottom_line_9.setAutoDraw(True)
            
            # *right_line_9* updates
            if right_line_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_line_9.frameNStart = frameN  # exact frame index
                right_line_9.tStart = t  # local t and not account for scr refresh
                right_line_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_line_9, 'tStartRefresh')  # time at next scr refresh
                right_line_9.setAutoDraw(True)
            
            # *left_line_9* updates
            if left_line_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_line_9.frameNStart = frameN  # exact frame index
                left_line_9.tStart = t  # local t and not account for scr refresh
                left_line_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_line_9, 'tStartRefresh')  # time at next scr refresh
                left_line_9.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials.addData('text_29.started', text_29.tStartRefresh)
        trials.addData('text_29.stopped', text_29.tStopRefresh)
        trials.addData('text_30.started', text_30.tStartRefresh)
        trials.addData('text_30.stopped', text_30.tStopRefresh)
        trials.addData('image_13.started', image_13.tStartRefresh)
        trials.addData('image_13.stopped', image_13.tStopRefresh)
        trials.addData('polygon_9.started', polygon_9.tStartRefresh)
        trials.addData('polygon_9.stopped', polygon_9.tStopRefresh)
        trials.addData('bottom_line_9.started', bottom_line_9.tStartRefresh)
        trials.addData('bottom_line_9.stopped', bottom_line_9.tStopRefresh)
        trials.addData('right_line_9.started', right_line_9.tStartRefresh)
        trials.addData('right_line_9.stopped', right_line_9.tStopRefresh)
        trials.addData('left_line_9.started', left_line_9.tStartRefresh)
        trials.addData('left_line_9.stopped', left_line_9.tStopRefresh)
        # the Routine "question7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed played_story repeats of 'trials'
    
    
    # ------Prepare to start Routine "question8"-------
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
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    question8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "question8"-------
    while continueRoutine:
        # get current time
        t = question8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=question8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        
        # *text_32* updates
        if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_32.frameNStart = frameN  # exact frame index
            text_32.tStart = t  # local t and not account for scr refresh
            text_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
            text_32.setAutoDraw(True)
        if text_32.status == STARTED:  # only update if drawing
            text_32.setText(captured_string, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        
        # *polygon_10* updates
        if polygon_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_10.frameNStart = frameN  # exact frame index
            polygon_10.tStart = t  # local t and not account for scr refresh
            polygon_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_10, 'tStartRefresh')  # time at next scr refresh
            polygon_10.setAutoDraw(True)
        
        # *bottom_line_10* updates
        if bottom_line_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottom_line_10.frameNStart = frameN  # exact frame index
            bottom_line_10.tStart = t  # local t and not account for scr refresh
            bottom_line_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_line_10, 'tStartRefresh')  # time at next scr refresh
            bottom_line_10.setAutoDraw(True)
        
        # *right_line_10* updates
        if right_line_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_line_10.frameNStart = frameN  # exact frame index
            right_line_10.tStart = t  # local t and not account for scr refresh
            right_line_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_line_10, 'tStartRefresh')  # time at next scr refresh
            right_line_10.setAutoDraw(True)
        
        # *left_line_10* updates
        if left_line_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_line_10.frameNStart = frameN  # exact frame index
            left_line_10.tStart = t  # local t and not account for scr refresh
            left_line_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_line_10, 'tStartRefresh')  # time at next scr refresh
            left_line_10.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    trials_6.addData('text_31.started', text_31.tStartRefresh)
    trials_6.addData('text_31.stopped', text_31.tStopRefresh)
    trials_6.addData('text_32.started', text_32.tStartRefresh)
    trials_6.addData('text_32.stopped', text_32.tStopRefresh)
    trials_6.addData('image_14.started', image_14.tStartRefresh)
    trials_6.addData('image_14.stopped', image_14.tStopRefresh)
    trials_6.addData('polygon_10.started', polygon_10.tStartRefresh)
    trials_6.addData('polygon_10.stopped', polygon_10.tStopRefresh)
    trials_6.addData('bottom_line_10.started', bottom_line_10.tStartRefresh)
    trials_6.addData('bottom_line_10.stopped', bottom_line_10.tStopRefresh)
    trials_6.addData('right_line_10.started', right_line_10.tStartRefresh)
    trials_6.addData('right_line_10.stopped', right_line_10.tStopRefresh)
    trials_6.addData('left_line_10.started', left_line_10.tStartRefresh)
    trials_6.addData('left_line_10.stopped', left_line_10.tStopRefresh)
    # the Routine "question8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_6'


# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=1, method='sequential', 
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
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    end_of_taskComponents = [text_36]
    for thisComponent in end_of_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_of_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "end_of_task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_of_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_of_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_36* updates
        if text_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_36.frameNStart = frameN  # exact frame index
            text_36.tStart = t  # local t and not account for scr refresh
            text_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_36, 'tStartRefresh')  # time at next scr refresh
            text_36.setAutoDraw(True)
        if text_36.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_36.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_36.tStop = t  # not accounting for scr refresh
                text_36.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_36, 'tStopRefresh')  # time at next scr refresh
                text_36.setAutoDraw(False)
        for key in event.getKeys():
            if key in ['escape']: 
                core.quit()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    trials_8.addData('text_36.started', text_36.tStartRefresh)
    trials_8.addData('text_36.stopped', text_36.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_8'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
