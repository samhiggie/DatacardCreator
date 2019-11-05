from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggHTheoryUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggHTheory'
        self.uncertaintyNames = [
            'THU_ggH_MuUp',
            'THU_ggH_MuDown',
            'THU_ggH_ResUp',
            'THU_ggH_ResDown',
            'THU_ggH_Mig01Up',
            'THU_ggH_Mig01Down',
            'THU_ggH_Mig12Up',
            'THU_ggH_Mig12Down',
            'THU_ggH_VBF2jUp',
            'THU_ggH_VBF2jDown',
            'THU_ggH_VBF3jUp',
            'THU_ggH_VBF3jDown',
            'THU_ggH_PT60Up',
            'THU_ggH_PT60Down',
            'THU_ggH_PT120Up',
            'THU_ggH_PT120Down',
            'THU_ggH_qmtopUp',
            'THU_ggH_qmtopDown',
        ]
        self.eventDictionaryModifications = {
            'THU_ggH_MuUp':self.CreateMuUpDictionary,
            'THU_ggH_MuDown':self.CreateMuDownDictionary,
            'THU_ggH_ResUp':self.CreateResUpDictionary,
            'THU_ggH_ResDown':self.CreateResDownDictionary,
            'THU_ggH_Mig01Up':self.CreateMig01UpDictionary,
            'THU_ggH_Mig01Down':self.CreateMig01DownDictionary,
            'THU_ggH_Mig12Up':self.CreateMig12UpDictionary,
            'THU_ggH_Mig12Down':self.CreateMig12DownDictionary,
            'THU_ggH_VBF2jUp':self.CreateVBF2jUpDictionary,
            'THU_ggH_VBF2jDown':self.CreateVBF2jDownDictionary,
            'THU_ggH_VBF3jUp':self.CreateVBF3jUpDictionary,
            'THU_ggH_VBF3jDown':self.CreateVBF3jDownDictionary,
            'THU_ggH_PT60Up':self.CreatePT60UpDictinoary,
            'THU_ggH_PT60Down':self.CreatePT60DownDictionary,
            'THU_ggH_PT120Up':self.CreatePT120UpDictionary,
            'THU_ggH_PT120Down':self.CreatePT120DownDictionary,
            'THU_ggH_qmtopUp':self.CreateqmtopUpDictionary,
            'THU_ggH_qmtopDown':self.CreateqmtopDownDictionary,
        }
    def CreateMuUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_Mu_13TeV))
        
        return modifiedEventDictionary

    def CreateMuDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_Mu_13TeV))
    
        return modifiedEventDictionary
        
    def CreateResUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_Res_13TeV))

        return modifiedEventDictionary

    def CreateResDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_Res_13TeV))

        return modifiedEventDictionary

    def CreateMig01UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_Mig01_13TeV))

        return modifiedEventDictionary

    def CreateMig01DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_Mig01_13TeV))

        return modifiedEventDictionary

    def CreateMig12UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_Mig12_13TeV))

        return modifiedEventDictionary

    def CreateMig12DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_Mig12_13TeV))

        return modifiedEventDictionary

    def CreateVBF2jUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_VBF2j_13TeV))

        return modifiedEventDictionary

    def CreateVBF2jDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_VBF2j_13TeV))

        return modifiedEventDictionary

    def CreateVBF3jUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_VBF3j_13TeV))

        return modifiedEventDictionary

    def CreateVBF3jDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_VBF3j_13TeV))
        
        return modifiedEventDictionary

    def CreatePT60UpDictinoary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_PT60_13TeV))
        
        return modifiedEventDictionary

    def CreatePT60DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_PT60_13TeV))
        
        return modifiedEventDictionary

    def CreatePT120UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_PT120_13TeV))

        return modifiedEventDictionary

    def CreatePT120DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_PT120_13TeV))

        return modifiedEventDictionary

    def CreateqmtopUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0+theTree.THU_ggH_qmtop_13TeV))

        return modifiedEventDictionary

    def CreateqmtopDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = (theTree.FinalWeighting*(1.0-theTree.THU_ggH_qmtop_13TeV))

        return modifiedEventDictionary
