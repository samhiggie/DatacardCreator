from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.FakeFactorUncertainty import FakeFactorUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

FakeSample = Sample()
FakeSample.name = 'jetFakes'
FakeSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
FakeSample.files = ['Fake.root']
FakeSample.definition = ''
FakeSample.uncertainties = [
    FakeFactorUncertainty()
    ]
FakeSample.eventDictionaryInstance = MuTauEventDictionary
FakeSample.CreateEventWeight = FakeSample.CreateEventWeight_Fake
FakeSample.startEntry = 2250000
FakeSample.endEntry =  3000000
