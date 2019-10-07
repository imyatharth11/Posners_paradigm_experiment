#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 08, 2019, at 04:45
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
    originPath='C:\\Users\\ruhma\\Desktop\\psych_ass2\\Assigntment2_psychology_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[900, 700], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "Introduction_exo"
Introduction_exoClock = core.Clock()
Experiment_introduction = visual.TextStim(win=win, name='Experiment_introduction',
    text='Intro\n\npress space to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Trial_exo"
Trial_exoClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stimuli_resp = keyboard.Keyboard()
rect_left = visual.Rect(
    win=win, name='rect_left',units='cm', 
    width=(6, 6)[0], height=(6, 6)[1],
    ori=0, pos=(-6, 0),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-2.0, interpolate=True)
rect_right = visual.Rect(
    win=win, name='rect_right',units='cm', 
    width=(6,6)[0], height=(6,6)[1],
    ori=0, pos=(6, 0),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-3.0, interpolate=True)
rect_highlight = visual.Rect(
    win=win, name='rect_highlight',units='cm', 
    width=(6,6)[0], height=(6,6)[1],
    ori=0, pos=[0,0],
    lineWidth=7, lineColor=[255, 255, 0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-4.0, interpolate=True)
cross_cue = visual.ShapeStim(
    win=win, name='cross_cue', vertices='cross',units='cm', 
    size=(2, 2),
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=[255, 255, 0], lineColorSpace='rgb',
    fillColor=[255, 255, 0], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
resp_stimuli = keyboard.Keyboard()

# Initialize components for Routine "Blank"
BlankClock = core.Clock()

# Initialize components for Routine "Introduction_endo"
Introduction_endoClock = core.Clock()
Experiment_introduction_2 = visual.TextStim(win=win, name='Experiment_introduction_2',
    text='Intro\n\npress space to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Trial_endo"
Trial_endoClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stimuli_resp_2 = keyboard.Keyboard()
rect_left_2 = visual.Rect(
    win=win, name='rect_left_2',units='cm', 
    width=(6, 6)[0], height=(6, 6)[1],
    ori=0, pos=(-6, 0),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-2.0, interpolate=True)
rect_right_2 = visual.Rect(
    win=win, name='rect_right_2',units='cm', 
    width=(6, 6)[0], height=(6, 6)[1],
    ori=0, pos=(6, 0),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-3.0, interpolate=True)
Arrow = visual.ImageStim(
    win=win,
    name='Arrow', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0, 5), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
rect_highlight_2 = visual.Rect(
    win=win, name='rect_highlight_2',units='cm', 
    width=(6, 6)[0], height=(6, 6)[1],
    ori=0, pos=[0,0],
    lineWidth=7, lineColor=[255,255,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='hsv',
    opacity=1, depth=-5.0, interpolate=True)
cross_cue_2 = visual.ShapeStim(
    win=win, name='cross_cue_2', vertices='cross',units='cm', 
    size=(2, 2),
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=[255, 255, 0], lineColorSpace='rgb',
    fillColor=[255, 255, 0], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
resp_stimuli_2 = keyboard.Keyboard()

# Initialize components for Routine "Thankyou"
ThankyouClock = core.Clock()
Thanks = visual.TextStim(win=win, name='Thanks',
    text='Thanks for taking the xyz\n\npress space/enter to exit',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Introduction_exo"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
Introduction_exoComponents = [Experiment_introduction, key_resp]
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
    if Experiment_introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Experiment_introduction.frameNStart = frameN  # exact frame index
        Experiment_introduction.tStart = t  # local t and not account for scr refresh
        Experiment_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Experiment_introduction, 'tStartRefresh')  # time at next scr refresh
        Experiment_introduction.setAutoDraw(True)
    
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
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
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
    # update component parameters for each repeat
    stimuli_resp.keys = []
    stimuli_resp.rt = []
    rect_highlight.setPos(Pos_highlight_exo)
    cross_cue.setPos(Pos_cue_exo)
    resp_stimuli.keys = []
    resp_stimuli.rt = []
    # keep track of which components have finished
    Trial_exoComponents = [text, stimuli_resp, rect_left, rect_right, rect_highlight, cross_cue, resp_stimuli]
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
    while continueRoutine:
        # get current time
        t = Trial_exoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_exoClock)
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
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *stimuli_resp* updates
        waitOnFlip = False
        if stimuli_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            stimuli_resp.frameNStart = frameN  # exact frame index
            stimuli_resp.tStart = t  # local t and not account for scr refresh
            stimuli_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_resp, 'tStartRefresh')  # time at next scr refresh
            stimuli_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stimuli_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stimuli_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stimuli_resp.status == STARTED and not waitOnFlip:
            theseKeys = stimuli_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                stimuli_resp.keys = theseKeys.name  # just the last key pressed
                stimuli_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
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
            if tThisFlipGlobal > rect_left.tStartRefresh + 0.4-frameTolerance:
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
            if tThisFlipGlobal > rect_right.tStartRefresh + 0.4-frameTolerance:
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
            if tThisFlipGlobal > rect_highlight.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                rect_highlight.tStop = t  # not accounting for scr refresh
                rect_highlight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect_highlight, 'tStopRefresh')  # time at next scr refresh
                rect_highlight.setAutoDraw(False)
        
        # *cross_cue* updates
        if cross_cue.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            cross_cue.frameNStart = frameN  # exact frame index
            cross_cue.tStart = t  # local t and not account for scr refresh
            cross_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_cue, 'tStartRefresh')  # time at next scr refresh
            cross_cue.setAutoDraw(True)
        if cross_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_cue.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                cross_cue.tStop = t  # not accounting for scr refresh
                cross_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_cue, 'tStopRefresh')  # time at next scr refresh
                cross_cue.setAutoDraw(False)
        
        # *resp_stimuli* updates
        waitOnFlip = False
        if resp_stimuli.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            resp_stimuli.frameNStart = frameN  # exact frame index
            resp_stimuli.tStart = t  # local t and not account for scr refresh
            resp_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_stimuli, 'tStartRefresh')  # time at next scr refresh
            resp_stimuli.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_stimuli.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_stimuli.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_stimuli.status == STARTED and not waitOnFlip:
            theseKeys = resp_stimuli.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp_stimuli.keys = theseKeys.name  # just the last key pressed
                resp_stimuli.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
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
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if stimuli_resp.keys in ['', [], None]:  # No response was made
        stimuli_resp.keys = None
    trials.addData('stimuli_resp.keys',stimuli_resp.keys)
    if stimuli_resp.keys != None:  # we had a response
        trials.addData('stimuli_resp.rt', stimuli_resp.rt)
    trials.addData('stimuli_resp.started', stimuli_resp.tStartRefresh)
    trials.addData('stimuli_resp.stopped', stimuli_resp.tStopRefresh)
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
    trials.addData('resp_stimuli.keys',resp_stimuli.keys)
    if resp_stimuli.keys != None:  # we had a response
        trials.addData('resp_stimuli.rt', resp_stimuli.rt)
    trials.addData('resp_stimuli.started', resp_stimuli.tStartRefresh)
    trials.addData('resp_stimuli.stopped', resp_stimuli.tStopRefresh)
    # the Routine "Trial_exo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankComponents = []
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
    while continueRoutine:
        # get current time
        t = BlankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlankClock)
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
    # the Routine "Blank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# ------Prepare to start Routine "Introduction_endo"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
