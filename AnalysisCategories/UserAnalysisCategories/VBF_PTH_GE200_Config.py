import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInVBFHighCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary["Njets"] >= 2.0
            and theEventDictionary.eventDictionary['mjj'] > 350.0
            and theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['HiggsPt'] >= 200.0
    ):
        return True
    else:
        return False
    return False

VBFHigh = AnalysisCategoryDef.AnalysisCategory()
VBFHigh.name = 'mt_vbf_PTH_GE_200'
VBFHigh.IsInCategory = IsInVBFHighCategory
VBFHigh.rollingVariable = 'mjj'
VBFHigh.rollingBins = [350.0,700.0,1200.0,10000.0]
VBFHigh.reconstructionVariable = 'M_sv'
VBFHigh.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
