#!/bin/bash
source ./model-list.sh
#MODELS=(tung-algo)
for MODEL in "${MODELS[@]}"; do
    rm -fr services/${MODEL}
done;
