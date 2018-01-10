#!/bin/zsh

python validate.py --model_path=fcn_with_maskedconv_pascal_1_99.pkl --dataset=pascal
python validate.py --model_path=fcn_with_maskedconv2_pascal_1_99.pkl --dataset=pascal
python validate.py --model_path=fcn_with_maskedconv3_pascal_1_99.pkl --dataset=pascal
