#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 09, 2019, at 02:56
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
psychopyVersion = '3.2.3'
expName = 'Assignment2_psychology'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Session': '001'}
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
    originPath='C:\\Users\\ruhma\\Desktop\\psych\\Assigntment2_psychology_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Start_experiment"
Start_experimentClock = core.Clock()
Start_Experiment = visual.TextStim(win=win, name='Start_Experiment',
    text='Press any key to start the experiment\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp_start = keyboard.Keyboard()

# Initialize components for Routine "Introduction_exo"
Introduction_exoClock = core.Clock()
Experiment_introduction = visual.TextStim(win=win, name='Experiment_introduction',
    text="\n\nYou will see a Fixation point and two boxes.\n\nPress the left arrow key if the 'X' is in the left box and right arrow key if the 'X' is in the right box.\n\nPress space to continue\n",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp_continue_exo = keyboard.Keyboard()

# Initialize components for Routine "Trial_exo"
Trial_exoClock = core.Clock()
Fixation_point = visual.TextStim(win=win, name='Fixation_point',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rect_left = visual.Rect(
    win=win, name='rect_left',units='cm', 
    width=(6, 6)[0], height=(6, 6)[1],
    ori=0, pos=(-7, 0),
    lineWidth=8, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-1.0, interpolate=True)
rect_right = visual.Rect(
    win=win, name='rect_right',units='cm', 
    width=(6,6)[0], height=(6,6)[1],
    ori=0, pos=(7, 0),
    lineWidth=8, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-2.0, interpolate=True)
rect_highlight = visual.Rect(
    win=win, name='rect_highlight',units='cm', 
    width=(6,6)[0], height=(6,6)[1],
    ori=0, pos=[0,0],
    lineWidth=9, lineColor=[255, 255, 0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-3.0, interpolate=True)
cross_cue = visual.ShapeStim(
    win=win, name='cross_cue', vertices='cross',units='cm', 
    size=(2, 2),
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=[255, 255, 0], lineColorSpace='rgb',
    fillColor=[255, 255, 0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
resp_stimuli = keyboard.Keyboard()

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Introduction_endo"
Introduction_endoClock = core.Clock()
Experiment_introduction_2 = visual.TextStim(win=win, name='Experiment_introduction_2',
    text="You will see a Fixation point and two boxes.\n\nPress the left arrow key if the 'X' is in the left box and right arrow key if the 'X' is in the right box.\n\nPress space to continue\n",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp_endo = keyboard.Keyboard()

# Initialize components for Routine "Trial_endo"
Trial_endoClock = core.Clock()
fixationPoint = visual.TextStim(win=win, name='fixationPoint',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rect_left_2 = visual.Rect(
    win=win, name='rect_left_2',units='cm', 
    width=(6, 6)[0], height=(6, 6)[1],
    ori=0, pos=(-7, 0),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-1.0, interpolate=True)
rect_right_2 = visual.Rect(
    win=win, name='rect_right_2',units='cm', 
    width=(6, 6)[0], height=(6, 6)[1],
    ori=0, pos=(7, 0),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-2.0, interpolate=True)
Arrow = visual.ImageStim(
    win=win,
    name='Arrow', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0, 3.5), size=(3, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
cross_cue_2 = visual.ShapeStim(
    win=win, name='cross_cue_2', vertices='cross',units='cm', 
    size=(2, 2),
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=[255, 255, 0], lineColorSpace='rgb',
    fillColor=[255, 255, 0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
resp_stimuli_2 = keyboard.Keyboard()

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thankyou"
ThankyouClock = core.Clock()
Thanks = visual.TextStim(win=win, name='Thanks',
    text='Thank you for participating in the experiment!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start_experiment"-------
# update component parameters for each repeat
resp_start.keys = []
resp_start.rt = []
# keep track of which components have finished
Start_experimentComponents = [Start_Experiment, resp_start]
for thisComponent in Start_experimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start_experimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Start_experiment"-------
while continueRoutine:
    # get current time
    t = Start_experimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_experimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Start_Experiment* updates
    if Start_Experiment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Start_Experiment.frameNStart = frameN  # exact frame index
        Start_Experiment.tStart = t  # local t and not account for scr refresh
        Start_Experiment.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Start_Experiment, 'tStartRefresh')  # time at next scr refresh
        Start_Experiment.setAutoDraw(True)
    
    # *resp_start* updates
    waitOnFlip = False
    if resp_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_start.frameNStart = frameN  # exact frame index
        resp_start.tStart = t  # local t and not account for scr refresh
        resp_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_start, 'tStartRefresh')  # time at next scr refresh
        resp_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_start.status == STARTED and not waitOnFlip:
        theseKeys = resp_start.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            resp_start.keys = theseKeys.name  # just the last key pressed
            resp_start.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_experimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_experiment"-------
for thisComponent in Start_experimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Start_Experiment.started', Start_Experiment.tStartRefresh)
thisExp.addData('Start_Experiment.stopped', Start_Experiment.tStopRefresh)
# check responses
if resp_start.keys in ['', [], None]:  # No response was made
    resp_start.keys = None
thisExp.addData('resp_start.keys',resp_start.keys)
if resp_start.keys != None:  # we had a response
    thisExp.addData('resp_start.rt', resp_start.rt)
thisExp.addData('resp_start.started', resp_start.tStartRefresh)
thisExp.addData('resp_start.stopped', resp_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start_experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Introduction_exo"-------
# update component parameters for each repeat
resp_continue_exo.keys = []
resp_continue_exo.rt = []
# keep track of which components have finished
Introduction_exoComponents = [Experiment_introduction, resp_continue_exo]
for thisComponent in Introduction_exoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Introduction_exoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Introduction_exo"-------
while continueRoutine:
    # get current time
    t = Introduction_exoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Introduction_exoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Experiment_introduction* updates
    if Experiment_introduction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Experiment_introduction.frameNStart = frameN  # exact frame index
        Experiment_introduction.tStart = t  # local t and not account for scr refresh
        Experiment_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Experiment_introduction, 'tStartRefresh')  # time at next scr refresh
        Experiment_introduction.setAutoDraw(True)
    
    # *resp_continue_exo* updates
    waitOnFlip = False
    if resp_continue_exo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        resp_continue_exo.frameNStart = frameN  # exact frame index
        resp_continue_exo.tStart = t  # local t and not account for scr refresh
        resp_continue_exo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_continue_exo, 'tStartRefresh')  # time at next scr refresh
        resp_continue_exo.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_continue_exo.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_continue_exo.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_continue_exo.status == STARTED and not waitOnFlip:
        theseKeys = resp_continue_exo.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            resp_continue_exo.keys = theseKeys.name  # just the last key pressed
            resp_continue_exo.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_exoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction_exo"-------
for thisComponent in Introduction_exoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Experiment_introduction.started', Experiment_introduction.tStartRefresh)
thisExp.addData('Experiment_introduction.stopped', Experiment_introduction.tStopRefresh)
# check responses
if resp_continue_exo.keys in ['', [], None]:  # No response was made
    resp_continue_exo.keys = None
thisExp.addData('resp_continue_exo.keys',resp_continue_exo.keys)
if resp_continue_exo.keys != None:  # we had a response
    thisExp.addData('resp_continue_exo.rt', resp_continue_exo.rt)
thisExp.addData('resp_continue_exo.started', resp_continue_exo.tStartRefresh)
thisExp.addData('resp_continue_exo.stopped', resp_continue_exo.tStopRefresh)
thisExp.nextEntry()
# the Routine "Introduction_exo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment.xlsx'),
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
    
    # ------Prepare to start Routine "Trial_exo"-------
    routineTimer.add(0.900000)
    # update component parameters for each repeat
    rect_highlight.setPos(Pos_highlight_exo)
    cross_cue.setPos(Pos_cue_exo)
    resp_stimuli.keys = []
    resp_stimuli.rt = []
    # keep track of which components have finished
    Trial_exoComponents = [Fixation_point, rect_left, rect_right, rect_highlight, cross_cue, resp_stimuli]
    for thisComponent in Trial_exoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_exoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Trial_exo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Trial_exoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_exoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_point* updates
        if Fixation_point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_point.frameNStart = frameN  # exact frame index
            Fixation_point.tStart = t  # local t and not account for scr refresh
            Fixation_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_point, 'tStartRefresh')  # time at next scr refresh
            Fixation_point.setAutoDraw(True)
        if Fixation_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_point.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_point.tStop = t  # not accounting for scr refresh
                Fixation_point.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_point, 'tStopRefresh')  # time at next scr refresh
                Fixation_point.setAutoDraw(False)
        
        # *rect_left* updates
        if rect_left.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            rect_left.frameNStart = frameN  # exact frame index
            rect_left.tStart = t  # local t and not account for scr refresh
            rect_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect_left, 'tStartRefresh')  # time at next scr refresh
            rect_left.setAutoDraw(True)
        if rect_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect_left.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                rect_left.tStop = t  # not accounting for scr refresh
                rect_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect_left, 'tStopRefresh')  # time at next scr refresh
                rect_left.setAutoDraw(False)
        
        # *rect_right* updates
        if rect_right.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            rect_right.frameNStart = frameN  # exact frame index
            rect_right.tStart = t  # local t and not account for scr refresh
            rect_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect_right, 'tStartRefresh')  # time at next scr refresh
            rect_right.setAutoDraw(True)
        if rect_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect_right.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                rect_right.tStop = t  # not accounting for scr refresh
                rect_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect_right, 'tStopRefresh')  # time at next scr refresh
                rect_right.setAutoDraw(False)
        
        # *rect_highlight* updates
        if rect_highlight.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            rect_highlight.frameNStart = frameN  # exact frame index
            rect_highlight.tStart = t  # local t and not account for scr refresh
            rect_highlight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect_highlight, 'tStartRefresh')  # time at next scr refresh
            rect_highlight.setAutoDraw(True)
        if rect_highlight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect_highlight.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                rect_highlight.tStop = t  # not accounting for scr refresh
                rect_highlight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect_highlight, 'tStopRefresh')  # time at next scr refresh
                rect_highlight.setAutoDraw(False)
        
        # *cross_cue* updates
        if cross_cue.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
            # keep track of start time/frame for later
            cross_cue.frameNStart = frameN  # exact frame index
            cross_cue.tStart = t  # local t and not account for scr refresh
            cross_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_cue, 'tStartRefresh')  # time at next scr refresh
            cross_cue.setAutoDraw(True)
        if cross_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_cue.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                cross_cue.tStop = t  # not accounting for scr refresh
                cross_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_cue, 'tStopRefresh')  # time at next scr refresh
                cross_cue.setAutoDraw(False)
        
        # *resp_stimuli* updates
        waitOnFlip = False
        if resp_stimuli.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            resp_stimuli.frameNStart = frameN  # exact frame index
            resp_stimuli.tStart = t  # local t and not account for scr refresh
            resp_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_stimuli, 'tStartRefresh')  # time at next scr refresh
            resp_stimuli.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_stimuli.clock.reset)  # t=0 on next screen flip
        if resp_stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_stimuli.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                resp_stimuli.tStop = t  # not accounting for scr refresh
                resp_stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_stimuli, 'tStopRefresh')  # time at next scr refresh
                resp_stimuli.status = FINISHED
        if resp_stimuli.status == STARTED and not waitOnFlip:
            theseKeys = resp_stimuli.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp_stimuli.keys.append(theseKeys.name)  # storing all keys
                resp_stimuli.rt.append(theseKeys.rt)
                # was this 'correct'?
                if (resp_stimuli.keys == str(correctresp_exo)) or (resp_stimuli.keys == correctresp_exo):
                    resp_stimuli.corr = 1
                else:
                    resp_stimuli.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_exoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_exo"-------
    for thisComponent in Trial_exoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Fixation_point.started', Fixation_point.tStartRefresh)
    trials.addData('Fixation_point.stopped', Fixation_point.tStopRefresh)
    trials.addData('rect_left.started', rect_left.tStartRefresh)
    trials.addData('rect_left.stopped', rect_left.tStopRefresh)
    trials.addData('rect_right.started', rect_right.tStartRefresh)
    trials.addData('rect_right.stopped', rect_right.tStopRefresh)
    trials.addData('rect_highlight.started', rect_highlight.tStartRefresh)
    trials.addData('rect_highlight.stopped', rect_highlight.tStopRefresh)
    trials.addData('cross_cue.started', cross_cue.tStartRefresh)
    trials.addData('cross_cue.stopped', cross_cue.tStopRefresh)
    # check responses
    if resp_stimuli.keys in ['', [], None]:  # No response was made
        resp_stimuli.keys = None
        # was no response the correct answer?!
        if str(correctresp_exo).lower() == 'none':
           resp_stimuli.corr = 1;  # correct non-response
        else:
           resp_stimuli.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp_stimuli.keys',resp_stimuli.keys)
    trials.addData('resp_stimuli.corr', resp_stimuli.corr)
    if resp_stimuli.keys != None:  # we had a response
        trials.addData('resp_stimuli.rt', resp_stimuli.rt)
    trials.addData('resp_stimuli.started', resp_stimuli.tStartRefresh)
    trials.addData('resp_stimuli.stopped', resp_stimuli.tStopRefresh)
    
    # ------Prepare to start Routine "Blank"-------
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankComponents = [Fixation]
    for thisComponent in BlankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank"-------
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Fixation.started', Fixation.tStartRefresh)
    thisExp.addData('Fixation.stopped', Fixation.tStopRefresh)
