from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES import JESUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

STSample = Sample()
STSample.name = 'STT'
STSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
STSample.files = ['ST_t_top.root',
                  'ST_t_antitop.root',
                  'ST_tW_top.root',
                  'ST_tW_antitop.root']
STSample.definition = '(gen_match_1 == 1 || gen_match_1 == 2) && gen_match_2 == 5'
STSample.uncertainties = [
    TESUncertainty(),
    JESUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
]
STSample.eventDictionaryInstance = MuTauEventDictionary
STSample.CreateEventWeight = STSample.CreateEventWeight_Standard
