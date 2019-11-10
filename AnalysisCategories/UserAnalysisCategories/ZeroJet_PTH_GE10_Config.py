import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInZeroJetHighCategory(theanalysisCategory,theEventDictionary):
    if (
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] == 0
            and theEventDictionary.eventDictionary['HiggsPt'] >= 10.0
    ):
        return True
    else:
        return False
    return False

ZeroJetHigh = AnalysisCategoryDef.AnalysisCategory()
ZeroJetHigh.name = 'mt_0jet_PTH_GE10'
ZeroJetHigh.IsInCategory = IsInZeroJetHighCategory
ZeroJetHigh.rollingVariable = 'TauPt'
ZeroJetHigh.rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
ZeroJetHigh.reconstructionVariable = 'M_sv'
ZeroJetHigh.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
