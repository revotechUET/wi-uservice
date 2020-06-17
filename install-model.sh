#!/bin/bash
 
MODEL=$1
MODELNAME=$2
MODEL_FILENAME=$3
UPDATE=$4

CLI_JAR=./openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar
OCLASSPATH=./wi-generators/generators/wipm/target/wipm-openapi-generator-1.0.0.jar:$CLI_JAR
MAINCLASS=org.openapitools.codegen.OpenAPIGenerator

SPEC=./model-specs/$MODEL/spec.yaml
OUTDIR=./services/$MODEL
java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR

SEDCMD='s/"#\/definitions\/"/"#\/definitions\/'$MODELNAME'"/g'
sed -i $SEDCMD ./services/$MODEL/src/specs/openapi.yaml

if [[ ""$UPDATE == "1" ]]; then
    echo "my code ==> gen code " $UPDATE
    cp ./model-specs/$MODEL/${MODELNAME}_Estimator.py services/$MODEL/src/ml_models/models
else
    echo "gen code ==> my code -- " $UPDATE
    #cp -n services/$MODEL/src/ml_models/models/${MODELNAME}_Estimator.py ./model-specs/$MODEL
    cp ./model-specs/$MODEL/${MODEL_FILENAME}_estimator.py services/$MODEL/src/ml_models/models
    mkdir services/$MODEL/static
    touch services/$MODEL/static/donot.remove
fi

if [ -f ./model-specs/$MODEL/model_options.py ]; then
    cp ./model-specs/$MODEL/model_options.py services/$MODEL/src/ml_models
else 
    echo "SINGLE_STEP_PIPELINE = False" > services/$MODEL/src/ml_models/model_options.py
fi