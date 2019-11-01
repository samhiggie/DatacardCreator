from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class FakeFactorUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'FF_Uncertainty'
        self.uncertaintyNames = [
            "CMS_rawFF_mt_qcd_0jet_unc1Up",
            "CMS_rawFF_mt_qcd_0jet_unc2Up",
            "CMS_rawFF_mt_qcd_1jet_unc1Up",
            "CMS_rawFF_mt_qcd_1jet_unc2Up",
            "CMS_rawFF_mt_w_0jet_unc1Up",
            "CMS_rawFF_mt_w_0jet_unc2Up",
            "CMS_rawFF_mt_w_1jet_unc1Up",
            "CMS_rawFF_mt_w_1jet_unc2Up",
            "CMS_rawFF_mt_tt_unc1Up",
            "CMS_rawFF_mt_tt_unc2Up",
            "CMS_FF_closure_mvis_mt_qcd_unc1Up",
            "CMS_FF_closure_mvis_mt_qcd_unc2Up",
            "CMS_FF_closure_mvis_mt_w_unc1Up",
            #"CMS_FF_closure_mvis_mt_w_unc2Up",
            "CMS_FF_closure_mvis_mt_tt_unc1Up",
            "CMS_FF_closure_mvis_mt_tt_unc2Up",
            "CMS_FF_closure_OSSS_mvis_mt_qcd_unc1Up",
            #"CMS_FF_closure_OSSS_mvis_mt_qcd_unc2Up",
            "CMS_FF_closure_mt_mt_w_unc1Up",
            "CMS_FF_closure_mt_mt_w_unc2Up",
            "CMS_rawFF_mt_qcd_0jet_unc1Down",
            "CMS_rawFF_mt_qcd_0jet_unc2Down",
            "CMS_rawFF_mt_qcd_1jet_unc1Down",
            "CMS_rawFF_mt_qcd_1jet_unc2Down",
            "CMS_rawFF_mt_w_0jet_unc1Down",
            "CMS_rawFF_mt_w_0jet_unc2Down",
            "CMS_rawFF_mt_w_1jet_unc1Down",
            "CMS_rawFF_mt_w_1jet_unc2Down",
            "CMS_rawFF_mt_tt_unc1Down",
            "CMS_rawFF_mt_tt_unc2Down",
            "CMS_FF_closure_mvis_mt_qcd_unc1Down",
            "CMS_FF_closure_mvis_mt_qcd_unc2Down",
            "CMS_FF_closure_mvis_mt_w_unc1Down",
            #"CMS_FF_closure_mvis_mt_w_unc2Down",
            "CMS_FF_closure_mvis_mt_tt_unc1Down",
            "CMS_FF_closure_mvis_mt_tt_unc2Down",
            "CMS_FF_closure_OSSS_mvis_mt_qcd_unc1Down",
            #"CMS_FF_closure_OSSS_mvis_mt_qcd_unc2Down",
            "CMS_FF_closure_mt_mt_w_unc1Down",
            "CMS_FF_closure_mt_mt_w_unc2Down"            
            ]
        self.eventDictionaryModifications = {
            "CMS_rawFF_mt_qcd_0jet_unc1Up":self.CreateRawQCD0JetUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_0jet_unc2Up":self.CreateRawQCD0JetUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc1Up":self.CreateRawQCD1JetUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc2Up":self.CreateRawQCD1JetUnc2UpDictionary,
            "CMS_rawFF_mt_w_0jet_unc1Up":self.CreateRawW0JetUnc1UpDictionary,
            "CMS_rawFF_mt_w_0jet_unc2Up":self.CreateRawW0JetUnc2UpDictionary,
            "CMS_rawFF_mt_w_1jet_unc1Up":self.CreateRawW1JetUnc1UpDictionary,
            "CMS_rawFF_mt_w_1jet_unc2Up":self.CreateRawW1JetUnc2UpDictionary,
            "CMS_rawFF_mt_tt_unc1Up":self.CreateRawTT0JetUnc1UpDictionary,
            "CMS_rawFF_mt_tt_unc2Up":self.CreateRawTT0JetUnc2UpDictionary,
            "CMS_FF_closure_mvis_mt_qcd_unc1Up":self.CreateMvisClosureQCDUnc1UpDictionary,
            "CMS_FF_closure_mvis_mt_qcd_unc2Up":self.CreateMvisClosureQCDUnc2UpDictionary,
            "CMS_FF_closure_mvis_mt_w_unc1Up":self.CreateMvisClosureWUnc1UpDictionary,
            #"CMS_FF_closure_mvis_mt_w_unc2Up":,
            "CMS_FF_closure_mvis_mt_tt_unc1Up":self.CreateMvisClosureTTUnc1UpDictionary,
            "CMS_FF_closure_mvis_mt_tt_unc2Up":self.CreateMvisClosureTTUnc2UpDictionary,
            "CMS_FF_closure_OSSS_mvis_mt_qcd_unc1Up":self.CreateOSSSClosureQCDUnc1UpDictionary,
            #"CMS_FF_closure_OSSS_mvis_mt_qcd_unc2Up":,
            "CMS_FF_closure_mt_mt_w_unc1Up":self.CreateMTClosureWUnc1UpDictionary,
            "CMS_FF_closure_mt_mt_w_unc2Up":self.CreateMTClosureWUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_0jet_unc1Down":self.CreateRawQCD0JetUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_0jet_unc2Down":self.CreateRawQCD0JetUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc1Down":self.CreateRawQCD1JetUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc2Down":self.CreateRawQCD1JetUnc2DownDictionary,
            "CMS_rawFF_mt_w_0jet_unc1Down":self.CreateRawW0JetUnc1DownDictionary,
            "CMS_rawFF_mt_w_0jet_unc2Down":self.CreateRawW0JetUnc2DownDictionary,
            "CMS_rawFF_mt_w_1jet_unc1Down":self.CreateRawW1JetUnc1DownDictionary,
            "CMS_rawFF_mt_w_1jet_unc2Down":self.CreateRawW1JetUnc2DownDictionary,
            "CMS_rawFF_mt_tt_unc1Down":self.CreateRawTT0JetUnc1DownDictionary,
            "CMS_rawFF_mt_tt_unc2Down":self.CreateRawTT0JetUnc2DownDictionary,
            "CMS_FF_closure_mvis_mt_qcd_unc1Down":self.CreateMvisClosureQCDUnc1DownDictionary,
            "CMS_FF_closure_mvis_mt_qcd_unc2Down":self.CreateMvisClosureQCDUnc2DownDictionary,
            "CMS_FF_closure_mvis_mt_w_unc1Down":self.CreateMvisClosureWUnc1DownDictionary,
            #"CMS_FF_closure_mvis_mt_w_unc2Down":,
            "CMS_FF_closure_mvis_mt_tt_unc1Down":self.CreateMvisClosureTTUnc1DownDictionary,
            "CMS_FF_closure_mvis_mt_tt_unc2Down":self.CreateMvisClosureTTUnc2DownDictionary,
            "CMS_FF_closure_OSSS_mvis_mt_qcd_unc1Down":self.CreateOSSSClosureQCDUnc1DownDictionary,
            #"CMS_FF_closure_OSSS_mvis_mt_qcd_unc2Down":,
            "CMS_FF_closure_mt_mt_w_unc1Down":self.CreateMTClosureWUnc1DownDictionary,
            "CMS_FF_closure_mt_mt_w_unc2Down":self.CreateMTClosureWUnc2DownDictionary
            }

        #QCD raw uncerts
    def CreateRawQCD0JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD0JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD0JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD0JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc2_down
        return modifiedEventDictionary
    #W raw uncerts
    def CreateRawW0JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc1_up
        return modifiedEventDictionary
    def CreateRawW0JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc1_down
        return modifiedEventDictionary
    def CreateRawW0JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc2_up
        return modifiedEventDictionary
    def CreateRawW0JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc2_down
        return modifiedEventDictionary
    def CreateRawW1JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc1_up
        return modifiedEventDictionary
    def CreateRawW1JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc1_down
        return modifiedEventDictionary
    def CreateRawW1JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc2_up
        return modifiedEventDictionary
    def CreateRawW1JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc2_down
        return modifiedEventDictionary
    #TTbar raw uncerts
    def CreateRawTT0JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc1_up
        return modifiedEventDictionary
    def CreateRawTT0JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc1_down
        return modifiedEventDictionary
    def CreateRawTT0JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc2_up
        return modifiedEventDictionary
    def CreateRawTT0JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc2_down
        return modifiedEventDictionary
        #QCD mvis closure
    def CreateMvisClosureQCDUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_unc1_up
        return modifiedEventDictionary
    def CreateMvisClosureQCDUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_unc1_down
        return modifiedEventDictionary
    def CreateMvisClosureQCDUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_unc2_up
        return modifiedEventDictionary
    def CreateMvisClosureQCDUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_unc2_down
        return modifiedEventDictionary
        #W mvis closure
    def CreateMvisClosureWUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_unc1_up
        return modifiedEventDictionary
    def CreateMvisClosureWUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_unc1_down
        return modifiedEventDictionary
        
        #ttbar mvis closure
    def CreateMvisClosureTTUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_tt_unc1_up
        return modifiedEventDictionary
    def CreateMvisClosureTTUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_tt_unc1_down
        return modifiedEventDictionary
    def CreateMvisClosureTTUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_tt_unc2_up
        return modifiedEventDictionary
    def CreateMvisClosureTTUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_tt_unc2_down
        return modifiedEventDictionary
        #W mt closure
    def CreateMTClosureWUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc1_up
        return modifiedEventDictionary
    def CreateMTClosureWUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc1_down
        return modifiedEventDictionary
    def CreateMTClosureWUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc2_up
        return modifiedEventDictionary
    def CreateMTClosureWUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc2_down
        return modifiedEventDictionary
        #qcd osss closure
    def CreateOSSSClosureQCDUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.osssclosure_qcd_unc1_up
        return modifiedEventDictionary
    def CreateOSSSClosureQCDUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.osssclosure_qcd_unc1_down
        return modifiedEventDictionary

