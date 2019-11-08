#!/usr/bin/bash
cmsenv
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/jetFakes_Splits/jetFakes2Config.py --OutputFileName "$1"_jetFakes2.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/jetFakes_Splits/jetFakes3Config.py --OutputFileName "$1"_jetFakes3.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/jetFakes_Splits/jetFakes4Config.py --OutputFileName "$1"_jetFakes4.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/jetFakes_Splits/jetFakes5Config.py --OutputFileName "$1"_jetFakes5.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/jetFakes_Splits/jetFakes6Config.py --OutputFileName "$1"_jetFakes6.root"
tmux select-layout even-vertical

python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/$1/jetFakes_Splits/jetFakes1Config.py --OutputFileName $1_jetFakes1.root
