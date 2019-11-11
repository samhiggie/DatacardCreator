#!/usr/bin/bash
#Non split signals are,
#1 VBF
#2 WH
#3 ZH
cmsenv
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/WHConfig.py  --OutputFileName "$1"_WH.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/ZHConfig.py  --OutputFileName "$1"_ZH.root"
tmux select-layout even-vertical
python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/VBFConfig.py  --OutputFileName $1_VBF.root
