from Samples.SampleDefinition import Sample

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

DataSample = Sample()
DataSample.name = 'data_obs'
DataSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
DataSample.files = ['Data.root']
DataSample.uncertainties = []
DataSample.eventDictionaryInstance = MuTauEventDictionary
DataSample.CreateEventWeight = DataSample.CreateEventWeight_Standard
