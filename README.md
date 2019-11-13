# DatacardCreator
My general purpose, python configured histogram based data card creator.

In general: I very much recommend looking at some of my personally used configurations set up around the repository to learn how to make 
your own.

## Samples
This contains the template/master class for the samples. These samples will define the basic paramater of each sample to be considered by combine
and contain/be responsible for the uncertainties on the sample. It also handles the nominal histogram for its sample.

Will require a way to tell what values are in the event (EventDefinition/EventDictionary) and a way to define the
uncertainties on the sample (Uncertainties). 

Finally, a master configuration that combines these, and some additional information is needed

### EventDefinition
This contains the template/master event dictionary class. This class's responsibility is to define basic quantities of an event (i.e. things that
can be read straight from a tree), and constructed quantities (i.e. things that can be constructed from the basic quantities).

The event dictionary contains, 3 important dictionaries, and then an important instance variable that
contains the weight. 

#### UserEventDictionaries
This is a convenient place to put your particular kind of event dictionary

#### EventDictionary.py
Contains the master class for event dictionaries. User event dictionaries will need to be instances 
of this class.

#### How do I write an event dictionary for the values that could be used to determine if an event is in a category?
- Open a python file. At the top, import the event dictionary with: `from Samples.EventDefinition.EventDictionary import EventDictionary`
- You will now need to define a function that takes two arguments. The first is the event dictionary 
  object, and the second is the tree with the current entry loaded. The end result of this function 
  must be to fill the `basicQuantitites` dictionary variable of the event dictionary object with a 
  dictionary in VariableName:Value format for a nominal event read from the tree. It is important
  to take note of these variable names, as they will be used later for reconstruction, rolling, 
  uncertainties, and deciding if an event falls in a category or not.

  Note: the point of this function is only to fill quantities that can be read directly from the 
  tree! In the next step we will fill quantities that can be computed from these. This makes it
  easy to propagate uncertainties on basic quantities to all apropriate quantities.
  
- You will now need to define a function that takes two arguments. The first is the event dictionary 
  object and the second is the basic quantities dictionary you just defined filling. This function
  will define filling the event dictionary object's `constructedQuantities` dictionary with variables
  that you can get from the basic quantities (things like m_vis, etc.).
  
  The reason it is done this way is so that if a basic quantity changes for an uncertainty, we have a
  predefined scheme for calculating the values that depend on it to see how they change.
  
- You will now need to create the dictionary instance, like so: `myEventDictionary =  EventDictionary()`
- Set its `FillBasicQuantities` function to the first function you defined with   `myEventDictionary.FillBasicQuantities = FunctionOne`
- Then Set its `FillConstructedQuantities` function to the second function you defined with: 
  `myEventDictionary.FillConstructedQuantities = FunctionTwo`  

### Uncertainties
This contains the template/master class for the uncertainties on samples. Each defined uncertainty must be a derived child of this class.
It will define the various up/down uncertainties related to the overall category of uncertainty, handle their histograms,
and maintain a dictionary of functions used for modifying the nominal event dictionaries to use the uncertainty values.

#### UserUncertainties
Simply a convenient place to place all your user defined uncertainties

#### UncertaintyDef.py
Contains the parent class for uncertainties. All user defined uncertainties will need to *inherrit* 
from this class, instead of simply being an instance of it. Uncertainties must be their own defined
classes.

#### How do I write my own uncertainty?
- Open up a python file, and at the top import the parent uncertainty class with `from Samples.Uncertainties.UncertaintyDef import Uncertainty`
- Uncertainties must be their own class that inherrits from `Uncertainty`, like so: `class myUncertainty(Uncertainty):`
- The init function must set it's name (whatever is convenient and let's you understand it) with 
  `self.name = "myUncertainty"`
- The init function must write the names of the uncertainties *as read by Combine* associated with 
  this source of uncertainty into a list assigned to `self.uncertaintyNames`
- The init function must also create a dictionary `self.eventDictionaryModifications = {...}`.
  This dictionary must be filled with uncertainty names as defined above in the keys, and for values
  it will take class defined functions for how to calculate a modified event dictionary associated 
  with the uncertainty. That is, the dictionary will be in "{uncertaintyName:self.function}" form.
- Next you will have to create a bunch of functions associated with the class that will define how 
  to calculate a modified version of the event dictionary associated with the particular uncertainty.
  These functions will take three arguments, "self",theTree with the entry loaded, and the nominal 
  event dictionary associated with the event. To make a copy of the nominal event dictionary just do
  `modifiedEventDictionary = nominalEventDictionary.Clone()`. Basic quantities can then be modified,
  and the event dictionary `FillConstructedQuantities()` function can then be called on it.
  remember, if your uncertainty has modified any basic quantities, you should call 
  `modifiedEventDictionary.FillContstructedQuantities(...)` and `modifiedEventDictionary.CompileCompleteDictionary()`
  to set the dictionary up properly. If you have only modified the weight, `modifiedEventDictionary.Weight`, this is not
  necessary
  
  remember to return the modified dictionary at the end of the function

