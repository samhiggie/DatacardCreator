from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES import JESUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VVSample = Sample()
VVSample.name = 'VVL'
VVSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
VVSample.files = ['WW.root',
                  'ZZ.root',
                  'WZ.root',
                  'EWKZLL.root',
                  'EWKZNuNu.root',
                  'ST_t_top.root',
                  'ST_t_antitop.root',
                  'ST_tW_top.root',
                  'ST_tW_antitop.root']
VVSample.definition = 'gen_match_2 < 5'
VVSample.uncertainties = [
    TESUncertainty(),
    JESUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
]
VVSample.eventDictionaryInstance = MuTauEventDictionary
VVSample.CreateEventWeight = VVSample.CreateEventWeight_Standard