Introduction_endoComponents = [Experiment_introduction_2, key_resp_3]
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
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
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
    # update component parameters for each repeat
    stimuli_resp_2.keys = []
    stimuli_resp_2.rt = []
    Arrow.setImage(Image_arrow)
    rect_highlight_2.setPos(Pos_highlight_endo)
    cross_cue_2.setPos(Pos_cue_exo)
    resp_stimuli_2.keys = []
    resp_stimuli_2.rt = []
    # keep track of which components have finished
    Trial_endoComponents = [text_2, stimuli_resp_2, rect_left_2, rect_right_2, Arrow, rect_highlight_2, cross_cue_2, resp_stimuli_2]
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
    while continueRoutine:
        # get current time
        t = Trial_endoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_endoClock)
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
            if tThisFlipGlobal > text_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *stimuli_resp_2* updates
        waitOnFlip = False
        if stimuli_resp_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            stimuli_resp_2.frameNStart = frameN  # exact frame index
            stimuli_resp_2.tStart = t  # local t and not account for scr refresh
            stimuli_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_resp_2, 'tStartRefresh')  # time at next scr refresh
            stimuli_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stimuli_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stimuli_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stimuli_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = stimuli_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                stimuli_resp_2.keys = theseKeys.name  # just the last key pressed
                stimuli_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
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
            if tThisFlipGlobal > rect_left_2.tStartRefresh + 0.8-frameTolerance:
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
            if tThisFlipGlobal > rect_right_2.tStartRefresh + 0.8-frameTolerance:
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
            if tThisFlipGlobal > Arrow.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                Arrow.tStop = t  # not accounting for scr refresh
                Arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Arrow, 'tStopRefresh')  # time at next scr refresh
                Arrow.setAutoDraw(False)
        
        # *rect_highlight_2* updates
        if rect_highlight_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            rect_highlight_2.frameNStart = frameN  # exact frame index
            rect_highlight_2.tStart = t  # local t and not account for scr refresh
            rect_highlight_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect_highlight_2, 'tStartRefresh')  # time at next scr refresh
            rect_highlight_2.setAutoDraw(True)
        if rect_highlight_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect_highlight_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                rect_highlight_2.tStop = t  # not accounting for scr refresh
                rect_highlight_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect_highlight_2, 'tStopRefresh')  # time at next scr refresh
                rect_highlight_2.setAutoDraw(False)
        
        # *cross_cue_2* updates
        if cross_cue_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            cross_cue_2.frameNStart = frameN  # exact frame index
            cross_cue_2.tStart = t  # local t and not account for scr refresh
            cross_cue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_cue_2, 'tStartRefresh')  # time at next scr refresh
            cross_cue_2.setAutoDraw(True)
        if cross_cue_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_cue_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                cross_cue_2.tStop = t  # not accounting for scr refresh
                cross_cue_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_cue_2, 'tStopRefresh')  # time at next scr refresh
                cross_cue_2.setAutoDraw(False)
        
        # *resp_stimuli_2* updates
        waitOnFlip = False
        if resp_stimuli_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
            if tThisFlipGlobal > resp_stimuli_2.tStartRefresh + 0.2-frameTolerance:
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
    trials_2.addData('text_2.started', text_2.tStartRefresh)
    trials_2.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if stimuli_resp_2.keys in ['', [], None]:  # No response was made
        stimuli_resp_2.keys = None
    trials_2.addData('stimuli_resp_2.keys',stimuli_resp_2.keys)
    if stimuli_resp_2.keys != None:  # we had a response
        trials_2.addData('stimuli_resp_2.rt', stimuli_resp_2.rt)
    trials_2.addData('stimuli_resp_2.started', stimuli_resp_2.tStartRefresh)
    trials_2.addData('stimuli_resp_2.stopped', stimuli_resp_2.tStopRefresh)
    trials_2.addData('rect_left_2.started', rect_left_2.tStartRefresh)
    trials_2.addData('rect_left_2.stopped', rect_left_2.tStopRefresh)
    trials_2.addData('rect_right_2.started', rect_right_2.tStartRefresh)
    trials_2.addData('rect_right_2.stopped', rect_right_2.tStopRefresh)
    trials_2.addData('Arrow.started', Arrow.tStartRefresh)
    trials_2.addData('Arrow.stopped', Arrow.tStopRefresh)
    trials_2.addData('rect_highlight_2.started', rect_highlight_2.tStartRefresh)
    trials_2.addData('rect_highlight_2.stopped', rect_highlight_2.tStopRefresh)
    trials_2.addData('cross_cue_2.started', cross_cue_2.tStartRefresh)
    trials_2.addData('cross_cue_2.stopped', cross_cue_2.tStopRefresh)
    # check responses
    if resp_stimuli_2.keys in ['', [], None]:  # No response was made
        resp_stimuli_2.keys = None
    trials_2.addData('resp_stimuli_2.keys',resp_stimuli_2.keys)
    if resp_stimuli_2.keys != None:  # we had a response
        trials_2.addData('resp_stimuli_2.rt', resp_stimuli_2.rt)
    trials_2.addData('resp_stimuli_2.started', resp_stimuli_2.tStartRefresh)
    trials_2.addData('resp_stimuli_2.stopped', resp_stimuli_2.tStopRefresh)
    # the Routine "Trial_endo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_2'


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
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
