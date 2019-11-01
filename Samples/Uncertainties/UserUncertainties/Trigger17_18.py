from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class Trigger1718Uncertainty(Uncertainty):
    def __init__(self):
        self.name = "2017/2018 Trigger"
        self.uncertaintyNames = [
            "CMS_singlemutrgUp",
            "CMS_mutautrgUp",
            "CMS_singlemutrgDown",
            "CMS_mutautrgDown",
            ]
        self.eventDictionaryModifications = {
            "CMS_singlemutrgUp":self.CreateSingleMuTrgUpDictionary,
            "CMS_mutautrgUp":self.CreateMuTauTrgUpDictionary,
            "CMS_singlemutrgDown":self.CreateSingleMuTrgDownDictionary,
            "CMS_mutautrgDown":self.CreateMuTauTrgDownDictionary,
            }
    def CreateSingleMuTrgUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger24or27_UP
        return modifiedEventDictionary
    def CreateSingleMuTrgDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger24or27_DOWN
        return modifiedEventDictionary
    def CreateMuTauTrgUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger2027_UP
        return modifiedEventDictionary
    def CreateMuTauTrgDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger2027_DOWN
        return modifiedEventDictionary
