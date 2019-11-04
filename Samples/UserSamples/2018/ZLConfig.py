from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.ZPT import ZPTUncertainty
from Samples.Uncertainties.UserUncertainties.ZLShape import ZLShapeUncertainty
from Samples.Uncertainties.UserUncertainties.JES import JESUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

DYLSample = Sample()
DYLSample.name = 'ZL'
DYLSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
DYLSample.files = ['DY.root']
DYLSample.definition = 'gen_match_2 < 5'
DYLSample.uncertainties = [
    TESUncertainty(),
    ZPTUncertainty(),
    JESUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    ZLShapeUncertainty(),
]
DYLSample.eventDictionaryInstance = MuTauEventDictionary
DYLSample.CreateEventWeight = DYLSample.CreateEventWeight_Standard
