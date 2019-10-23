#Okay, this will provide the framework needed for deciding which events will fit into which categories, 
#and whether uncertainties or what have-you push an event from one category to another, or out of validity entirely.
#it will neeed a few things

#Category should specify it's own reconstruction variable, to be taken from the event dictionary lists.

#Needs:
#User defined function that we feed to is that takes the event dictionary of the event,
#looks at whichever quantities it wants, and then sends back a true/false?
#call the function "IsInCategory()"

import ROOT
from array import array

class AnalysisCategory():
    def __init__(self):
        self.name = ''                
        self.rollingVariable = ''
        self.reconstructionVariable = ''
        self.rollingBins = []
        self.reconstructionBins = []        
    #default function
    #needs to properly defined by the user
    def IsInCategory(self,theEventDictionary):
        raise RuntimeError("No Proper way to decide if an event is in this category! Please define a proper IsInCategory()!") 
    #a quick function to create our template histogram
    def CreateTemplateHistogram(self):
        rollingArray = array('d',self.rollingBins)        
        reconstructionArray = array('d',self.reconstructionBins)
        nRollingBins = len(self.rollingBins)-1 #fence posting problem.
        nReconstructionBins = len(self.reconstructionBins)-1 #fence posting problem

        self.templateHistogram = ROOT.TH2F(self.name+"_template",self.name+"_name",nReconstructionBins,reconstructionArray,nRollingBins,rollingArray)
    
