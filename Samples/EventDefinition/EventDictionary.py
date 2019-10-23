#a class that will help us define what quantities pulled from the tree mean what
#and how to compute the various category relevant quantities.
#We'll split the quantities computed up into two basic tiers.
#One: The basic quantities. Quantities that (while they may change in uncertainites) are not reliant on other quantiites
#Two: the constructed quantities. Quantities dependent on the possibly shifting basic quantities

#We'll need two functions defined in a user configuration to properly fill both dictionaries
#they must overwrite the basic functions, which if called will just error out.
#"FillBasicQuantities" and "FillConstructedQuantities"
#FillConstructedQuantities will take the basic quantities as an argument.
import ROOT

class EventDictionary():
    def __init__(self):
        self.basicQuantities = {}
        self.constructedQuantities = {}
        self.eventDictionary = {}
        self.Weight = 0.0
    #default basic quantitiy function. This needs to be defined by the user
    def FillBasicQuantities(self,theTree):
        raise RuntimeError("Default Basic Quantity Function! Define a way to fill all basic quantities and replace this function with it!")
    #defailt constructed quantities function. This also needs to be defined by the user
    def FillConstructedQuantities(self,basicQuantities):
        raise RuntimeError("Default Constructed Quantity Function! Define a way to fill all basic Quantities and replace this function with it!")
    #this will fill both the basic and the constructed quantities for the nominal values provided
    #the weight of the event will have to be handled later by the sample (may need fake factors, so the sample will decide)
    def CreateCompleteEvent(self,theTree):
        self.FillBasicQuantities(self,theTree)
        self.FillConstructedQuantities(self,self.basicQuantities)        
        self.CompileCompleteDictionary()
    def CompileCompleteDictionary(self):
        self.eventDictionary = self.basicQuantities.copy()
        self.eventDictionary.update(self.constructedQuantities)
    def Clone(self):
        clonedEventDictionary = EventDictionary()
        clonedEventDictionary.basicQuantities = self.basicQuantities.copy()
        clonedEventDictionary.constructedQuantities = self.constructedQuantities.copy()
        clonedEventDictionary.eventDictionary = self.eventDictionary.copy()
        clonedEventDictionary.FillBasicQuantities = self.FillBasicQuantities
        clonedEventDictionary.FillConstructedQuantities = self.FillConstructedQuantities
        clonedEventDictionary.Weight = self.Weight
        return clonedEventDictionary
