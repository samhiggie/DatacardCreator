from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class PrefiringUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'Prefiring'
        self.uncertaintyNames = [
            "CMS_prefiringUp",
            "CMS_prefiringDown",
            ]
        self.eventDictionaryModifications = {
            "CMS_prefiringUp":self.CreatePrefiringDictionaryUp,
            "CMS_prefiringDown":self.CreatePrefiringDictionaryDown,
            }

    def CreatePrefiringDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_PrefiringWeighting_UP
        return modifiedEventDictionary

    def CreatePrefiringDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_PrefiringWeighting_DOWN
        return modifiedEventDictionary
