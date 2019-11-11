#!/usr/bin/bash
#our "easy" to calculate configs
#1 Data
#2 STL
#3 STT
#4 TTL
#5 TTT
#6 VVL
#7 VVT
#8 ZL
cmsenv 
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/STLConfig.py --OutputFileName "$1"_STL.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/STTConfig.py --OutputFileName "$1"_STT.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/TTLConfig.py --OutputFileName "$1"_TTL.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/TTTConfig.py --OutputFileName "$1"_TTT.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/VVLConfig.py --OutputFileName "$1"_VVL.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/VVTConfig.py --OutputFileName "$1"_VVT.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/ZLConfig.py --OutputFileName "$1"_ZL.root"
tmux select-layout even-vertical
python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/DataConfig.py --OutputFileName "$1"_Data.root
