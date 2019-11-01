import ROOT
from Samples.Uncertainties.UncertaintyDef import Uncertainty

class ZLShapeUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ZLShape'
        self.uncertaintyNames = [
            "CMS_ZLShape_mt_1prongUp",
            "CMS_ZLShape_mt_1prongDown",
            "CMS_ZLShape_mt_1prong1pizeroUp",
            "CMS_ZLShape_mt_1prong1pizeroDown"
        ]
        self.eventDictionaryModifications = {
            "CMS_ZLShape_mt_1prongUp":self.CreateOneProngUpDictionary,
            "CMS_ZLShape_mt_1prongDown":self.CreateOneProngDownDictionary,
            "CMS_ZLShape_mt_1prong1pizeroUp":self.CreateOneProngOnePizeroUpDictionary,
            "CMS_ZLShape_mt_1prong1pizeroDown":self.CreateOneProngOnePizeroDownDictionary
        }
    def CreateOneProngUpDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        if(theTree.l2_decayMode == 0):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.EES_E_UP)
                metVector.SetPtEtaPhiM(theTree.EES_MET_UP,0.0,theTree.EES_METPhi_DOWN,0.0)
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.MES_E_UP)
                metVector.SetPtEtaPhiM(theTree.MES_MET_UP,0.0,theTree.MES_METPhi_UP,0.0)
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateOneProngDownDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        if(theTree.l2_decayMode == 0):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.EES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.EES_MET_DOWN,0.0,theTree.EES_METPhi_DOWN,0.0)
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.MES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.MES_MET_DOWN,0.0,theTree.MES_METPhi_DOWN,0.0)
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateOneProngOnePizeroUpDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        if(theTree.l2_decayMode == 1):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.EES_E_UP)
                metVector.SetPtEtaPhiM(theTree.EES_MET_UP,0.0,theTree.EES_METPhi_DOWN,0.0)
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.MES_E_UP)
                metVector.SetPtEtaPhiM(theTree.MES_MET_UP,0.0,theTree.MES_METPhi_UP,0.0)
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateOneProngOnePizeroDownDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        if(theTree.l2_decayMode == 1):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.EES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.EES_MET_DOWN,0.0,theTree.EES_METPhi_DOWN,0.0)
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.MES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.MES_MET_DOWN,0.0,theTree.MES_METPhi_DOWN,0.0)
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
