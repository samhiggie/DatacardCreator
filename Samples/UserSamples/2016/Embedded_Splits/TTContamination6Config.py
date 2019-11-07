from Samples.SampleDefinition import Sample

#
from Samples.Uncertainties.UserUncertainties.TTbarContamination import TTbarContaminationUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

TTContamination = Sample()
TTContamination.name = 'TTContamination'
TTContamination.path = '/data/aloeliger/SMHTT_Selected_2016_TTContamination/'
TTContamination.files = ['TT.root']
TTContamination.definition = ''
TTContamination.uncertainties = [
    TTbarContaminationUncertainty()
    ]
TTContamination.eventDictionaryInstance = MuTauEventDictionary
TTContamination.CreateEventWeight = TTContamination.CreateEventWeight_Standard
TTContamination.startEntry = 20000
TTContamination.startEntry = 24000
