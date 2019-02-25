/************************************** 
 * Part1_Subjective_Segmentation Test *
 **************************************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'part1_subjective_segmentation';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin, trials_4LoopScheduler);
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);
const loop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop3LoopBegin, loop3LoopScheduler);
flowScheduler.add(loop3LoopScheduler);
flowScheduler.add(loop3LoopEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(final_test_introRoutineBegin);
flowScheduler.add(final_test_introRoutineEachFrame);
flowScheduler.add(final_test_introRoutineEnd);
const trials_5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_5LoopBegin, trials_5LoopScheduler);
flowScheduler.add(trials_5LoopScheduler);
flowScheduler.add(trials_5LoopEnd);
const trials_8LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_8LoopBegin, trials_8LoopScheduler);
flowScheduler.add(trials_8LoopScheduler);
flowScheduler.add(trials_8LoopEnd);
flowScheduler.add(end_of_introRoutineBegin);
flowScheduler.add(end_of_introRoutineEachFrame);
flowScheduler.add(end_of_introRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({configURL: 'config.json', expInfo: expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.0.4';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('completedURL', 'incompleteURL');

  return Scheduler.Event.NEXT;
}

var introClock;
var welcome_2;
var image_10;
var shows_jobsClock;
var image;
var text_2;
var intro_2Clock;
var welcome;
var text_12;
var just_perspective_2Clock;
var text_18;
var image_9;
var q1Clock;
var text_8;
var text_9;
var image_5;
var q2Clock;
var text_10;
var text_11;
var image_6;
var q3Clock;
var text_13;
var text_14;
var image_7;
var q4Clock;
var text_15;
var text_16;
var image_8;
var intro_practicetestClock;
var text_5;
var testClock;
var question1_2;
var question2_2;
var question3_2;
var question4_2;
var question5_2;
var question6_2;
var image_3;
var final_test_introClock;
var text_3;
var final_test_iClock;
var image_2;
var text_4;
var test3Clock;
var question1_3;
var question2_3;
var question3_3;
var question4_3;
var question5_3;
var question6_3;
var image_4;
var segmentation_instructionsClock;
var text_6;
var end_of_introClock;
var text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  welcome_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.5], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  
  image_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_10', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [1.5, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "shows_jobs"
  shows_jobsClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.85, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.7)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  
  // Initialize components for Routine "intro_2"
  intro_2Clock = new util.Clock();
  welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.6)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  
  // Initialize components for Routine "just_perspective_2"
  just_perspective_2Clock = new util.Clock();
  text_18 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_18',
    text: 'default text',
    font: 'Arial',
    pos: [(- 0.5), 0.25], height: 0.1,  wrapWidth: 0.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  image_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0.25], size : [0.85, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "q1"
  q1Clock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.4)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'default text',
    font: 'Arial',
    pos: [(- 0.5), 0.25], height: 0.1,  wrapWidth: 0.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0.25], size : [0.85, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "q2"
  q2Clock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.4)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: 'default text',
    font: 'Arial',
    pos: [(- 0.5), 0.25], height: 0.1,  wrapWidth: 0.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0.25], size : [0.85, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "q3"
  q3Clock = new util.Clock();
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.4)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'default text',
    font: 'Arial',
    pos: [(- 0.5), 0.25], height: 0.1,  wrapWidth: 0.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  image_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_7', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0.25], size : [0.85, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "q4"
  q4Clock = new util.Clock();
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.4)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: 'default text',
    font: 'Arial',
    pos: [(- 0.5), 0.25], height: 0.1,  wrapWidth: 0.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  image_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_8', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0.25], size : [0.85, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "intro_practicetest"
  intro_practicetestClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'indicate the order in which the questions appeared:',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "test"
  testClock = new util.Clock();
  
  question1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question1_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.6], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  question2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question2_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.35], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  question3_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question3_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.12], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  question4_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question4_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.12)], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  question5_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question5_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.35)], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  question6_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question6_2',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.6)], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.85)], size : [0.25, 0.125],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "final_test_intro"
  final_test_introClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Final Tests',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "final_test_i"
  final_test_iClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.85, 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.7)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "test3"
  test3Clock = new util.Clock();
  
  question1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question1_3',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.6], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  question2_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question2_3',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.35], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  question3_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question3_3',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0.12], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  question4_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question4_3',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.12)], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  question5_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question5_3',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.35)], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  question6_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question6_3',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.6)], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.85)], size : [0.25, 0.125],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "segmentation_instructions"
  segmentation_instructionsClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  
  // Initialize components for Routine "end_of_intro"
  end_of_introClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'end of introduction',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var trials_2;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'instructions.xlsx',
    seed: undefined, name: 'trials_2'});
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial_2 of trials_2) {
    thisScheduler.add(importConditions(trials_2));
    thisScheduler.add(introRoutineBegin);
    thisScheduler.add(introRoutineEachFrame);
    thisScheduler.add(introRoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial_2));
  }

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

var trials_4;
function trials_4LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_4 = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'jobsPics.xlsx',
    seed: undefined, name: 'trials_4'});
  psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial_4 of trials_4) {
    thisScheduler.add(importConditions(trials_4));
    thisScheduler.add(shows_jobsRoutineBegin);
    thisScheduler.add(shows_jobsRoutineEachFrame);
    thisScheduler.add(shows_jobsRoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial_4));
  }

  return Scheduler.Event.NEXT;
}


function trials_4LoopEnd() {
  psychoJS.experiment.removeLoop(trials_4);

  return Scheduler.Event.NEXT;
}

var loop3;
function loop3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  loop3 = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'instructions2.xlsx',
    seed: undefined, name: 'loop3'});
  psychoJS.experiment.addLoop(loop3); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisLoop3 of loop3) {
    thisScheduler.add(importConditions(loop3));
    thisScheduler.add(intro_2RoutineBegin);
    thisScheduler.add(intro_2RoutineEachFrame);
    thisScheduler.add(intro_2RoutineEnd);
    thisScheduler.add(endLoopIteration(thisLoop3));
  }

  return Scheduler.Event.NEXT;
}


function loop3LoopEnd() {
  psychoJS.experiment.removeLoop(loop3);

  return Scheduler.Event.NEXT;
}

var trials_3;
function trials_3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'whichRole.xlsx',
    seed: undefined, name: 'trials_3'});
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial_3 of trials_3) {
    thisScheduler.add(importConditions(trials_3));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(endLoopIteration(thisTrial_3));
  }

  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS,
    nReps: 5, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(just_perspective_2RoutineBegin);
    thisScheduler.add(just_perspective_2RoutineEachFrame);
    thisScheduler.add(just_perspective_2RoutineEnd);
    thisScheduler.add(q1RoutineBegin);
    thisScheduler.add(q1RoutineEachFrame);
    thisScheduler.add(q1RoutineEnd);
    thisScheduler.add(q2RoutineBegin);
    thisScheduler.add(q2RoutineEachFrame);
    thisScheduler.add(q2RoutineEnd);
    thisScheduler.add(q3RoutineBegin);
    thisScheduler.add(q3RoutineEachFrame);
    thisScheduler.add(q3RoutineEnd);
    thisScheduler.add(q4RoutineBegin);
    thisScheduler.add(q4RoutineEachFrame);
    thisScheduler.add(q4RoutineEnd);
    thisScheduler.add(intro_practicetestRoutineBegin);
    thisScheduler.add(intro_practicetestRoutineEachFrame);
    thisScheduler.add(intro_practicetestRoutineEnd);
    thisScheduler.add(testRoutineBegin);
    thisScheduler.add(testRoutineEachFrame);
    thisScheduler.add(testRoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}

var trials_5;
function trials_5LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_5 = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'whichRole.xlsx',
    seed: undefined, name: 'trials_5'});
  psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial_5 of trials_5) {
    thisScheduler.add(importConditions(trials_5));
    const trials_7LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trials_7LoopBegin, trials_7LoopScheduler);
    thisScheduler.add(trials_7LoopScheduler);
    thisScheduler.add(trials_7LoopEnd);
    thisScheduler.add(endLoopIteration(thisTrial_5));
  }

  return Scheduler.Event.NEXT;
}

var trials_7;
function trials_7LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_7 = new TrialHandler({
    psychoJS,
    nReps: 5, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_7'});
  psychoJS.experiment.addLoop(trials_7); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial_7 of trials_7) {
    thisScheduler.add(importConditions(trials_7));
    thisScheduler.add(final_test_iRoutineBegin);
    thisScheduler.add(final_test_iRoutineEachFrame);
    thisScheduler.add(final_test_iRoutineEnd);
    thisScheduler.add(test3RoutineBegin);
    thisScheduler.add(test3RoutineEachFrame);
    thisScheduler.add(test3RoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial_7));
  }

  return Scheduler.Event.NEXT;
}


function trials_7LoopEnd() {
  psychoJS.experiment.removeLoop(trials_7);

  return Scheduler.Event.NEXT;
}


function trials_5LoopEnd() {
  psychoJS.experiment.removeLoop(trials_5);

  return Scheduler.Event.NEXT;
}

var trials_8;
function trials_8LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_8 = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'instructions_segment.xlsx',
    seed: undefined, name: 'trials_8'});
  psychoJS.experiment.addLoop(trials_8); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial_8 of trials_8) {
    thisScheduler.add(importConditions(trials_8));
    thisScheduler.add(segmentation_instructionsRoutineBegin);
    thisScheduler.add(segmentation_instructionsRoutineEachFrame);
    thisScheduler.add(segmentation_instructionsRoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial_8));
  }

  return Scheduler.Event.NEXT;
}


function trials_8LoopEnd() {
  psychoJS.experiment.removeLoop(trials_8);

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var key_resp_8;
var introComponents;
function introRoutineBegin() {
  //------Prepare to start Routine 'intro'-------
  t = 0;
  introClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  welcome_2.setText(instruct_text);
  key_resp_8 = new core.BuilderKeyResponse(psychoJS);
  
  image_10.setImage(this_pic);
  // keep track of which components have finished
  introComponents = [];
  introComponents.push(welcome_2);
  introComponents.push(key_resp_8);
  introComponents.push(image_10);
  
  for (const thisComponent of introComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function introRoutineEachFrame() {
  //------Loop for each frame of Routine 'intro'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = introClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *welcome_2* updates
  if (t >= 0.0 && welcome_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    welcome_2.tStart = t;  // (not accounting for frame time here)
    welcome_2.frameNStart = frameN;  // exact frame index
    welcome_2.setAutoDraw(true);
  }

  
  // *key_resp_8* updates
  if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_8.tStart = t;  // (not accounting for frame time here)
    key_resp_8.frameNStart = frameN;  // exact frame index
    key_resp_8.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_8.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_8.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_8.rt = key_resp_8.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *image_10* updates
  if (t >= 0.0 && image_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_10.tStart = t;  // (not accounting for frame time here)
    image_10.frameNStart = frameN;  // exact frame index
    image_10.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of introComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEnd() {
  //------Ending Routine 'intro'-------
  for (const thisComponent of introComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_8.keys === undefined || key_resp_8.keys.length === 0) {    // No response was made
      key_resp_8.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
  if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "intro" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_2;
var shows_jobsComponents;
function shows_jobsRoutineBegin() {
  //------Prepare to start Routine 'shows_jobs'-------
  t = 0;
  shows_jobsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  image.setImage(rolePic);
  key_resp_2 = new core.BuilderKeyResponse(psychoJS);
  text_2.setText(job);
  
  // keep track of which components have finished
  shows_jobsComponents = [];
  shows_jobsComponents.push(image);
  shows_jobsComponents.push(key_resp_2);
  shows_jobsComponents.push(text_2);
  
  for (const thisComponent of shows_jobsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function shows_jobsRoutineEachFrame() {
  //------Loop for each frame of Routine 'shows_jobs'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = shows_jobsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image* updates
  if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  
  // *key_resp_2* updates
  if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_2.tStart = t;  // (not accounting for frame time here)
    key_resp_2.frameNStart = frameN;  // exact frame index
    key_resp_2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_2.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_2.rt = key_resp_2.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of shows_jobsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function shows_jobsRoutineEnd() {
  //------Ending Routine 'shows_jobs'-------
  for (const thisComponent of shows_jobsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_2.keys === undefined || key_resp_2.keys.length === 0) {    // No response was made
      key_resp_2.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
  if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "shows_jobs" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_6;
var intro_2Components;
function intro_2RoutineBegin() {
  //------Prepare to start Routine 'intro_2'-------
  t = 0;
  intro_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  welcome.setText(instruct_text);
  key_resp_6 = new core.BuilderKeyResponse(psychoJS);
  text_12.setText(instruct_text2);
  
  // keep track of which components have finished
  intro_2Components = [];
  intro_2Components.push(welcome);
  intro_2Components.push(key_resp_6);
  intro_2Components.push(text_12);
  
  for (const thisComponent of intro_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function intro_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'intro_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = intro_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *welcome* updates
  if (t >= 0.0 && welcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    welcome.tStart = t;  // (not accounting for frame time here)
    welcome.frameNStart = frameN;  // exact frame index
    welcome.setAutoDraw(true);
  }

  
  // *key_resp_6* updates
  if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_6.tStart = t;  // (not accounting for frame time here)
    key_resp_6.frameNStart = frameN;  // exact frame index
    key_resp_6.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_6.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_6.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_6.rt = key_resp_6.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // *text_12* updates
  if (t >= 0.0 && text_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_12.tStart = t;  // (not accounting for frame time here)
    text_12.frameNStart = frameN;  // exact frame index
    text_12.setAutoDraw(true);
  }

  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of intro_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function intro_2RoutineEnd() {
  //------Ending Routine 'intro_2'-------
  for (const thisComponent of intro_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_6.keys === undefined || key_resp_6.keys.length === 0) {    // No response was made
      key_resp_6.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
  if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "intro_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_14;
var just_perspective_2Components;
function just_perspective_2RoutineBegin() {
  //------Prepare to start Routine 'just_perspective_2'-------
  t = 0;
  just_perspective_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_18.setText(roleName);
  image_9.setImage(rolePic);
  key_resp_14 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  just_perspective_2Components = [];
  just_perspective_2Components.push(text_18);
  just_perspective_2Components.push(image_9);
  just_perspective_2Components.push(key_resp_14);
  
  for (const thisComponent of just_perspective_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function just_perspective_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'just_perspective_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = just_perspective_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_18* updates
  if (t >= 0.0 && text_18.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_18.tStart = t;  // (not accounting for frame time here)
    text_18.frameNStart = frameN;  // exact frame index
    text_18.setAutoDraw(true);
  }

  
  // *image_9* updates
  if (t >= 0.0 && image_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_9.tStart = t;  // (not accounting for frame time here)
    image_9.frameNStart = frameN;  // exact frame index
    image_9.setAutoDraw(true);
  }

  
  // *key_resp_14* updates
  if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_14.tStart = t;  // (not accounting for frame time here)
    key_resp_14.frameNStart = frameN;  // exact frame index
    key_resp_14.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_14.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_14.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_14.rt = key_resp_14.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of just_perspective_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function just_perspective_2RoutineEnd() {
  //------Ending Routine 'just_perspective_2'-------
  for (const thisComponent of just_perspective_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_14.keys === undefined || key_resp_14.keys.length === 0) {    // No response was made
      key_resp_14.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
  if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
      routineTimer.reset();
      }
  
  // the Routine "just_perspective_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_10;
var q1Components;
function q1RoutineBegin() {
  //------Prepare to start Routine 'q1'-------
  t = 0;
  q1Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_8.setText(('A: ' + Q1));
  text_9.setText(roleName);
  image_5.setImage(rolePic);
  key_resp_10 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  q1Components = [];
  q1Components.push(text_8);
  q1Components.push(text_9);
  q1Components.push(image_5);
  q1Components.push(key_resp_10);
  
  for (const thisComponent of q1Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function q1RoutineEachFrame() {
  //------Loop for each frame of Routine 'q1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = q1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_8* updates
  if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_8.tStart = t;  // (not accounting for frame time here)
    text_8.frameNStart = frameN;  // exact frame index
    text_8.setAutoDraw(true);
  }

  
  // *text_9* updates
  if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_9.tStart = t;  // (not accounting for frame time here)
    text_9.frameNStart = frameN;  // exact frame index
    text_9.setAutoDraw(true);
  }

  
  // *image_5* updates
  if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_5.tStart = t;  // (not accounting for frame time here)
    image_5.frameNStart = frameN;  // exact frame index
    image_5.setAutoDraw(true);
  }

  
  // *key_resp_10* updates
  if (t >= 0.0 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_10.tStart = t;  // (not accounting for frame time here)
    key_resp_10.frameNStart = frameN;  // exact frame index
    key_resp_10.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_10.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_10.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_10.rt = key_resp_10.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of q1Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function q1RoutineEnd() {
  //------Ending Routine 'q1'-------
  for (const thisComponent of q1Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_10.keys === undefined || key_resp_10.keys.length === 0) {    // No response was made
      key_resp_10.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
  if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
      routineTimer.reset();
      }
  
  // the Routine "q1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_11;
var q2Components;
function q2RoutineBegin() {
  //------Prepare to start Routine 'q2'-------
  t = 0;
  q2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_10.setText(('B: ' + Q2));
  text_11.setText(roleName);
  image_6.setImage(rolePic);
  key_resp_11 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  q2Components = [];
  q2Components.push(text_10);
  q2Components.push(text_11);
  q2Components.push(image_6);
  q2Components.push(key_resp_11);
  
  for (const thisComponent of q2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function q2RoutineEachFrame() {
  //------Loop for each frame of Routine 'q2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = q2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_10* updates
  if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_10.tStart = t;  // (not accounting for frame time here)
    text_10.frameNStart = frameN;  // exact frame index
    text_10.setAutoDraw(true);
  }

  
  // *text_11* updates
  if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_11.tStart = t;  // (not accounting for frame time here)
    text_11.frameNStart = frameN;  // exact frame index
    text_11.setAutoDraw(true);
  }

  
  // *image_6* updates
  if (t >= 0.0 && image_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_6.tStart = t;  // (not accounting for frame time here)
    image_6.frameNStart = frameN;  // exact frame index
    image_6.setAutoDraw(true);
  }

  
  // *key_resp_11* updates
  if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_11.tStart = t;  // (not accounting for frame time here)
    key_resp_11.frameNStart = frameN;  // exact frame index
    key_resp_11.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_11.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_11.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_11.rt = key_resp_11.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of q2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function q2RoutineEnd() {
  //------Ending Routine 'q2'-------
  for (const thisComponent of q2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_11.keys === undefined || key_resp_11.keys.length === 0) {    // No response was made
      key_resp_11.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
  if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
      routineTimer.reset();
      }
  
  // the Routine "q2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_12;
var q3Components;
function q3RoutineBegin() {
  //------Prepare to start Routine 'q3'-------
  t = 0;
  q3Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_13.setText(('C: ' + Q3));
  text_14.setText(roleName);
  image_7.setImage(rolePic);
  key_resp_12 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  q3Components = [];
  q3Components.push(text_13);
  q3Components.push(text_14);
  q3Components.push(image_7);
  q3Components.push(key_resp_12);
  
  for (const thisComponent of q3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function q3RoutineEachFrame() {
  //------Loop for each frame of Routine 'q3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = q3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_13* updates
  if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_13.tStart = t;  // (not accounting for frame time here)
    text_13.frameNStart = frameN;  // exact frame index
    text_13.setAutoDraw(true);
  }

  
  // *text_14* updates
  if (t >= 0.0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_14.tStart = t;  // (not accounting for frame time here)
    text_14.frameNStart = frameN;  // exact frame index
    text_14.setAutoDraw(true);
  }

  
  // *image_7* updates
  if (t >= 0.0 && image_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_7.tStart = t;  // (not accounting for frame time here)
    image_7.frameNStart = frameN;  // exact frame index
    image_7.setAutoDraw(true);
  }

  
  // *key_resp_12* updates
  if (t >= 0.0 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_12.tStart = t;  // (not accounting for frame time here)
    key_resp_12.frameNStart = frameN;  // exact frame index
    key_resp_12.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_12.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_12.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_12.rt = key_resp_12.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of q3Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function q3RoutineEnd() {
  //------Ending Routine 'q3'-------
  for (const thisComponent of q3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_12.keys === undefined || key_resp_12.keys.length === 0) {    // No response was made
      key_resp_12.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
  if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
      routineTimer.reset();
      }
  
  // the Routine "q3" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_13;
var q4Components;
function q4RoutineBegin() {
  //------Prepare to start Routine 'q4'-------
  t = 0;
  q4Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_15.setText(('D: ' + Q4));
  text_16.setText(roleName);
  image_8.setImage(rolePic);
  key_resp_13 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  q4Components = [];
  q4Components.push(text_15);
  q4Components.push(text_16);
  q4Components.push(image_8);
  q4Components.push(key_resp_13);
  
  for (const thisComponent of q4Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function q4RoutineEachFrame() {
  //------Loop for each frame of Routine 'q4'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = q4Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_15* updates
  if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_15.tStart = t;  // (not accounting for frame time here)
    text_15.frameNStart = frameN;  // exact frame index
    text_15.setAutoDraw(true);
  }

  
  // *text_16* updates
  if (t >= 0.0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_16.tStart = t;  // (not accounting for frame time here)
    text_16.frameNStart = frameN;  // exact frame index
    text_16.setAutoDraw(true);
  }

  
  // *image_8* updates
  if (t >= 0.0 && image_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_8.tStart = t;  // (not accounting for frame time here)
    image_8.frameNStart = frameN;  // exact frame index
    image_8.setAutoDraw(true);
  }

  
  // *key_resp_13* updates
  if (t >= 0.0 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_13.tStart = t;  // (not accounting for frame time here)
    key_resp_13.frameNStart = frameN;  // exact frame index
    key_resp_13.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_13.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_13.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_13.rt = key_resp_13.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of q4Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function q4RoutineEnd() {
  //------Ending Routine 'q4'-------
  for (const thisComponent of q4Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_13.keys === undefined || key_resp_13.keys.length === 0) {    // No response was made
      key_resp_13.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
  if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
      routineTimer.reset();
      }
  
  // the Routine "q4" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_4;
var intro_practicetestComponents;
function intro_practicetestRoutineBegin() {
  //------Prepare to start Routine 'intro_practicetest'-------
  t = 0;
  intro_practicetestClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_4 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  intro_practicetestComponents = [];
  intro_practicetestComponents.push(text_5);
  intro_practicetestComponents.push(key_resp_4);
  
  for (const thisComponent of intro_practicetestComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function intro_practicetestRoutineEachFrame() {
  //------Loop for each frame of Routine 'intro_practicetest'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = intro_practicetestClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_5* updates
  if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_5.tStart = t;  // (not accounting for frame time here)
    text_5.frameNStart = frameN;  // exact frame index
    text_5.setAutoDraw(true);
  }

  
  // *key_resp_4* updates
  if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_4.tStart = t;  // (not accounting for frame time here)
    key_resp_4.frameNStart = frameN;  // exact frame index
    key_resp_4.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_4.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_4.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_4.rt = key_resp_4.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of intro_practicetestComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function intro_practicetestRoutineEnd() {
  //------Ending Routine 'intro_practicetest'-------
  for (const thisComponent of intro_practicetestComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_4.keys === undefined || key_resp_4.keys.length === 0) {    // No response was made
      key_resp_4.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
  if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
      routineTimer.reset();
      }
  
  // the Routine "intro_practicetest" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var testComponents;
function testRoutineBegin() {
  //------Prepare to start Routine 'test'-------
  t = 0;
  testClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  
  question1_2.setText(text1);
  question2_2.setText(text2);
  question3_2.setText(text3);
  question4_2.setText(text4);
  question5_2.setText(text5);
  question6_2.setText(text6);
  
  // keep track of which components have finished
  testComponents = [];
  testComponents.push(question1_2);
  testComponents.push(question2_2);
  testComponents.push(question3_2);
  testComponents.push(question4_2);
  testComponents.push(question5_2);
  testComponents.push(question6_2);
  testComponents.push(image_3);
  
  for (const thisComponent of testComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function testRoutineEachFrame() {
  //------Loop for each frame of Routine 'test'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = testClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  
  // *question1_2* updates
  if (t >= 0.0 && question1_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question1_2.tStart = t;  // (not accounting for frame time here)
    question1_2.frameNStart = frameN;  // exact frame index
    question1_2.setAutoDraw(true);
  }

  
  // *question2_2* updates
  if (t >= 0.0 && question2_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question2_2.tStart = t;  // (not accounting for frame time here)
    question2_2.frameNStart = frameN;  // exact frame index
    question2_2.setAutoDraw(true);
  }

  
  // *question3_2* updates
  if (t >= 0.0 && question3_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question3_2.tStart = t;  // (not accounting for frame time here)
    question3_2.frameNStart = frameN;  // exact frame index
    question3_2.setAutoDraw(true);
  }

  
  // *question4_2* updates
  if (t >= 0.0 && question4_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question4_2.tStart = t;  // (not accounting for frame time here)
    question4_2.frameNStart = frameN;  // exact frame index
    question4_2.setAutoDraw(true);
  }

  
  // *question5_2* updates
  if (t >= 0.0 && question5_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question5_2.tStart = t;  // (not accounting for frame time here)
    question5_2.frameNStart = frameN;  // exact frame index
    question5_2.setAutoDraw(true);
  }

  
  // *question6_2* updates
  if (t >= 0.0 && question6_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question6_2.tStart = t;  // (not accounting for frame time here)
    question6_2.frameNStart = frameN;  // exact frame index
    question6_2.setAutoDraw(true);
  }

  
  
  // *image_3* updates
  if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_3.tStart = t;  // (not accounting for frame time here)
    image_3.frameNStart = frameN;  // exact frame index
    image_3.setAutoDraw(true);
  }

  if (image_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
    image_3.setImage(this_image);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of testComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function testRoutineEnd() {
  //------Ending Routine 'test'-------
  for (const thisComponent of testComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  
  // the Routine "test" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var final_test_introComponents;
function final_test_introRoutineBegin() {
  //------Prepare to start Routine 'final_test_intro'-------
  t = 0;
  final_test_introClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  final_test_introComponents = [];
  final_test_introComponents.push(text_3);
  
  for (const thisComponent of final_test_introComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function final_test_introRoutineEachFrame() {
  //------Loop for each frame of Routine 'final_test_intro'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = final_test_introClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_3* updates
  if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_3.tStart = t;  // (not accounting for frame time here)
    text_3.frameNStart = frameN;  // exact frame index
    text_3.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_3.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of final_test_introComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function final_test_introRoutineEnd() {
  //------Ending Routine 'final_test_intro'-------
  for (const thisComponent of final_test_introComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var key_resp_3;
var final_test_iComponents;
function final_test_iRoutineBegin() {
  //------Prepare to start Routine 'final_test_i'-------
  t = 0;
  final_test_iClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  image_2.setImage(rolePic);
  key_resp_3 = new core.BuilderKeyResponse(psychoJS);
  text_4.setText(roleName);
  // keep track of which components have finished
  final_test_iComponents = [];
  final_test_iComponents.push(image_2);
  final_test_iComponents.push(key_resp_3);
  final_test_iComponents.push(text_4);
  
  for (const thisComponent of final_test_iComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function final_test_iRoutineEachFrame() {
  //------Loop for each frame of Routine 'final_test_i'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = final_test_iClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image_2* updates
  if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_2.tStart = t;  // (not accounting for frame time here)
    image_2.frameNStart = frameN;  // exact frame index
    image_2.setAutoDraw(true);
  }

  
  // *key_resp_3* updates
  if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_3.tStart = t;  // (not accounting for frame time here)
    key_resp_3.frameNStart = frameN;  // exact frame index
    key_resp_3.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_3.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_3.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_3.rt = key_resp_3.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // *text_4* updates
  if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_4.tStart = t;  // (not accounting for frame time here)
    text_4.frameNStart = frameN;  // exact frame index
    text_4.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of final_test_iComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function final_test_iRoutineEnd() {
  //------Ending Routine 'final_test_i'-------
  for (const thisComponent of final_test_iComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_3.keys === undefined || key_resp_3.keys.length === 0) {    // No response was made
      key_resp_3.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
  if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
      routineTimer.reset();
      }
  
  // the Routine "final_test_i" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var test3Components;
function test3RoutineBegin() {
  //------Prepare to start Routine 'test3'-------
  t = 0;
  test3Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  
  question1_3.setText(text1);
  question2_3.setText(text2);
  question3_3.setText(text3);
  question4_3.setText(text4);
  question5_3.setText(text5);
  question6_3.setText(text6);
  
  // keep track of which components have finished
  test3Components = [];
  test3Components.push(question1_3);
  test3Components.push(question2_3);
  test3Components.push(question3_3);
  test3Components.push(question4_3);
  test3Components.push(question5_3);
  test3Components.push(question6_3);
  test3Components.push(image_4);
  
  for (const thisComponent of test3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function test3RoutineEachFrame() {
  //------Loop for each frame of Routine 'test3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = test3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  
  // *question1_3* updates
  if (t >= 0.0 && question1_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question1_3.tStart = t;  // (not accounting for frame time here)
    question1_3.frameNStart = frameN;  // exact frame index
    question1_3.setAutoDraw(true);
  }

  
  // *question2_3* updates
  if (t >= 0.0 && question2_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question2_3.tStart = t;  // (not accounting for frame time here)
    question2_3.frameNStart = frameN;  // exact frame index
    question2_3.setAutoDraw(true);
  }

  
  // *question3_3* updates
  if (t >= 0.0 && question3_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question3_3.tStart = t;  // (not accounting for frame time here)
    question3_3.frameNStart = frameN;  // exact frame index
    question3_3.setAutoDraw(true);
  }

  
  // *question4_3* updates
  if (t >= 0.0 && question4_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question4_3.tStart = t;  // (not accounting for frame time here)
    question4_3.frameNStart = frameN;  // exact frame index
    question4_3.setAutoDraw(true);
  }

  
  // *question5_3* updates
  if (t >= 0.0 && question5_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question5_3.tStart = t;  // (not accounting for frame time here)
    question5_3.frameNStart = frameN;  // exact frame index
    question5_3.setAutoDraw(true);
  }

  
  // *question6_3* updates
  if (t >= 0.0 && question6_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    question6_3.tStart = t;  // (not accounting for frame time here)
    question6_3.frameNStart = frameN;  // exact frame index
    question6_3.setAutoDraw(true);
  }

  
  
  // *image_4* updates
  if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_4.tStart = t;  // (not accounting for frame time here)
    image_4.frameNStart = frameN;  // exact frame index
    image_4.setAutoDraw(true);
  }

  if (image_4.status === PsychoJS.Status.STARTED){ // only update if being drawn
    image_4.setImage(this_image);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of test3Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function test3RoutineEnd() {
  //------Ending Routine 'test3'-------
  for (const thisComponent of test3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  
  // the Routine "test3" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_5;
var segmentation_instructionsComponents;
function segmentation_instructionsRoutineBegin() {
  //------Prepare to start Routine 'segmentation_instructions'-------
  t = 0;
  segmentation_instructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_5 = new core.BuilderKeyResponse(psychoJS);
  text_6.setText(instructText);
  
  // keep track of which components have finished
  segmentation_instructionsComponents = [];
  segmentation_instructionsComponents.push(key_resp_5);
  segmentation_instructionsComponents.push(text_6);
  
  for (const thisComponent of segmentation_instructionsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function segmentation_instructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'segmentation_instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = segmentation_instructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *key_resp_5* updates
  if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_5.tStart = t;  // (not accounting for frame time here)
    key_resp_5.frameNStart = frameN;  // exact frame index
    key_resp_5.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_5.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_5.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_5.rt = key_resp_5.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // *text_6* updates
  if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_6.tStart = t;  // (not accounting for frame time here)
    text_6.frameNStart = frameN;  // exact frame index
    text_6.setAutoDraw(true);
  }

  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of segmentation_instructionsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function segmentation_instructionsRoutineEnd() {
  //------Ending Routine 'segmentation_instructions'-------
  for (const thisComponent of segmentation_instructionsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_5.keys === undefined || key_resp_5.keys.length === 0) {    // No response was made
      key_resp_5.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
  if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "segmentation_instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_7;
var end_of_introComponents;
function end_of_introRoutineBegin() {
  //------Prepare to start Routine 'end_of_intro'-------
  t = 0;
  end_of_introClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_7 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  end_of_introComponents = [];
  end_of_introComponents.push(text);
  end_of_introComponents.push(key_resp_7);
  
  for (const thisComponent of end_of_introComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function end_of_introRoutineEachFrame() {
  //------Loop for each frame of Routine 'end_of_intro'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = end_of_introClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text.setAutoDraw(false);
  }
  
  // *key_resp_7* updates
  if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_7.tStart = t;  // (not accounting for frame time here)
    key_resp_7.frameNStart = frameN;  // exact frame index
    key_resp_7.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_7.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['y', 'n', 'left', 'right', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_7.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_7.rt = key_resp_7.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of end_of_introComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function end_of_introRoutineEnd() {
  //------Ending Routine 'end_of_intro'-------
  for (const thisComponent of end_of_introComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_7.keys === undefined || key_resp_7.keys.length === 0) {    // No response was made
      key_resp_7.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
  if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
      routineTimer.reset();
      }
  
  // the Routine "end_of_intro" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  psychoJS.window.close();
  psychoJS.quit({message, isCompleted});

  return Scheduler.Event.QUIT;
}
