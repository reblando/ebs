#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Tue Jan 14 16:52:47 2020
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, microphone
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
expName = 'recall_fmri'  # from the Builder filename that created this script
expInfo = {'participant': 'test', 'sA': '0', 'sB': '1', 'lA': '0', 'lB': '1', 'block_struct': '1', 'play_stories': '0', 'block': '1', 'behavioral': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexreblando/Desktop/ebs/fMRI experiment/psychopy code/2_recall_fMRI.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Startup"
StartupClock = core.Clock()
import numpy as np
import random 


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

#turning matrices into lists and remove zeros
action_list_block1 = list(action_matrix_block1.flatten())
action_list_block1 = np.asarray([x for x in action_list_block1 if x != 0])
action_list_block2 = list(action_matrix_block2.flatten())
action_list_block2 = np.asarray([x for x in action_list_block2 if x != 0])
story_list_block1 = list(story_matrix_block1.flatten())
story_list_block1 = np.asarray([x for x in story_list_block1 if x != 0])
story_list_block2 = list(story_matrix_block2.flatten())
story_list_block2 = np.asarray([x for x in story_list_block2 if x != 0])

#shuffling the story and action lists
randperm1 = np.random.permutation(8)
randperm2 = np.random.permutation(8)

action_list_block1 = action_list_block1[randperm1]
story_list_block1 = story_list_block1[randperm1]
action_list_block2 = action_list_block2[randperm2]
story_list_block2 = story_list_block2[randperm2]

all_action = np.concatenate((action_list_block1, action_list_block2), axis = 0)
all_story = np.concatenate((story_list_block1, story_list_block2), axis = 0)
print('action', all_action)
print('story', all_story)

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


thisExp.addData('story_list_block1', story_list_block1)
thisExp.addData('action_list_block1', action_list_block1)
thisExp.addData('story_list_block2', story_list_block2)
thisExp.addData('action_list_block2', action_list_block2)

print(story_list_block1)
print(action_list_block1)

#VLC
timer = core.Clock()
from psychopy import core, visual

import vlc
mom=vlc.Instance()
p=mom.media_player_new()
#p.set_fullscreen(True)

#selecting block to present
if int(expInfo['block']) == 1:
    block1_play = 1
    block2_play = 0
elif int(expInfo['block']) == 2:
    block1_play = 0
    block2_play = 1









# Initialize components for Routine "recall_instructions"
recall_instructionsClock = core.Clock()
text_76 = visual.TextStim(win=win, name='text_76',
    text='Recall Instructions',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "recall_instructions_behavioral"
recall_instructions_behavioralClock = core.Clock()
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

# Initialize components for Routine "Block1_SR"
Block1_SRClock = core.Clock()
text_70 = visual.TextStim(win=win, name='text_70',
    text='Block 1 of Story Recall',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "Trigger"
TriggerClock = core.Clock()
textTrigger = visual.TextStim(win=win, name='textTrigger',
    text='waiting for the scanner',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "routine_6sec_wait"
routine_6sec_waitClock = core.Clock()
image_23 = visual.ImageStim(
    win=win, name='image_23',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "info_recall1"
info_recall1Clock = core.Clock()


# Initialize components for Routine "intro_recall"
intro_recallClock = core.Clock()

text_41 = visual.TextStim(win=win, name='text_41',
    text='default text',
    font='Arial',
    pos=(-.02, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='Recall    of 6',
    font='Arial',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_51 = visual.TextStim(win=win, name='text_51',
    text='(press the space bar to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "recall_type1"
recall_type1Clock = core.Clock()

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

text_48 = visual.TextStim(win=win, name='text_48',
    text='default text',
    font='Arial',
    pos=(-.7, .7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "intro_recall"
intro_recallClock = core.Clock()

text_41 = visual.TextStim(win=win, name='text_41',
    text='default text',
    font='Arial',
    pos=(-.02, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='Recall    of 6',
    font='Arial',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_51 = visual.TextStim(win=win, name='text_51',
    text='(press the space bar to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "recall_recording1"
recall_recording1Clock = core.Clock()

image_18 = visual.ImageStim(
    win=win, name='image_18',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_69 = visual.TextStim(win=win, name='text_69',
    text='Please say everything you remember about this story (press a button on the button box when you have finished):',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "save_recall_data"
save_recall_dataClock = core.Clock()


# Initialize components for Routine "routine_6sec_wait"
routine_6sec_waitClock = core.Clock()
image_23 = visual.ImageStim(
    win=win, name='image_23',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Block2_SR"
Block2_SRClock = core.Clock()

text_71 = visual.TextStim(win=win, name='text_71',
    text='Block 2 of Story Recall',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Trigger"
TriggerClock = core.Clock()
textTrigger = visual.TextStim(win=win, name='textTrigger',
    text='waiting for the scanner',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "info_recall2"
info_recall2Clock = core.Clock()


# Initialize components for Routine "intro_recall"
intro_recallClock = core.Clock()

text_41 = visual.TextStim(win=win, name='text_41',
    text='default text',
    font='Arial',
    pos=(-.02, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='Recall    of 6',
    font='Arial',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_51 = visual.TextStim(win=win, name='text_51',
    text='(press the space bar to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "recall_type2"
recall_type2Clock = core.Clock()

text_72 = visual.TextStim(win=win, name='text_72',
    text='Type everything you recall here (press return to submit your response):',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_73 = visual.TextStim(win=win, name='text_73',
    text='default text',
    font='Arial',
    pos=[-.9, -0.15], height=0.1, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_19 = visual.ImageStim(
    win=win, name='image_19',
    image='sin', mask=None,
    ori=0, pos=(0, .5), size=(.75, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
polygon_11 = visual.Line(
    win=win, name='polygon_11',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.125),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
bottom_line_11 = visual.Line(
    win=win, name='bottom_line_11',
    start=(-(1.85, 1)[0]/2.0, 0), end=(+(1.85, 1)[0]/2.0, 0),
    ori=0, pos=(0, -.975),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
right_line_11 = visual.Line(
    win=win, name='right_line_11',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(.925, -.55),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
left_line_11 = visual.Line(
    win=win, name='left_line_11',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(-.925, -.55),
    lineWidth=20, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[128,128,128], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)

text_74 = visual.TextStim(win=win, name='text_74',
    text='default text',
    font='Arial',
    pos=(-.7, .7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "intro_recall"
intro_recallClock = core.Clock()

text_41 = visual.TextStim(win=win, name='text_41',
    text='default text',
    font='Arial',
    pos=(-.02, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='Recall    of 6',
    font='Arial',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_51 = visual.TextStim(win=win, name='text_51',
    text='(press the space bar to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "recall_recording2"
recall_recording2Clock = core.Clock()

image_20 = visual.ImageStim(
    win=win, name='image_20',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_75 = visual.TextStim(win=win, name='text_75',
    text='Please say everything you remember about this story (press a button on the button box when you have finished):',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "save_recall_data"
save_recall_dataClock = core.Clock()


# Initialize components for Routine "routine_6sec_wait"
routine_6sec_waitClock = core.Clock()
image_23 = visual.ImageStim(
    win=win, name='image_23',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

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

# ------Prepare to start Routine "Startup"-------
t = 0
StartupClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
StartupComponents = []
for thisComponent in StartupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Startup"-------
while continueRoutine:
    # get current time
    t = StartupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Startup"-------
for thisComponent in StartupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Startup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "recall_instructions"-------
t = 0
recall_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_30 = event.BuilderKeyResponse()
# keep track of which components have finished
recall_instructionsComponents = [text_76, key_resp_30]
for thisComponent in recall_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "recall_instructions"-------
while continueRoutine:
    # get current time
    t = recall_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_76* updates
    if t >= 0.0 and text_76.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_76.tStart = t
        text_76.frameNStart = frameN  # exact frame index
        text_76.setAutoDraw(True)
    
    # *key_resp_30* updates
    if t >= 0.0 and key_resp_30.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_30.tStart = t
        key_resp_30.frameNStart = frameN  # exact frame index
        key_resp_30.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_30.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_30.keys = theseKeys[-1]  # just the last key pressed
            key_resp_30.rt = key_resp_30.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
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
if key_resp_30.keys in ['', [], None]:  # No response was made
    key_resp_30.keys=None
thisExp.addData('key_resp_30.keys',key_resp_30.keys)
if key_resp_30.keys != None:  # we had a response
    thisExp.addData('key_resp_30.rt', key_resp_30.rt)
thisExp.nextEntry()
# the Routine "recall_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
behav_recall_instructions = data.TrialHandler(nReps=int(expInfo['behavioral']), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='behav_recall_instructions')
thisExp.addLoop(behav_recall_instructions)  # add the loop to the experiment
thisBehav_recall_instruction = behav_recall_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBehav_recall_instruction.rgb)
if thisBehav_recall_instruction != None:
    for paramName in thisBehav_recall_instruction:
        exec('{} = thisBehav_recall_instruction[paramName]'.format(paramName))

for thisBehav_recall_instruction in behav_recall_instructions:
    currentLoop = behav_recall_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisBehav_recall_instruction.rgb)
    if thisBehav_recall_instruction != None:
        for paramName in thisBehav_recall_instruction:
            exec('{} = thisBehav_recall_instruction[paramName]'.format(paramName))
    
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
        
        # ------Prepare to start Routine "recall_instructions_behavioral"-------
        t = 0
        recall_instructions_behavioralClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_10 = event.BuilderKeyResponse()
        text_6.setText(instructText)
        # keep track of which components have finished
        recall_instructions_behavioralComponents = [key_resp_10, text_6, text_24]
        for thisComponent in recall_instructions_behavioralComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "recall_instructions_behavioral"-------
        while continueRoutine:
            # get current time
            t = recall_instructions_behavioralClock.getTime()
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
            for thisComponent in recall_instructions_behavioralComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "recall_instructions_behavioral"-------
        for thisComponent in recall_instructions_behavioralComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys=None
        trials_3.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            trials_3.addData('key_resp_10.rt', key_resp_10.rt)
        # the Routine "recall_instructions_behavioral" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed int(expInfo['behavioral']) repeats of 'behav_recall_instructions'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=block1_play, method='sequential', 
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
    
    # ------Prepare to start Routine "Block1_SR"-------
    t = 0
    Block1_SRClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    count_recall = 0
    # keep track of which components have finished
    Block1_SRComponents = [text_70]
    for thisComponent in Block1_SRComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Block1_SR"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block1_SRClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_70* updates
        if t >= 0.0 and text_70.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_70.tStart = t
            text_70.frameNStart = frameN  # exact frame index
            text_70.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_70.status == STARTED and t >= frameRemains:
            text_70.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1_SRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block1_SR"-------
    for thisComponent in Block1_SRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "Trigger"-------
    t = 0
    TriggerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    getTrigger = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    TriggerComponents = [textTrigger, getTrigger]
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trigger"-------
    while continueRoutine:
        # get current time
        t = TriggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textTrigger* updates
        if t >= 0.0 and textTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTrigger.tStart = t
            textTrigger.frameNStart = frameN  # exact frame index
            textTrigger.setAutoDraw(True)
        
        # *getTrigger* updates
        if t >= 0.0 and getTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            getTrigger.tStart = t
            getTrigger.frameNStart = frameN  # exact frame index
            getTrigger.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(getTrigger.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if getTrigger.status == STARTED:
            theseKeys = event.getKeys(keyList=['5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                getTrigger.keys = theseKeys[-1]  # just the last key pressed
                getTrigger.rt = getTrigger.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trigger"-------
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if getTrigger.keys in ['', [], None]:  # No response was made
        getTrigger.keys=None
    trials.addData('getTrigger.keys',getTrigger.keys)
    if getTrigger.keys != None:  # we had a response
        trials.addData('getTrigger.rt', getTrigger.rt)
    triggerTime = globalClock.getTime()
    thisExp.addData('triggerTime', triggerTime)
    def getRelTime(start = triggerTime):
        return globalClock.getTime() - start
    # the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "routine_6sec_wait"-------
    t = 0
    routine_6sec_waitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_6sec_waitComponents = [image_23]
    for thisComponent in routine_6sec_waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_6sec_wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_6sec_waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_23* updates
        if t >= 0.0 and image_23.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_23.tStart = t
            image_23.frameNStart = frameN  # exact frame index
            image_23.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_23.status == STARTED and t >= frameRemains:
            image_23.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_6sec_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_6sec_wait"-------
    for thisComponent in routine_6sec_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
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
        
        # ------Prepare to start Routine "info_recall1"-------
        t = 0
        info_recall1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if int(expInfo['behavioral']) == 1:
            nreps_audiorecord = 0
            if action_list_block1[count] == 1:
                nreps_type = 1
            if action_list_block1[count] == 2:
                nreps_type = 1
            if action_list_block1[count] == 3:
                nreps_type = 0
            if action_list_block1[count] == 4:
                nreps_type = 1
        
        if int(expInfo['behavioral']) == 0:
            nreps_type = 0
            if action_list_block1[count] == 1:
                nreps_audiorecord = 1
            if action_list_block1[count] == 2:
                nreps_audiorecord = 1
            if action_list_block1[count] == 3:
                nreps_audiorecord = 0
            if action_list_block1[count] == 4:
                nreps_audiorecord = 1
        
        
        # keep track of which components have finished
        info_recall1Components = []
        for thisComponent in info_recall1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "info_recall1"-------
        while continueRoutine:
            # get current time
            t = info_recall1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in info_recall1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "info_recall1"-------
        for thisComponent in info_recall1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "info_recall1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_13 = data.TrialHandler(nReps=nreps_type, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_13')
        thisExp.addLoop(trials_13)  # add the loop to the experiment
        thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
        if thisTrial_13 != None:
            for paramName in thisTrial_13:
                exec('{} = thisTrial_13[paramName]'.format(paramName))
        
        for thisTrial_13 in trials_13:
            currentLoop = trials_13
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
            if thisTrial_13 != None:
                for paramName in thisTrial_13:
                    exec('{} = thisTrial_13[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "intro_recall"-------
            t = 0
            intro_recallClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            count_recall += 1
            text_41.setText(count_recall)
            key_resp_26 = event.BuilderKeyResponse()
            # keep track of which components have finished
            intro_recallComponents = [text_41, key_resp_26, text_42, text_51]
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "intro_recall"-------
            while continueRoutine:
                # get current time
                t = intro_recallClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_41* updates
                if t >= 0.0 and text_41.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_41.tStart = t
                    text_41.frameNStart = frameN  # exact frame index
                    text_41.setAutoDraw(True)
                
                # *key_resp_26* updates
                if t >= 0.0 and key_resp_26.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_26.tStart = t
                    key_resp_26.frameNStart = frameN  # exact frame index
                    key_resp_26.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if key_resp_26.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_26.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_26.rt = key_resp_26.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_42* updates
                if t >= 0.0 and text_42.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_42.tStart = t
                    text_42.frameNStart = frameN  # exact frame index
                    text_42.setAutoDraw(True)
                
                # *text_51* updates
                if t >= 0.0 and text_51.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_51.tStart = t
                    text_51.frameNStart = frameN  # exact frame index
                    text_51.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_recallComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "intro_recall"-------
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if key_resp_26.keys in ['', [], None]:  # No response was made
                key_resp_26.keys=None
            trials_13.addData('key_resp_26.keys',key_resp_26.keys)
            if key_resp_26.keys != None:  # we had a response
                trials_13.addData('key_resp_26.rt', key_resp_26.rt)
            # the Routine "intro_recall" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "recall_type1"-------
            t = 0
            recall_type1Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            event.clearEvents()
            thisExp.addData('recall_StartTime', getRelTime())
            cursorCounter=0
            cursorVariable='|'
            captured_string=''
            subject_response_finished=False
            shift_flag = False
            text_10.alignHoriz ='left'
            text_10.alignVert = 'top'
            text_10.wrapWidth = 1.8
            text_10.height = .05
            
            this_recall_pic = storyDict.get(story_list_block1[count], {}).get('pic')
            
            image_4.setImage(this_recall_pic)
            countdownClock = core.CountdownTimer(300) # 300 s = 5 minutes  countdownStarted = True 
            timeText = '5:00' 
            # keep track of which components have finished
            recall_type1Components = [text_9, text_10, image_4, polygon, bottom_line, right_line_2, left_line, text_48]
            for thisComponent in recall_type1Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "recall_type1"-------
            while continueRoutine:
                # get current time
                t = recall_type1Clock.getTime()
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
                timeRemaining = countdownClock.getTime() 
                if timeRemaining <= 0.0: 
                    continueRoutine = False 
                else: 
                    minutes = int(timeRemaining/60.0) # the integer number of minutes 
                    seconds = int(timeRemaining - (minutes * 60.0)) 
                    if seconds < 10:
                        timeText = str(minutes) + ':0' + str(seconds) # create a string of characters representing the time 
                    else:
                        timeText = str(minutes) + ':' + str(seconds) # create a string of characters representing the time 
                
                # *text_48* updates
                if t >= 0.0 and text_48.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_48.tStart = t
                    text_48.frameNStart = frameN  # exact frame index
                    text_48.setAutoDraw(True)
                if text_48.status == STARTED:  # only update if drawing
                    text_48.setText(timeText, log=False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in recall_type1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "recall_type1"-------
            for thisComponent in recall_type1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('recall_EndTime', getRelTime())
            
            # the Routine "recall_type1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nreps_type repeats of 'trials_13'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_17 = data.TrialHandler(nReps=nreps_audiorecord, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_17')
        thisExp.addLoop(trials_17)  # add the loop to the experiment
        thisTrial_17 = trials_17.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
        if thisTrial_17 != None:
            for paramName in thisTrial_17:
                exec('{} = thisTrial_17[paramName]'.format(paramName))
        
        for thisTrial_17 in trials_17:
            currentLoop = trials_17
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
            if thisTrial_17 != None:
                for paramName in thisTrial_17:
                    exec('{} = thisTrial_17[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "intro_recall"-------
            t = 0
            intro_recallClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            count_recall += 1
            text_41.setText(count_recall)
            key_resp_26 = event.BuilderKeyResponse()
            # keep track of which components have finished
            intro_recallComponents = [text_41, key_resp_26, text_42, text_51]
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "intro_recall"-------
            while continueRoutine:
                # get current time
                t = intro_recallClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_41* updates
                if t >= 0.0 and text_41.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_41.tStart = t
                    text_41.frameNStart = frameN  # exact frame index
                    text_41.setAutoDraw(True)
                
                # *key_resp_26* updates
                if t >= 0.0 and key_resp_26.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_26.tStart = t
                    key_resp_26.frameNStart = frameN  # exact frame index
                    key_resp_26.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if key_resp_26.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_26.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_26.rt = key_resp_26.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_42* updates
                if t >= 0.0 and text_42.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_42.tStart = t
                    text_42.frameNStart = frameN  # exact frame index
                    text_42.setAutoDraw(True)
                
                # *text_51* updates
                if t >= 0.0 and text_51.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_51.tStart = t
                    text_51.frameNStart = frameN  # exact frame index
                    text_51.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_recallComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "intro_recall"-------
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if key_resp_26.keys in ['', [], None]:  # No response was made
                key_resp_26.keys=None
            trials_17.addData('key_resp_26.keys',key_resp_26.keys)
            if key_resp_26.keys != None:  # we had a response
                trials_17.addData('key_resp_26.rt', key_resp_26.rt)
            # the Routine "intro_recall" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "recall_recording1"-------
            t = 0
            recall_recording1Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('recall_StartTime', getRelTime())
            this_recall_pic = storyDict.get(story_list_block1[count], {}).get('pic')
            event.clearEvents()
            image_18.setImage(this_recall_pic)
            recall_audio = microphone.AdvAudioCapture(name='recall_audio', saveDir=wavDirName, stereo=False)
            key_resp_25 = event.BuilderKeyResponse()
            # keep track of which components have finished
            recall_recording1Components = [image_18, text_69, recall_audio, key_resp_25]
            for thisComponent in recall_recording1Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "recall_recording1"-------
            while continueRoutine:
                # get current time
                t = recall_recording1Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *image_18* updates
                if t >= 0.0 and image_18.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_18.tStart = t
                    image_18.frameNStart = frameN  # exact frame index
                    image_18.setAutoDraw(True)
                
                # *text_69* updates
                if t >= 0.0 and text_69.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_69.tStart = t
                    text_69.frameNStart = frameN  # exact frame index
                    text_69.setAutoDraw(True)
                
                # *recall_audio* updates
                if t >= 0.0 and recall_audio.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    recall_audio.tStart = t
                    recall_audio.frameNStart = frameN  # exact frame index
                    recall_audio.status = STARTED
                    recall_audio.record(sec=600, block=False)  # start the recording thread
                
                if recall_audio.status == STARTED and not recall_audio.recorder.running:
                    recall_audio.status = FINISHED
                
                # *key_resp_25* updates
                if t >= 0.0 and key_resp_25.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_25.tStart = t
                    key_resp_25.frameNStart = frameN  # exact frame index
                    key_resp_25.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if key_resp_25.status == STARTED:
                    theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_25.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_25.rt = key_resp_25.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in recall_recording1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "recall_recording1"-------
            for thisComponent in recall_recording1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('recall_EndTime', getRelTime())
            # recall_audio stop & responses
            recall_audio.stop()  # sometimes helpful
            if not recall_audio.savedFile:
                recall_audio.savedFile = None
            # store data for trials_17 (TrialHandler)
            trials_17.addData('recall_audio.filename', recall_audio.savedFile)
            # check responses
            if key_resp_25.keys in ['', [], None]:  # No response was made
                key_resp_25.keys=None
            trials_17.addData('key_resp_25.keys',key_resp_25.keys)
            if key_resp_25.keys != None:  # we had a response
                trials_17.addData('key_resp_25.rt', key_resp_25.rt)
            # the Routine "recall_recording1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nreps_audiorecord repeats of 'trials_17'
        
        
        # ------Prepare to start Routine "save_recall_data"-------
        t = 0
        save_recall_dataClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.saveAsWideText(filename+'_safety.csv', appendFile=True)
        # keep track of which components have finished
        save_recall_dataComponents = []
        for thisComponent in save_recall_dataComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "save_recall_data"-------
        while continueRoutine:
            # get current time
            t = save_recall_dataClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in save_recall_dataComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "save_recall_data"-------
        for thisComponent in save_recall_dataComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "save_recall_data" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_6sec_wait"-------
        t = 0
        routine_6sec_waitClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        routine_6sec_waitComponents = [image_23]
        for thisComponent in routine_6sec_waitComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_6sec_wait"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = routine_6sec_waitClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_23* updates
            if t >= 0.0 and image_23.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_23.tStart = t
                image_23.frameNStart = frameN  # exact frame index
                image_23.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_23.status == STARTED and t >= frameRemains:
                image_23.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_6sec_waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_6sec_wait"-------
        for thisComponent in routine_6sec_waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_4'
    
    thisExp.nextEntry()
    
# completed block1_play repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=block2_play, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "Block2_SR"-------
    t = 0
    Block2_SRClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    count_recall = 0
    # keep track of which components have finished
    Block2_SRComponents = [text_71]
    for thisComponent in Block2_SRComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Block2_SR"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block2_SRClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_71* updates
        if t >= 0.0 and text_71.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_71.tStart = t
            text_71.frameNStart = frameN  # exact frame index
            text_71.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_71.status == STARTED and t >= frameRemains:
            text_71.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block2_SRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block2_SR"-------
    for thisComponent in Block2_SRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "Trigger"-------
    t = 0
    TriggerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    getTrigger = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    TriggerComponents = [textTrigger, getTrigger]
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trigger"-------
    while continueRoutine:
        # get current time
        t = TriggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textTrigger* updates
        if t >= 0.0 and textTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTrigger.tStart = t
            textTrigger.frameNStart = frameN  # exact frame index
            textTrigger.setAutoDraw(True)
        
        # *getTrigger* updates
        if t >= 0.0 and getTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            getTrigger.tStart = t
            getTrigger.frameNStart = frameN  # exact frame index
            getTrigger.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(getTrigger.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if getTrigger.status == STARTED:
            theseKeys = event.getKeys(keyList=['5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                getTrigger.keys = theseKeys[-1]  # just the last key pressed
                getTrigger.rt = getTrigger.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trigger"-------
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if getTrigger.keys in ['', [], None]:  # No response was made
        getTrigger.keys=None
    trials_2.addData('getTrigger.keys',getTrigger.keys)
    if getTrigger.keys != None:  # we had a response
        trials_2.addData('getTrigger.rt', getTrigger.rt)
    triggerTime = globalClock.getTime()
    thisExp.addData('triggerTime', triggerTime)
    def getRelTime(start = triggerTime):
        return globalClock.getTime() - start
    # the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_20 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('count_8.xlsx'),
        seed=None, name='trials_20')
    thisExp.addLoop(trials_20)  # add the loop to the experiment
    thisTrial_20 = trials_20.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
    if thisTrial_20 != None:
        for paramName in thisTrial_20:
            exec('{} = thisTrial_20[paramName]'.format(paramName))
    
    for thisTrial_20 in trials_20:
        currentLoop = trials_20
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
        if thisTrial_20 != None:
            for paramName in thisTrial_20:
                exec('{} = thisTrial_20[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "info_recall2"-------
        t = 0
        info_recall2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if int(expInfo['behavioral']) == 1:
            nreps_audiorecord = 0
            if action_list_block2[count] == 1:
                nreps_type = 1
            if action_list_block2[count] == 2:
                nreps_type = 1
            if action_list_block2[count] == 3:
                nreps_type = 0
            if action_list_block2[count] == 4:
                nreps_type = 1
        
        if int(expInfo['behavioral']) == 0:
            nreps_type = 0
            if action_list_block2[count] == 1:
                nreps_audiorecord = 1
            if action_list_block2[count] == 2:
                nreps_audiorecord = 1
            if action_list_block2[count] == 3:
                nreps_audiorecord = 0
            if action_list_block2[count] == 4:
                nreps_audiorecord = 1
        
        
        # keep track of which components have finished
        info_recall2Components = []
        for thisComponent in info_recall2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "info_recall2"-------
        while continueRoutine:
            # get current time
            t = info_recall2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in info_recall2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "info_recall2"-------
        for thisComponent in info_recall2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "info_recall2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_18 = data.TrialHandler(nReps=nreps_type, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_18')
        thisExp.addLoop(trials_18)  # add the loop to the experiment
        thisTrial_18 = trials_18.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
        if thisTrial_18 != None:
            for paramName in thisTrial_18:
                exec('{} = thisTrial_18[paramName]'.format(paramName))
        
        for thisTrial_18 in trials_18:
            currentLoop = trials_18
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
            if thisTrial_18 != None:
                for paramName in thisTrial_18:
                    exec('{} = thisTrial_18[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "intro_recall"-------
            t = 0
            intro_recallClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            count_recall += 1
            text_41.setText(count_recall)
            key_resp_26 = event.BuilderKeyResponse()
            # keep track of which components have finished
            intro_recallComponents = [text_41, key_resp_26, text_42, text_51]
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "intro_recall"-------
            while continueRoutine:
                # get current time
                t = intro_recallClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_41* updates
                if t >= 0.0 and text_41.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_41.tStart = t
                    text_41.frameNStart = frameN  # exact frame index
                    text_41.setAutoDraw(True)
                
                # *key_resp_26* updates
                if t >= 0.0 and key_resp_26.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_26.tStart = t
                    key_resp_26.frameNStart = frameN  # exact frame index
                    key_resp_26.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if key_resp_26.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_26.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_26.rt = key_resp_26.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_42* updates
                if t >= 0.0 and text_42.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_42.tStart = t
                    text_42.frameNStart = frameN  # exact frame index
                    text_42.setAutoDraw(True)
                
                # *text_51* updates
                if t >= 0.0 and text_51.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_51.tStart = t
                    text_51.frameNStart = frameN  # exact frame index
                    text_51.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_recallComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "intro_recall"-------
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if key_resp_26.keys in ['', [], None]:  # No response was made
                key_resp_26.keys=None
            trials_18.addData('key_resp_26.keys',key_resp_26.keys)
            if key_resp_26.keys != None:  # we had a response
                trials_18.addData('key_resp_26.rt', key_resp_26.rt)
            # the Routine "intro_recall" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "recall_type2"-------
            t = 0
            recall_type2Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            event.clearEvents()
            thisExp.addData('recall_StartTime', getRelTime())
            cursorCounter=0
            cursorVariable='|'
            captured_string=''
            subject_response_finished=False
            shift_flag = False
            text_10.alignHoriz ='left'
            text_10.alignVert = 'top'
            text_10.wrapWidth = 1.8
            text_10.height = .05
            
            this_recall_pic = storyDict.get(story_list_block2[count], {}).get('pic')
            
            image_19.setImage(this_recall_pic)
            countdownClock = core.CountdownTimer(300) # 300 s = 5 minutes  countdownStarted = True 
            timeText = '5:00' 
            # keep track of which components have finished
            recall_type2Components = [text_72, text_73, image_19, polygon_11, bottom_line_11, right_line_11, left_line_11, text_74]
            for thisComponent in recall_type2Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "recall_type2"-------
            while continueRoutine:
                # get current time
                t = recall_type2Clock.getTime()
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
                    
                    
                    
                
                
                
                
                
                # *text_72* updates
                if t >= 0.0 and text_72.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_72.tStart = t
                    text_72.frameNStart = frameN  # exact frame index
                    text_72.setAutoDraw(True)
                
                # *text_73* updates
                if t >= 0.0 and text_73.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_73.tStart = t
                    text_73.frameNStart = frameN  # exact frame index
                    text_73.setAutoDraw(True)
                if text_73.status == STARTED:  # only update if drawing
                    text_73.setText(captured_string, log=False)
                
                # *image_19* updates
                if t >= 0.0 and image_19.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_19.tStart = t
                    image_19.frameNStart = frameN  # exact frame index
                    image_19.setAutoDraw(True)
                
                # *polygon_11* updates
                if t >= 0.0 and polygon_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_11.tStart = t
                    polygon_11.frameNStart = frameN  # exact frame index
                    polygon_11.setAutoDraw(True)
                
                # *bottom_line_11* updates
                if t >= 0.0 and bottom_line_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    bottom_line_11.tStart = t
                    bottom_line_11.frameNStart = frameN  # exact frame index
                    bottom_line_11.setAutoDraw(True)
                
                # *right_line_11* updates
                if t >= 0.0 and right_line_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    right_line_11.tStart = t
                    right_line_11.frameNStart = frameN  # exact frame index
                    right_line_11.setAutoDraw(True)
                
                # *left_line_11* updates
                if t >= 0.0 and left_line_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    left_line_11.tStart = t
                    left_line_11.frameNStart = frameN  # exact frame index
                    left_line_11.setAutoDraw(True)
                timeRemaining = countdownClock.getTime() 
                if timeRemaining <= 0.0: 
                    continueRoutine = False 
                else: 
                    minutes = int(timeRemaining/60.0) # the integer number of minutes 
                    seconds = int(timeRemaining - (minutes * 60.0)) 
                    if seconds < 10:
                        timeText = str(minutes) + ':0' + str(seconds) # create a string of characters representing the time 
                    else:
                        timeText = str(minutes) + ':' + str(seconds) # create a string of characters representing the time 
                
                # *text_74* updates
                if t >= 0.0 and text_74.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_74.tStart = t
                    text_74.frameNStart = frameN  # exact frame index
                    text_74.setAutoDraw(True)
                if text_74.status == STARTED:  # only update if drawing
                    text_74.setText(timeText, log=False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in recall_type2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "recall_type2"-------
            for thisComponent in recall_type2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('recall_EndTime', getRelTime())
            
            # the Routine "recall_type2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nreps_type repeats of 'trials_18'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_19 = data.TrialHandler(nReps=nreps_audiorecord, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_19')
        thisExp.addLoop(trials_19)  # add the loop to the experiment
        thisTrial_19 = trials_19.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
        if thisTrial_19 != None:
            for paramName in thisTrial_19:
                exec('{} = thisTrial_19[paramName]'.format(paramName))
        
        for thisTrial_19 in trials_19:
            currentLoop = trials_19
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
            if thisTrial_19 != None:
                for paramName in thisTrial_19:
                    exec('{} = thisTrial_19[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "intro_recall"-------
            t = 0
            intro_recallClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            count_recall += 1
            text_41.setText(count_recall)
            key_resp_26 = event.BuilderKeyResponse()
            # keep track of which components have finished
            intro_recallComponents = [text_41, key_resp_26, text_42, text_51]
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "intro_recall"-------
            while continueRoutine:
                # get current time
                t = intro_recallClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_41* updates
                if t >= 0.0 and text_41.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_41.tStart = t
                    text_41.frameNStart = frameN  # exact frame index
                    text_41.setAutoDraw(True)
                
                # *key_resp_26* updates
                if t >= 0.0 and key_resp_26.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_26.tStart = t
                    key_resp_26.frameNStart = frameN  # exact frame index
                    key_resp_26.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if key_resp_26.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_26.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_26.rt = key_resp_26.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_42* updates
                if t >= 0.0 and text_42.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_42.tStart = t
                    text_42.frameNStart = frameN  # exact frame index
                    text_42.setAutoDraw(True)
                
                # *text_51* updates
                if t >= 0.0 and text_51.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_51.tStart = t
                    text_51.frameNStart = frameN  # exact frame index
                    text_51.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_recallComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "intro_recall"-------
            for thisComponent in intro_recallComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if key_resp_26.keys in ['', [], None]:  # No response was made
                key_resp_26.keys=None
            trials_19.addData('key_resp_26.keys',key_resp_26.keys)
            if key_resp_26.keys != None:  # we had a response
                trials_19.addData('key_resp_26.rt', key_resp_26.rt)
            # the Routine "intro_recall" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "recall_recording2"-------
            t = 0
            recall_recording2Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('recall_StartTime', getRelTime())
            this_recall_pic = storyDict.get(story_list_block2[count], {}).get('pic')
            event.clearEvents()
            image_20.setImage(this_recall_pic)
            recall_audio_2 = microphone.AdvAudioCapture(name='recall_audio_2', saveDir=wavDirName, stereo=False)
            key_resp_27 = event.BuilderKeyResponse()
            # keep track of which components have finished
            recall_recording2Components = [image_20, text_75, recall_audio_2, key_resp_27]
            for thisComponent in recall_recording2Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "recall_recording2"-------
            while continueRoutine:
                # get current time
                t = recall_recording2Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *image_20* updates
                if t >= 0.0 and image_20.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_20.tStart = t
                    image_20.frameNStart = frameN  # exact frame index
                    image_20.setAutoDraw(True)
                
                # *text_75* updates
                if t >= 0.0 and text_75.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_75.tStart = t
                    text_75.frameNStart = frameN  # exact frame index
                    text_75.setAutoDraw(True)
                
                # *recall_audio_2* updates
                if t >= 0.0 and recall_audio_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    recall_audio_2.tStart = t
                    recall_audio_2.frameNStart = frameN  # exact frame index
                    recall_audio_2.status = STARTED
                    recall_audio_2.record(sec=600, block=False)  # start the recording thread
                
                if recall_audio_2.status == STARTED and not recall_audio_2.recorder.running:
                    recall_audio_2.status = FINISHED
                
                # *key_resp_27* updates
                if t >= 0.0 and key_resp_27.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_27.tStart = t
                    key_resp_27.frameNStart = frameN  # exact frame index
                    key_resp_27.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_27.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if key_resp_27.status == STARTED:
                    theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_27.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_27.rt = key_resp_27.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in recall_recording2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "recall_recording2"-------
            for thisComponent in recall_recording2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('recall_EndTime', getRelTime())
            # recall_audio_2 stop & responses
            recall_audio_2.stop()  # sometimes helpful
            if not recall_audio_2.savedFile:
                recall_audio_2.savedFile = None
            # store data for trials_19 (TrialHandler)
            trials_19.addData('recall_audio_2.filename', recall_audio_2.savedFile)
            # check responses
            if key_resp_27.keys in ['', [], None]:  # No response was made
                key_resp_27.keys=None
            trials_19.addData('key_resp_27.keys',key_resp_27.keys)
            if key_resp_27.keys != None:  # we had a response
                trials_19.addData('key_resp_27.rt', key_resp_27.rt)
            # the Routine "recall_recording2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nreps_audiorecord repeats of 'trials_19'
        
        
        # ------Prepare to start Routine "save_recall_data"-------
        t = 0
        save_recall_dataClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.saveAsWideText(filename+'_safety.csv', appendFile=True)
        # keep track of which components have finished
        save_recall_dataComponents = []
        for thisComponent in save_recall_dataComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "save_recall_data"-------
        while continueRoutine:
            # get current time
            t = save_recall_dataClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in save_recall_dataComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "save_recall_data"-------
        for thisComponent in save_recall_dataComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "save_recall_data" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_6sec_wait"-------
        t = 0
        routine_6sec_waitClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        routine_6sec_waitComponents = [image_23]
        for thisComponent in routine_6sec_waitComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_6sec_wait"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = routine_6sec_waitClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_23* updates
            if t >= 0.0 and image_23.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_23.tStart = t
                image_23.frameNStart = frameN  # exact frame index
                image_23.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_23.status == STARTED and t >= frameRemains:
                image_23.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_6sec_waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_6sec_wait"-------
        for thisComponent in routine_6sec_waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_20'
    
    thisExp.nextEntry()
    
# completed block2_play repeats of 'trials_2'


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
    routineTimer.add(0.500000)
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
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_36.status == STARTED and t >= frameRemains:
            text_36.setAutoDraw(False)
        for key in event.getKeys():
            if key in ['escape']: 
                core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_of_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
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
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
