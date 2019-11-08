import ROOT
import argparse
from AnalysisCategories.AnalysisCategoryDef import AnalysisCategory
from tqdm import tqdm
from Samples.SampleDefinition import Sample
import Utilities.RecursiveLoader
import Utilities.HistogramUnroller

def LoadAnalysisCategory(analysisCategoryFile,theLoader):
    theAnalysisConfigModule = theLoader.LoadFromDirectoryPath(analysisCategoryFile)
    for item in dir(theAnalysisConfigModule):
        theAnalysisConfig = getattr(theAnalysisConfigModule,item)
        if isinstance(theAnalysisConfig,AnalysisCategory):
            return theAnalysisConfig

def LoadSample(sampleFile,theLoader):
    theSampleConfigModule = theLoader.LoadFromDirectoryPath(sampleFile)
    for item in dir(theSampleConfigModule):
        theSampleConfig = getattr(theSampleConfigModule,item)
        if isinstance(theSampleConfig,Sample):
            return theSampleConfig

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a datacard using user defined samples and analysis categories")
    parser.add_argument('--AnalysisConfigFiles',nargs="+",help="Specify the analysis category configurations",required=True)
    parser.add_argument('--SampleConfigFiles',nargs="+",help="Specify the sample configuration files",required=True)
    parser.add_argument('--OutputFileName',nargs="?",help="Name the output file.",default="NewDatacard.root")

    args = parser.parse_args()

    theLoader = Utilities.RecursiveLoader.RecursiveLoader()
    theUnroller = Utilities.HistogramUnroller.HistogramUnroller()

    analysisCategories = []
    #let's retrieve the anlaysis categories.
    for analysisConfigFile in args.AnalysisConfigFiles:
        analysisCategories.append(LoadAnalysisCategory(analysisConfigFile,theLoader))

    #we need to create all the template histograms
    for analysisCategory in analysisCategories:
        analysisCategory.CreateTemplateHistogram()        

    outputSamples = []
    for sampleFile in args.SampleConfigFiles:
        outputSamples.append(LoadSample(sampleFile,theLoader))

    #ths should be where the magic happens and all our histograms get filled.
    for outputSample in outputSamples:
        print("Processing sample: "+outputSample.name)
        outputSample.InitializeSample()
        outputSample.InitializeAllHistograms(analysisCategories)
        #some debug
        #numEntries = outputSample.chain.GetEntries()
        #if outputSample.name == 'embedded':
        #    numEntries = 100000
        if outputSample.startEntry != None:
            chainStart = outputSample.startEntry
        else:
            chainStart = 0
        if outputSample.endEntry != None:
            if outputSample.endEntry < outputSample.chain.GetEntries():
                chainEnd = outputSample.endEntry
            else:
                chainEnd = outputSample.chain.GetEntries()
        else:
            chainEnd = outputSample.chain.GetEntries()
        for i in tqdm(range(chainStart,chainEnd)):
            outputSample.chain.GetEntry(i)
            outputSample.ProcessEvent(outputSample.chain,analysisCategories)
    #we should now be done with all of our samples, all histograms filled.
    #let's get them, unroll them, and store them away.
    #start with making the directories we're going to want.
    outputFile = ROOT.TFile(args.OutputFileName,"RECREATE")    
    directories = {}    
    for analysisCategory in analysisCategories:
        directories[analysisCategory.name] = outputFile.mkdir(analysisCategory.name)
    #now for each sample get the complete dictionary of histograms
    completeHistogramDictionary = {}
    for analysisCategory in analysisCategories:
        completeHistogramDictionary[analysisCategory.name] = {}
    for outputSample in outputSamples:
        theSampleHistograms = outputSample.GetAllHistograms()
        #once we have that, loop over the analysis categories and unroll each of the contained lists
        for analysisCategory in analysisCategories:
            theSampleHistograms[analysisCategory.name] = theUnroller.UnrollHistogramDictionary(theSampleHistograms[analysisCategory.name])
            for histogram in theSampleHistograms[analysisCategory.name]:
                completeHistogramDictionary[analysisCategory.name][histogram] = theSampleHistograms[analysisCategory.name][histogram]

    #Okay, now we unrolled all our histograms and combined them, 
    #if we have any final things to do (addition/subtraction) let's do them now
    for outputSample in outputSamples:    
        for analysisCategory in analysisCategories:
            #let's first see if the outputSample has any final actions it would like taken
            #before any of the histograms get written out.
            try:
                outputSample.EndAction(completeHistogramDictionary,analysisCategory)
            except AttributeError:
                pass
    #now let's write
    for analysisCategory in analysisCategories:
        directories[analysisCategory.name].cd()
        for histogram in completeHistogramDictionary[analysisCategory.name]:
            completeHistogramDictionary[analysisCategory.name][histogram].Write()
    
            
        
