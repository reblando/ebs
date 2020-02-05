#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.1),
    on Wed Feb  5 15:37:56 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, microphone
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
expName = 'listening_fmri'  # from the Builder filename that created this script
expInfo = {'participant': 'test', 'sA': '0', 'sB': '1', 'lA': '0', 'lB': '1', 'block_struct': '1', 'play_stories': '0', 'block': '1', 'behavioral': '0', 'random_seed': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_bk%s_%s' % (expInfo['participant'],expInfo['block'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexreblando/Documents/GitHub/ebs/fMRI experiment/psychopy code/1_listening_fMRI.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
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

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

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

#shuffling the story and action lists
randperm1 = np.random.RandomState(seed=int(expInfo['random_seed'])).permutation(8)
randperm2 = np.random.RandomState(seed= (int(expInfo['random_seed']) + 1)).permutation(8)

if int(expInfo['block']) == 1:
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
else: 
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














# Initialize components for Routine "listening_instructions_block1"
listening_instructions_block1Clock = core.Clock()
key_resp_5 = keyboard.Keyboard()
text_87 = visual.TextStim(win=win, name='text_87',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_88 = visual.TextStim(win=win, name='text_88',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "left_hand"
left_handClock = core.Clock()
key_resp_31 = keyboard.Keyboard()
text_89 = visual.TextStim(win=win, name='text_89',
    text='The numbers "1", "2", and "3" correspond to the first three fingers on your left hand. ',
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_27 = visual.ImageStim(
    win=win,
    name='image_27', 
    image='icon/lefthand.png', mask=None,
    ori=0, pos=(-.5, .2), size=(0.6, 1.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_97 = visual.TextStim(win=win, name='text_97',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "right_hand"
right_handClock = core.Clock()
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='icon/righthand.png', mask=None,
    ori=0, pos=(.5, .2), size=(0.6, 1.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_21 = keyboard.Keyboard()
text_78 = visual.TextStim(win=win, name='text_78',
    text='The numbers "4", "5", and "6" correspond to the first three fingers on your right hand. ',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_96 = visual.TextStim(win=win, name='text_96',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_28 = visual.ImageStim(
    win=win,
    name='image_28', 
    image='icon/lefthand.png', mask=None,
    ori=0, pos=(-.5, .2), size=(0.6, 1.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "practice_presses"
practice_pressesClock = core.Clock()
key_resp_36 = keyboard.Keyboard()
text_94 = visual.TextStim(win=win, name='text_94',
    text="We'll do a quick practice to get familiar with this. Press the button that appears on the screen.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_95 = visual.TextStim(win=win, name='text_95',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "test4"
test4Clock = core.Clock()
text_90 = visual.TextStim(win=win, name='text_90',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_32 = keyboard.Keyboard()

# Initialize components for Routine "test1"
test1Clock = core.Clock()
text_91 = visual.TextStim(win=win, name='text_91',
    text='1',
    font='Arial',
    pos=(0, 0), height=.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_33 = keyboard.Keyboard()

# Initialize components for Routine "test3"
test3Clock = core.Clock()
text_92 = visual.TextStim(win=win, name='text_92',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_34 = keyboard.Keyboard()

# Initialize components for Routine "test5"
test5Clock = core.Clock()
text_93 = visual.TextStim(win=win, name='text_93',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_35 = keyboard.Keyboard()

# Initialize components for Routine "good_job"
good_jobClock = core.Clock()
text_98 = visual.TextStim(win=win, name='text_98',
    text='Good job! We will begin the experiment now.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_99 = visual.TextStim(win=win, name='text_99',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_37 = keyboard.Keyboard()

# Initialize components for Routine "Trigger"
TriggerClock = core.Clock()
textTrigger = visual.TextStim(win=win, name='textTrigger',
    text='waiting for the scanner',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
getTrigger = keyboard.Keyboard()
text_76 = visual.TextStim(win=win, name='text_76',
    text='Block    of Story Listening',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_77 = visual.TextStim(win=win, name='text_77',
    text=(int(expInfo['block'])),
    font='Arial',
    pos=(-.16, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "routine_6sec_wait"
routine_6sec_waitClock = core.Clock()
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "info"
infoClock = core.Clock()

# Initialize components for Routine "storycount"
storycountClock = core.Clock()

story_count = 0


text_38 = visual.TextStim(win=win, name='text_38',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_8 = keyboard.Keyboard()
text_39 = visual.TextStim(win=win, name='text_39',
    text='Story     out of 6',
    font='Arial',
    pos=(0.03, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text = visual.TextStim(win=win, name='text',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ask_to_assume"
ask_to_assumeClock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='Please assume the perspective of:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_30 = keyboard.Keyboard()
text_79 = visual.TextStim(win=win, name='text_79',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "perspective"
perspectiveClock = core.Clock()







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
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_22 = keyboard.Keyboard()

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
text_80 = visual.TextStim(win=win, name='text_80',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "perspective_test"
perspective_testClock = core.Clock()
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
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
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
    depth=-1.0);
key_resp_15 = keyboard.Keyboard()
text_81 = visual.TextStim(win=win, name='text_81',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "perspective"
perspectiveClock = core.Clock()







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
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_22 = keyboard.Keyboard()

# Initialize components for Routine "story_begin"
story_beginClock = core.Clock()
text_50 = visual.TextStim(win=win, name='text_50',
    text='When you are ready, press any button to begin listening to the story. ',
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

# Initialize components for Routine "show_image_3sec"
show_image_3secClock = core.Clock()

# Initialize components for Routine "play_audio_story"
play_audio_storyClock = core.Clock()

# Initialize components for Routine "show_storyimage1"
show_storyimage1Clock = core.Clock()
key_resp_28 = keyboard.Keyboard()
image_21 = visual.ImageStim(
    win=win,
    name='image_21', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "routine_6sec_wait"
routine_6sec_waitClock = core.Clock()
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "end_story"
end_storyClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
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

# Initialize components for Routine "Trigger"
TriggerClock = core.Clock()
textTrigger = visual.TextStim(win=win, name='textTrigger',
    text='waiting for the scanner',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
getTrigger = keyboard.Keyboard()
text_76 = visual.TextStim(win=win, name='text_76',
    text='Block    of Story Listening',
    font='Arial',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_77 = visual.TextStim(win=win, name='text_77',
    text=(int(expInfo['block'])),
    font='Arial',
    pos=(-.16, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "routine_6sec_wait"
routine_6sec_waitClock = core.Clock()
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "info_2"
info_2Clock = core.Clock()

# Initialize components for Routine "storycount_2"
storycount_2Clock = core.Clock()
text_55 = visual.TextStim(win=win, name='text_55',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_56 = visual.TextStim(win=win, name='text_56',
    text='Story     out of 6',
    font='Arial',
    pos=(0.03, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()
text_82 = visual.TextStim(win=win, name='text_82',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ask_to_assume_2"
ask_to_assume_2Clock = core.Clock()
text_57 = visual.TextStim(win=win, name='text_57',
    text='Please assume the perspective of:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_17 = keyboard.Keyboard()
text_83 = visual.TextStim(win=win, name='text_83',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "perspective_2"
perspective_2Clock = core.Clock()
text_60 = visual.TextStim(win=win, name='text_60',
    text='default text',
    font='Arial',
    pos=(0, -.3), height=0.15, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, .25), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_58 = visual.TextStim(win=win, name='text_58',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_23 = keyboard.Keyboard()

# Initialize components for Routine "intro_test_2"
intro_test_2Clock = core.Clock()
text_62 = visual.TextStim(win=win, name='text_62',
    text='Please indicate the order in which the questions appeared:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_18 = keyboard.Keyboard()
text_84 = visual.TextStim(win=win, name='text_84',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "perspective_test_4"
perspective_test_4Clock = core.Clock()
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

# Initialize components for Routine "p_again_2"
p_again_2Clock = core.Clock()
text_59 = visual.TextStim(win=win, name='text_59',
    text='Here is the perspective one more time:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_19 = keyboard.Keyboard()
text_85 = visual.TextStim(win=win, name='text_85',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "perspective_3"
perspective_3Clock = core.Clock()







text_61 = visual.TextStim(win=win, name='text_61',
    text='default text',
    font='Arial',
    pos=(0, -.3), height=0.15, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='sin', mask=None,
    ori=0, pos=(0, .25), size=(0.85, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_63 = visual.TextStim(win=win, name='text_63',
    text='(press any button to continue)',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_24 = keyboard.Keyboard()

# Initialize components for Routine "story_begin_2"
story_begin_2Clock = core.Clock()
text_64 = visual.TextStim(win=win, name='text_64',
    text='When you are ready, press any button to begin listening to the story. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()

# Initialize components for Routine "play_audio_story_2"
play_audio_story_2Clock = core.Clock()

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
story_presses_2 = keyboard.Keyboard()
text_65 = visual.TextStim(win=win, name='text_65',
    text="Press '9' if you think that sentence was the beginning of a new 'part' of the story.",
    font='Arial',
    pos=(.85, -.6), height=0.05, wrapWidth=.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_66 = visual.TextStim(win=win, name='text_66',
    text="Press '1' if you think that sentence was in the same 'part' of the story as the previous sentence. ",
    font='Arial',
    pos=(-.85, -.6), height=0.05, wrapWidth=.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "show_image_3sec"
show_image_3secClock = core.Clock()

# Initialize components for Routine "play_audio_story_2"
play_audio_story_2Clock = core.Clock()

# Initialize components for Routine "show_storyimage2"
show_storyimage2Clock = core.Clock()
key_resp_29 = keyboard.Keyboard()
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "routine_6sec_wait"
routine_6sec_waitClock = core.Clock()
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "end_story_2"
end_story_2Clock = core.Clock()
text_67 = visual.TextStim(win=win, name='text_67',
    text='default text',
    font='Arial',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_68 = visual.TextStim(win=win, name='text_68',
    text='End of story',
    font='Arial',
    pos=(-.1, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_of_task"
end_of_taskClock = core.Clock()
text_36 = visual.TextStim(win=win, name='text_36',
    text='End of the block. Please wait for your experimenter',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Startup"-------
# update component parameters for each repeat
# keep track of which components have finished
StartupComponents = []
for thisComponent in StartupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Startup"-------
while continueRoutine:
    # get current time
    t = StartupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartupClock)
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
    for thisComponent in StartupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Startup"-------
for thisComponent in StartupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Startup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_14 = data.TrialHandler(nReps=block1_play, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_14')
thisExp.addLoop(trials_14)  # add the loop to the experiment
thisTrial_14 = trials_14.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
if thisTrial_14 != None:
    for paramName in thisTrial_14:
        exec('{} = thisTrial_14[paramName]'.format(paramName))

for thisTrial_14 in trials_14:
    currentLoop = trials_14
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
    if thisTrial_14 != None:
        for paramName in thisTrial_14:
            exec('{} = thisTrial_14[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_13 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('listening_instructions.xlsx'),
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
        
        # ------Prepare to start Routine "listening_instructions_block1"-------
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        text_87.setText((instructions))
        # keep track of which components have finished
        listening_instructions_block1Components = [key_resp_5, text_87, text_88]
        for thisComponent in listening_instructions_block1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        listening_instructions_block1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "listening_instructions_block1"-------
        while continueRoutine:
            # get current time
            t = listening_instructions_block1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=listening_instructions_block1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = key_resp_5.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_5.keys = theseKeys.name  # just the last key pressed
                    key_resp_5.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_87* updates
            if text_87.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_87.frameNStart = frameN  # exact frame index
                text_87.tStart = t  # local t and not account for scr refresh
                text_87.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_87, 'tStartRefresh')  # time at next scr refresh
                text_87.setAutoDraw(True)
            
            # *text_88* updates
            if text_88.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_88.frameNStart = frameN  # exact frame index
                text_88.tStart = t  # local t and not account for scr refresh
                text_88.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_88, 'tStartRefresh')  # time at next scr refresh
                text_88.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in listening_instructions_block1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "listening_instructions_block1"-------
        for thisComponent in listening_instructions_block1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials_13.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials_13.addData('key_resp_5.rt', key_resp_5.rt)
        trials_13.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        trials_13.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        trials_13.addData('text_87.started', text_87.tStartRefresh)
        trials_13.addData('text_87.stopped', text_87.tStopRefresh)
        trials_13.addData('text_88.started', text_88.tStartRefresh)
        trials_13.addData('text_88.stopped', text_88.tStopRefresh)
        # the Routine "listening_instructions_block1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_13'
    
    
    # ------Prepare to start Routine "left_hand"-------
    # update component parameters for each repeat
    key_resp_31.keys = []
    key_resp_31.rt = []
    # keep track of which components have finished
    left_handComponents = [key_resp_31, text_89, image_27, text_97]
    for thisComponent in left_handComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    left_handClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "left_hand"-------
    while continueRoutine:
        # get current time
        t = left_handClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=left_handClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_31* updates
        waitOnFlip = False
        if key_resp_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_31.frameNStart = frameN  # exact frame index
            key_resp_31.tStart = t  # local t and not account for scr refresh
            key_resp_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_31, 'tStartRefresh')  # time at next scr refresh
            key_resp_31.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_31.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_31.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_31.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_31.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_31.keys = theseKeys.name  # just the last key pressed
                key_resp_31.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_89* updates
        if text_89.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_89.frameNStart = frameN  # exact frame index
            text_89.tStart = t  # local t and not account for scr refresh
            text_89.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_89, 'tStartRefresh')  # time at next scr refresh
            text_89.setAutoDraw(True)
        
        # *image_27* updates
        if image_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_27.frameNStart = frameN  # exact frame index
            image_27.tStart = t  # local t and not account for scr refresh
            image_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_27, 'tStartRefresh')  # time at next scr refresh
            image_27.setAutoDraw(True)
        
        # *text_97* updates
        if text_97.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_97.frameNStart = frameN  # exact frame index
            text_97.tStart = t  # local t and not account for scr refresh
            text_97.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_97, 'tStartRefresh')  # time at next scr refresh
            text_97.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in left_handComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "left_hand"-------
    for thisComponent in left_handComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_31.keys in ['', [], None]:  # No response was made
        key_resp_31.keys = None
    trials_14.addData('key_resp_31.keys',key_resp_31.keys)
    if key_resp_31.keys != None:  # we had a response
        trials_14.addData('key_resp_31.rt', key_resp_31.rt)
    trials_14.addData('key_resp_31.started', key_resp_31.tStartRefresh)
    trials_14.addData('key_resp_31.stopped', key_resp_31.tStopRefresh)
    trials_14.addData('text_89.started', text_89.tStartRefresh)
    trials_14.addData('text_89.stopped', text_89.tStopRefresh)
    trials_14.addData('image_27.started', image_27.tStartRefresh)
    trials_14.addData('image_27.stopped', image_27.tStopRefresh)
    trials_14.addData('text_97.started', text_97.tStartRefresh)
    trials_14.addData('text_97.stopped', text_97.tStopRefresh)
    # the Routine "left_hand" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "right_hand"-------
    # update component parameters for each repeat
    key_resp_21.keys = []
    key_resp_21.rt = []
    # keep track of which components have finished
    right_handComponents = [image_24, key_resp_21, text_78, text_96, image_28]
    for thisComponent in right_handComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    right_handClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "right_hand"-------
    while continueRoutine:
        # get current time
        t = right_handClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=right_handClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_24* updates
        if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_24.frameNStart = frameN  # exact frame index
            image_24.tStart = t  # local t and not account for scr refresh
            image_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
            image_24.setAutoDraw(True)
        
        # *key_resp_21* updates
        waitOnFlip = False
        if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_21.frameNStart = frameN  # exact frame index
            key_resp_21.tStart = t  # local t and not account for scr refresh
            key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
            key_resp_21.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_21.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_21.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_21.keys = theseKeys.name  # just the last key pressed
                key_resp_21.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_78* updates
        if text_78.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_78.frameNStart = frameN  # exact frame index
            text_78.tStart = t  # local t and not account for scr refresh
            text_78.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_78, 'tStartRefresh')  # time at next scr refresh
            text_78.setAutoDraw(True)
        
        # *text_96* updates
        if text_96.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_96.frameNStart = frameN  # exact frame index
            text_96.tStart = t  # local t and not account for scr refresh
            text_96.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_96, 'tStartRefresh')  # time at next scr refresh
            text_96.setAutoDraw(True)
        
        # *image_28* updates
        if image_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_28.frameNStart = frameN  # exact frame index
            image_28.tStart = t  # local t and not account for scr refresh
            image_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_28, 'tStartRefresh')  # time at next scr refresh
            image_28.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in right_handComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "right_hand"-------
    for thisComponent in right_handComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_14.addData('image_24.started', image_24.tStartRefresh)
    trials_14.addData('image_24.stopped', image_24.tStopRefresh)
    # check responses
    if key_resp_21.keys in ['', [], None]:  # No response was made
        key_resp_21.keys = None
    trials_14.addData('key_resp_21.keys',key_resp_21.keys)
    if key_resp_21.keys != None:  # we had a response
        trials_14.addData('key_resp_21.rt', key_resp_21.rt)
    trials_14.addData('key_resp_21.started', key_resp_21.tStartRefresh)
    trials_14.addData('key_resp_21.stopped', key_resp_21.tStopRefresh)
    trials_14.addData('text_78.started', text_78.tStartRefresh)
    trials_14.addData('text_78.stopped', text_78.tStopRefresh)
    trials_14.addData('text_96.started', text_96.tStartRefresh)
    trials_14.addData('text_96.stopped', text_96.tStopRefresh)
    thisExp.addData('image_28.started', image_28.tStartRefresh)
    thisExp.addData('image_28.stopped', image_28.tStopRefresh)
    # the Routine "right_hand" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice_presses"-------
    # update component parameters for each repeat
    key_resp_36.keys = []
    key_resp_36.rt = []
    # keep track of which components have finished
    practice_pressesComponents = [key_resp_36, text_94, text_95]
    for thisComponent in practice_pressesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_pressesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_presses"-------
    while continueRoutine:
        # get current time
        t = practice_pressesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_pressesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_36* updates
        waitOnFlip = False
        if key_resp_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_36.frameNStart = frameN  # exact frame index
            key_resp_36.tStart = t  # local t and not account for scr refresh
            key_resp_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_36, 'tStartRefresh')  # time at next scr refresh
            key_resp_36.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_36.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_36.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_36.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_36.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_36.keys = theseKeys.name  # just the last key pressed
                key_resp_36.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_94* updates
        if text_94.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_94.frameNStart = frameN  # exact frame index
            text_94.tStart = t  # local t and not account for scr refresh
            text_94.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_94, 'tStartRefresh')  # time at next scr refresh
            text_94.setAutoDraw(True)
        
        # *text_95* updates
        if text_95.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_95.frameNStart = frameN  # exact frame index
            text_95.tStart = t  # local t and not account for scr refresh
            text_95.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_95, 'tStartRefresh')  # time at next scr refresh
            text_95.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_pressesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_presses"-------
    for thisComponent in practice_pressesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_36.keys in ['', [], None]:  # No response was made
        key_resp_36.keys = None
    trials_14.addData('key_resp_36.keys',key_resp_36.keys)
    if key_resp_36.keys != None:  # we had a response
        trials_14.addData('key_resp_36.rt', key_resp_36.rt)
    trials_14.addData('key_resp_36.started', key_resp_36.tStartRefresh)
    trials_14.addData('key_resp_36.stopped', key_resp_36.tStopRefresh)
    trials_14.addData('text_94.started', text_94.tStartRefresh)
    trials_14.addData('text_94.stopped', text_94.tStopRefresh)
    trials_14.addData('text_95.started', text_95.tStartRefresh)
    trials_14.addData('text_95.stopped', text_95.tStopRefresh)
    # the Routine "practice_presses" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test4"-------
    # update component parameters for each repeat
    key_resp_32.keys = []
    key_resp_32.rt = []
    # keep track of which components have finished
    test4Components = [text_90, key_resp_32]
    for thisComponent in test4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "test4"-------
    while continueRoutine:
        # get current time
        t = test4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_90* updates
        if text_90.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_90.frameNStart = frameN  # exact frame index
            text_90.tStart = t  # local t and not account for scr refresh
            text_90.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_90, 'tStartRefresh')  # time at next scr refresh
            text_90.setAutoDraw(True)
        
        # *key_resp_32* updates
        waitOnFlip = False
        if key_resp_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_32.frameNStart = frameN  # exact frame index
            key_resp_32.tStart = t  # local t and not account for scr refresh
            key_resp_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_32, 'tStartRefresh')  # time at next scr refresh
            key_resp_32.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_32.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_32.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_32.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_32.getKeys(keyList=['1', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_32.keys = theseKeys.name  # just the last key pressed
                key_resp_32.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test4"-------
    for thisComponent in test4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_14.addData('text_90.started', text_90.tStartRefresh)
    trials_14.addData('text_90.stopped', text_90.tStopRefresh)
    # check responses
    if key_resp_32.keys in ['', [], None]:  # No response was made
        key_resp_32.keys = None
    trials_14.addData('key_resp_32.keys',key_resp_32.keys)
    if key_resp_32.keys != None:  # we had a response
        trials_14.addData('key_resp_32.rt', key_resp_32.rt)
    trials_14.addData('key_resp_32.started', key_resp_32.tStartRefresh)
    trials_14.addData('key_resp_32.stopped', key_resp_32.tStopRefresh)
    # the Routine "test4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test1"-------
    # update component parameters for each repeat
    key_resp_33.keys = []
    key_resp_33.rt = []
    # keep track of which components have finished
    test1Components = [text_91, key_resp_33]
    for thisComponent in test1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "test1"-------
    while continueRoutine:
        # get current time
        t = test1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_91* updates
        if text_91.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_91.frameNStart = frameN  # exact frame index
            text_91.tStart = t  # local t and not account for scr refresh
            text_91.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_91, 'tStartRefresh')  # time at next scr refresh
            text_91.setAutoDraw(True)
        
        # *key_resp_33* updates
        waitOnFlip = False
        if key_resp_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_33.frameNStart = frameN  # exact frame index
            key_resp_33.tStart = t  # local t and not account for scr refresh
            key_resp_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_33, 'tStartRefresh')  # time at next scr refresh
            key_resp_33.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_33.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_33.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_33.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_33.getKeys(keyList=['8', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_33.keys = theseKeys.name  # just the last key pressed
                key_resp_33.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test1"-------
    for thisComponent in test1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_14.addData('text_91.started', text_91.tStartRefresh)
    trials_14.addData('text_91.stopped', text_91.tStopRefresh)
    # check responses
    if key_resp_33.keys in ['', [], None]:  # No response was made
        key_resp_33.keys = None
    trials_14.addData('key_resp_33.keys',key_resp_33.keys)
    if key_resp_33.keys != None:  # we had a response
        trials_14.addData('key_resp_33.rt', key_resp_33.rt)
    trials_14.addData('key_resp_33.started', key_resp_33.tStartRefresh)
    trials_14.addData('key_resp_33.stopped', key_resp_33.tStopRefresh)
    # the Routine "test1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test3"-------
    # update component parameters for each repeat
    key_resp_34.keys = []
    key_resp_34.rt = []
    # keep track of which components have finished
    test3Components = [text_92, key_resp_34]
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
        
        # *text_92* updates
        if text_92.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_92.frameNStart = frameN  # exact frame index
            text_92.tStart = t  # local t and not account for scr refresh
            text_92.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_92, 'tStartRefresh')  # time at next scr refresh
            text_92.setAutoDraw(True)
        
        # *key_resp_34* updates
        waitOnFlip = False
        if key_resp_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_34.frameNStart = frameN  # exact frame index
            key_resp_34.tStart = t  # local t and not account for scr refresh
            key_resp_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_34, 'tStartRefresh')  # time at next scr refresh
            key_resp_34.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_34.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_34.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_34.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_34.getKeys(keyList=['6', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_34.keys = theseKeys.name  # just the last key pressed
                key_resp_34.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
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
    trials_14.addData('text_92.started', text_92.tStartRefresh)
    trials_14.addData('text_92.stopped', text_92.tStopRefresh)
    # check responses
    if key_resp_34.keys in ['', [], None]:  # No response was made
        key_resp_34.keys = None
    trials_14.addData('key_resp_34.keys',key_resp_34.keys)
    if key_resp_34.keys != None:  # we had a response
        trials_14.addData('key_resp_34.rt', key_resp_34.rt)
    trials_14.addData('key_resp_34.started', key_resp_34.tStartRefresh)
    trials_14.addData('key_resp_34.stopped', key_resp_34.tStopRefresh)
    # the Routine "test3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test5"-------
    # update component parameters for each repeat
    key_resp_35.keys = []
    key_resp_35.rt = []
    # keep track of which components have finished
    test5Components = [text_93, key_resp_35]
    for thisComponent in test5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "test5"-------
    while continueRoutine:
        # get current time
        t = test5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_93* updates
        if text_93.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_93.frameNStart = frameN  # exact frame index
            text_93.tStart = t  # local t and not account for scr refresh
            text_93.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_93, 'tStartRefresh')  # time at next scr refresh
            text_93.setAutoDraw(True)
        
        # *key_resp_35* updates
        waitOnFlip = False
        if key_resp_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_35.frameNStart = frameN  # exact frame index
            key_resp_35.tStart = t  # local t and not account for scr refresh
            key_resp_35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_35, 'tStartRefresh')  # time at next scr refresh
            key_resp_35.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_35.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_35.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_35.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_35.getKeys(keyList=['2', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_35.keys = theseKeys.name  # just the last key pressed
                key_resp_35.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test5"-------
    for thisComponent in test5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_14.addData('text_93.started', text_93.tStartRefresh)
    trials_14.addData('text_93.stopped', text_93.tStopRefresh)
    # check responses
    if key_resp_35.keys in ['', [], None]:  # No response was made
        key_resp_35.keys = None
    trials_14.addData('key_resp_35.keys',key_resp_35.keys)
    if key_resp_35.keys != None:  # we had a response
        trials_14.addData('key_resp_35.rt', key_resp_35.rt)
    trials_14.addData('key_resp_35.started', key_resp_35.tStartRefresh)
    trials_14.addData('key_resp_35.stopped', key_resp_35.tStopRefresh)
    # the Routine "test5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "good_job"-------
    # update component parameters for each repeat
    key_resp_37.keys = []
    key_resp_37.rt = []
    # keep track of which components have finished
    good_jobComponents = [text_98, text_99, key_resp_37]
    for thisComponent in good_jobComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    good_jobClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "good_job"-------
    while continueRoutine:
        # get current time
        t = good_jobClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=good_jobClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_98* updates
        if text_98.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_98.frameNStart = frameN  # exact frame index
            text_98.tStart = t  # local t and not account for scr refresh
            text_98.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_98, 'tStartRefresh')  # time at next scr refresh
            text_98.setAutoDraw(True)
        
        # *text_99* updates
        if text_99.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_99.frameNStart = frameN  # exact frame index
            text_99.tStart = t  # local t and not account for scr refresh
            text_99.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_99, 'tStartRefresh')  # time at next scr refresh
            text_99.setAutoDraw(True)
        
        # *key_resp_37* updates
        waitOnFlip = False
        if key_resp_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_37.frameNStart = frameN  # exact frame index
            key_resp_37.tStart = t  # local t and not account for scr refresh
            key_resp_37.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_37, 'tStartRefresh')  # time at next scr refresh
            key_resp_37.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_37.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_37.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_37.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_37.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_37.keys = theseKeys.name  # just the last key pressed
                key_resp_37.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in good_jobComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "good_job"-------
    for thisComponent in good_jobComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_14.addData('text_98.started', text_98.tStartRefresh)
    trials_14.addData('text_98.stopped', text_98.tStopRefresh)
    trials_14.addData('text_99.started', text_99.tStartRefresh)
    trials_14.addData('text_99.stopped', text_99.tStopRefresh)
    # check responses
    if key_resp_37.keys in ['', [], None]:  # No response was made
        key_resp_37.keys = None
    trials_14.addData('key_resp_37.keys',key_resp_37.keys)
    if key_resp_37.keys != None:  # we had a response
        trials_14.addData('key_resp_37.rt', key_resp_37.rt)
    trials_14.addData('key_resp_37.started', key_resp_37.tStartRefresh)
    trials_14.addData('key_resp_37.stopped', key_resp_37.tStopRefresh)
    # the Routine "good_job" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed block1_play repeats of 'trials_14'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=block1_play, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "Trigger"-------
    # update component parameters for each repeat
    getTrigger.keys = []
    getTrigger.rt = []
    # keep track of which components have finished
    TriggerComponents = [textTrigger, getTrigger, text_76, text_77]
    for thisComponent in TriggerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Trigger"-------
    while continueRoutine:
        # get current time
        t = TriggerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TriggerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textTrigger* updates
        if textTrigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textTrigger.frameNStart = frameN  # exact frame index
            textTrigger.tStart = t  # local t and not account for scr refresh
            textTrigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textTrigger, 'tStartRefresh')  # time at next scr refresh
            textTrigger.setAutoDraw(True)
        
        # *getTrigger* updates
        waitOnFlip = False
        if getTrigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            getTrigger.frameNStart = frameN  # exact frame index
            getTrigger.tStart = t  # local t and not account for scr refresh
            getTrigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(getTrigger, 'tStartRefresh')  # time at next scr refresh
            getTrigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(getTrigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(getTrigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if getTrigger.status == STARTED and not waitOnFlip:
            theseKeys = getTrigger.getKeys(keyList=['equal'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                getTrigger.keys = theseKeys.name  # just the last key pressed
                getTrigger.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_76* updates
        if text_76.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_76.frameNStart = frameN  # exact frame index
            text_76.tStart = t  # local t and not account for scr refresh
            text_76.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_76, 'tStartRefresh')  # time at next scr refresh
            text_76.setAutoDraw(True)
        
        # *text_77* updates
        if text_77.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_77.frameNStart = frameN  # exact frame index
            text_77.tStart = t  # local t and not account for scr refresh
            text_77.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_77, 'tStartRefresh')  # time at next scr refresh
            text_77.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trigger"-------
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('textTrigger.started', textTrigger.tStartRefresh)
    trials_3.addData('textTrigger.stopped', textTrigger.tStopRefresh)
    # check responses
    if getTrigger.keys in ['', [], None]:  # No response was made
        getTrigger.keys = None
    trials_3.addData('getTrigger.keys',getTrigger.keys)
    if getTrigger.keys != None:  # we had a response
        trials_3.addData('getTrigger.rt', getTrigger.rt)
    trials_3.addData('getTrigger.started', getTrigger.tStartRefresh)
    trials_3.addData('getTrigger.stopped', getTrigger.tStopRefresh)
    triggerTime = globalClock.getTime()
    thisExp.addData('triggerTime', triggerTime)
    def getRelTime(start = triggerTime):
        return globalClock.getTime() - start
    trials_3.addData('text_76.started', text_76.tStartRefresh)
    trials_3.addData('text_76.stopped', text_76.tStopRefresh)
    trials_3.addData('text_77.started', text_77.tStartRefresh)
    trials_3.addData('text_77.stopped', text_77.tStopRefresh)
    # the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "routine_6sec_wait"-------
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    thisExp.addData('startWait', getRelTime())
    # keep track of which components have finished
    routine_6sec_waitComponents = [image_23]
    for thisComponent in routine_6sec_waitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_6sec_waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "routine_6sec_wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_6sec_waitClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_6sec_waitClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_23* updates
        if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_23.frameNStart = frameN  # exact frame index
            image_23.tStart = t  # local t and not account for scr refresh
            image_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
            image_23.setAutoDraw(True)
        if image_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_23.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                image_23.tStop = t  # not accounting for scr refresh
                image_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_23, 'tStopRefresh')  # time at next scr refresh
                image_23.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_6sec_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_6sec_wait"-------
    for thisComponent in routine_6sec_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('endWait', getRelTime())
    trials_3.addData('image_23.started', image_23.tStartRefresh)
    trials_3.addData('image_23.stopped', image_23.tStopRefresh)
    
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
        
        # ------Prepare to start Routine "info"-------
        # update component parameters for each repeat
        if action_list_block1[count] == 1:
            nreps_whole = 1
            nreps_persp = 1
        if action_list_block1[count] == 2:
            nreps_whole = 1
            nreps_persp = 1
        if action_list_block1[count] == 3:
            nreps_whole = 0
        if action_list_block1[count] == 4:
            nreps_whole = 1
            nreps_persp = 0
        # keep track of which components have finished
        infoComponents = []
        for thisComponent in infoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "info"-------
        while continueRoutine:
            # get current time
            t = infoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=infoClock)
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
            for thisComponent in infoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "info"-------
        for thisComponent in infoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "info" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_5 = data.TrialHandler(nReps=nreps_whole, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
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
            
            # ------Prepare to start Routine "storycount"-------
            # update component parameters for each repeat
            story_count += 1
            print(story_list_block1[count])
            print(action_list_block1[count])
            #set the perspective
            #get the story file and the story pic
            this_story_file = storyDict.get(story_list_block1[count], {}).get('storyFile')
            this_story_pic = storyDict.get(story_list_block1[count], {}).get('pic')
            print(this_story_pic)
            
            #select the perspective if the action matrix is '1' or '2'
            if action_list_block1[count] == 1 or action_list_block1[count] == 2:
                this_perspective = storyDict.get(story_list_block1[count], {}).get(action_list_block1[count])
                print(this_perspective)
                if this_perspective == 'Couples Therapist':
                    display_pic = 'jobphotos/couples.jpg'
                    question1 = 'For how long has the initiator of the breakup been thinking about breaking up with his/her partner?'
                    question2 ='What is the initial reason stated by the initiator for why he/she is breaking up?'
                    question3 ='Does the person who is being broken up with want to break up, and what’s the reason stated by them for this?'
                    question4 = 'Who wants what items back as a result of the breakup?'
                    question5 = 'What is the initial reason stated by the initiator for why he/she wanted to meet?'
                    question6 = 'Who wants how many letters burned as a result of the breakup?'
                if this_perspective == 'Restaurant Critic':
                    display_pic = 'jobphotos/restaurant_critic.jpg'
                    question1 = 'How is the restaurant decorated?'
                    question2 ='What are the menus like?'
                    question3 = 'What does each client order?' 
                    question4 = 'How do the clients like the food?'
                    question5 = 'How is the restaurant supplied?'
                    question6 = 'How do the clients like the chairs?'
                if this_perspective == 'Airport Customer Experience Manager':
                    display_pic = 'jobphotos/acem.jpg'
                    question1 = 'When the clients arrive at the airport, how much time do they have until their flight departs?'
                    question2 ='What is the reason for the hold-up at security?'
                    question3 ='Toward which gate are the clients walking?'
                    question4 ='What section and seat does each client sit in on the plane?' 
                    question5 = 'Toward which security line are the clients walking?'
                    question6 = 'What section and seat are roped off on the plane?'
                if this_perspective == 'Grocery Store Customer Experience Manager':
                    display_pic = 'jobphotos/gscem.jpg'
                    question1 = 'What is the grocery store like upon entering?'
                    question2 ='What items do the clients pick out to buy?'
                    question3 ='How many checkout lanes are open, and which one do the clients step into?'
                    question4 = 'How much are the groceries, and what method of payment do the clients use?'
                    question5 = 'What is the grocery store like when the clients leave?'
                    question6 = 'How many checkout lanes are closed, and which one do the clients step into?'
                if this_perspective == 'Dean of Academic Studies':
                    display_pic ='jobphotos/dean.jpg'
                    question1 = 'What is the lecture hall like?'
                    question2 ='What class are the students in, and what is the day’s lecture about?'
                    question3 ='What is something taught in lecture?'
                    question4 = 'What is the next assessment/assignment for the class, and when is it scheduled/due?'
                    question5 = 'What class are the students in, and what was yesterday’s lecture about?'
                    question6 = 'What is the lecture hall’s max capacity?'
                if this_perspective == 'Wedding Planner':
                    display_pic = 'jobphotos/weddingplanner.jpg'
                    question1 = 'For how long has the couple been dating?'
                    question2 ='How many diamonds are on the ring, and what is the diamond color?'
                    question3 ='In/on what item is the ring presented?'
                    question4 = 'Who does the new fiancee text first?'
                    question5 = 'For how long has the couple known the other was going to propose?'
                    question6 = 'Who does the new fiancee hug first?'
                if this_perspective == 'Business Reporter':
                    display_pic = 'jobphotos/business_reporter.jpg'
                    question1 = 'What is each business person’s job title?'
                    question2 = 'How much money is at stake in the initial offer made?'
                    question3 = 'What is the name of the other industry competitor? '
                    question4 =  'With what gesture do the business partners secure the deal?'
                    question5 = 'What is each business person’s salary?'
                    question6 =  'How much money is at stake in the final offer made?'
                if this_perspective == 'Matchmaker':
                    display_pic = 'jobphotos/matchmaker.jpg'
                    question1 = 'What object is the initiator of the interaction holding when he/she first notices the other person?' 
                    question2 ='What is the initial question that begins the conversation between the couple?'
                    question3 ='When will be the next time the couple meets and for what occasion?'
                    question4 = 'What time is it when the couple parts?'
                    question5 = 'What is the initial question that ends the conversation between the couple?'
                    question6 = 'What object is the initiator of the interaction holding when he/she leaves the other person?'
            
            
            
            
            
            
            
            text_38.setText((story_count))
            key_resp_8.keys = []
            key_resp_8.rt = []
            # keep track of which components have finished
            storycountComponents = [text_38, key_resp_8, text_39, text]
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
                    theseKeys = key_resp_8.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
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
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                
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
            trials_5.addData('text_38.started', text_38.tStartRefresh)
            trials_5.addData('text_38.stopped', text_38.tStopRefresh)
            # check responses
            if key_resp_8.keys in ['', [], None]:  # No response was made
                key_resp_8.keys = None
            trials_5.addData('key_resp_8.keys',key_resp_8.keys)
            if key_resp_8.keys != None:  # we had a response
                trials_5.addData('key_resp_8.rt', key_resp_8.rt)
            trials_5.addData('key_resp_8.started', key_resp_8.tStartRefresh)
            trials_5.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
            trials_5.addData('text_39.started', text_39.tStartRefresh)
            trials_5.addData('text_39.stopped', text_39.tStopRefresh)
            trials_5.addData('text.started', text.tStartRefresh)
            trials_5.addData('text.stopped', text.tStopRefresh)
            # the Routine "storycount" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials = data.TrialHandler(nReps=nreps_persp, method='sequential', 
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
                
                # ------Prepare to start Routine "ask_to_assume"-------
                # update component parameters for each repeat
                key_resp_30.keys = []
                key_resp_30.rt = []
                # keep track of which components have finished
                ask_to_assumeComponents = [text_33, key_resp_30, text_79]
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
                    
                    # *key_resp_30* updates
                    waitOnFlip = False
                    if key_resp_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_30.frameNStart = frameN  # exact frame index
                        key_resp_30.tStart = t  # local t and not account for scr refresh
                        key_resp_30.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_30, 'tStartRefresh')  # time at next scr refresh
                        key_resp_30.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_30.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_30.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_30.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_30.keys = theseKeys.name  # just the last key pressed
                            key_resp_30.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_79* updates
                    if text_79.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_79.frameNStart = frameN  # exact frame index
                        text_79.tStart = t  # local t and not account for scr refresh
                        text_79.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_79, 'tStartRefresh')  # time at next scr refresh
                        text_79.setAutoDraw(True)
                    
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
                trials.addData('text_33.started', text_33.tStartRefresh)
                trials.addData('text_33.stopped', text_33.tStopRefresh)
                # check responses
                if key_resp_30.keys in ['', [], None]:  # No response was made
                    key_resp_30.keys = None
                trials.addData('key_resp_30.keys',key_resp_30.keys)
                if key_resp_30.keys != None:  # we had a response
                    trials.addData('key_resp_30.rt', key_resp_30.rt)
                trials.addData('key_resp_30.started', key_resp_30.tStartRefresh)
                trials.addData('key_resp_30.stopped', key_resp_30.tStopRefresh)
                trials.addData('text_79.started', text_79.tStartRefresh)
                trials.addData('text_79.stopped', text_79.tStopRefresh)
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
                    
                    text_4.setText(this_perspective)
                    image.setImage(display_pic)
                    key_resp_22.keys = []
                    key_resp_22.rt = []
                    # keep track of which components have finished
                    perspectiveComponents = [text_4, image, text_5, key_resp_22]
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
                        
                        # *key_resp_22* updates
                        waitOnFlip = False
                        if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            key_resp_22.frameNStart = frameN  # exact frame index
                            key_resp_22.tStart = t  # local t and not account for scr refresh
                            key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
                            key_resp_22.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if key_resp_22.status == STARTED and not waitOnFlip:
                            theseKeys = key_resp_22.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                            if len(theseKeys):
                                theseKeys = theseKeys[0]  # at least one key was pressed
                                
                                # check for quit:
                                if "escape" == theseKeys:
                                    endExpNow = True
                                key_resp_22.keys = theseKeys.name  # just the last key pressed
                                key_resp_22.rt = theseKeys.rt
                                # a response ends the routine
                                continueRoutine = False
                        
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
                    # check responses
                    if key_resp_22.keys in ['', [], None]:  # No response was made
                        key_resp_22.keys = None
                    trials_7.addData('key_resp_22.keys',key_resp_22.keys)
                    if key_resp_22.keys != None:  # we had a response
                        trials_7.addData('key_resp_22.rt', key_resp_22.rt)
                    trials_7.addData('key_resp_22.started', key_resp_22.tStartRefresh)
                    trials_7.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
                    # the Routine "perspective" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # ------Prepare to start Routine "intro_test"-------
                    # update component parameters for each repeat
                    key_resp_7.keys = []
                    key_resp_7.rt = []
                    # keep track of which components have finished
                    intro_testComponents = [text_37, key_resp_7, text_80]
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
                            theseKeys = key_resp_7.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                            if len(theseKeys):
                                theseKeys = theseKeys[0]  # at least one key was pressed
                                
                                # check for quit:
                                if "escape" == theseKeys:
                                    endExpNow = True
                                key_resp_7.keys = theseKeys.name  # just the last key pressed
                                key_resp_7.rt = theseKeys.rt
                                # a response ends the routine
                                continueRoutine = False
                        
                        # *text_80* updates
                        if text_80.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_80.frameNStart = frameN  # exact frame index
                            text_80.tStart = t  # local t and not account for scr refresh
                            text_80.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_80, 'tStartRefresh')  # time at next scr refresh
                            text_80.setAutoDraw(True)
                        
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
                    trials_7.addData('text_80.started', text_80.tStartRefresh)
                    trials_7.addData('text_80.stopped', text_80.tStopRefresh)
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
                    
                    
                    question1_3.setText(text1)
                    question2_3.setText(text2
)
                    question3_3.setText(text3)
                    question4_3.setText(text4)
                    question5_3.setText(text5
)
                    question6_3.setText(text6)
                    # keep track of which components have finished
                    perspective_testComponents = [question1_3, question2_3, question3_3, question4_3, question5_3, question6_3, image_16]
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
                            trials_7.finished= True 
                            continueRoutine = False
                        #question 1 selection, keypress 8 on button box
                        if event.getKeys(['8']):
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
                        
                        #question 2 selection, keypress 7 on button box
                        if event.getKeys(['7']):
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
                        
                        #question 3 selection, keypress 6 on button box
                        if event.getKeys(['6']):
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
                        
                        #question 4 selection, keypress 1 on button box
                        if event.getKeys(['1']):
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
                        
                        #question 5 selection, keypress 2 on button box
                        if event.getKeys(['2']):
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
                        
                        #question 6 collection, keypress 3 on button box
                        if event.getKeys(['3']):
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
                        
                        # *image_16* updates
                        if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            image_16.frameNStart = frameN  # exact frame index
                            image_16.tStart = t  # local t and not account for scr refresh
                            image_16.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
                            image_16.setAutoDraw(True)
                        if image_16.status == STARTED:  # only update if drawing
                            image_16.setImage(this_image, log=False)
                        
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
                    trials_7.addData('question1_3.started', question1_3.tStartRefresh)
                    trials_7.addData('question1_3.stopped', question1_3.tStopRefresh)
                    trials_7.addData('question2_3.started', question2_3.tStartRefresh)
                    trials_7.addData('question2_3.stopped', question2_3.tStopRefresh)
                    trials_7.addData('question3_3.started', question3_3.tStartRefresh)
                    trials_7.addData('question3_3.stopped', question3_3.tStopRefresh)
                    trials_7.addData('question4_3.started', question4_3.tStartRefresh)
                    trials_7.addData('question4_3.stopped', question4_3.tStopRefresh)
                    trials_7.addData('question5_3.started', question5_3.tStartRefresh)
                    trials_7.addData('question5_3.stopped', question5_3.tStopRefresh)
                    trials_7.addData('question6_3.started', question6_3.tStartRefresh)
                    trials_7.addData('question6_3.stopped', question6_3.tStopRefresh)
                    trials_7.addData('image_16.started', image_16.tStartRefresh)
                    trials_7.addData('image_16.stopped', image_16.tStopRefresh)
                    # the Routine "perspective_test" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 7 repeats of 'trials_7'
                
                
                # ------Prepare to start Routine "p_again"-------
                # update component parameters for each repeat
                key_resp_15.keys = []
                key_resp_15.rt = []
                # keep track of which components have finished
                p_againComponents = [text_49, key_resp_15, text_81]
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
                        theseKeys = key_resp_15.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_15.keys = theseKeys.name  # just the last key pressed
                            key_resp_15.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_81* updates
                    if text_81.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_81.frameNStart = frameN  # exact frame index
                        text_81.tStart = t  # local t and not account for scr refresh
                        text_81.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_81, 'tStartRefresh')  # time at next scr refresh
                        text_81.setAutoDraw(True)
                    
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
                trials.addData('text_49.started', text_49.tStartRefresh)
                trials.addData('text_49.stopped', text_49.tStopRefresh)
                # check responses
                if key_resp_15.keys in ['', [], None]:  # No response was made
                    key_resp_15.keys = None
                trials.addData('key_resp_15.keys',key_resp_15.keys)
                if key_resp_15.keys != None:  # we had a response
                    trials.addData('key_resp_15.rt', key_resp_15.rt)
                trials.addData('key_resp_15.started', key_resp_15.tStartRefresh)
                trials.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
                trials.addData('text_81.started', text_81.tStartRefresh)
                trials.addData('text_81.stopped', text_81.tStopRefresh)
                # the Routine "p_again" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "perspective"-------
                # update component parameters for each repeat
                event.clearEvents()
                
                text_4.setText(this_perspective)
                image.setImage(display_pic)
                key_resp_22.keys = []
                key_resp_22.rt = []
                # keep track of which components have finished
                perspectiveComponents = [text_4, image, text_5, key_resp_22]
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
                    
                    # *key_resp_22* updates
                    waitOnFlip = False
                    if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_22.frameNStart = frameN  # exact frame index
                        key_resp_22.tStart = t  # local t and not account for scr refresh
                        key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
                        key_resp_22.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_22.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_22.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_22.keys = theseKeys.name  # just the last key pressed
                            key_resp_22.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
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
                trials.addData('text_4.started', text_4.tStartRefresh)
                trials.addData('text_4.stopped', text_4.tStopRefresh)
                trials.addData('image.started', image.tStartRefresh)
                trials.addData('image.stopped', image.tStopRefresh)
                trials.addData('text_5.started', text_5.tStartRefresh)
                trials.addData('text_5.stopped', text_5.tStopRefresh)
                # check responses
                if key_resp_22.keys in ['', [], None]:  # No response was made
                    key_resp_22.keys = None
                trials.addData('key_resp_22.keys',key_resp_22.keys)
                if key_resp_22.keys != None:  # we had a response
                    trials.addData('key_resp_22.rt', key_resp_22.rt)
                trials.addData('key_resp_22.started', key_resp_22.tStartRefresh)
                trials.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
                # the Routine "perspective" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed nreps_persp repeats of 'trials'
            
            
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
                    theseKeys = key_resp_14.getKeys(keyList=['1', '2', '3', '4', '5', '6', 'space'], waitRelease=False)
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
            trials_5.addData('text_50.started', text_50.tStartRefresh)
            trials_5.addData('text_50.stopped', text_50.tStopRefresh)
            # check responses
            if key_resp_14.keys in ['', [], None]:  # No response was made
                key_resp_14.keys = None
            trials_5.addData('key_resp_14.keys',key_resp_14.keys)
            if key_resp_14.keys != None:  # we had a response
                trials_5.addData('key_resp_14.rt', key_resp_14.rt)
            trials_5.addData('key_resp_14.started', key_resp_14.tStartRefresh)
            trials_5.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
            # the Routine "story_begin" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_2 = data.TrialHandler(nReps=int(expInfo['behavioral']), method='sequential', 
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
                
                # set up handler to look after randomisation of conditions etc
                trials_21 = data.TrialHandler(nReps=int(expInfo['play_stories']), method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_21')
                thisExp.addLoop(trials_21)  # add the loop to the experiment
                thisTrial_21 = trials_21.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
                if thisTrial_21 != None:
                    for paramName in thisTrial_21:
                        exec('{} = thisTrial_21[paramName]'.format(paramName))
                
                for thisTrial_21 in trials_21:
                    currentLoop = trials_21
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
                    if thisTrial_21 != None:
                        for paramName in thisTrial_21:
                            exec('{} = thisTrial_21[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "play_audio_story"-------
                    # update component parameters for each repeat
                    thisExp.addData('clip_StartTime', getRelTime())
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
                    thisExp.addData('clip_EndTime', getRelTime())
                    # the Routine "play_audio_story" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed int(expInfo['play_stories']) repeats of 'trials_21'
                
                
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
                
            # completed int(expInfo['behavioral']) repeats of 'trials_2'
            
            
            # set up handler to look after randomisation of conditions etc
            trials_22 = data.TrialHandler(nReps=int(expInfo['play_stories']), method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_22')
            thisExp.addLoop(trials_22)  # add the loop to the experiment
            thisTrial_22 = trials_22.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
            if thisTrial_22 != None:
                for paramName in thisTrial_22:
                    exec('{} = thisTrial_22[paramName]'.format(paramName))
            
            for thisTrial_22 in trials_22:
                currentLoop = trials_22
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
                if thisTrial_22 != None:
                    for paramName in thisTrial_22:
                        exec('{} = thisTrial_22[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "show_image_3sec"-------
                # update component parameters for each repeat
                thisExp.addData('storyImage_StartTime', getRelTime())
                start_time = globalClock.getTime()
                stim = visual.ImageStim(win, image=this_story_pic)
                stim.draw()
                while p.is_playing() or (globalClock.getTime()-start_time < 3):
                   stim.draw()
                   win.flip()
                
                continueRoutine=False
                # keep track of which components have finished
                show_image_3secComponents = []
                for thisComponent in show_image_3secComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                show_image_3secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "show_image_3sec"-------
                while continueRoutine:
                    # get current time
                    t = show_image_3secClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=show_image_3secClock)
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
                    for thisComponent in show_image_3secComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "show_image_3sec"-------
                for thisComponent in show_image_3secComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('storyImage_EndTime', getRelTime())
                # the Routine "show_image_3sec" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_16 = data.TrialHandler(nReps=1 - int(expInfo['behavioral']), method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions(this_story_file),
                    seed=None, name='trials_16')
                thisExp.addLoop(trials_16)  # add the loop to the experiment
                thisTrial_16 = trials_16.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
                if thisTrial_16 != None:
                    for paramName in thisTrial_16:
                        exec('{} = thisTrial_16[paramName]'.format(paramName))
                
                for thisTrial_16 in trials_16:
                    currentLoop = trials_16
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
                    if thisTrial_16 != None:
                        for paramName in thisTrial_16:
                            exec('{} = thisTrial_16[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "play_audio_story"-------
                    # update component parameters for each repeat
                    thisExp.addData('clip_StartTime', getRelTime())
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
                    thisExp.addData('clip_EndTime', getRelTime())
                    # the Routine "play_audio_story" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 1 - int(expInfo['behavioral']) repeats of 'trials_16'
                
                thisExp.nextEntry()
                
            # completed int(expInfo['play_stories']) repeats of 'trials_22'
            
            
            # set up handler to look after randomisation of conditions etc
            trials_23 = data.TrialHandler(nReps=1 - int(expInfo['play_stories']), method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_23')
            thisExp.addLoop(trials_23)  # add the loop to the experiment
            thisTrial_23 = trials_23.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
            if thisTrial_23 != None:
                for paramName in thisTrial_23:
                    exec('{} = thisTrial_23[paramName]'.format(paramName))
            
            for thisTrial_23 in trials_23:
                currentLoop = trials_23
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
                if thisTrial_23 != None:
                    for paramName in thisTrial_23:
                        exec('{} = thisTrial_23[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "show_storyimage1"-------
                # update component parameters for each repeat
                key_resp_28.keys = []
                key_resp_28.rt = []
                image_21.setImage(this_story_pic)
                thisExp.addData('clip_StartTime', getRelTime())
                # keep track of which components have finished
                show_storyimage1Components = [key_resp_28, image_21]
                for thisComponent in show_storyimage1Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                show_storyimage1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "show_storyimage1"-------
                while continueRoutine:
                    # get current time
                    t = show_storyimage1Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=show_storyimage1Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *key_resp_28* updates
                    waitOnFlip = False
                    if key_resp_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_28.frameNStart = frameN  # exact frame index
                        key_resp_28.tStart = t  # local t and not account for scr refresh
                        key_resp_28.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_28, 'tStartRefresh')  # time at next scr refresh
                        key_resp_28.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_28.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_28.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_28.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_28.getKeys(keyList=['space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_28.keys = theseKeys.name  # just the last key pressed
                            key_resp_28.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *image_21* updates
                    if image_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_21.frameNStart = frameN  # exact frame index
                        image_21.tStart = t  # local t and not account for scr refresh
                        image_21.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_21, 'tStartRefresh')  # time at next scr refresh
                        image_21.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in show_storyimage1Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "show_storyimage1"-------
                for thisComponent in show_storyimage1Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if key_resp_28.keys in ['', [], None]:  # No response was made
                    key_resp_28.keys = None
                trials_23.addData('key_resp_28.keys',key_resp_28.keys)
                if key_resp_28.keys != None:  # we had a response
                    trials_23.addData('key_resp_28.rt', key_resp_28.rt)
                trials_23.addData('key_resp_28.started', key_resp_28.tStartRefresh)
                trials_23.addData('key_resp_28.stopped', key_resp_28.tStopRefresh)
                trials_23.addData('image_21.started', image_21.tStartRefresh)
                trials_23.addData('image_21.stopped', image_21.tStopRefresh)
                thisExp.addData('clip_EndTime', getRelTime())
                # the Routine "show_storyimage1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 - int(expInfo['play_stories']) repeats of 'trials_23'
            
            
            # ------Prepare to start Routine "routine_6sec_wait"-------
            routineTimer.add(6.000000)
            # update component parameters for each repeat
            thisExp.addData('startWait', getRelTime())
            # keep track of which components have finished
            routine_6sec_waitComponents = [image_23]
            for thisComponent in routine_6sec_waitComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            routine_6sec_waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "routine_6sec_wait"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_6sec_waitClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routine_6sec_waitClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_23* updates
                if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_23.frameNStart = frameN  # exact frame index
                    image_23.tStart = t  # local t and not account for scr refresh
                    image_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
                    image_23.setAutoDraw(True)
                if image_23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_23.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        image_23.tStop = t  # not accounting for scr refresh
                        image_23.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_23, 'tStopRefresh')  # time at next scr refresh
                        image_23.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_6sec_waitComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "routine_6sec_wait"-------
            for thisComponent in routine_6sec_waitComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('endWait', getRelTime())
            trials_5.addData('image_23.started', image_23.tStartRefresh)
            trials_5.addData('image_23.stopped', image_23.tStopRefresh)
            
            # ------Prepare to start Routine "end_story"-------
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            text_6.setText((story_count))
            # keep track of which components have finished
            end_storyComponents = [text_6, text_52]
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
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = end_storyClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=end_storyClock)
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
                if text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_6.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        text_6.tStop = t  # not accounting for scr refresh
                        text_6.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                        text_6.setAutoDraw(False)
                
                # *text_52* updates
                if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_52.frameNStart = frameN  # exact frame index
                    text_52.tStart = t  # local t and not account for scr refresh
                    text_52.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
                    text_52.setAutoDraw(True)
                if text_52.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_52.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        text_52.tStop = t  # not accounting for scr refresh
                        text_52.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_52, 'tStopRefresh')  # time at next scr refresh
                        text_52.setAutoDraw(False)
                for key in event.getKeys():
                    if key in ['t']: 
                        trials_14.finished = 1
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
            trials_5.addData('text_6.started', text_6.tStartRefresh)
            trials_5.addData('text_6.stopped', text_6.tStopRefresh)
            trials_5.addData('text_52.started', text_52.tStartRefresh)
            trials_5.addData('text_52.stopped', text_52.tStopRefresh)
            thisExp.saveAsWideText(filename+'_safety.csv', appendFile=True)
            thisExp.nextEntry()
            
        # completed nreps_whole repeats of 'trials_5'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Block1'
    
    thisExp.nextEntry()
    
# completed block1_play repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=block2_play, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "Trigger"-------
    # update component parameters for each repeat
    getTrigger.keys = []
    getTrigger.rt = []
    # keep track of which components have finished
    TriggerComponents = [textTrigger, getTrigger, text_76, text_77]
    for thisComponent in TriggerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Trigger"-------
    while continueRoutine:
        # get current time
        t = TriggerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TriggerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textTrigger* updates
        if textTrigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textTrigger.frameNStart = frameN  # exact frame index
            textTrigger.tStart = t  # local t and not account for scr refresh
            textTrigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textTrigger, 'tStartRefresh')  # time at next scr refresh
            textTrigger.setAutoDraw(True)
        
        # *getTrigger* updates
        waitOnFlip = False
        if getTrigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            getTrigger.frameNStart = frameN  # exact frame index
            getTrigger.tStart = t  # local t and not account for scr refresh
            getTrigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(getTrigger, 'tStartRefresh')  # time at next scr refresh
            getTrigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(getTrigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(getTrigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if getTrigger.status == STARTED and not waitOnFlip:
            theseKeys = getTrigger.getKeys(keyList=['equal'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                getTrigger.keys = theseKeys.name  # just the last key pressed
                getTrigger.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_76* updates
        if text_76.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_76.frameNStart = frameN  # exact frame index
            text_76.tStart = t  # local t and not account for scr refresh
            text_76.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_76, 'tStartRefresh')  # time at next scr refresh
            text_76.setAutoDraw(True)
        
        # *text_77* updates
        if text_77.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_77.frameNStart = frameN  # exact frame index
            text_77.tStart = t  # local t and not account for scr refresh
            text_77.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_77, 'tStartRefresh')  # time at next scr refresh
            text_77.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trigger"-------
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('textTrigger.started', textTrigger.tStartRefresh)
    trials_4.addData('textTrigger.stopped', textTrigger.tStopRefresh)
    # check responses
    if getTrigger.keys in ['', [], None]:  # No response was made
        getTrigger.keys = None
    trials_4.addData('getTrigger.keys',getTrigger.keys)
    if getTrigger.keys != None:  # we had a response
        trials_4.addData('getTrigger.rt', getTrigger.rt)
    trials_4.addData('getTrigger.started', getTrigger.tStartRefresh)
    trials_4.addData('getTrigger.stopped', getTrigger.tStopRefresh)
    triggerTime = globalClock.getTime()
    thisExp.addData('triggerTime', triggerTime)
    def getRelTime(start = triggerTime):
        return globalClock.getTime() - start
    trials_4.addData('text_76.started', text_76.tStartRefresh)
    trials_4.addData('text_76.stopped', text_76.tStopRefresh)
    trials_4.addData('text_77.started', text_77.tStartRefresh)
    trials_4.addData('text_77.stopped', text_77.tStopRefresh)
    # the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "routine_6sec_wait"-------
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    thisExp.addData('startWait', getRelTime())
    # keep track of which components have finished
    routine_6sec_waitComponents = [image_23]
    for thisComponent in routine_6sec_waitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_6sec_waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "routine_6sec_wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_6sec_waitClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_6sec_waitClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_23* updates
        if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_23.frameNStart = frameN  # exact frame index
            image_23.tStart = t  # local t and not account for scr refresh
            image_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
            image_23.setAutoDraw(True)
        if image_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_23.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                image_23.tStop = t  # not accounting for scr refresh
                image_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_23, 'tStopRefresh')  # time at next scr refresh
                image_23.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_6sec_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_6sec_wait"-------
    for thisComponent in routine_6sec_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('endWait', getRelTime())
    trials_4.addData('image_23.started', image_23.tStartRefresh)
    trials_4.addData('image_23.stopped', image_23.tStopRefresh)
    
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
        
        # ------Prepare to start Routine "info_2"-------
        # update component parameters for each repeat
        if action_list_block2[count] == 1:
            nreps_whole = 1
            nreps_persp = 1
        if action_list_block2[count] == 2:
            nreps_whole = 1
            nreps_persp = 1
        if action_list_block2[count] == 3:
            nreps_whole = 0
        if action_list_block2[count] == 4:
            nreps_whole = 1
            nreps_persp = 0
        # keep track of which components have finished
        info_2Components = []
        for thisComponent in info_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        info_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "info_2"-------
        while continueRoutine:
            # get current time
            t = info_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=info_2Clock)
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
            for thisComponent in info_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "info_2"-------
        for thisComponent in info_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "info_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_9 = data.TrialHandler(nReps=nreps_whole, method='sequential', 
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
            
            # ------Prepare to start Routine "storycount_2"-------
            # update component parameters for each repeat
            story_count += 1
            print(story_list_block2[count])
            print(action_list_block2[count])
            #set the perspective
            #get the story file and the story pic
            this_story_file = storyDict.get(story_list_block2[count], {}).get('storyFile')
            this_story_pic = storyDict.get(story_list_block2[count], {}).get('pic')
            
            #select the perspective if the action matrix is '1' or '2'
            if action_list_block2[count] == 1 or action_list_block2[count] == 2:
                this_perspective = storyDict.get(story_list_block2[count], {}).get(action_list_block2[count])
                print(this_perspective)
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
            
            
            
            
            
            
            
            text_55.setText((story_count))
            key_resp_2.keys = []
            key_resp_2.rt = []
            # keep track of which components have finished
            storycount_2Components = [text_55, text_56, key_resp_2, text_82]
            for thisComponent in storycount_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            storycount_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "storycount_2"-------
            while continueRoutine:
                # get current time
                t = storycount_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=storycount_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_55* updates
                if text_55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_55.frameNStart = frameN  # exact frame index
                    text_55.tStart = t  # local t and not account for scr refresh
                    text_55.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_55, 'tStartRefresh')  # time at next scr refresh
                    text_55.setAutoDraw(True)
                
                # *text_56* updates
                if text_56.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_56.frameNStart = frameN  # exact frame index
                    text_56.tStart = t  # local t and not account for scr refresh
                    text_56.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_56, 'tStartRefresh')  # time at next scr refresh
                    text_56.setAutoDraw(True)
                
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
                    theseKeys = key_resp_2.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        key_resp_2.keys = theseKeys.name  # just the last key pressed
                        key_resp_2.rt = theseKeys.rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_82* updates
                if text_82.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_82.frameNStart = frameN  # exact frame index
                    text_82.tStart = t  # local t and not account for scr refresh
                    text_82.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_82, 'tStartRefresh')  # time at next scr refresh
                    text_82.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in storycount_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "storycount_2"-------
            for thisComponent in storycount_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_9.addData('text_55.started', text_55.tStartRefresh)
            trials_9.addData('text_55.stopped', text_55.tStopRefresh)
            trials_9.addData('text_56.started', text_56.tStartRefresh)
            trials_9.addData('text_56.stopped', text_56.tStopRefresh)
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            trials_9.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                trials_9.addData('key_resp_2.rt', key_resp_2.rt)
            trials_9.addData('key_resp_2.started', key_resp_2.tStartRefresh)
            trials_9.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
            trials_9.addData('text_82.started', text_82.tStartRefresh)
            trials_9.addData('text_82.stopped', text_82.tStopRefresh)
            # the Routine "storycount_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_10 = data.TrialHandler(nReps=nreps_persp, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_10')
            thisExp.addLoop(trials_10)  # add the loop to the experiment
            thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
            if thisTrial_10 != None:
                for paramName in thisTrial_10:
                    exec('{} = thisTrial_10[paramName]'.format(paramName))
            
            for thisTrial_10 in trials_10:
                currentLoop = trials_10
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
                if thisTrial_10 != None:
                    for paramName in thisTrial_10:
                        exec('{} = thisTrial_10[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "ask_to_assume_2"-------
                # update component parameters for each repeat
                key_resp_17.keys = []
                key_resp_17.rt = []
                # keep track of which components have finished
                ask_to_assume_2Components = [text_57, key_resp_17, text_83]
                for thisComponent in ask_to_assume_2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                ask_to_assume_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "ask_to_assume_2"-------
                while continueRoutine:
                    # get current time
                    t = ask_to_assume_2Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=ask_to_assume_2Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    for key in event.getKeys():
                        if key in ['q']: 
                            trials_10.finished = 1
                            continueRoutine = False
                    
                    # *text_57* updates
                    if text_57.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_57.frameNStart = frameN  # exact frame index
                        text_57.tStart = t  # local t and not account for scr refresh
                        text_57.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_57, 'tStartRefresh')  # time at next scr refresh
                        text_57.setAutoDraw(True)
                    
                    # *key_resp_17* updates
                    waitOnFlip = False
                    if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_17.frameNStart = frameN  # exact frame index
                        key_resp_17.tStart = t  # local t and not account for scr refresh
                        key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
                        key_resp_17.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_17.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_17.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_17.keys = theseKeys.name  # just the last key pressed
                            key_resp_17.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_83* updates
                    if text_83.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_83.frameNStart = frameN  # exact frame index
                        text_83.tStart = t  # local t and not account for scr refresh
                        text_83.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_83, 'tStartRefresh')  # time at next scr refresh
                        text_83.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in ask_to_assume_2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "ask_to_assume_2"-------
                for thisComponent in ask_to_assume_2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials_10.addData('text_57.started', text_57.tStartRefresh)
                trials_10.addData('text_57.stopped', text_57.tStopRefresh)
                # check responses
                if key_resp_17.keys in ['', [], None]:  # No response was made
                    key_resp_17.keys = None
                trials_10.addData('key_resp_17.keys',key_resp_17.keys)
                if key_resp_17.keys != None:  # we had a response
                    trials_10.addData('key_resp_17.rt', key_resp_17.rt)
                trials_10.addData('key_resp_17.started', key_resp_17.tStartRefresh)
                trials_10.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
                trials_10.addData('text_83.started', text_83.tStartRefresh)
                trials_10.addData('text_83.stopped', text_83.tStopRefresh)
                # the Routine "ask_to_assume_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_11 = data.TrialHandler(nReps=7, method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_11')
                thisExp.addLoop(trials_11)  # add the loop to the experiment
                thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
                if thisTrial_11 != None:
                    for paramName in thisTrial_11:
                        exec('{} = thisTrial_11[paramName]'.format(paramName))
                
                for thisTrial_11 in trials_11:
                    currentLoop = trials_11
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
                    if thisTrial_11 != None:
                        for paramName in thisTrial_11:
                            exec('{} = thisTrial_11[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "perspective_2"-------
                    # update component parameters for each repeat
                    event.clearEvents()
                    text_60.setText(this_perspective)
                    image_2.setImage(display_pic)
                    key_resp_23.keys = []
                    key_resp_23.rt = []
                    # keep track of which components have finished
                    perspective_2Components = [text_60, image_2, text_58, key_resp_23]
                    for thisComponent in perspective_2Components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    perspective_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    continueRoutine = True
                    
                    # -------Run Routine "perspective_2"-------
                    while continueRoutine:
                        # get current time
                        t = perspective_2Clock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=perspective_2Clock)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        for key in event.getKeys():
                            if key in ['q']: 
                                trials_11.finished = 1
                                continueRoutine = False
                        
                        # *text_60* updates
                        if text_60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_60.frameNStart = frameN  # exact frame index
                            text_60.tStart = t  # local t and not account for scr refresh
                            text_60.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_60, 'tStartRefresh')  # time at next scr refresh
                            text_60.setAutoDraw(True)
                        
                        # *image_2* updates
                        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            image_2.frameNStart = frameN  # exact frame index
                            image_2.tStart = t  # local t and not account for scr refresh
                            image_2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                            image_2.setAutoDraw(True)
                        
                        # *text_58* updates
                        if text_58.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_58.frameNStart = frameN  # exact frame index
                            text_58.tStart = t  # local t and not account for scr refresh
                            text_58.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_58, 'tStartRefresh')  # time at next scr refresh
                            text_58.setAutoDraw(True)
                        
                        # *key_resp_23* updates
                        waitOnFlip = False
                        if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            key_resp_23.frameNStart = frameN  # exact frame index
                            key_resp_23.tStart = t  # local t and not account for scr refresh
                            key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
                            key_resp_23.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if key_resp_23.status == STARTED and not waitOnFlip:
                            theseKeys = key_resp_23.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                            if len(theseKeys):
                                theseKeys = theseKeys[0]  # at least one key was pressed
                                
                                # check for quit:
                                if "escape" == theseKeys:
                                    endExpNow = True
                                key_resp_23.keys = theseKeys.name  # just the last key pressed
                                key_resp_23.rt = theseKeys.rt
                                # a response ends the routine
                                continueRoutine = False
                        
                        # check for quit (typically the Esc key)
                        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in perspective_2Components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "perspective_2"-------
                    for thisComponent in perspective_2Components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    trials_11.addData('text_60.started', text_60.tStartRefresh)
                    trials_11.addData('text_60.stopped', text_60.tStopRefresh)
                    trials_11.addData('image_2.started', image_2.tStartRefresh)
                    trials_11.addData('image_2.stopped', image_2.tStopRefresh)
                    trials_11.addData('text_58.started', text_58.tStartRefresh)
                    trials_11.addData('text_58.stopped', text_58.tStopRefresh)
                    # check responses
                    if key_resp_23.keys in ['', [], None]:  # No response was made
                        key_resp_23.keys = None
                    trials_11.addData('key_resp_23.keys',key_resp_23.keys)
                    if key_resp_23.keys != None:  # we had a response
                        trials_11.addData('key_resp_23.rt', key_resp_23.rt)
                    trials_11.addData('key_resp_23.started', key_resp_23.tStartRefresh)
                    trials_11.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
                    # the Routine "perspective_2" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # ------Prepare to start Routine "intro_test_2"-------
                    # update component parameters for each repeat
                    key_resp_18.keys = []
                    key_resp_18.rt = []
                    # keep track of which components have finished
                    intro_test_2Components = [text_62, key_resp_18, text_84]
                    for thisComponent in intro_test_2Components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    intro_test_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    continueRoutine = True
                    
                    # -------Run Routine "intro_test_2"-------
                    while continueRoutine:
                        # get current time
                        t = intro_test_2Clock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=intro_test_2Clock)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_62* updates
                        if text_62.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_62.frameNStart = frameN  # exact frame index
                            text_62.tStart = t  # local t and not account for scr refresh
                            text_62.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_62, 'tStartRefresh')  # time at next scr refresh
                            text_62.setAutoDraw(True)
                        
                        # *key_resp_18* updates
                        waitOnFlip = False
                        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            key_resp_18.frameNStart = frameN  # exact frame index
                            key_resp_18.tStart = t  # local t and not account for scr refresh
                            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
                            key_resp_18.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if key_resp_18.status == STARTED and not waitOnFlip:
                            theseKeys = key_resp_18.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                            if len(theseKeys):
                                theseKeys = theseKeys[0]  # at least one key was pressed
                                
                                # check for quit:
                                if "escape" == theseKeys:
                                    endExpNow = True
                                key_resp_18.keys = theseKeys.name  # just the last key pressed
                                key_resp_18.rt = theseKeys.rt
                                # a response ends the routine
                                continueRoutine = False
                        
                        # *text_84* updates
                        if text_84.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_84.frameNStart = frameN  # exact frame index
                            text_84.tStart = t  # local t and not account for scr refresh
                            text_84.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_84, 'tStartRefresh')  # time at next scr refresh
                            text_84.setAutoDraw(True)
                        
                        # check for quit (typically the Esc key)
                        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in intro_test_2Components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "intro_test_2"-------
                    for thisComponent in intro_test_2Components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    trials_11.addData('text_62.started', text_62.tStartRefresh)
                    trials_11.addData('text_62.stopped', text_62.tStopRefresh)
                    # check responses
                    if key_resp_18.keys in ['', [], None]:  # No response was made
                        key_resp_18.keys = None
                    trials_11.addData('key_resp_18.keys',key_resp_18.keys)
                    if key_resp_18.keys != None:  # we had a response
                        trials_11.addData('key_resp_18.rt', key_resp_18.rt)
                    trials_11.addData('key_resp_18.started', key_resp_18.tStartRefresh)
                    trials_11.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
                    trials_11.addData('text_84.started', text_84.tStartRefresh)
                    trials_11.addData('text_84.stopped', text_84.tStopRefresh)
                    # the Routine "intro_test_2" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # ------Prepare to start Routine "perspective_test_4"-------
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
                    perspective_test_4Components = [question1_2, question2_2, question3_2, question4_2, question5_2, question6_2, image_15]
                    for thisComponent in perspective_test_4Components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    perspective_test_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    continueRoutine = True
                    
                    # -------Run Routine "perspective_test_4"-------
                    while continueRoutine:
                        # get current time
                        t = perspective_test_4Clock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=perspective_test_4Clock)
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
                        #question 1 selection, keypress 8 on button box
                        if event.getKeys(['8']):
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
                        
                        #question 2 selection, keypress 7 on button box
                        if event.getKeys(['7']):
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
                        
                        #question 3 selection, keypress 6 on button box
                        if event.getKeys(['6']):
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
                        
                        #question 4 selection, keypress 1 on button box
                        if event.getKeys(['1']):
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
                        
                        #question 5 selection, keypress 2 on button box
                        if event.getKeys(['2']):
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
                        
                        #question 6 collection, keypress 3 on button box
                        if event.getKeys(['3']):
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
                        for thisComponent in perspective_test_4Components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "perspective_test_4"-------
                    for thisComponent in perspective_test_4Components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    trials_11.addData('question1_2.started', question1_2.tStartRefresh)
                    trials_11.addData('question1_2.stopped', question1_2.tStopRefresh)
                    trials_11.addData('question2_2.started', question2_2.tStartRefresh)
                    trials_11.addData('question2_2.stopped', question2_2.tStopRefresh)
                    trials_11.addData('question3_2.started', question3_2.tStartRefresh)
                    trials_11.addData('question3_2.stopped', question3_2.tStopRefresh)
                    trials_11.addData('question4_2.started', question4_2.tStartRefresh)
                    trials_11.addData('question4_2.stopped', question4_2.tStopRefresh)
                    trials_11.addData('question5_2.started', question5_2.tStartRefresh)
                    trials_11.addData('question5_2.stopped', question5_2.tStopRefresh)
                    trials_11.addData('question6_2.started', question6_2.tStartRefresh)
                    trials_11.addData('question6_2.stopped', question6_2.tStopRefresh)
                    trials_11.addData('image_15.started', image_15.tStartRefresh)
                    trials_11.addData('image_15.stopped', image_15.tStopRefresh)
                    # the Routine "perspective_test_4" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 7 repeats of 'trials_11'
                
                
                # ------Prepare to start Routine "p_again_2"-------
                # update component parameters for each repeat
                key_resp_19.keys = []
                key_resp_19.rt = []
                # keep track of which components have finished
                p_again_2Components = [text_59, key_resp_19, text_85]
                for thisComponent in p_again_2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                p_again_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "p_again_2"-------
                while continueRoutine:
                    # get current time
                    t = p_again_2Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=p_again_2Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_59* updates
                    if text_59.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_59.frameNStart = frameN  # exact frame index
                        text_59.tStart = t  # local t and not account for scr refresh
                        text_59.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_59, 'tStartRefresh')  # time at next scr refresh
                        text_59.setAutoDraw(True)
                    
                    # *key_resp_19* updates
                    waitOnFlip = False
                    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_19.frameNStart = frameN  # exact frame index
                        key_resp_19.tStart = t  # local t and not account for scr refresh
                        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
                        key_resp_19.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_19.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_19.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_19.keys = theseKeys.name  # just the last key pressed
                            key_resp_19.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_85* updates
                    if text_85.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_85.frameNStart = frameN  # exact frame index
                        text_85.tStart = t  # local t and not account for scr refresh
                        text_85.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_85, 'tStartRefresh')  # time at next scr refresh
                        text_85.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in p_again_2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "p_again_2"-------
                for thisComponent in p_again_2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials_10.addData('text_59.started', text_59.tStartRefresh)
                trials_10.addData('text_59.stopped', text_59.tStopRefresh)
                # check responses
                if key_resp_19.keys in ['', [], None]:  # No response was made
                    key_resp_19.keys = None
                trials_10.addData('key_resp_19.keys',key_resp_19.keys)
                if key_resp_19.keys != None:  # we had a response
                    trials_10.addData('key_resp_19.rt', key_resp_19.rt)
                trials_10.addData('key_resp_19.started', key_resp_19.tStartRefresh)
                trials_10.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
                trials_10.addData('text_85.started', text_85.tStartRefresh)
                trials_10.addData('text_85.stopped', text_85.tStopRefresh)
                # the Routine "p_again_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "perspective_3"-------
                # update component parameters for each repeat
                event.clearEvents()
                
                text_61.setText(this_perspective)
                image_17.setImage(display_pic)
                key_resp_24.keys = []
                key_resp_24.rt = []
                # keep track of which components have finished
                perspective_3Components = [text_61, image_17, text_63, key_resp_24]
                for thisComponent in perspective_3Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                perspective_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "perspective_3"-------
                while continueRoutine:
                    # get current time
                    t = perspective_3Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=perspective_3Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    for key in event.getKeys():
                        if key in ['q']: 
                            trials.finished = 1
                            continueRoutine = False
                    
                    # *text_61* updates
                    if text_61.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_61.frameNStart = frameN  # exact frame index
                        text_61.tStart = t  # local t and not account for scr refresh
                        text_61.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_61, 'tStartRefresh')  # time at next scr refresh
                        text_61.setAutoDraw(True)
                    
                    # *image_17* updates
                    if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_17.frameNStart = frameN  # exact frame index
                        image_17.tStart = t  # local t and not account for scr refresh
                        image_17.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
                        image_17.setAutoDraw(True)
                    
                    # *text_63* updates
                    if text_63.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_63.frameNStart = frameN  # exact frame index
                        text_63.tStart = t  # local t and not account for scr refresh
                        text_63.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_63, 'tStartRefresh')  # time at next scr refresh
                        text_63.setAutoDraw(True)
                    
                    # *key_resp_24* updates
                    waitOnFlip = False
                    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_24.frameNStart = frameN  # exact frame index
                        key_resp_24.tStart = t  # local t and not account for scr refresh
                        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
                        key_resp_24.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_24.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_24.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_24.keys = theseKeys.name  # just the last key pressed
                            key_resp_24.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in perspective_3Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "perspective_3"-------
                for thisComponent in perspective_3Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials_10.addData('text_61.started', text_61.tStartRefresh)
                trials_10.addData('text_61.stopped', text_61.tStopRefresh)
                trials_10.addData('image_17.started', image_17.tStartRefresh)
                trials_10.addData('image_17.stopped', image_17.tStopRefresh)
                trials_10.addData('text_63.started', text_63.tStartRefresh)
                trials_10.addData('text_63.stopped', text_63.tStopRefresh)
                # check responses
                if key_resp_24.keys in ['', [], None]:  # No response was made
                    key_resp_24.keys = None
                trials_10.addData('key_resp_24.keys',key_resp_24.keys)
                if key_resp_24.keys != None:  # we had a response
                    trials_10.addData('key_resp_24.rt', key_resp_24.rt)
                trials_10.addData('key_resp_24.started', key_resp_24.tStartRefresh)
                trials_10.addData('key_resp_24.stopped', key_resp_24.tStopRefresh)
                # the Routine "perspective_3" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed nreps_persp repeats of 'trials_10'
            
            
            # ------Prepare to start Routine "story_begin_2"-------
            # update component parameters for each repeat
            key_resp_20.keys = []
            key_resp_20.rt = []
            # keep track of which components have finished
            story_begin_2Components = [text_64, key_resp_20]
            for thisComponent in story_begin_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            story_begin_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "story_begin_2"-------
            while continueRoutine:
                # get current time
                t = story_begin_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=story_begin_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_64* updates
                if text_64.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_64.frameNStart = frameN  # exact frame index
                    text_64.tStart = t  # local t and not account for scr refresh
                    text_64.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_64, 'tStartRefresh')  # time at next scr refresh
                    text_64.setAutoDraw(True)
                
                # *key_resp_20* updates
                waitOnFlip = False
                if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_20.frameNStart = frameN  # exact frame index
                    key_resp_20.tStart = t  # local t and not account for scr refresh
                    key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
                    key_resp_20.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_20.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_20.getKeys(keyList=['9', '8', '7', '6', '5', '4', '3', '2', '1', 'space'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        key_resp_20.keys = theseKeys.name  # just the last key pressed
                        key_resp_20.rt = theseKeys.rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in story_begin_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "story_begin_2"-------
            for thisComponent in story_begin_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_9.addData('text_64.started', text_64.tStartRefresh)
            trials_9.addData('text_64.stopped', text_64.tStopRefresh)
            # check responses
            if key_resp_20.keys in ['', [], None]:  # No response was made
                key_resp_20.keys = None
            trials_9.addData('key_resp_20.keys',key_resp_20.keys)
            if key_resp_20.keys != None:  # we had a response
                trials_9.addData('key_resp_20.rt', key_resp_20.rt)
            trials_9.addData('key_resp_20.started', key_resp_20.tStartRefresh)
            trials_9.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
            # the Routine "story_begin_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_12 = data.TrialHandler(nReps=int(expInfo['behavioral']), method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(this_story_file),
                seed=None, name='trials_12')
            thisExp.addLoop(trials_12)  # add the loop to the experiment
            thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
            if thisTrial_12 != None:
                for paramName in thisTrial_12:
                    exec('{} = thisTrial_12[paramName]'.format(paramName))
            
            for thisTrial_12 in trials_12:
                currentLoop = trials_12
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
                if thisTrial_12 != None:
                    for paramName in thisTrial_12:
                        exec('{} = thisTrial_12[paramName]'.format(paramName))
                
                # set up handler to look after randomisation of conditions etc
                trials_24 = data.TrialHandler(nReps=int(expInfo['play_stories']), method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='trials_24')
                thisExp.addLoop(trials_24)  # add the loop to the experiment
                thisTrial_24 = trials_24.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
                if thisTrial_24 != None:
                    for paramName in thisTrial_24:
                        exec('{} = thisTrial_24[paramName]'.format(paramName))
                
                for thisTrial_24 in trials_24:
                    currentLoop = trials_24
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
                    if thisTrial_24 != None:
                        for paramName in thisTrial_24:
                            exec('{} = thisTrial_24[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "play_audio_story_2"-------
                    # update component parameters for each repeat
                    thisExp.addData('clip_StartTime', getRelTime())
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
                    play_audio_story_2Components = []
                    for thisComponent in play_audio_story_2Components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    play_audio_story_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    continueRoutine = True
                    
                    # -------Run Routine "play_audio_story_2"-------
                    while continueRoutine:
                        # get current time
                        t = play_audio_story_2Clock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=play_audio_story_2Clock)
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
                        for thisComponent in play_audio_story_2Components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "play_audio_story_2"-------
                    for thisComponent in play_audio_story_2Components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('clip_EndTime', getRelTime())
                    # the Routine "play_audio_story_2" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed int(expInfo['play_stories']) repeats of 'trials_24'
                
                
                # ------Prepare to start Routine "trial_2"-------
                # update component parameters for each repeat
                story_presses_2.keys = []
                story_presses_2.rt = []
                event.clearEvents()
                stim = visual.ImageStim(win, image=this_story_pic)
                
                # keep track of which components have finished
                trial_2Components = [story_presses_2, text_65, text_66]
                for thisComponent in trial_2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "trial_2"-------
                while continueRoutine:
                    # get current time
                    t = trial_2Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *story_presses_2* updates
                    waitOnFlip = False
                    if story_presses_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        story_presses_2.frameNStart = frameN  # exact frame index
                        story_presses_2.tStart = t  # local t and not account for scr refresh
                        story_presses_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(story_presses_2, 'tStartRefresh')  # time at next scr refresh
                        story_presses_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(story_presses_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(story_presses_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if story_presses_2.status == STARTED and not waitOnFlip:
                        theseKeys = story_presses_2.getKeys(keyList=['1', '9'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            if story_presses_2.keys == []:  # then this was the first keypress
                                story_presses_2.keys = theseKeys.name  # just the first key pressed
                                story_presses_2.rt = theseKeys.rt
                                # a response ends the routine
                                continueRoutine = False
                    stim.draw()
                    
                    for key in event.getKeys():
                        if key in ['t']: 
                            trials_12.finished = 1
                            continueRoutine = False
                    
                    # *text_65* updates
                    if text_65.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_65.frameNStart = frameN  # exact frame index
                        text_65.tStart = t  # local t and not account for scr refresh
                        text_65.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_65, 'tStartRefresh')  # time at next scr refresh
                        text_65.setAutoDraw(True)
                    
                    # *text_66* updates
                    if text_66.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_66.frameNStart = frameN  # exact frame index
                        text_66.tStart = t  # local t and not account for scr refresh
                        text_66.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_66, 'tStartRefresh')  # time at next scr refresh
                        text_66.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trial_2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "trial_2"-------
                for thisComponent in trial_2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if story_presses_2.keys in ['', [], None]:  # No response was made
                    story_presses_2.keys = None
                trials_12.addData('story_presses_2.keys',story_presses_2.keys)
                if story_presses_2.keys != None:  # we had a response
                    trials_12.addData('story_presses_2.rt', story_presses_2.rt)
                trials_12.addData('story_presses_2.started', story_presses_2.tStartRefresh)
                trials_12.addData('story_presses_2.stopped', story_presses_2.tStopRefresh)
                trials_12.addData('text_65.started', text_65.tStartRefresh)
                trials_12.addData('text_65.stopped', text_65.tStopRefresh)
                trials_12.addData('text_66.started', text_66.tStartRefresh)
                trials_12.addData('text_66.stopped', text_66.tStopRefresh)
                # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed int(expInfo['behavioral']) repeats of 'trials_12'
            
            
            # set up handler to look after randomisation of conditions etc
            trials_25 = data.TrialHandler(nReps=int(expInfo['play_stories']), method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_25')
            thisExp.addLoop(trials_25)  # add the loop to the experiment
            thisTrial_25 = trials_25.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
            if thisTrial_25 != None:
                for paramName in thisTrial_25:
                    exec('{} = thisTrial_25[paramName]'.format(paramName))
            
            for thisTrial_25 in trials_25:
                currentLoop = trials_25
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
                if thisTrial_25 != None:
                    for paramName in thisTrial_25:
                        exec('{} = thisTrial_25[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "show_image_3sec"-------
                # update component parameters for each repeat
                thisExp.addData('storyImage_StartTime', getRelTime())
                start_time = globalClock.getTime()
                stim = visual.ImageStim(win, image=this_story_pic)
                stim.draw()
                while p.is_playing() or (globalClock.getTime()-start_time < 3):
                   stim.draw()
                   win.flip()
                
                continueRoutine=False
                # keep track of which components have finished
                show_image_3secComponents = []
                for thisComponent in show_image_3secComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                show_image_3secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "show_image_3sec"-------
                while continueRoutine:
                    # get current time
                    t = show_image_3secClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=show_image_3secClock)
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
                    for thisComponent in show_image_3secComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "show_image_3sec"-------
                for thisComponent in show_image_3secComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('storyImage_EndTime', getRelTime())
                # the Routine "show_image_3sec" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials_15 = data.TrialHandler(nReps=1 - int(expInfo['behavioral']), method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions(this_story_file),
                    seed=None, name='trials_15')
                thisExp.addLoop(trials_15)  # add the loop to the experiment
                thisTrial_15 = trials_15.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
                if thisTrial_15 != None:
                    for paramName in thisTrial_15:
                        exec('{} = thisTrial_15[paramName]'.format(paramName))
                
                for thisTrial_15 in trials_15:
                    currentLoop = trials_15
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
                    if thisTrial_15 != None:
                        for paramName in thisTrial_15:
                            exec('{} = thisTrial_15[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "play_audio_story_2"-------
                    # update component parameters for each repeat
                    thisExp.addData('clip_StartTime', getRelTime())
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
                    play_audio_story_2Components = []
                    for thisComponent in play_audio_story_2Components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    play_audio_story_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    continueRoutine = True
                    
                    # -------Run Routine "play_audio_story_2"-------
                    while continueRoutine:
                        # get current time
                        t = play_audio_story_2Clock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=play_audio_story_2Clock)
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
                        for thisComponent in play_audio_story_2Components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "play_audio_story_2"-------
                    for thisComponent in play_audio_story_2Components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('clip_EndTime', getRelTime())
                    # the Routine "play_audio_story_2" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 1 - int(expInfo['behavioral']) repeats of 'trials_15'
                
                thisExp.nextEntry()
                
            # completed int(expInfo['play_stories']) repeats of 'trials_25'
            
            
            # set up handler to look after randomisation of conditions etc
            trials_26 = data.TrialHandler(nReps=1 - int(expInfo['play_stories']), method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_26')
            thisExp.addLoop(trials_26)  # add the loop to the experiment
            thisTrial_26 = trials_26.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_26.rgb)
            if thisTrial_26 != None:
                for paramName in thisTrial_26:
                    exec('{} = thisTrial_26[paramName]'.format(paramName))
            
            for thisTrial_26 in trials_26:
                currentLoop = trials_26
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_26.rgb)
                if thisTrial_26 != None:
                    for paramName in thisTrial_26:
                        exec('{} = thisTrial_26[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "show_storyimage2"-------
                # update component parameters for each repeat
                key_resp_29.keys = []
                key_resp_29.rt = []
                image_22.setImage(this_story_pic)
                thisExp.addData('clip_StartTime', getRelTime())
                # keep track of which components have finished
                show_storyimage2Components = [key_resp_29, image_22]
                for thisComponent in show_storyimage2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                show_storyimage2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                continueRoutine = True
                
                # -------Run Routine "show_storyimage2"-------
                while continueRoutine:
                    # get current time
                    t = show_storyimage2Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=show_storyimage2Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *key_resp_29* updates
                    waitOnFlip = False
                    if key_resp_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_29.frameNStart = frameN  # exact frame index
                        key_resp_29.tStart = t  # local t and not account for scr refresh
                        key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
                        key_resp_29.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_29.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_29.getKeys(keyList=['space'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            key_resp_29.keys = theseKeys.name  # just the last key pressed
                            key_resp_29.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *image_22* updates
                    if image_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_22.frameNStart = frameN  # exact frame index
                        image_22.tStart = t  # local t and not account for scr refresh
                        image_22.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
                        image_22.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in show_storyimage2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "show_storyimage2"-------
                for thisComponent in show_storyimage2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if key_resp_29.keys in ['', [], None]:  # No response was made
                    key_resp_29.keys = None
                trials_26.addData('key_resp_29.keys',key_resp_29.keys)
                if key_resp_29.keys != None:  # we had a response
                    trials_26.addData('key_resp_29.rt', key_resp_29.rt)
                trials_26.addData('key_resp_29.started', key_resp_29.tStartRefresh)
                trials_26.addData('key_resp_29.stopped', key_resp_29.tStopRefresh)
                trials_26.addData('image_22.started', image_22.tStartRefresh)
                trials_26.addData('image_22.stopped', image_22.tStopRefresh)
                thisExp.addData('clip_EndTime', getRelTime())
                # the Routine "show_storyimage2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 - int(expInfo['play_stories']) repeats of 'trials_26'
            
            
            # ------Prepare to start Routine "routine_6sec_wait"-------
            routineTimer.add(6.000000)
            # update component parameters for each repeat
            thisExp.addData('startWait', getRelTime())
            # keep track of which components have finished
            routine_6sec_waitComponents = [image_23]
            for thisComponent in routine_6sec_waitComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            routine_6sec_waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "routine_6sec_wait"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_6sec_waitClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routine_6sec_waitClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_23* updates
                if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_23.frameNStart = frameN  # exact frame index
                    image_23.tStart = t  # local t and not account for scr refresh
                    image_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
                    image_23.setAutoDraw(True)
                if image_23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_23.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        image_23.tStop = t  # not accounting for scr refresh
                        image_23.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_23, 'tStopRefresh')  # time at next scr refresh
                        image_23.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_6sec_waitComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "routine_6sec_wait"-------
            for thisComponent in routine_6sec_waitComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('endWait', getRelTime())
            trials_9.addData('image_23.started', image_23.tStartRefresh)
            trials_9.addData('image_23.stopped', image_23.tStopRefresh)
            
            # ------Prepare to start Routine "end_story_2"-------
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            text_67.setText((story_count))
            # keep track of which components have finished
            end_story_2Components = [text_67, text_68]
            for thisComponent in end_story_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            end_story_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "end_story_2"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = end_story_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=end_story_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_67* updates
                if text_67.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_67.frameNStart = frameN  # exact frame index
                    text_67.tStart = t  # local t and not account for scr refresh
                    text_67.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_67, 'tStartRefresh')  # time at next scr refresh
                    text_67.setAutoDraw(True)
                if text_67.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_67.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        text_67.tStop = t  # not accounting for scr refresh
                        text_67.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_67, 'tStopRefresh')  # time at next scr refresh
                        text_67.setAutoDraw(False)
                
                # *text_68* updates
                if text_68.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_68.frameNStart = frameN  # exact frame index
                    text_68.tStart = t  # local t and not account for scr refresh
                    text_68.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_68, 'tStartRefresh')  # time at next scr refresh
                    text_68.setAutoDraw(True)
                if text_68.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_68.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        text_68.tStop = t  # not accounting for scr refresh
                        text_68.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_68, 'tStopRefresh')  # time at next scr refresh
                        text_68.setAutoDraw(False)
                for key in event.getKeys():
                    if key in ['t']: 
                        trials_14.finished = 1
                        continueRoutine = False
                        
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in end_story_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "end_story_2"-------
            for thisComponent in end_story_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_9.addData('text_67.started', text_67.tStartRefresh)
            trials_9.addData('text_67.stopped', text_67.tStopRefresh)
            trials_9.addData('text_68.started', text_68.tStartRefresh)
            trials_9.addData('text_68.stopped', text_68.tStopRefresh)
            thisExp.saveAsWideText(filename+'_safety.csv', appendFile=True)
            thisExp.nextEntry()
            
        # completed nreps_whole repeats of 'trials_9'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_6'
    
    thisExp.nextEntry()
    
# completed block2_play repeats of 'trials_4'


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
    routineTimer.add(0.500000)
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
            if tThisFlipGlobal > text_36.tStartRefresh + .5-frameTolerance:
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
