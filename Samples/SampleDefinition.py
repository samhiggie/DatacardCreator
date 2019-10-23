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
from EventDefinition.EventDictionary import EventDictionary

class Sample():
    def __init__(self):
        self.name= ""
        self.path=""
        self.files=""
        self.definition = ''
        self.uncertainties = []        
        self.eventDictionaryInstance = EventDictionary()
        #this does not need to be user defined
        self.nominalHistograms = {}
    #load the files and trees into a chain.
    def InitializeSample(self):
        self.chain = ROOT.TChain("mt_Selected")
        for theFile in self.files:
            self.chain.Add(self.path+theFile)
        self.chain = self.chain.CopyTree(self.definition)
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
    # create a quick list of nominal histograms for each analysis category
    def CreateNominalHistograms(self,analysisCategories):
        for analysisCategory in analysisCategories:
            theHistogram = analysisCategory.templateHistogram.Clone()
            theHistogram.SetNameTitle(self.name,self.name)
            self.nominalHistograms[analysisCategory.name] = theHistogram
    #Return all histograms belonging to the sample and it's uncertainties across all categories
    #it will return a dictionary split up by analysis category name 
    def GetAllHistograms(self):
        completeHistogramDictionary = {}
        for analysisCategoryName in self.nominalHistograms:
            histogramList = []
            histogramList.append(self.nominalHistograms[analysisCategoryName]) # this retrieves the nominal histogram
            for uncertainty in self.uncertainties:                
                for upDownName in uncertainty.histograms[analysisCategoryName]:
                    histogramList.append(uncertainty.histograms[analysisCategoryName][upDownName])
            completeHistogramDictionary[analysisCategoryName] = histogramList
        return completeHistogramDictionary

    #this will sort of be the master function for creating and filling histograms
    def ProcessEvent(self,theTree,analysisCategories):
        #first things first, let's get the event dictionary,
        self.eventDictionaryInstance.CreateCompleteEvent(theTree)
        #then decide what weight we're using for this event
        self.CreateEventWeight(self.eventDictionaryInstance,theTree)        
        #then, we'll figure out if our event nominally falls in any of the analysis categories
        for analysisCategory in analysisCategories:
            if analysisCategory.IsInCategory(analysisCategory,self.eventDictionaryInstance):
                self.nominalHistograms[analysisCategory.name].Fill(self.eventDictionaryInstance.eventDictionary[analysisCategory.reconstructionVariable],self.eventDictionaryInstance.eventDictionary[analysisCategory.rollingVariable],self.eventDictionaryInstance.Weight)
        #then let's go through our uncertainties and process all of them.
        for uncertainty in self.uncertainties:
            uncertainty.ProcessAllHistograms(analysisCategories,theTree,self.eventDictionaryInstance)
    #Function for initializing all histograms
    def InitializeAllHistograms(self,analysisCategories):
        self.CreateNominalHistograms(analysisCategories)
        for uncertainty in self.uncertainties:
            uncertainty.CreateAllHistograms(self,analysisCategories)
        