# completed 3 repeats of 'trials'


# ------Prepare to start Routine "Introduction_endo"-------
# update component parameters for each repeat
resp_endo.keys = []
resp_endo.rt = []
# keep track of which components have finished
Introduction_endoComponents = [Experiment_introduction_2, resp_endo]
for thisComponent in Introduction_endoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Introduction_endoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Introduction_endo"-------
while continueRoutine:
    # get current time
    t = Introduction_endoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Introduction_endoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Experiment_introduction_2* updates
    if Experiment_introduction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Experiment_introduction_2.frameNStart = frameN  # exact frame index
        Experiment_introduction_2.tStart = t  # local t and not account for scr refresh
        Experiment_introduction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Experiment_introduction_2, 'tStartRefresh')  # time at next scr refresh
        Experiment_introduction_2.setAutoDraw(True)
    
    # *resp_endo* updates
    waitOnFlip = False
    if resp_endo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_endo.frameNStart = frameN  # exact frame index
        resp_endo.tStart = t  # local t and not account for scr refresh
        resp_endo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_endo, 'tStartRefresh')  # time at next scr refresh
        resp_endo.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_endo.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_endo.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_endo.status == STARTED and not waitOnFlip:
        theseKeys = resp_endo.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            resp_endo.keys = theseKeys.name  # just the last key pressed
            resp_endo.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_endoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction_endo"-------
