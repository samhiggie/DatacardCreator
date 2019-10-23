#a quick class created for unrolling histograms.
import ROOT
from array import array

class HistogramUnroller():
    def __init__(self):
        pass
    #basic histogram unrolling function.
    def UnrollHistogram(self,histogram):
        nBinsX = histogram.GetNbinsX()
        nBinsY = histogram.GetNbinsY()
        nBins = nBinsX*nBinsY

        binArray = array('d',[i for i in range(nBins+1)])
        NewHisto = ROOT.TH1F(histogram.GetName(),
                             histogram.GetTitle(),
                             nBins,
                             binArray)
        for i in range(1,nBinsY+1):
            for j in range(1,nBinsX+1):
                NewHisto.SetBinContent(j+(i-1)*nBinsX,histogram.GetBinContent(j,i))
                NewHisto.SetBinError(j+(i-1)*nBinsX,histogram.GetBinError(j,i))
        return NewHisto
    
    #function for unrolling lists of histograms.
    def UnrollHistogramList(self,listOfHistograms):
        for i in range(len(listOfHistograms)):
            listOfHistograms[i] = self.UnrollHistogram(listOfHistograms[i])
        return listOfHistograms
