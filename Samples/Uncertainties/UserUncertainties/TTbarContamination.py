#this will need a special way to do the addition/subtraction of the ttbar samples from the embedded

from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class TTbarContaminationUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'TTbarContamination'
        self.uncertaintyNames = [
            'CMS_htt_emb_ttbar',
        ]
        self.eventDictionaryModifications = {
            'CMS_htt_emb_ttbar': self.CreateTTbarContaminationDictionary
            }
    def CreateTTbarContaminationDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        return modifiedEventDictionary
