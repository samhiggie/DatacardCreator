from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES import JESUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

STSample = Sample()
STSample.name = 'STL'
STSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
STSample.files = ['ST_t_top.root',
                  'ST_t_antitop.root',
                  'ST_tW_top.root',
                  'ST_tW_antitop.root']
STSample.definition = 'gen_match_2 < 5'
STSample.uncertainties = [
    TESUncertainty(),
    JESUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
]
STSample.eventDictionaryInstance = MuTauEventDictionary
STSample.CreateEventWeight = STSample.CreateEventWeight_Standard
