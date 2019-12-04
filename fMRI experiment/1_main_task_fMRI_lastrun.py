#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.1),
    on Tue Dec  3 15:18:32 2019
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
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Users/alexreblando/Documents/GitHub/ebs/fMRI experiment/1_main_task_fMRI_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "storycount"
storycountClock = core.Clock()
text_38 = visual.TextStim(win=win, name='text_38',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()
text_39 = visual.TextStim(win=win, name='text_39',
    text='Story     out of 8',
    font='Arial',
    pos=(0.03, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
timer = core.Clock()
from psychopy import core, visual

import vlc
mom=vlc.Instance()
p=mom.media_player_new()
#p.set_fullscreen(True)

# Initialize components for Routine "ask_to_assume"
ask_to_assumeClock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='Please assume the perspective of:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "perspective"
perspectiveClock = core.Clock()
import numpy as np
import random 

#make basic matrix of all stories
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

#construct the action matrix based on the inputted social and location perspectives
action_matrix = np.zeros(shape = [4, 4], dtype = int)
these_social_ps = [0,1]
these_location_ps = [0,1]

for i in range(2):
    action_matrix[these_social_ps[i],:] += 1
    action_matrix[:,these_location_ps[i]] += 2
    
action_matrix[action_matrix == 0] = 4

#construct the block molds
block_mold1 = np.array([[0, 1, 0, 1], [1,0,1,0],[0,1,0,1], [1,0,1,0]])
block_mold2 = np.array([[1,0,1,0],[0,1,0,1], [1,0,1,0],[0, 1, 0, 1]])
#randomly select a mold for the first half of the presented stories
flip = random.randint(0, 1)
print(flip)
if flip == 0:
    action_matrix_block1 = np.multiply(action_matrix, block_mold1)
    action_matrix_block2 = np.multiply(action_matrix, block_mold2)
    story_matrix_block1 = np.multiply(story_matrix, block_mold1)
    story_matrix_block2 = np.multiply(story_matrix, block_mold2)
else:
    action_matrix_block1 = np.multiply(action_matrix, block_mold2)
    action_matrix_block2 = np.multiply(action_matrix, block_mold1)
    story_matrix_block1 = np.multiply(story_matrix, block_mold2)
    story_matrix_block2 = np.multiply(story_matrix, block_mold1)

#treat the matrices so that they are in list form shuffled ready for experiment
#turn matrices into lists and remove zeros
action_list_block1 = list(action_matrix_block1.flatten())
action_list_block1 = np.asarray([x for x in action_list_block1 if x != 0])
action_list_block2 = list(action_matrix_block2.flatten())
action_list_block2 = np.asarray([x for x in action_list_block2 if x != 0])
story_list_block1 = list(story_matrix_block1.flatten())
story_list_block1 = np.asarray([x for x in story_list_block1 if x != 0])
story_list_block2 = list(story_matrix_block2.flatten())
print(story_list_block2)
story_list_block2 = np.asarray([x for x in story_list_block2 if x != 0])

#rand perm the lists, same block same randperm
randperm1 = np.random.permutation(8)
randperm2 = np.random.permutation(8)

action_list_block1 = action_list_block1[randperm1]
story_list_block1 = story_list_block1[randperm1]
action_list_block2 = action_list_block2[randperm2]
story_list_block2 = story_list_block2[randperm2]

#create a dictionary for all the stories and their values
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












text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, -.3), height=0.15, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, .25), size=(0.85, 0.75),
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
    text='Please indicate the order in which the questions appeared:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "perspective_test"
perspective_testClock = core.Clock()
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
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=(0, -.85), size=(0.25, 0.125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "p_again"
p_againClock = core.Clock()
text_49 = visual.TextStim(win=win, name='text_49',
    text='Here is the perspective one more time:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "perspective"
perspectiveClock = core.Clock()
import numpy as np
import random 

#make basic matrix of all stories
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

#construct the action matrix based on the inputted social and location perspectives
action_matrix = np.zeros(shape = [4, 4], dtype = int)
these_social_ps = [0,1]
these_location_ps = [0,1]

for i in range(2):
    action_matrix[these_social_ps[i],:] += 1
    action_matrix[:,these_location_ps[i]] += 2
    
action_matrix[action_matrix == 0] = 4

#construct the block molds
block_mold1 = np.array([[0, 1, 0, 1], [1,0,1,0],[0,1,0,1], [1,0,1,0]])
block_mold2 = np.array([[1,0,1,0],[0,1,0,1], [1,0,1,0],[0, 1, 0, 1]])
#randomly select a mold for the first half of the presented stories
flip = random.randint(0, 1)
print(flip)
if flip == 0:
    action_matrix_block1 = np.multiply(action_matrix, block_mold1)
    action_matrix_block2 = np.multiply(action_matrix, block_mold2)
    story_matrix_block1 = np.multiply(story_matrix, block_mold1)
    story_matrix_block2 = np.multiply(story_matrix, block_mold2)
else:
    action_matrix_block1 = np.multiply(action_matrix, block_mold2)
    action_matrix_block2 = np.multiply(action_matrix, block_mold1)
    story_matrix_block1 = np.multiply(story_matrix, block_mold2)
    story_matrix_block2 = np.multiply(story_matrix, block_mold1)

#treat the matrices so that they are in list form shuffled ready for experiment
#turn matrices into lists and remove zeros
action_list_block1 = list(action_matrix_block1.flatten())
action_list_block1 = np.asarray([x for x in action_list_block1 if x != 0])
action_list_block2 = list(action_matrix_block2.flatten())
action_list_block2 = np.asarray([x for x in action_list_block2 if x != 0])
story_list_block1 = list(story_matrix_block1.flatten())
story_list_block1 = np.asarray([x for x in story_list_block1 if x != 0])
story_list_block2 = list(story_matrix_block2.flatten())
print(story_list_block2)
story_list_block2 = np.asarray([x for x in story_list_block2 if x != 0])

#rand perm the lists, same block same randperm
randperm1 = np.random.permutation(8)
randperm2 = np.random.permutation(8)

action_list_block1 = action_list_block1[randperm1]
story_list_block1 = story_list_block1[randperm1]
action_list_block2 = action_list_block2[randperm2]
story_list_block2 = story_list_block2[randperm2]

#create a dictionary for all the stories and their values
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












text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, -.3), height=0.15, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, .25), size=(0.85, 0.75),
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

# Initialize components for Routine "story_begin"
story_beginClock = core.Clock()
text_50 = visual.TextStim(win=win, name='text_50',
    text='When you are ready, press the space bar to begin listening to the story. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "play_audio_story"
play_audio_storyClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
story_presses = keyboard.Keyboard()
text_34 = visual.TextStim(win=win, name='text_34',
    text="Press '9' if you think that sentence was the beginning of a new 'part' of the story.",
    font='Arial',
    pos=(.85, -.6), height=0.05, wrapWidth=.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_35 = visual.TextStim(win=win, name='text_35',
    text="Press '1' if you think that sentence was in the same 'part' of the story as the previous sentence. ",
    font='Arial',
    pos=(-.85, -.6), height=0.05, wrapWidth=.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "end_story"
end_storyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text='End of story',
    font='Arial',
    pos=(-.1, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_16 = keyboard.Keyboard()

# Initialize components for Routine "RECALL_BREAK"
RECALL_BREAKClock = core.Clock()
text_45 = visual.TextStim(win=win, name='text_45',
    text='Part 3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "recall_instructions"
recall_instructionsClock = core.Clock()
key_resp_2 = keyboard.Keyboard()
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
key_resp_10 = keyboard.Keyboard()
text_42 = visual.TextStim(win=win, name='text_42',
    text='Recall     out of 8',
    font='Arial',
    pos=(0.02, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_51 = visual.TextStim(win=win, name='text_51',
    text='(press the space bar to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

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
    win=win,
    name='image_4', 
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
Block1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('count_8.xlsx'),
    seed=None, name='Block1')
thisExp.addLoop(Block1)  # add the loop to the experiment
thisBlock1 = Block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

for thisBlock1 in Block1:
    currentLoop = Block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "storycount"-------
    # update component parameters for each repeat
    text_38.setText((count + 1))
    key_resp_8.keys = []
    key_resp_8.rt = []
    event.clearEvents()
    count_image = 0
    if action_list_block1[count] == 3:
        print(action_list_block1[count])
        Block1.finished = 1
        continueRoutine=False 
    # keep track of which components have finished
    storycountComponents = [text_38, key_resp_8, text_39]
    for thisComponent in storycountComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    storycountClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "storycount"-------
    while continueRoutine:
        # get current time
        t = storycountClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=storycountClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_38* updates
        if text_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_38.frameNStart = frameN  # exact frame index
            text_38.tStart = t  # local t and not account for scr refresh
            text_38.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_38, 'tStartRefresh')  # time at next scr refresh
            text_38.setAutoDraw(True)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_8.keys = theseKeys.name  # just the last key pressed
                key_resp_8.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_39* updates
        if text_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_39.frameNStart = frameN  # exact frame index
            text_39.tStart = t  # local t and not account for scr refresh
            text_39.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_39, 'tStartRefresh')  # time at next scr refresh
            text_39.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    Block1.addData('text_38.started', text_38.tStartRefresh)
    Block1.addData('text_38.stopped', text_38.tStopRefresh)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    Block1.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        Block1.addData('key_resp_8.rt', key_resp_8.rt)
    Block1.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    Block1.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    Block1.addData('text_39.started', text_39.tStartRefresh)
    Block1.addData('text_39.stopped', text_39.tStopRefresh)
    # the Routine "storycount" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ask_to_assume"-------
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    if action_list_block1[count] == 3 or 
    # keep track of which components have finished
    ask_to_assumeComponents = [text_33, key_resp_5]
    for thisComponent in ask_to_assumeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ask_to_assumeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ask_to_assume"-------
    while continueRoutine:
        # get current time
        t = ask_to_assumeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ask_to_assumeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_33* updates
        if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_33.frameNStart = frameN  # exact frame index
            text_33.tStart = t  # local t and not account for scr refresh
            text_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
            text_33.setAutoDraw(True)
        
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
        for key in event.getKeys():
            if key in ['q']: 
                trials.finished = 1
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    Block1.addData('text_33.started', text_33.tStartRefresh)
    Block1.addData('text_33.stopped', text_33.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    Block1.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        Block1.addData('key_resp_5.rt', key_resp_5.rt)
    Block1.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    Block1.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "ask_to_assume" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_7 = data.TrialHandler(nReps=7, method='sequential', 
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
        # update component parameters for each repeat
        event.clearEvents()
        #set the perspective
        #get the story file and the story pic
        this_story_file = storyDict.get(story_list_block1[count], {}).get('storyFile')
        this_story_pic = storyDict.get(story_list_block1[count], {}).get('pic')
        
        #if the action matrix determines '3' or '4'then no perspective 
        #and no perspective quiz
        if action_list_block1[count] == 4:
            print(action_list_block1[count])
            trials_7.finished = 1
            continueRoutine=False
        
        #select the perspective if the action matrix is '1' or '2'
        if action_list_block1[count] == 1 or action_list_block1[count] == 2:
            print(action_list_block1[count])
            this_perspective = storyDict.get(story_list_block1[count], {}).get(action_list_block1[count])
            if this_perspective == 'Couples Therapist':
                display_pic = 'jobphotos/couples.jpg'
                question1 = 'For how long has the initiator of the breakup been thinking about breaking up with his/her partner?'
                question2 ='What is the initial reason stated by the initiator for why he/she is breaking up?'
                question3 ='Does the person who is being broken up with want to break up, and what’s the reason stated by them for this?'
                question4 = 'Who wants what items back as a result of the breakup?'
                question5 = 'Does the person being broken up with expect that this is coming?'
                question6 = 'Who witnesses the breakup?'
            if this_perspective == 'Restaurant Critic':
                display_pic = 'jobphotos/restaurant_critic.jpg'
                question1 = 'How is the restaurant decorated?'
                question2 ='What are the menus like?'
                question3 = 'What does each client order?' 
                question4 = 'How do the clients like the food?'
                question5 = 'What meal is being served?'
                question6 = 'How old is the waiter?'
            if this_perspective == 'Airport Customer Experience Manager':
                display_pic = 'jobphotos/acem.jpg'
                question1 = 'When the clients arrive at the airport, how much time do they have until their flight departs?'
                question2 ='What is the reason for the hold-up at security?'
                question3 ='Toward which gate are the clients walking?'
                question4 ='What section and seat does each client sit in on the plane?' 
                question5 = 'Are the security guards friendly or rude?'
                question6 = 'Are the airport restrooms clean?'
            if this_perspective == 'Grocery Store Customer Experience Manager':
                display_pic = 'jobphotos/gscem.jpg'
                question1 = 'What is the grocery store like upon entering?'
                question2 ='What items do the clients pick out to buy?'
                question3 ='How many checkout lanes are open, and which one do the clients step into?'
                question4 = 'How much are the groceries, and what method of payment do the clients use?'
                question5 = 'How long does it take for the cashier to scan all of the customers’ groceries?'
                question6 = 'What type of grocery bags do the clients use?'
            if this_perspective == 'Dean of Academic Studies':
                display_pic ='jobphotos/dean.jpg'
                question1 = 'What is the lecture hall like?'
                question2 ='What class are the students in, and what is the day’s lecture about?'
                question3 ='What is something taught in lecture?'
                question4 = 'What is the next assessment/assignment for the class, and when is it scheduled/due?'
                question5 = 'Are the students paying attention?'
                question6 = 'Are the desks comfortable?'
            if this_perspective == 'Wedding Planner':
                display_pic = 'jobphotos/weddingplanner.jpg'
                question1 = 'For how long has the couple been dating?'
                question2 ='How many diamonds are on the ring, and what is the diamond color?'
                question3 ='In/on what item is the ring presented?'
                question4 = 'Who does the new fiancee text first?'
                question5 = 'Is anyone taking pictures of the proposal?'
                question6 = 'How long does the proposal take?'
            if this_perspective == 'Business Reporter':
                display_pic = 'jobphotos/business_reporter.jpg'
                question1 = 'What is each business person’s job title?'
                question2 = 'How much money is at stake in the initial offer made?'
                question3 = 'What is the name of the other industry competitor? '
                question4 =  'With what gesture do the business partners secure the deal?'
                question5 = 'Is the deal fair?'
                question6 =  'How long does it take to make the deal?'
            if this_perspective == 'Matchmaker':
                display_pic = 'jobphotos/matchmaker.jpg'
                question1 = 'What object is the initiator of the interaction holding when he/she first notices the other person?' 
                question2 ='What is the initial question that begins the conversation between the couple?'
                question3 ='When will be the next time the couple meets and for what occasion?'
                question4 = 'What time is it when the couple parts?'
                question5 = 'Is the couple going to get married?'
                question6 = 'Who shows more interest?'
        
        
        
        
        
        
        
        text_4.setText(this_perspective)
        image.setImage(display_pic)
        # keep track of which components have finished
        perspectiveComponents = [text_4, image, text_5]
        for thisComponent in perspectiveComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        perspectiveClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "perspective"-------
        while continueRoutine:
            # get current time
            t = perspectiveClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=perspectiveClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            for key in event.getKeys():
                if key in ['space']: 
                    continueRoutine = False
                if key in ['q']: 
                    trials.finished = 1
                    continueRoutine = False
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_7.addData('text_4.started', text_4.tStartRefresh)
        trials_7.addData('text_4.stopped', text_4.tStopRefresh)
        trials_7.addData('image.started', image.tStartRefresh)
        trials_7.addData('image.stopped', image.tStopRefresh)
        trials_7.addData('text_5.started', text_5.tStartRefresh)
        trials_7.addData('text_5.stopped', text_5.tStopRefresh)
        # the Routine "perspective" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "intro_test"-------
        # update component parameters for each repeat
        key_resp_7.keys = []
        key_resp_7.rt = []
        # keep track of which components have finished
        intro_testComponents = [text_37, key_resp_7]
        for thisComponent in intro_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intro_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "intro_test"-------
        while continueRoutine:
            # get current time
            t = intro_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intro_testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_37* updates
            if text_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_37.frameNStart = frameN  # exact frame index
                text_37.tStart = t  # local t and not account for scr refresh
                text_37.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
                text_37.setAutoDraw(True)
            
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
        trials_7.addData('text_37.started', text_37.tStartRefresh)
        trials_7.addData('text_37.stopped', text_37.tStopRefresh)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_7.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_7.addData('key_resp_7.rt', key_resp_7.rt)
        trials_7.addData('key_resp_7.started', key_resp_7.tStartRefresh)
        trials_7.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
        # the Routine "intro_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "perspective_test"-------
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
        perspective_testComponents = [question1_2, question2_2, question3_2, question4_2, question5_2, question6_2, image_15]
        for thisComponent in perspective_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        perspective_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "perspective_test"-------
        while continueRoutine:
            # get current time
            t = perspective_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=perspective_testClock)
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
                this_image = 'icon/bar5.jpg'
            
            if checkCount == 1:
                this_image = 'icon/bar2.png'
            if checkCount == 2: 
                this_image = 'icon/bar3.jpg'
            if checkCount == 3:
                this_image = 'icon/bar4.png'
            
            # *image_15* updates
            if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_15.frameNStart = frameN  # exact frame index
                image_15.tStart = t  # local t and not account for scr refresh
                image_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
                image_15.setAutoDraw(True)
            if image_15.status == STARTED:  # only update if drawing
                image_15.setImage(this_image, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        trials_7.addData('question1_2.started', question1_2.tStartRefresh)
        trials_7.addData('question1_2.stopped', question1_2.tStopRefresh)
        trials_7.addData('question2_2.started', question2_2.tStartRefresh)
        trials_7.addData('question2_2.stopped', question2_2.tStopRefresh)
        trials_7.addData('question3_2.started', question3_2.tStartRefresh)
        trials_7.addData('question3_2.stopped', question3_2.tStopRefresh)
        trials_7.addData('question4_2.started', question4_2.tStartRefresh)
        trials_7.addData('question4_2.stopped', question4_2.tStopRefresh)
        trials_7.addData('question5_2.started', question5_2.tStartRefresh)
        trials_7.addData('question5_2.stopped', question5_2.tStopRefresh)
        trials_7.addData('question6_2.started', question6_2.tStartRefresh)
        trials_7.addData('question6_2.stopped', question6_2.tStopRefresh)
        trials_7.addData('image_15.started', image_15.tStartRefresh)
        trials_7.addData('image_15.stopped', image_15.tStopRefresh)
        # the Routine "perspective_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 7 repeats of 'trials_7'
    
    
    # ------Prepare to start Routine "p_again"-------
    # update component parameters for each repeat
    key_resp_15.keys = []
    key_resp_15.rt = []
    # keep track of which components have finished
    p_againComponents = [text_49, key_resp_15]
    for thisComponent in p_againComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    p_againClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "p_again"-------
    while continueRoutine:
        # get current time
        t = p_againClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=p_againClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_49* updates
        if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_49.frameNStart = frameN  # exact frame index
            text_49.tStart = t  # local t and not account for scr refresh
            text_49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
            text_49.setAutoDraw(True)
        
        # *key_resp_15* updates
        waitOnFlip = False
        if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.tStart = t  # local t and not account for scr refresh
            key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_15.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_15.keys = theseKeys.name  # just the last key pressed
                key_resp_15.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in p_againComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "p_again"-------
    for thisComponent in p_againComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1.addData('text_49.started', text_49.tStartRefresh)
    Block1.addData('text_49.stopped', text_49.tStopRefresh)
    # check responses
    if key_resp_15.keys in ['', [], None]:  # No response was made
        key_resp_15.keys = None
    Block1.addData('key_resp_15.keys',key_resp_15.keys)
    if key_resp_15.keys != None:  # we had a response
        Block1.addData('key_resp_15.rt', key_resp_15.rt)
    Block1.addData('key_resp_15.started', key_resp_15.tStartRefresh)
    Block1.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
    # the Routine "p_again" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "perspective"-------
    # update component parameters for each repeat
    event.clearEvents()
    #set the perspective
    #get the story file and the story pic
    this_story_file = storyDict.get(story_list_block1[count], {}).get('storyFile')
    this_story_pic = storyDict.get(story_list_block1[count], {}).get('pic')
    
    #if the action matrix determines '3' or '4'then no perspective 
    #and no perspective quiz
    if action_list_block1[count] == 4:
        print(action_list_block1[count])
        trials_7.finished = 1
        continueRoutine=False
    
    #select the perspective if the action matrix is '1' or '2'
    if action_list_block1[count] == 1 or action_list_block1[count] == 2:
        print(action_list_block1[count])
        this_perspective = storyDict.get(story_list_block1[count], {}).get(action_list_block1[count])
        if this_perspective == 'Couples Therapist':
            display_pic = 'jobphotos/couples.jpg'
            question1 = 'For how long has the initiator of the breakup been thinking about breaking up with his/her partner?'
            question2 ='What is the initial reason stated by the initiator for why he/she is breaking up?'
            question3 ='Does the person who is being broken up with want to break up, and what’s the reason stated by them for this?'
            question4 = 'Who wants what items back as a result of the breakup?'
            question5 = 'Does the person being broken up with expect that this is coming?'
            question6 = 'Who witnesses the breakup?'
        if this_perspective == 'Restaurant Critic':
            display_pic = 'jobphotos/restaurant_critic.jpg'
            question1 = 'How is the restaurant decorated?'
            question2 ='What are the menus like?'
            question3 = 'What does each client order?' 
            question4 = 'How do the clients like the food?'
            question5 = 'What meal is being served?'
            question6 = 'How old is the waiter?'
        if this_perspective == 'Airport Customer Experience Manager':
            display_pic = 'jobphotos/acem.jpg'
            question1 = 'When the clients arrive at the airport, how much time do they have until their flight departs?'
            question2 ='What is the reason for the hold-up at security?'
            question3 ='Toward which gate are the clients walking?'
            question4 ='What section and seat does each client sit in on the plane?' 
            question5 = 'Are the security guards friendly or rude?'
            question6 = 'Are the airport restrooms clean?'
        if this_perspective == 'Grocery Store Customer Experience Manager':
            display_pic = 'jobphotos/gscem.jpg'
            question1 = 'What is the grocery store like upon entering?'
            question2 ='What items do the clients pick out to buy?'
            question3 ='How many checkout lanes are open, and which one do the clients step into?'
            question4 = 'How much are the groceries, and what method of payment do the clients use?'
            question5 = 'How long does it take for the cashier to scan all of the customers’ groceries?'
            question6 = 'What type of grocery bags do the clients use?'
        if this_perspective == 'Dean of Academic Studies':
            display_pic ='jobphotos/dean.jpg'
            question1 = 'What is the lecture hall like?'
            question2 ='What class are the students in, and what is the day’s lecture about?'
            question3 ='What is something taught in lecture?'
            question4 = 'What is the next assessment/assignment for the class, and when is it scheduled/due?'
            question5 = 'Are the students paying attention?'
            question6 = 'Are the desks comfortable?'
        if this_perspective == 'Wedding Planner':
            display_pic = 'jobphotos/weddingplanner.jpg'
            question1 = 'For how long has the couple been dating?'
            question2 ='How many diamonds are on the ring, and what is the diamond color?'
            question3 ='In/on what item is the ring presented?'
            question4 = 'Who does the new fiancee text first?'
            question5 = 'Is anyone taking pictures of the proposal?'
            question6 = 'How long does the proposal take?'
        if this_perspective == 'Business Reporter':
            display_pic = 'jobphotos/business_reporter.jpg'
            question1 = 'What is each business person’s job title?'
            question2 = 'How much money is at stake in the initial offer made?'
            question3 = 'What is the name of the other industry competitor? '
            question4 =  'With what gesture do the business partners secure the deal?'
            question5 = 'Is the deal fair?'
            question6 =  'How long does it take to make the deal?'
        if this_perspective == 'Matchmaker':
            display_pic = 'jobphotos/matchmaker.jpg'
            question1 = 'What object is the initiator of the interaction holding when he/she first notices the other person?' 
            question2 ='What is the initial question that begins the conversation between the couple?'
            question3 ='When will be the next time the couple meets and for what occasion?'
            question4 = 'What time is it when the couple parts?'
            question5 = 'Is the couple going to get married?'
            question6 = 'Who shows more interest?'
    
    
    
    
    
    
    
    text_4.setText(this_perspective)
    image.setImage(display_pic)
    # keep track of which components have finished
    perspectiveComponents = [text_4, image, text_5]
    for thisComponent in perspectiveComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    perspectiveClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "perspective"-------
    while continueRoutine:
        # get current time
        t = perspectiveClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=perspectiveClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        for key in event.getKeys():
            if key in ['space']: 
                continueRoutine = False
            if key in ['q']: 
                trials.finished = 1
                continueRoutine = False
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    Block1.addData('text_4.started', text_4.tStartRefresh)
    Block1.addData('text_4.stopped', text_4.tStopRefresh)
    Block1.addData('image.started', image.tStartRefresh)
    Block1.addData('image.stopped', image.tStopRefresh)
    Block1.addData('text_5.started', text_5.tStartRefresh)
    Block1.addData('text_5.stopped', text_5.tStopRefresh)
    # the Routine "perspective" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "story_begin"-------
    # update component parameters for each repeat
    key_resp_14.keys = []
    key_resp_14.rt = []
    # keep track of which components have finished
    story_beginComponents = [text_50, key_resp_14]
    for thisComponent in story_beginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    story_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "story_begin"-------
    while continueRoutine:
        # get current time
        t = story_beginClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=story_beginClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_50* updates
        if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_50.frameNStart = frameN  # exact frame index
            text_50.tStart = t  # local t and not account for scr refresh
            text_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
            text_50.setAutoDraw(True)
        
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
        for thisComponent in story_beginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "story_begin"-------
    for thisComponent in story_beginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1.addData('text_50.started', text_50.tStartRefresh)
    Block1.addData('text_50.stopped', text_50.tStopRefresh)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
    Block1.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        Block1.addData('key_resp_14.rt', key_resp_14.rt)
    Block1.addData('key_resp_14.started', key_resp_14.tStartRefresh)
    Block1.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
    # the Routine "story_begin" was not non-slip safe, so reset the non-slip timer
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
        
        # ------Prepare to start Routine "play_audio_story"-------
        # update component parameters for each repeat
        if action_list_block1[count] == 3:
            continueRoutine = False
        
        start_time = globalClock.getTime()
        m=mom.media_new(audio)
        p.set_media(m)
        p.play()
        stim = visual.ImageStim(win, image=this_story_pic)
        stim.draw()
        while p.is_playing() or (globalClock.getTime()-start_time < 2):
           stim.draw()
           win.flip()
        
        p.stop()
        
        continueRoutine=False
        # keep track of which components have finished
        play_audio_storyComponents = []
        for thisComponent in play_audio_storyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        play_audio_storyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "play_audio_story"-------
        while continueRoutine:
            # get current time
            t = play_audio_storyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=play_audio_storyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if event.getKeys(['q']):
                continueRoutine=False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in play_audio_storyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "play_audio_story"-------
        for thisComponent in play_audio_storyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "play_audio_story" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        # update component parameters for each repeat
        story_presses.keys = []
        story_presses.rt = []
        event.clearEvents()
        stim = visual.ImageStim(win, image=this_story_pic)
        
        # keep track of which components have finished
        trialComponents = [story_presses, text_34, text_35]
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
            
            # *story_presses* updates
            waitOnFlip = False
            if story_presses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                story_presses.frameNStart = frameN  # exact frame index
                story_presses.tStart = t  # local t and not account for scr refresh
                story_presses.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(story_presses, 'tStartRefresh')  # time at next scr refresh
                story_presses.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(story_presses.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(story_presses.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if story_presses.status == STARTED and not waitOnFlip:
                theseKeys = story_presses.getKeys(keyList=['1', '9'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if story_presses.keys == []:  # then this was the first keypress
                        story_presses.keys = theseKeys.name  # just the first key pressed
                        story_presses.rt = theseKeys.rt
                        # a response ends the routine
                        continueRoutine = False
            stim.draw()
            
            for key in event.getKeys():
                if key in ['t']: 
                    trials_2.finished = 1
                    continueRoutine = False
            
            # *text_34* updates
            if text_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_34.frameNStart = frameN  # exact frame index
                text_34.tStart = t  # local t and not account for scr refresh
                text_34.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_34, 'tStartRefresh')  # time at next scr refresh
                text_34.setAutoDraw(True)
            
            # *text_35* updates
            if text_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_35.frameNStart = frameN  # exact frame index
                text_35.tStart = t  # local t and not account for scr refresh
                text_35.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_35, 'tStartRefresh')  # time at next scr refresh
                text_35.setAutoDraw(True)
            
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
        # check responses
        if story_presses.keys in ['', [], None]:  # No response was made
            story_presses.keys = None
        trials_2.addData('story_presses.keys',story_presses.keys)
        if story_presses.keys != None:  # we had a response
            trials_2.addData('story_presses.rt', story_presses.rt)
        trials_2.addData('story_presses.started', story_presses.tStartRefresh)
        trials_2.addData('story_presses.stopped', story_presses.tStopRefresh)
        trials_2.addData('text_34.started', text_34.tStartRefresh)
        trials_2.addData('text_34.stopped', text_34.tStopRefresh)
        trials_2.addData('text_35.started', text_35.tStartRefresh)
        trials_2.addData('text_35.stopped', text_35.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    
    # ------Prepare to start Routine "end_story"-------
    # update component parameters for each repeat
    text.setText((count + 1))
    key_resp_16.keys = []
    key_resp_16.rt = []
    # keep track of which components have finished
    end_storyComponents = [text, text_52, key_resp_16]
    for thisComponent in end_storyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_storyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "end_story"-------
    while continueRoutine:
        # get current time
        t = end_storyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_storyClock)
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
        
        # *text_52* updates
        if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_52.frameNStart = frameN  # exact frame index
            text_52.tStart = t  # local t and not account for scr refresh
            text_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
            text_52.setAutoDraw(True)
        
        # *key_resp_16* updates
        waitOnFlip = False
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_16.keys = theseKeys.name  # just the last key pressed
                key_resp_16.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_storyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_story"-------
    for thisComponent in end_storyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1.addData('text.started', text.tStartRefresh)
    Block1.addData('text.stopped', text.tStopRefresh)
    Block1.addData('text_52.started', text_52.tStartRefresh)
    Block1.addData('text_52.stopped', text_52.tStopRefresh)
    # check responses
    if key_resp_16.keys in ['', [], None]:  # No response was made
        key_resp_16.keys = None
    Block1.addData('key_resp_16.keys',key_resp_16.keys)
    if key_resp_16.keys != None:  # we had a response
        Block1.addData('key_resp_16.rt', key_resp_16.rt)
    Block1.addData('key_resp_16.started', key_resp_16.tStartRefresh)
    Block1.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
    # the Routine "end_story" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block1'


# ------Prepare to start Routine "RECALL_BREAK"-------
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
story_time = timer.getTime()
thisExp.addData('story time', story_time)
# keep track of which components have finished
RECALL_BREAKComponents = [text_45, key_resp_6]
for thisComponent in RECALL_BREAKComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RECALL_BREAKClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "RECALL_BREAK"-------
while continueRoutine:
    # get current time
    t = RECALL_BREAKClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RECALL_BREAKClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_45* updates
    if text_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_45.frameNStart = frameN  # exact frame index
        text_45.tStart = t  # local t and not account for scr refresh
        text_45.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
        text_45.setAutoDraw(True)
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
thisExp.addData('text_45.started', text_45.tStartRefresh)
thisExp.addData('text_45.stopped', text_45.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
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
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    text_6.setText(instructText)
    # keep track of which components have finished
    recall_instructionsComponents = [key_resp_2, text_6, text_24]
    for thisComponent in recall_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recall_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "recall_instructions"-------
    while continueRoutine:
        # get current time
        t = recall_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recall_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            text_24.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
        key_resp_2.keys = None
    trials_3.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_3.addData('key_resp_2.rt', key_resp_2.rt)
    trials_3.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials_3.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    trials_3.addData('text_6.started', text_6.tStartRefresh)
    trials_3.addData('text_6.stopped', text_6.tStopRefresh)
    trials_3.addData('text_24.started', text_24.tStartRefresh)
    trials_3.addData('text_24.stopped', text_24.tStopRefresh)
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
    # update component parameters for each repeat
    text_41.setText((count + 1))
    key_resp_10.keys = []
    key_resp_10.rt = []
    # keep track of which components have finished
    recallcount_2Components = [text_41, key_resp_10, text_42, text_51]
    for thisComponent in recallcount_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recallcount_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "recallcount_2"-------
    while continueRoutine:
        # get current time
        t = recallcount_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recallcount_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_41* updates
        if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_41.frameNStart = frameN  # exact frame index
            text_41.tStart = t  # local t and not account for scr refresh
            text_41.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
            text_41.setAutoDraw(True)
        
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
        
        # *text_42* updates
        if text_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_42.frameNStart = frameN  # exact frame index
            text_42.tStart = t  # local t and not account for scr refresh
            text_42.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
            text_42.setAutoDraw(True)
        
        # *text_51* updates
        if text_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_51.frameNStart = frameN  # exact frame index
            text_51.tStart = t  # local t and not account for scr refresh
            text_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_51, 'tStartRefresh')  # time at next scr refresh
            text_51.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    trials_4.addData('text_41.started', text_41.tStartRefresh)
    trials_4.addData('text_41.stopped', text_41.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    trials_4.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        trials_4.addData('key_resp_10.rt', key_resp_10.rt)
    trials_4.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    trials_4.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    trials_4.addData('text_42.started', text_42.tStartRefresh)
    trials_4.addData('text_42.stopped', text_42.tStopRefresh)
    trials_4.addData('text_51.started', text_51.tStartRefresh)
    trials_4.addData('text_51.stopped', text_51.tStopRefresh)
    # the Routine "recallcount_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "recall_3"-------
    # update component parameters for each repeat
    event.clearEvents()
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
    countdownClock = core.CountdownTimer(300) # 300 s = 5 minutes  countdownStarted = True 
    timeText = '5:00' 
    # keep track of which components have finished
    recall_3Components = [text_9, text_10, image_4, polygon, bottom_line, right_line_2, left_line, text_48]
    for thisComponent in recall_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recall_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "recall_3"-------
    while continueRoutine:
        # get current time
        t = recall_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recall_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
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
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:  # only update if drawing
            text_10.setText(captured_string, log=False)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        
        # *bottom_line* updates
        if bottom_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottom_line.frameNStart = frameN  # exact frame index
            bottom_line.tStart = t  # local t and not account for scr refresh
            bottom_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_line, 'tStartRefresh')  # time at next scr refresh
            bottom_line.setAutoDraw(True)
        
        # *right_line_2* updates
        if right_line_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_line_2.frameNStart = frameN  # exact frame index
            right_line_2.tStart = t  # local t and not account for scr refresh
            right_line_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_line_2, 'tStartRefresh')  # time at next scr refresh
            right_line_2.setAutoDraw(True)
        
        # *left_line* updates
        if left_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_line.frameNStart = frameN  # exact frame index
            left_line.tStart = t  # local t and not account for scr refresh
            left_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_line, 'tStartRefresh')  # time at next scr refresh
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
        if text_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_48.frameNStart = frameN  # exact frame index
            text_48.tStart = t  # local t and not account for scr refresh
            text_48.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_48, 'tStartRefresh')  # time at next scr refresh
            text_48.setAutoDraw(True)
        if text_48.status == STARTED:  # only update if drawing
            text_48.setText(timeText, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    trials_4.addData('text_9.started', text_9.tStartRefresh)
    trials_4.addData('text_9.stopped', text_9.tStopRefresh)
    trials_4.addData('text_10.started', text_10.tStartRefresh)
    trials_4.addData('text_10.stopped', text_10.tStopRefresh)
    trials_4.addData('image_4.started', image_4.tStartRefresh)
    trials_4.addData('image_4.stopped', image_4.tStopRefresh)
    trials_4.addData('polygon.started', polygon.tStartRefresh)
    trials_4.addData('polygon.stopped', polygon.tStopRefresh)
    trials_4.addData('bottom_line.started', bottom_line.tStartRefresh)
    trials_4.addData('bottom_line.stopped', bottom_line.tStopRefresh)
    trials_4.addData('right_line_2.started', right_line_2.tStartRefresh)
    trials_4.addData('right_line_2.stopped', right_line_2.tStopRefresh)
    trials_4.addData('left_line.started', left_line.tStartRefresh)
    trials_4.addData('left_line.stopped', left_line.tStopRefresh)
    trials_4.addData('text_48.started', text_48.tStartRefresh)
    trials_4.addData('text_48.stopped', text_48.tStopRefresh)
    # the Routine "recall_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


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
    routineTimer.add(1.000000)
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
            if tThisFlipGlobal > text_36.tStartRefresh + 1.0-frameTolerance:
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
    
# completed 5 repeats of 'trials_8'


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
