#do I want to do this as an inheriting class, instead of an instance?
#Probably. Multiple distributions are going to need their own TES uncertainties 
#

from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class TESUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'TES'
        self.uncertaintyNames = [
            "CMS_scale_t_1prongUp",
            "CMS_scale_t_1prongDown",
            "CMS_scale_t_1prong1pizeroUp",
            "CMS_scale_t_1prong1pizeroDown",
            "CMS_scale_t_3prongUp",
            "CMS_scale_t_3prongDown"
            ]        
        self.eventDictionaryModifications = {
            "CMS_scale_t_1prongUp":self.CreateOneProngUpModifiedDictionary,
            "CMS_scale_t_1prongDown":self.CreateOneProngDownModifiedDictionary,
            "CMS_scale_t_1prong1pizeroUp":self.CreateOneProngOnePizeroUpModifiedDictionary,
            "CMS_scale_t_1prong1pizeroDown":self.CreateOneProngOnePizeroDownModifiedDictionary,
            "CMS_scale_t_3prongUp":self.CreateThreeProngUpModifiedDictionary,
            "CMS_scale_t_3prongDown":self.CreateThreeProngDownModifiedDictionary
        }
    def CreateOneProngUpModifiedDictionary(self,theTree,nominalEventDictionary):
        tauVectorUp = ROOT.TLorentzVector()
        metVectorUp = ROOT.TLorentzVector()
        if(theTree.l2_decayMode == 0):
            tauVectorUp.SetPtEtaPhiE(theTree.TES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.TES_E_UP)
            metVectorUp.SetPtEtaPhiM(theTree.TES_MET_UP,0.0,theTree.TES_METPhi_UP,0.0)
        else:
            tauVectorUp.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVectorUp.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
            
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["TauPt"] = tauVectorUp.Pt()
        modifiedEventDictionary.basicQuantities["TauM"] = tauVectorUp.M()
        modifiedEventDictionary.basicQuantities["TauE"] = tauVectorUp.E()
        modifiedEventDictionary.basicQuantities["MET"] = metVectorUp.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVectorUp.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
    
    def CreateOneProngDownModifiedDictionary(self,theTree,nominalEventDictionary):
        tauVectorDown = ROOT.TLorentzVector()
        metVectorDown = ROOT.TLorentzVector()
        if(theTree.l2_decayMode == 0):
            tauVectorDown.SetPtEtaPhiE(theTree.TES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.TES_E_DOWN)
            metVectorDown.SetPtEtaPhiM(theTree.TES_MET_DOWN,0.0,theTree.TES_METPhi_DOWN,0.0)
        else:
            tauVectorDown.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVectorDown.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["TauPt"] = tauVectorDown.Pt()
        modifiedEventDictionary.basicQuantities["TauM"] = tauVectorDown.M()
        modifiedEventDictionary.basicQuantities["TauE"] = tauVectorDown.E()
        modifiedEventDictionary.basicQuantities["MET"] = metVectorDown.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVectorDown.Phi()

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateOneProngOnePizeroUpModifiedDictionary(self,theTree,nominalEventDictionary):
        tauVectorUp = ROOT.TLorentzVector()
        metVectorUp = ROOT.TLorentzVector()
        if(theTree.l2_decayMode == 1):
            tauVectorUp.SetPtEtaPhiE(theTree.TES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.TES_E_UP)
            metVectorUp.SetPtEtaPhiM(theTree.TES_MET_UP,0.0,theTree.TES_METPhi_UP,0.0)
        else:
            tauVectorUp.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVectorUp.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["TauPt"] = tauVectorUp.Pt()
        modifiedEventDictionary.basicQuantities["TauM"] = tauVectorUp.M()
        modifiedEventDictionary.basicQuantities["TauE"] = tauVectorUp.E()
        modifiedEventDictionary.basicQuantities["MET"] = metVectorUp.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVectorUp.Phi()

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateOneProngOnePizeroDownModifiedDictionary(self,theTree,nominalEventDictionary):
        tauVectorDown = ROOT.TLorentzVector()
        metVectorDown = ROOT.TLorentzVector()
        if(theTree.l2_decayMode == 1):
            tauVectorDown.SetPtEtaPhiE(theTree.TES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.TES_E_DOWN)
            metVectorDown.SetPtEtaPhiM(theTree.TES_MET_DOWN,0.0,theTree.TES_METPhi_DOWN,0.0)
        else:
            tauVectorDown.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVectorDown.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["TauPt"] = tauVectorDown.Pt()
        modifiedEventDictionary.basicQuantities["TauM"] = tauVectorDown.M()
        modifiedEventDictionary.basicQuantities["TauE"] = tauVectorDown.E()
        modifiedEventDictionary.basicQuantities["MET"] = metVectorDown.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVectorDown.Phi()

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateThreeProngUpModifiedDictionary(self,theTree,nominalEventDictionary):
        tauVectorUp = ROOT.TLorentzVector()
        metVectorUp = ROOT.TLorentzVector()
        if(theTree.l2_decayMode == 10):
            tauVectorUp.SetPtEtaPhiE(theTree.TES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.TES_E_UP)
            metVectorUp.SetPtEtaPhiM(theTree.TES_MET_UP,0.0,theTree.TES_METPhi_UP,0.0)
        else:
            tauVectorUp.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVectorUp.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["TauPt"] = tauVectorUp.Pt()
        modifiedEventDictionary.basicQuantities["TauM"] = tauVectorUp.M()
        modifiedEventDictionary.basicQuantities["TauE"] = tauVectorUp.E()
        modifiedEventDictionary.basicQuantities["MET"] = metVectorUp.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVectorUp.Phi()

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateThreeProngDownModifiedDictionary(self,theTree,nominalEventDictionary):
        tauVectorDown = ROOT.TLorentzVector()
        metVectorDown = ROOT.TLorentzVector()
        if(theTree.l2_decayMode == 10):
            tauVectorDown.SetPtEtaPhiE(theTree.TES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.TES_E_DOWN)
            metVectorDown.SetPtEtaPhiM(theTree.TES_MET_DOWN,0.0,theTree.TES_METPhi_DOWN,0.0)
        else:
            tauVectorDown.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVectorDown.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["TauPt"] = tauVectorDown.Pt()
        modifiedEventDictionary.basicQuantities["TauM"] = tauVectorDown.M()
        modifiedEventDictionary.basicQuantities["TauE"] = tauVectorDown.E()
        modifiedEventDictionary.basicQuantities["MET"] = metVectorDown.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVectorDown.Phi()

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
