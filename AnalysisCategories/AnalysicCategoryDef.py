#Okay, this will provide the framework needed for deciding which events will fit into which categories, 
#and whether uncertainties or what have-you push an event from one category to another, or out of validity entirely.
#it will neeed a few things

#Category should specify it's own reconstruction variable, to be taken from the event dictionary lists.

#Needs:
#User defined function that we feed to is that takes the event dictionary of the event,
#looks at whichever quantities it wants, and then sends back a true/false?
#call the function "IsInCategory()"

import ROOT

class AnalysisCategory():
    def __init__(self):
        self.Name = ''                
    #default function
    #needs to properly defined by the user
    def IsInCategory(self,theEventDictionary):
        raise RuntimeError("No Proper way to decide if an event is in this category! Please define a proper IsInCategory()!") 
