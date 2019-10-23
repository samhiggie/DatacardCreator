import ROOT

class Uncertainty():
    def __init__(self):
        self.name = ''
        self.uncertaintyNames = []        
        self.uncertaintyModifications = {}
        self.eventDictionaryModifications = {}
        #create a dictionary of dictionaries with histograms for the uncertainties
        #takes a list of all the considered analysis categories.
    def CreateAllHistograms(self,sample,analysisCategories):
        self.histograms={}
        for analysisCategory in analysisCategories:
            dictionaryOfHistograms={}
            for name in self.uncertaintyNames:
                newClonedHisto = analysisCategory.templateHistogram.Clone()
                newClonedHisto.SetNameTitle(sample.name+"_"+name,sample.name+"_"+name)
                dictionaryOfHistograms[name] = newClonedHisto
            self.histograms[analysisCategory.name]=dictionaryOfHistograms
    def ProcessAllHistograms(self,analysisCategories,theTree,nominalEventDictionary):
        for category in analysisCategories:
            for name in self.uncertaintyNames:
                uncertaintyDictionary = self.eventDictionaryModifications[name](theTree,nominalEventDictionary)
                if category.IsInCategory(category,uncertaintyDictionary):
                    self.histograms[category.name][name].Fill(uncertaintyDictionary.eventDictionary[category.reconstructionVariable],uncertaintyDictionary.eventDictionary[category.rollingVariable],uncertaintyDictionary.Weight)
