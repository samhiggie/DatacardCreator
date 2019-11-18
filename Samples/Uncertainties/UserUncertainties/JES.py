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
            "CMS_JetEC2Down", 
            "CMS_JetTotalDown",
            "CMS_JetTotalUp",
            "CMS_JetRelativeSampleDown",
            "CMS_JetRelativeStatHFDown",
            "CMS_JetRelativeStatFSRDown",
            "CMS_JetRelativeStatECDown",
            "CMS_JetRelativePtHFDown",
            "CMS_JetRelativePtEC2Down",
            "CMS_JetRelativePtEC1Down",
            "CMS_JetRelativePtBBDown",
            "CMS_JetRelativeJERHFDown",
            "CMS_JetRelativeJEREC2Down",
            "CMS_JetRelativeJEREC1Down",
            "CMS_JetRelativeFSRDown",
            "CMS_JetRelativeBalDown",
            "CMS_JetSinglePionECALDown", 
            "CMS_JetSinglePionHCALDown", 
            "CMS_JetAbsoluteFlavMapDown",
            "CMS_JetAbsoluteMPFBiasDown",
            "CMS_JetAbsoluteSampleDown",
            "CMS_JetAbsoluteScaleDown",
            "CMS_JetClosureDown",
            "CMS_JetFlavorQCDDown",
            "CMS_JetFragmentationDown",
            "CMS_JetPileUpDataMCDown",
            "CMS_JetPileUpPtBBDown",
            "CMS_JetPileUpPtEC1Down",
            "CMS_JetPileUpPtEC2Down",
            "CMS_JetPileUpPtHFDown",
            "CMS_JetPileUpPtRefDown",
            "CMS_JetEta0to3Down",
            "CMS_JetEta3to5Down",
            "CMS_JetEta0to5Down",
            "CMS_JetTimePtEtaDown",
            "CMS_JetRelativeSampleUp", 
            "CMS_JetRelativeStatHFUp", 
            "CMS_JetRelativeStatFSRUp",
            "CMS_JetRelativeStatECUp",
            "CMS_JetRelativePtHFUp",
            "CMS_JetRelativePtEC2Up",
            "CMS_JetRelativePtEC1Up",
            "CMS_JetRelativePtBBUp",
            "CMS_JetRelativeJERHFUp",
            "CMS_JetRelativeJEREC2Up",
            "CMS_JetRelativeJEREC1Up",
            "CMS_JetRelativeFSRUp",
            "CMS_JetRelativeBalUp",
            "CMS_JetSinglePionECALUp",
            "CMS_JetSinglePionHCALUp",
            "CMS_JetAbsoluteFlavMapUp",
            "CMS_JetAbsoluteMPFBiasUp",
            "CMS_JetAbsoluteSampleUp",
            "CMS_JetAbsoluteScaleUp",
            "CMS_JetClosureUp",
            "CMS_JetFlavorQCDUp",
            "CMS_JetFragmentationUp",
            "CMS_JetPileUpDataMCUp",
            "CMS_JetPileUpPtBBUp",
            "CMS_JetPileUpPtEC1Up",
            "CMS_JetPileUpPtEC2Up",
            "CMS_JetPileUpPtHFUp",
            "CMS_JetPileUpPtRefUp",
            "CMS_JetTimePtEtaUp"
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
            "CMS_JetEC2Down":self.CreateJetEC2DownDictionary,
            "CMS_JetRelativeStatHFDown":self.CreateJetRelativeStatHFDownDictionary,
            "CMS_JetRelativeStatFSRDown":self.CreateJetRelativeStatFSRDownDictionary,
            "CMS_JetRelativeStatECDown":self.CreateJetRelativeStatECDownDictionary,
            "CMS_JetRelativePtHFDown":self.CreateJetRelativePtHFDownDictionary,
            "CMS_JetRelativePtEC2Down":self.CreateJetRelativePtEC2DownDictionary,
            "CMS_JetRelativePtEC1Down":self.CreateJetRelativePtEC1DownDictionary,
            "CMS_JetRelativePtBBDown":self.CreateJetRelativePtBBDownDictionary,
            "CMS_JetRelativeJERHFDown":self.CreateJetRelativeJERHFDownDictionary,
            "CMS_JetRelativeJEREC2Down":self.CreateJetRelativeJEREC2DownDictionary,
            "CMS_JetRelativeJEREC1Down":self.CreateJetRelativeJEREC1DownDictionary,
            "CMS_JetRelativeFSRDown":self.CreateJetRelativeFSRDownDictionary,
            "CMS_JetSinglePionECALDown":self.CreateJetSinglePionECALDownDictionary,
            "CMS_JetSinglePionHCALDown":self.CreateJetSinglePionHCALDownDictionary,
            "CMS_JetAbsoluteFlavMapDown":self.CreateJetAbsoluteFlavMapDownDictionary,
            "CMS_JetAbsoluteMPFBiasDown":self.CreateJetAbsoluteMPFBiasDownDictionary,
            "CMS_JetAbsoluteSampleDown":self.CreateJetAbsoluteSampleDownDictionary,
            "CMS_JetAbsoluteScaleDown":self.CreateJetAbsoluteScaleDownDictionary,
            "CMS_JetClosureDown":self.CreateJetClosureDownDictionary,
            "CMS_JetFlavorQCDDown":self.CreateJetFlavorQCDDownDictionary,
            "CMS_JetFragmentationDown":self.CreateJetFragmentationDownDictionary,
            "CMS_JetPileUpDataMCDown":self.CreateJetPileUpDataMCDownDictionary,
            "CMS_JetPileUpPtBBDown":self.CreateJetPileUpPtBBDownDictionary,
            "CMS_JetPileUpPtEC1Down":self.CreateJetPileUpPtEC1DownDictionary,
            "CMS_JetPileUpPtEC2Down":self.CreateJetPileUpPtEC2DownDictionary,
            "CMS_JetPileUpPtHFDown":self.CreateJetPileUpPtHFDownDictionary,
            "CMS_JetPileUpPtRefDown":self.CreateJetPileUpPtRefDownDictionary,
            "CMS_JetTimePtEtaDown":self.CreateJetTimePtEtaDownDictionary,
            "CMS_JetRelativeStatHFUp":self.CreateJetRelativeStatHFUpDictionary,
            "CMS_JetRelativeStatFSRUp":self.CreateJetRelativeStatFSRUpDictionary,
            "CMS_JetRelativeStatECUp":self.CreateJetRelativeStatECUpDictionary,
            "CMS_JetRelativePtHFUp":self.CreateJetRelativePtHFUpDictionary,
            "CMS_JetRelativePtEC2Up":self.CreateJetRelativePtEC2UpDictionary,
            "CMS_JetRelativePtEC1Up":self.CreateJetRelativePtEC1UpDictionary,
            "CMS_JetRelativePtBBUp":self.CreateJetRelativePtBBUpDictionary,
            "CMS_JetRelativeJERHFUp":self.CreateJetRelativeJERHFUpDictionary,
            "CMS_JetRelativeJEREC2Up":self.CreateJetRelativeJEREC2UpDictionary,
            "CMS_JetRelativeJEREC1Up":self.CreateJetRelativeJEREC1UpDictionary,
            "CMS_JetRelativeFSRUp":self.CreateJetRelativeFSRUpDictionary,
            "CMS_JetSinglePionECALUp":self.CreateJetSinglePionECALUpDictionary,
            "CMS_JetSinglePionHCALUp":self.CreateJetSinglePionHCALUpDictionary,
            "CMS_JetAbsoluteFlavMapUp":self.CreateJetAbsoluteFlavMapUpDictionary,
            "CMS_JetAbsoluteMPFBiasUp":self.CreateJetAbsoluteMPFBiasUpDictionary,
            "CMS_JetAbsoluteSampleUp":self.CreateJetAbsoluteSampleUpDictionary,
            "CMS_JetAbsoluteScaleUp":self.CreateJetAbsoluteScaleUpDictionary,
            "CMS_JetClosureUp":self.CreateJetClosureUpDictionary,
            "CMS_JetFlavorQCDUp":self.CreateJetFlavorQCDUpDictionary,
            "CMS_JetFragmentationUp":self.CreateJetFragmentationUpDictionary,
            "CMS_JetPileUpDataMCUp":self.CreateJetPileUpDataMCUpDictionary,
            "CMS_JetPileUpPtBBUp":self.CreateJetPileUpPtBBUpDictionary,
            "CMS_JetPileUpPtEC1Up":self.CreateJetPileUpPtEC1UpDictionary,
            "CMS_JetPileUpPtEC2Up":self.CreateJetPileUpPtEC2UpDictionary,
            "CMS_JetPileUpPtHFUp":self.CreateJetPileUpPtHFUpDictionary,
            "CMS_JetPileUpPtRefUp":self.CreateJetPileUpPtRefUpDictionary,
            "CMS_JetTimePtEtaUp":self.CreateJetTimePtEtaUpDictionary
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

    def CreateJetRelativeStatHFUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeStatHFUp,0.0,theTree.metphi_JetRelativeStatHFUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeStatHFUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeStatHFUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeStatHFUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeStatHFDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeStatHFDown,0.0,theTree.metphi_JetRelativeStatHFDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeStatHFDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeStatHFDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeStatHFDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary


    def CreateJetRelativeStatFSRUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeStatFSRUp,0.0,theTree.metphi_JetRelativeStatFSRUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeStatFSRUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeStatFSRUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeStatFSRUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeStatFSRDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeStatFSRDown,0.0,theTree.metphi_JetRelativeStatFSRDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeStatFSRDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeStatFSRDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeStatFSRDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeStatECUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeStatECUp,0.0,theTree.metphi_JetRelativeStatECUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeStatECUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeStatECUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeStatECUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeStatECDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeStatECDown,0.0,theTree.metphi_JetRelativeStatECDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeStatECDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeStatECDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeStatECDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativePtHFUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtHFUp,0.0,theTree.metphi_JetRelativePtHFUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtHFUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtHFUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtHFUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativePtHFDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtHFDown,0.0,theTree.metphi_JetRelativePtHFDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtHFDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtHFDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtHFDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary


    def CreateJetRelativePtEC2UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtEC2Up,0.0,theTree.metphi_JetRelativePtEC2Up,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtEC2Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtEC2Up
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtEC2Up
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary


    def CreateJetRelativePtEC1UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtEC1Up,0.0,theTree.metphi_JetRelativePtEC1Up,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtEC1Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtEC1Up
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtEC1Up
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativePtEC1DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtEC1Down,0.0,theTree.metphi_JetRelativePtEC1Down,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtEC1Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtEC1Down
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtEC1Down
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary


    def CreateJetRelativePtEC2DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtEC2Down,0.0,theTree.metphi_JetRelativePtEC2Down,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtEC2Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtEC2Down
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtEC2Down
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativePtBBUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtBBUp,0.0,theTree.metphi_JetRelativePtBBUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtBBUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtBBUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtBBUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativePtBBDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativePtBBDown,0.0,theTree.metphi_JetRelativePtBBDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativePtBBDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativePtBBDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativePtBBDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeJERHFUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeJERHFUp,0.0,theTree.metphi_JetRelativeJERHFUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeJERHFUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeJERHFUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeJERHFUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeJERHFDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeJERHFDown,0.0,theTree.metphi_JetRelativeJERHFDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeJERHFDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeJERHFDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeJERHFDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeJEREC2UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeJEREC2Up,0.0,theTree.metphi_JetRelativeJEREC2Up,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeJEREC2Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeJEREC2Up
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeJEREC2Up
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeJEREC2DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeJEREC2Down,0.0,theTree.metphi_JetRelativeJEREC2Down,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeJEREC2Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeJEREC2Down
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeJEREC2Down
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeJEREC1UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeJEREC1Up,0.0,theTree.metphi_JetRelativeJEREC1Up,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeJEREC1Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeJEREC1Up
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeJEREC1Up
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeJEREC1DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeJEREC1Down,0.0,theTree.metphi_JetRelativeJEREC1Down,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeJEREC1Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeJEREC1Down
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeJEREC1Down
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetRelativeFSRUpDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetRelativeFSRUp,0.0,theTree.metphi_JetRelativeFSRUp,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeFSRUp
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeFSRUp
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeFSRUp

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetRelativeFSRDownDictionary(self,theTree,nominalEventDictionary):
            muVector = ROOT.TLorentzVector()
            tauVector = ROOT.TLorentzVector()
            metVector = ROOT.TLorentzVector()

            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met_JetRelativeFSRDown,0.0,theTree.metphi_JetRelativeFSRDown,0.0)
            
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
            modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
            modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeFSRDown
            modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeFSRDown
            modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeFSRDown

            modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
            modifiedEventDictionary.CompileCompleteDictionary()

            return modifiedEventDictionary

    def CreateJetSinglePionECALUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetSinglePionECALUp,0.0,theTree.metphi_JetSinglePionECALUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetSinglePionECALUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetSinglePionECALUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetSinglePionECALUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetSinglePionECALDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetSinglePionECALDown,0.0,theTree.metphi_JetSinglePionECALDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetSinglePionECALDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetSinglePionECALDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetSinglePionECALDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetSinglePionHCALUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetSinglePionHCALUp,0.0,theTree.metphi_JetSinglePionHCALUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetSinglePionHCALUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetSinglePionHCALUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetSinglePionHCALUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetSinglePionHCALDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetSinglePionHCALDown,0.0,theTree.metphi_JetSinglePionHCALDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetSinglePionHCALDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetSinglePionHCALDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetSinglePionHCALDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteFlavMapUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteFlavMapUp,0.0,theTree.metphi_JetAbsoluteFlavMapUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteFlavMapUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteFlavMapUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteFlavMapUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteFlavMapDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteFlavMapDown,0.0,theTree.metphi_JetAbsoluteFlavMapDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteFlavMapDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteFlavMapDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteFlavMapDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteMPFBiasUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteMPFBiasUp,0.0,theTree.metphi_JetAbsoluteMPFBiasUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteMPFBiasUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteMPFBiasUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteMPFBiasUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteMPFBiasDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteMPFBiasDown,0.0,theTree.metphi_JetAbsoluteMPFBiasDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteMPFBiasDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteMPFBiasDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteMPFBiasDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteSampleUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteSampleUp,0.0,theTree.metphi_JetAbsoluteSampleUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteSampleUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteSampleUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteSampleUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteSampleDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteSampleDown,0.0,theTree.metphi_JetAbsoluteSampleDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteSampleDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteSampleDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteSampleDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteScaleUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteScaleUp,0.0,theTree.metphi_JetAbsoluteScaleUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteScaleUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteScaleUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteScaleUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetAbsoluteScaleDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteScaleDown,0.0,theTree.metphi_JetAbsoluteScaleDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteScaleDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteScaleDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteScaleDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetClosureUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetClosureUp,0.0,theTree.metphi_JetClosureUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetClosureUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetClosureUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetClosureUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetClosureDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetClosureDown,0.0,theTree.metphi_JetClosureDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetClosureDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetClosureDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetClosureDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetFlavorQCDUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetFlavorQCDUp,0.0,theTree.metphi_JetFlavorQCDUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFlavorQCDUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFlavorQCDUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFlavorQCDUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetFlavorQCDDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetFlavorQCDDown,0.0,theTree.metphi_JetFlavorQCDDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFlavorQCDDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFlavorQCDDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFlavorQCDDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetFragmentationUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetFragmentationUp,0.0,theTree.metphi_JetFragmentationUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFragmentationUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFragmentationUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFragmentationUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetFragmentationDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetFragmentationDown,0.0,theTree.metphi_JetFragmentationDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFragmentationDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFragmentationDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFragmentationDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpDataMCUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpDataMCUp,0.0,theTree.metphi_JetPileUpDataMCUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpDataMCUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpDataMCUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpDataMCUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpDataMCDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpDataMCDown,0.0,theTree.metphi_JetPileUpDataMCDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpDataMCDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpDataMCDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpDataMCDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtBBUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtBBUp,0.0,theTree.metphi_JetPileUpPtBBUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtBBUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtBBUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtBBUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtBBDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtBBDown,0.0,theTree.metphi_JetPileUpPtBBDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtBBDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtBBDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtBBDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtEC1UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtEC1Up,0.0,theTree.metphi_JetPileUpPtEC1Up,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtEC1Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtEC1Up
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtEC1Up
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtEC1DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtEC1Down,0.0,theTree.metphi_JetPileUpPtEC1Down,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtEC1Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtEC1Down
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtEC1Down
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtEC2UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtEC2Up,0.0,theTree.metphi_JetPileUpPtEC2Up,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtEC2Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtEC2Up
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtEC2Up
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtEC2DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtEC2Down,0.0,theTree.metphi_JetPileUpPtEC2Down,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtEC2Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtEC2Down
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtEC2Down
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtHFUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtHFUp,0.0,theTree.metphi_JetPileUpPtHFUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtHFUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtHFUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtHFUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtHFDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtHFDown,0.0,theTree.metphi_JetPileUpPtHFDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtHFDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtHFDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtHFDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtRefUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtRefUp,0.0,theTree.metphi_JetPileUpPtRefUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtRefUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtRefUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtRefUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetPileUpPtRefDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetPileUpPtRefDown,0.0,theTree.metphi_JetPileUpPtRefDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetPileUpPtRefDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetPileUpPtRefDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetPileUpPtRefDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetTimePtEtaUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetTimePtEtaUp,0.0,theTree.metphi_JetTimePtEtaUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetTimePtEtaUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetTimePtEtaUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetTimePtEtaUp
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateJetTimePtEtaDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetTimePtEtaDown,0.0,theTree.metphi_JetTimePtEtaDown,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetTimePtEtaDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetTimePtEtaDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetTimePtEtaDown
    
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

