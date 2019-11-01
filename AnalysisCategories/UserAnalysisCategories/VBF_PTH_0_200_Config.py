import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInVBFLowCategory(theAnalysisCategory,theEventDictionary):
    if (
            theEventDictionary.eventDictionary['Njets'] >= 2.0
            and theEventDictionary.eventDictionary['mjj'] > 350.0
            and theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['HiggsPt'] < 200.0
            and theEventDictionary.eventDictionary['HiggsPt'] > 0.0
    ):
        return True
    else:
        return False
    return False
VBFLow = AnalysisCategoryDef.AnalysisCategory()
VBFLow.name = 'mt_vbf_PTH_0_200'
VBFLow.IsInCategory = IsInVBFLowCategory
VBFLow.rollingVariable = 'mjj'
VBFLow.rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
VBFLow.reconstructionVariable = 'M_sv'
VBFLow.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
