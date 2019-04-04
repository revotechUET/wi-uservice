#!/bin/bash
 
CLI_JAR=./openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar
OCLASSPATH=./wi-generators/generators/wipm/target/wipm-openapi-generator-1.0.0.jar:$CLI_JAR
MAINCLASS=org.openapitools.codegen.OpenAPIGenerator

if [[ $1 == huber ]]; then
    SPEC=./model-specs/huber.yaml
    OUTDIR=./services/huber
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/Huber"/g' ./services/huber/src/specs/openapi.yaml
    mkdir ./services/huber/static
elif [[ $1 == lasso ]]; then
    SPEC=./model-specs/lasso.yaml
    OUTDIR=./services/lasso
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/Lasso"/g' ./services/lasso/src/specs/openapi.yaml
    mkdir ./services/lasso/static
elif [[ $1 == linear_regression ]]; then
    SPEC=./model-specs/linear_regression.yaml
    OUTDIR=./services/linear_regression
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/LinearRegression"/g' ./services/linear_regression/src/specs/openapi.yaml
    mkdir ./services/linear_regression/static
elif [[ $1 == svm ]]; then
    SPEC=./model-specs/svm.yaml
    OUTDIR=./services/svm
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/SVM"/g' ./services/svm/src/specs/openapi.yaml
    mkdir ./services/svm/static
elif [[ $1 == xgboost ]]; then
    SPEC=./model-specs/xgboost.yaml
    OUTDIR=./services/xgboost
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/XGBoost"/g' ./services/xgboost/src/specs/openapi.yaml
    mkdir ./services/huber/static
elif [[ $1 == decision_tree ]]; then
    SPEC=./model-specs/decision_tree.yaml
    OUTDIR=./services/decision_tree
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/DecisionTree"/g' ./services/decision_tree/src/specs/openapi.yaml
    mkdir ./services/decision_tree/static
elif [[ $1 == neural_network ]]; then
    SPEC=./model-specs/neural_network.yaml
    OUTDIR=./services/neural_network
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/NeuralNetwork"/g' ./services/neural_network/src/specs/openapi.yaml
    mkdir ./services/neural_network/static
elif [[ $1 == random_forest ]]; then
    SPEC=./model-specs/random_forest.yaml
    OUTDIR=./services/random_forest
    java -cp $OCLASSPATH $MAINCLASS generate --skip-validate-spec -g wipm -i $SPEC -o $OUTDIR
    sed -i 's/"#\/definitions\/"/"#\/definitions\/RandomForest"/g' ./services/random_forest/src/specs/openapi.yaml
    mkdir ./services/random_forest/static
else
    echo Model not support
    exit
fi
