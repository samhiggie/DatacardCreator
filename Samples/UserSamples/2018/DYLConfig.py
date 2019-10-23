from Samples.SampleDefinition import Sample
from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

DYLSample = Sample()
DYLSample.name = 'DY'
DYLSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
DYLSample.files = ['DY.root']
DYLSample.definition = 'gen_match_2 < 5'
DYLSample.uncertainties = [
    TESUncertainty()
]
DYLSample.eventDictionaryInstance = MuTauEventDictionary
DYLSample.CreateEventWeight = DYLSample.CreateEventWeight_Standard
