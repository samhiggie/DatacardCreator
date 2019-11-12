# DatacardCreator
My general purpose, python configured histogram based data card creator.

## Samples
This contains the template/master class for the samples. These samples will define the basic paramater of each sample to be considered by combine
and contain/be responsible for the uncertainties on the sample. It also handles the nominal histogram for its sample.

Will require a way to tell what values are in the event (EventDefinition/EventDictionary) and a way to define the
uncertainties on the sample (Uncertainties).

### EventDefinition
This contains the template/master event dictionary class. This class's responsibility is to define basic quantities of an event (i.e. things that
can be read straight from a tree), and constructed quantities (i.e. things that can be constructed from the basic quantities).

##### UserEventDictionaries

#### EventDictionary.py

#### How do I write an event dictionary for the values that could be used to determine if an event is in a category?

### Uncertainties
This contains the template/master class for the uncertainties on samples. Each defined uncertainty must be a derived child of this class.
It will define the various up/down uncertainties related to the overall category of uncertainty, handle their histograms,
and maintain a dictionary of functions used for modifying the nominal event dictionaries to use the uncertainty values.

#### UserUncertainties

#### UncertaintyDef.py

#### How do I write my own uncertainty?

### SampleDefintion.py
Contains the master sample configuration class

### UserSamples
This is just a convenient place to put final user created 

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
how to do this.
- Next create the instance of the analysis category class with: `myAnalysisCategory = AnalysisCategoryDef.AnalysisCategory()`
- Set the category name (will show up in the root file as the directory name), with `myAnalysisCategory.name = theName`
- Set the function that has the criteria for being a part of this category with `myAnalysisCategory.IsInCategory = myFunction`
- Set the name of the rolling variable to the exact name as it shows up in the event dictionary, like so `myAnalysisCategory.rollingVariable = 'MyVariableName'`
- Set the bin boundaries for the rolling variable like so: `myAnalysisCategory.rollingBins = [HistogramLowEdge,bin_edge_1,bin_edge_2,bin_edge_3,...HistogramHighEdge]`
- set the reconstructionvariables and bins the same way with `reconstructionVariable` and `reconstructionBins` 


## Utilities
Contains various utility things for the data card creator, the loader and unroller.
