#!/usr/bin/bash
cmsenv
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/ggH_Splits/ggH2Config.py --OutputFileName "$1"_ggH2.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/ggH_Splits/ggH3Config.py --OutputFileName "$1"_ggH3.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/ggH_Splits/ggH4Config.py --OutputFileName "$1"_ggH4.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/ggH_Splits/ggH5Config.py --OutputFileName "$1"_ggH5.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/ggH_Splits/ggH6Config.py --OutputFileName "$1"_ggH6.root"
tmux select-layout even-vertical

python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/$1/ggH_Splits/ggH1Config.py --OutputFileName $1_ggH1.root

