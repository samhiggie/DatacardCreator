from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class MetRecoilUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'METRecoil'
        self.uncertaintyNames = [
            "CMS_htt_boson_reso_met_0jetUp",
            "CMS_htt_boson_reso_met_0jetDown",
            "CMS_htt_boson_scale_met_0jetUp",
            "CMS_htt_boson_scale_met_0jetDown",
            "CMS_htt_boson_reso_met_1jetUp",
            "CMS_htt_boson_reso_met_1jetDown",
            "CMS_htt_boson_scale_met_1jetUp",
            "CMS_htt_boson_scale_met_1jetDown",
            "CMS_htt_boson_reso_met_2jetUp",
            "CMS_htt_boson_reso_met_2jetDown",
            "CMS_htt_boson_scale_met_2jetUp",
            "CMS_htt_boson_scale_met_2jetDown",
            ]
        self.eventDictionaryModifications = {
            "CMS_htt_boson_reso_met_0jetUp":self.CreateReso0JetUpDictionary,
            "CMS_htt_boson_reso_met_0jetDown":self.CreateReso0JetDownDictionary,
            "CMS_htt_boson_scale_met_0jetUp":self.CreateResp0JetUpDictionary,
            "CMS_htt_boson_scale_met_0jetDown":self.CreateResp0JetDownDictionary,
            "CMS_htt_boson_reso_met_1jetUp":self.CreateReso1JetUpDictionary,
            "CMS_htt_boson_reso_met_1jetDown":self.CreateReso1JetDownDictionary,
            "CMS_htt_boson_scale_met_1jetUp":self.CreateResp1JetUpDictionary,
            "CMS_htt_boson_scale_met_1jetDown":self.CreateResp1JetDownDictionary,
            "CMS_htt_boson_reso_met_2jetUp":self.CreateReso2JetUpDictionary,
            "CMS_htt_boson_reso_met_2jetDown":self.CreateReso2JetDownDictionary,
            "CMS_htt_boson_scale_met_2jetUp":self.CreateResp2JetUpDictionary,
            "CMS_htt_boson_scale_met_2jetDown":self.CreateResp2JetDownDictionary,
        }
    def CreateReso0JetUpDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()        
        new_msv = theTree.m_sv
        if(theTree.njets == 0):
            metVector.SetPtEtaPhiM(theTree.met_resolutionUp,0.0,theTree.metphi_resolutionUp,0.0)
            new_msv = theTree.m_sv_ResolutionUp
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateReso0JetDownDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv        
        if(theTree.njets == 0):
            metVector.SetPtEtaPhiM(theTree.met_resolutionDown,0.0,theTree.metphi_resolutionDown,0.0)
            new_msv = theTree.m_sv_ResolutionDown
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
        
    def CreateResp0JetUpDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets == 0):
            metVector.SetPtEtaPhiM(theTree.met_responseUp,0.0,theTree.metphi_responseUp,0.0)
            new_msv = theTree.m_sv_ResponseUp
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateResp0JetDownDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets == 0):
            metVector.SetPtEtaPhiM(theTree.met_responseDown,0.0,theTree.metphi_responseDown,0.0)
            new_msv = theTree.m_sv_ResponseDown
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    #1 jet dictionary functions
    def CreateReso1JetUpDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        
        if(theTree.njets == 1):
            metVector.SetPtEtaPhiM(theTree.met_resolutionUp,0.0,theTree.metphi_resolutionUp,0.0)
            new_msv = theTree.m_sv_ResolutionUp
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateReso1JetDownDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets == 1):
            metVector.SetPtEtaPhiM(theTree.met_resolutionDown,0.0,theTree.metphi_resolutionDown,0.0)
            new_msv = theTree.m_sv_ResolutionUp
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
        
    def CreateResp1JetUpDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets == 1):
            metVector.SetPtEtaPhiM(theTree.met_responseUp,0.0,theTree.metphi_responseUp,0.0)
            new_msv = theTree.m_sv_ResponseUp
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateResp1JetDownDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets == 1):
            metVector.SetPtEtaPhiM(theTree.met_responseDown,0.0,theTree.metphi_responseDown,0.0)
            new_msv = theTree.m_sv_ResponseDown
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    # >= 2 jets dictionaries
    def CreateReso2JetUpDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets >= 2):
            metVector.SetPtEtaPhiM(theTree.met_resolutionUp,0.0,theTree.metphi_resolutionUp,0.0)
            new_msv = theTree.m_sv_ResolutionUp
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateReso2JetDownDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets >= 2):
            metVector.SetPtEtaPhiM(theTree.met_resolutionDown,0.0,theTree.metphi_resolutionDown,0.0)
            new_msv = theTree.m_sv_ResolutionDown
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
        
    def CreateResp2JetUpDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets >= 2):
            metVector.SetPtEtaPhiM(theTree.met_responseUp,0.0,theTree.metphi_responseUp,0.0)
            new_msv = theTree.m_sv_ResponseUp
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateResp2JetDownDictionary(self,theTree,nominalEventDictionary):
        metVector=ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if(theTree.njets >= 2):
            metVector.SetPtEtaPhiM(theTree.met_responseDown,0.0,theTree.metphi_responseDown,0.0)
            new_msv = theTree.m_sv_ResponseDown
        else:
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
