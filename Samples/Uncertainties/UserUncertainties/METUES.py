from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class METUESUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'METUES'
        self.uncertaintyNames = [
            "CMS_scale_met_unclusteredUp",
            "CMS_scale_met_unclusteredDown"
        ]
        self.eventDictionaryModifications={
            "CMS_scale_met_unclusteredUp":self.CreateMETUESUpDictionary,
            "CMS_scale_met_unclusteredDown":self.CreateMETUESDownDictionary
            }
    def CreateMETUESUpDictionary(self,theTree,nominalEventDictionary):
        metVector = ROOT.TLorentzVector()
        metVector.SetPtEtaPhiM(theTree.met_UESUp,0.0,theTree.metphi_UESUp,0.0)
            
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MET"] = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_UESUp
            
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
            
    def CreateMETUESDownDictionary(self,theTree,nominalEventDictionary):
        metVector = ROOT.TLorentzVector()
        metVector.SetPtEtaPhiM(theTree.met_UESDown,0.0,theTree.metphi_UESDown,0.0)
            
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MET"] = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_UESDown
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
