import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInBoostedOneJetCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and (theEventDictionary.eventDictionary['Njets'] == 1.0 or (theEventDictionary.eventDictionary['Njets'] >= 2.0 and theEventDictionary.eventDictionary['mjj']<=350.0))
            and theEventDictionary.eventDictionary['Njets'] == 1.0
    ):
        return True
    else:
        return False
    return False

Boosted1J = AnalysisCategoryDef.AnalysisCategory()
Boosted1J.name = 'mt_boosted_1J'
Boosted1J.IsInCategory = IsInBoostedOneJetCategory
Boosted1J.rollingVariable = 'HiggsPt'
Boosted1J.rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
Boosted1J.reconstructionVariable = 'M_sv'
Boosted1J.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]

