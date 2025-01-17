from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES import JESUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VVSample = Sample()
VVSample.name = 'VVT'
VVSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
VVSample.files = ['WW.root',
                  'ZZ.root',
                  'WZ.root']
VVSample.definition = '(gen_match_1 == 1 || gen_match_1 == 2) && gen_match_2 == 5'
VVSample.uncertainties = [
    TESUncertainty(),
    JESUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
]
VVSample.eventDictionaryInstance = MuTauEventDictionary
VVSample.CreateEventWeight = VVSample.CreateEventWeight_Standard
