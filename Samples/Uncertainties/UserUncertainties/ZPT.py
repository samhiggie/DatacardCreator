from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ZPTUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'DYShape'
        self.uncertaintyNames = [
            "CMS_htt_dyShapeUp",
            "CMS_htt_dyShapeDown",
            ]
        self.eventDictionaryModifications = {
            "CMS_htt_dyShapeUp":self.CreateDYShapeUpDictionary,
            "CMS_htt_dyShapeDown":self.CreateDYShapeDownDictionary,
            }
    def CreateDYShapeUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ZPT_UP
        
        return modifiedEventDictionary

    def CreateDYShapeDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ZPT_DOWN

        return modifiedEventDictionary
