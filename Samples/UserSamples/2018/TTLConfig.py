from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES import JESUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TTbarShape import TTbarShape

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

TTLSample = Sample()
TTLSample.name = 'TTL'
TTLSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
TTLSample.files = ['TTTo2L2Nu.root','TTToHadronic.root','TTToSemiLeptonic.root']
TTLSample.definition = 'gen_match_2 < 5'
TTLSample.uncertainties = [
    TESUncertainty(),
    JESUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    TTbarShape(),
]
TTLSample.eventDictionaryInstance = MuTauEventDictionary
TTLSample.CreateEventWeight = TTLSample.CreateEventWeight_Standard