for thisComponent in Introduction_endoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Experiment_introduction_2.started', Experiment_introduction_2.tStartRefresh)
thisExp.addData('Experiment_introduction_2.stopped', Experiment_introduction_2.tStopRefresh)
# check responses
if resp_endo.keys in ['', [], None]:  # No response was made
    resp_endo.keys = None
thisExp.addData('resp_endo.keys',resp_endo.keys)
if resp_endo.keys != None:  # we had a response
    thisExp.addData('resp_endo.rt', resp_endo.rt)
thisExp.addData('resp_endo.started', resp_endo.tStartRefresh)
thisExp.addData('resp_endo.stopped', resp_endo.tStopRefresh)
thisExp.nextEntry()
# the Routine "Introduction_endo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment.xlsx'),
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
    
    # ------Prepare to start Routine "Trial_endo"-------
    routineTimer.add(0.900000)
    # update component parameters for each repeat
    Arrow.setImage(Image_arrow)
    cross_cue_2.setPos(Pos_cue_exo)
    resp_stimuli_2.keys = []
    resp_stimuli_2.rt = []
    # keep track of which components have finished
    Trial_endoComponents = [fixationPoint, rect_left_2, rect_right_2, Arrow, cross_cue_2, resp_stimuli_2]
    for thisComponent in Trial_endoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_endoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Trial_endo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Trial_endoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_endoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationPoint* updates
        if fixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationPoint.frameNStart = frameN  # exact frame index
            fixationPoint.tStart = t  # local t and not account for scr refresh
            fixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationPoint, 'tStartRefresh')  # time at next scr refresh
            fixationPoint.setAutoDraw(True)
        if fixationPoint.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationPoint.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                fixationPoint.tStop = t  # not accounting for scr refresh
                fixationPoint.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationPoint, 'tStopRefresh')  # time at next scr refresh
                fixationPoint.setAutoDraw(False)
        
        # *rect_left_2* updates
        if rect_left_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            rect_left_2.frameNStart = frameN  # exact frame index
            rect_left_2.tStart = t  # local t and not account for scr refresh
            rect_left_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect_left_2, 'tStartRefresh')  # time at next scr refresh
            rect_left_2.setAutoDraw(True)
        if rect_left_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect_left_2.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                rect_left_2.tStop = t  # not accounting for scr refresh
                rect_left_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect_left_2, 'tStopRefresh')  # time at next scr refresh
                rect_left_2.setAutoDraw(False)
        
        # *rect_right_2* updates
        if rect_right_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            rect_right_2.frameNStart = frameN  # exact frame index
            rect_right_2.tStart = t  # local t and not account for scr refresh
            rect_right_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect_right_2, 'tStartRefresh')  # time at next scr refresh
            rect_right_2.setAutoDraw(True)
        if rect_right_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect_right_2.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                rect_right_2.tStop = t  # not accounting for scr refresh
                rect_right_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect_right_2, 'tStopRefresh')  # time at next scr refresh
                rect_right_2.setAutoDraw(False)
        
        # *Arrow* updates
        if Arrow.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            Arrow.frameNStart = frameN  # exact frame index
            Arrow.tStart = t  # local t and not account for scr refresh
            Arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Arrow, 'tStartRefresh')  # time at next scr refresh
            Arrow.setAutoDraw(True)
        if Arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Arrow.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Arrow.tStop = t  # not accounting for scr refresh
                Arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Arrow, 'tStopRefresh')  # time at next scr refresh
                Arrow.setAutoDraw(False)
        
        # *cross_cue_2* updates
        if cross_cue_2.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
            # keep track of start time/frame for later
            cross_cue_2.frameNStart = frameN  # exact frame index
            cross_cue_2.tStart = t  # local t and not account for scr refresh
            cross_cue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_cue_2, 'tStartRefresh')  # time at next scr refresh
            cross_cue_2.setAutoDraw(True)
        if cross_cue_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_cue_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                cross_cue_2.tStop = t  # not accounting for scr refresh
                cross_cue_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_cue_2, 'tStopRefresh')  # time at next scr refresh
                cross_cue_2.setAutoDraw(False)
        
        # *resp_stimuli_2* updates
        waitOnFlip = False
        if resp_stimuli_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            resp_stimuli_2.frameNStart = frameN  # exact frame index
            resp_stimuli_2.tStart = t  # local t and not account for scr refresh
            resp_stimuli_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_stimuli_2, 'tStartRefresh')  # time at next scr refresh
            resp_stimuli_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_stimuli_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_stimuli_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_stimuli_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_stimuli_2.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                resp_stimuli_2.tStop = t  # not accounting for scr refresh
                resp_stimuli_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_stimuli_2, 'tStopRefresh')  # time at next scr refresh
                resp_stimuli_2.status = FINISHED
        if resp_stimuli_2.status == STARTED and not waitOnFlip:
            theseKeys = resp_stimuli_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp_stimuli_2.keys = theseKeys.name  # just the last key pressed
                resp_stimuli_2.rt = theseKeys.rt
                # was this 'correct'?
                if (resp_stimuli_2.keys == str(correctresp_endo)) or (resp_stimuli_2.keys == correctresp_endo):
                    resp_stimuli_2.corr = 1
                else:
                    resp_stimuli_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_endoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_endo"-------
    for thisComponent in Trial_endoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('fixationPoint.started', fixationPoint.tStartRefresh)
    trials_2.addData('fixationPoint.stopped', fixationPoint.tStopRefresh)
    trials_2.addData('rect_left_2.started', rect_left_2.tStartRefresh)
    trials_2.addData('rect_left_2.stopped', rect_left_2.tStopRefresh)
    trials_2.addData('rect_right_2.started', rect_right_2.tStartRefresh)
    trials_2.addData('rect_right_2.stopped', rect_right_2.tStopRefresh)
    trials_2.addData('Arrow.started', Arrow.tStartRefresh)
    trials_2.addData('Arrow.stopped', Arrow.tStopRefresh)
    trials_2.addData('cross_cue_2.started', cross_cue_2.tStartRefresh)
    trials_2.addData('cross_cue_2.stopped', cross_cue_2.tStopRefresh)
    # check responses
    if resp_stimuli_2.keys in ['', [], None]:  # No response was made
        resp_stimuli_2.keys = None
        # was no response the correct answer?!
        if str(correctresp_endo).lower() == 'none':
           resp_stimuli_2.corr = 1;  # correct non-response
        else:
           resp_stimuli_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('resp_stimuli_2.keys',resp_stimuli_2.keys)
    trials_2.addData('resp_stimuli_2.corr', resp_stimuli_2.corr)
    if resp_stimuli_2.keys != None:  # we had a response
        trials_2.addData('resp_stimuli_2.rt', resp_stimuli_2.rt)
    trials_2.addData('resp_stimuli_2.started', resp_stimuli_2.tStartRefresh)
    trials_2.addData('resp_stimuli_2.stopped', resp_stimuli_2.tStopRefresh)
    
    # ------Prepare to start Routine "Blank"-------
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankComponents = [Fixation]
    for thisComponent in BlankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank"-------
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Fixation.started', Fixation.tStartRefresh)
    thisExp.addData('Fixation.stopped', Fixation.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Thankyou"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
ThankyouComponents = [Thanks, key_resp_2]
for thisComponent in ThankyouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankyouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Thankyou"-------
while continueRoutine:
    # get current time
    t = ThankyouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankyouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thanks* updates
    if Thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thanks.frameNStart = frameN  # exact frame index
        Thanks.tStart = t  # local t and not account for scr refresh
        Thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thanks, 'tStartRefresh')  # time at next scr refresh
        Thanks.setAutoDraw(True)
    
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
        theseKeys = key_resp_2.getKeys(keyList=['space', 'enter'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thankyou"-------
for thisComponent in ThankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Thanks.started', Thanks.tStartRefresh)
thisExp.addData('Thanks.stopped', Thanks.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Thankyou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
