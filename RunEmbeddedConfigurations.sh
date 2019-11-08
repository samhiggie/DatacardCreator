#!/usr/bin/bash
cmsenv
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/Embedded_Splits/Embedded2Config.py Samples/UserSamples/"$1"/Embedded_Splits/TTContamination2Config.py --OutputFileName "$1"_Embedded2.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/Embedded_Splits/Embedded3Config.py Samples/UserSamples/"$1"/Embedded_Splits/TTContamination3Config.py --OutputFileName "$1"_Embedded3.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/Embedded_Splits/Embedded4Config.py Samples/UserSamples/"$1"/Embedded_Splits/TTContamination4Config.py --OutputFileName "$1"_Embedded4.root"
tmux select-layout even-vertical
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/Embedded_Splits/Embedded5Config.py Samples/UserSamples/"$1"/Embedded_Splits/TTContamination5Config.py --OutputFileName "$1"_Embedded5.root"
tmux split-window "eval \`scramv1 runtime -sh\` && python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/"$1"/Embedded_Splits/Embedded6Config.py Samples/UserSamples/"$1"/Embedded_Splits/TTContamination6Config.py --OutputFileName "$1"_Embedded6.root"
tmux select-layout even-vertical

python CreateDatacard.py --AnalysisConfigFiles AnalysisCategories/UserAnalysisCategories/*_Config.py --SampleConfigFiles Samples/UserSamples/$1/Embedded_Splits/Embedded1Config.py Samples/UserSamples/$1/Embedded_Splits/TTContamination1Config.py --OutputFileName $1_Embedded1.root

