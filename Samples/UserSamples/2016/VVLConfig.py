from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES import JESUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VVSample = Sample()
VVSample.name = 'VVL'
VVSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
VVSample.files = ['WW.root',
                  'ZZ.root',
                  'WZ.root']
VVSample.definition = 'gen_match_2 < 5'
VVSample.uncertainties = [
    TESUncertainty(),
    JESUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
]
VVSample.eventDictionaryInstance = MuTauEventDictionary
VVSample.CreateEventWeight = VVSample.CreateEventWeight_Standard
