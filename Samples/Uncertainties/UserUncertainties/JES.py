from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class JESUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'JES'
        self.uncertaintyNames  =[
            "CMS_JetEta0to3Up",
            "CMS_JetEta0to3Down",
            "CMS_JetRelativeBalUp",
            "CMS_JetRelativeBalDown",
            "CMS_JetRelativeSampleUp",
            "CMS_JetRelativeSampleDown",
            "CMS_JetEta3to5Up",
            "CMS_JetEta3to5Down",
            "CMS_JetEta0to5Up",
            "CMS_JetEta0to5Down",
            "CMS_JetEC2Up",
            "CMS_JetEC2Down"
            ]

        self.eventDictionaryModifications ={
            "CMS_JetEta0to3Up":self.CreateJetEta0to3UpDictionary,
            "CMS_JetEta0to3Down":self.CreateJetEta0to3DownDictionary,
            "CMS_JetRelativeBalUp":self.CreateJetRelativeBalUpDictionary,
            "CMS_JetRelativeBalDown":self.CreateJetRelativeBalDownDictionary,
            "CMS_JetRelativeSampleUp":self.CreateJetRelativeSampleUpDictionary,
            "CMS_JetRelativeSampleDown":self.CreateJetRelativeSampleDownDictionary,
            "CMS_JetEta3to5Up":self.CreateJetEta3to5UpDictionary,
            "CMS_JetEta3to5Down":self.CreateJetEta3to5DownDictionary,
            "CMS_JetEta0to5Up":self.CreateJetEta0to5UpDictionary,
            "CMS_JetEta0to5Down":self.CreateJetEta0to5DownDictionary,
            "CMS_JetEC2Up":self.CreateJetEC2UpDictionary,
            "CMS_JetEC2Down":self.CreateJetEC2DownDictionary
            }
    def CreateJetEta0to3UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetEta0to3Up,0.0,theTree.metphi_JetEta0to3Up,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEta0to3Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEta0to3Up
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEta0to3Up
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
            
    def CreateJetEta0to3DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetEta0to3Down,0.0,theTree.metphi_JetEta0to3Down,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEta0to3Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEta0to3Down
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEta0to3Down
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetRelativeBalUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeBalUp,0.0,theTree.metphi_JetRelativeBalUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeBalUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeBalUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeBalUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeBalDownDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetRelativeBalDown,0.0,theTree.metphi_JetRelativeBalDown,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeBalDown
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeBalDown
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeBalDown

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetRelativeSampleUpDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetRelativeSampleUp,0.0,theTree.metphi_JetRelativeSampleUp,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeSampleUp
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeSampleUp
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeSampleUp

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetRelativeSampleDownDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetRelativeSampleDown,0.0,theTree.metphi_JetRelativeSampleDown,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeSampleDown
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeSampleDown
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeSampleDown

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetEta3to5UpDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetEta3to5Up,0.0,theTree.metphi_JetEta3to5Up,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEta3to5Up
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEta3to5Up
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEta3to5Up

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary
            
    def CreateJetEta3to5DownDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetEta3to5Down,0.0,theTree.metphi_JetEta3to5Down,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEta3to5Down
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEta3to5Down
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEta3to5Down

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetEta0to5UpDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetEta0to5Up,0.0,theTree.metphi_JetEta0to5Up,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEta0to5Up
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEta0to5Up
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEta0to5Up

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetEta0to5DownDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetEta0to5Down,0.0,theTree.metphi_JetEta0to5Down,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEta0to5Down
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEta0to5Down
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEta0to5Down

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetEC2UpDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetEC2Up,0.0,theTree.metphi_JetEC2Up,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2Up
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2Up
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2Up

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetEC2DownDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetEC2Down,0.0,theTree.metphi_JetEC2Down,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2Down
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2Down
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2Down

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary
