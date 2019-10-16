#a class that defines what we want out various samples to contain and do
#it will define the name, the files/paths to load into a chain 
#an additional definition on what it takes to be a part of the sample (cutstring)
#a list of all the uncertainties that apply to the sample
#a way to define the weight of events in the sample (with an eye towards Fake Factors vs not)
#a call that fills all the histograms associated with sample.

#okay how do we handle histograms? Each analysis category needs it's own ones
#the analysis category will define the various rollings and parameters, and the sample 
# will create nominals, and the analysis configuration over to it's uncertainties
# and allow the uncertainties 

import ROOT
from array import array
import math

class Sample():
    def __init__(self):
        self.Name= ""
        self.Path=""
        self.Files=""
        self.Uncertainties = []
    #default function to be replaced that defines how to weight the event
    #this will be replaced by the user in configuration, but I'll also provide
    # the two most common default ones I would use
    def CreateEventWeight(self,theEventDictionary,theTree):
        raise RuntimeError("Default CreateEventWeight()! Please define this function in the configuration!")
    #default weight creation functions
    def CreateEventWeight_Standard(self,theEventDictionary,theTree):
        theEventDictionary.Weight = theTree.FinalWeighting
    def CreateEventWeight_Fake(self,theEventDictionary,theTree):
        theEventDictionary.Weight = theTree.FinalWeighting * theTree.FinalWeighting.Event_Fake_Factor
        