### SampleDefintion.py
Contains the master sample configuration class

### UserSamples
This is just a convenient place to put final user created sample configurations

### How do I write a final sample configuration file to use in datacards?
- Open up a python file. At the top, import the sample definition `from Samples.SampleDefinition import Sample`
- Also, import all of the various uncertainties that your sample will need.
- Finally, import the event dictionary that contains the directions to import/make all the values your analysis will need.
- Make an instance of a sample `mySample = Sample()`
- Set it's name with `mySample.name`. This is the name of the nominal histogram as used in combine, `ZL`
- (optional) set the path to look to look for files in with `mySample.path`. This can help keep the files list in the next step 
  easier to manage
- Set the files to create the sample and histograms from with `mySample.files = ["File1.root","File2.root"...]`
- If your sample needs to only be a subset of the trees contained in the files, you can write a cut string with `mySample.definition`.
  I find this useful to filter by gen match or STXS bin for example.
- Next, add instances of all the uncertainties on your sample with `mySample.uncertainties = [myUncertaintyOne(),myUncertaintyTwo()...]`
- set the type of event dictionary the event will use with `mySample.eventDictionaryInstance = myEventDictionary`
- Finally, you will need to set a function to `mySample.CreateEventWeight`that will tell the event dictionary how to nominally weight 
  the event. A few default options are included in the sample code by default designed to work with my weighting code. There is 
  `mySample.CreateEventWeight_Standard` (so you would do `mySample.CreateEventWeight = mySample.CreateEventWeight_Standard`) which
  simply looks for a branch in the tree called `FinalWeighting` and nominally weights the event by this. There is also 
  `CreateEventWeight_Fake` which weights the event by `FinalWeighting` mulitplied by a branch in the tree called `Event_Fake_Factor`

## AnalysisCategories
This contains the template/master analysis category class, as well as any speicifc user defined classes. 
the major duty of the analysis classes are to define what events fall into the category, and to define a template histogram that 
the samples and their uncertainties can copy to fill.

### AnalysisCategoryDef.py
This is the master analysis category class. Analysis Categories are instances of this.

### UserAnalysisCategories
Just a convenient place to place userdefined analysis categories

### How do I write an analysis category for use in my datacards?
- Open a python file. At the top import the analysis category definition with: `import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef`
- Define a function that will take two arguments, the analysiscategory object, and the event dictionary that defines 
the current paramters of the event, or event modified for uncertainty (I call them theAnalysisCategory and 
theEventDictionary) This function must return true if the current considered event dictionary would place it inside 
this category, and false otherwise. Please check some current existing category configurations for examples of
how to do this. Unfortunately I suffered a lapse in judgement and called the final compiled dictionary that contains all event information `eventDictionary` inside of the `EventDictionary` class.
- Next create the instance of the analysis category class with: `myAnalysisCategory = AnalysisCategoryDef.AnalysisCategory()`
- Set the category name (will show up in the root file as the directory name), with `myAnalysisCategory.name = theName`
- Set the function that has the criteria for being a part of this category with `myAnalysisCategory.IsInCategory = myFunction`
- Set the name of the rolling variable to the exact name as it shows up in the event dictionary, like so `myAnalysisCategory.rollingVariable = 'MyVariableName'`
- Set the bin boundaries for the rolling variable like so: `myAnalysisCategory.rollingBins = [HistogramLowEdge,bin_edge_1,bin_edge_2,bin_edge_3,...HistogramHighEdge]`
- set the reconstructionvariables and bins the same way with `reconstructionVariable` and `reconstructionBins` 

## Utilities
Contains various utility things for the data card creator, the loader and unroller.

## CreateDatacard.py
This is the main driving script for creating datacards.

### Options
- `--AnalysisConfigFiles`: (required) takes any number of arguments, should be the analysis config files. Supports wildcarding
- `--SampleConfigFiles`: (required) takes any number of arguments, should the sample config files. Supports wildcarding.
- `--OutputFileName`: (Optional but recommended) provides the name for the final datacard file created. Otherwise it uses a default name
  of "NewDatacard.root"

## Disclaimer
This code is thorough, but not particularly efficient. I am working on increasing the efficiency, but 
until such time, I find it best to run these commands in a tmux session. I also, unfortunately do not
have much better advice for you than to use as many cores and resources as you resonably can in tmux 
to get the run time down, and hadd the files together at the end. You may also see in some random 
assorted scripts left around the repository, and from some configurations I've included, my attempts
at parallelization inside of tmux.

If you have any ideas or improvements, I would love for the use of this tool to extend beyond me, so let me know or open a PR.
