from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class TTbarShape(Uncertainty):
    def __init__(self):
        self.name = "TTbarShape"
        self.uncertaintyNames = [
            "CMS_htt_ttbarShapeUp",
            "CMS_htt_ttbarShapeDown"
        ]
        self.eventDictionaryModifications={
            "CMS_htt_ttbarShapeUp":self.CreateTTbarUpDictionary,
            "CMS_htt_ttbarShapeDown":self.CreateTTbarDownDictionary
            }
    def CreateTTbarUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TopPt_UP
        
        return modifiedEventDictionary

    def CreateTTbarDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TopPt_DOWN

        return modifiedEventDictionary
