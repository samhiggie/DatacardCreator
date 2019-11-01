import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInZeroJetLowCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] == 0
            and theEventDictionary.eventDictionary['HiggsPt'] <= 10.0
            and theEventDictionary.eventDictionary['HiggsPt'] > 0.0
    ):
        return True
    else:
        return False
    return False
    
ZeroJetLow = AnalysisCategoryDef.AnalysisCategory()
ZeroJetLow.name = 'mt_0jet_PTH_0_10'
ZeroJetLow.IsInCategory = IsInZeroJetLowCategory
ZeroJetLow.rollingVariable  = 'TauPt'
ZeroJetLow.rollingBins = [30.0,40.0,50.0,10000.0]
ZeroJetLow.reconstructionVariable='MVis'
ZeroJetLow.reconstructionBins=[50.0,60.0,70.0,80.0,90.0,100.0,110.0,120.0,130.0,140.0,150.0,9000.0]
