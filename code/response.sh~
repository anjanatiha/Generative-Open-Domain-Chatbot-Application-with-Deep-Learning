#!/bin/bash

source ~/tensorflow/bin/activate 

nmt="$PWD/nmt"
out_dir="$PWD/inout/output/nmt_model"

inference_input_file="$PWD/inout/output/nmt_model/my_infer_file.vi"
inference_output_file="$PWD/inout/output/nmt_model/output_infer"

cd $nmt
python -m nmt.nmt \
    --out_dir=$out_dir \
    --inference_input_file=$inference_input_file \
    --inference_output_file=$inference_output_file
