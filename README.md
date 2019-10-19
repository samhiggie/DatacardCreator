# DatacardCreator
My general purpose, python configured histogram based data card creator.

## AnalysisCategories
This contains the template/master analysis category class, as well as any speicifc user defined classes. 
the major duty of the analysis classes are to define what events fall into the category, and to define a template histogram that 
the samples and their uncertainties can copy to fill.
## EventDefinition
This contais the template/master event dictionary class. This classes responsibility is to define basic quantities of an event (i.e. things that
can be read straight from a tree), and constructed quantities (i.e. things that can be constructed from the basic quantities). The analysis category will use these 
dictionaries to decide whether this event falls in the analysis category, and the uncertainties copy and modify these to for the analysis categories to 
decide whether the uncertainty on the event falls on the category.
## Samples
This contains the template/master class for the samples. These samples will define the basic paramater of each sample to be considered by combine
and contain/be responsible for the uncertainties on the sample. It also handles the nominal histogram for its sample.
## Uncertainties
This contains the template/master class for the uncertainties on samples. Each defined uncertainty must be a derived child of this class.
It will define the various up/down uncertainties related to the overall category of uncertainty, handle their histograms,
and maintain a dictionary of fuinctions used for modifying the nominal event dictionaries to use the uncertainty values.
## Utilities
Contains various utility things for the data card creator, the loader and unroller.
