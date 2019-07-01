# WIML services generator

## Requirements
* Java (maven)
* Python (pip)
* MongoDB

## Structure
```bash
wi-uservice/
├── README.md             // this file
├── clean.sh
├── generate.sh           // command lines to start generating services code
├── install-model.sh      // command lines to generate each services
├── install.py
├── model-list.sh         // list of model-services to generate
├── model-specs           // specification for each model-service
├── openapi-generator     // openapi codegen tools
├── pm2                   // configuration for deployment by PM2
├── services              // folder storing services
└── wi-generators         // generator and template for generating services.
```

## Usage
### Clone the repository from Github
Run the command
```bash
git clone https://github.com/tunghoang/wi-uservice.git
```
### Build generator tools.
Go to folder `openapi-generator` (which contains `pom.xml` file) and run command `mvn package`. Then go to folder `wi-generators/generators/wipm` (which contains `pom.xml` file) and run command `mvn package`.  
You may need to run bellow command to use `wipm` generator as an option for generating code.
```bash
java -cp wi-generators/generators/wipm/target/wipm-openapi-generator-1.0.0.jar:openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar org.openapitools.codegen.OpenAPIGenerator
```
Refer to <https://openapi-generator.tech/docs/customization.html> for more details.

### Specify specification
Specification and model files are in subfolders of `model-specs` folder. Each subfolders is used for a service. For example `decision_tree` subfolder.
```bash
decision_tree/
├── decision_tree_estimator.py    // machine learning model class
├── info.json                     // model name and filename
└── spec.yaml                     // shortened version of specification for service
```

### Specify list of services to generate
List of services to generate is in `model-list.sh`.

### Generate service
Run the command to generate services listed in `model-list.sh`.
```bash
$ ./generate.sh
```
Generated services are in `services` folder. Each services contains its own `README.md` which guide to run the services.

## Deployment with PM2
Configuration to deploy services with PM2 are specified in `pm2/ecosystem.config.js`.
Go to `pm2` folder and run the command to deploy services.
```bash
pm2 start ecosystem.config.js
```
Refer to <https://pm2.io/doc/en/runtime/overview/> for more details about dealing with PM2.

## Modify generator and template
Generator is in `WipmGenerator.java` file in `wi-uservice/wi-generators/generators/wipm/src/main/java/wi/gen/ml` folder.  
Template files are in `wi-generators/generators/wipm/src/main/resources/wipm`.

## Reference
OpenAPI Generator: <https://openapi-generator.tech>  
OpenAPI Specification: <https://swagger.io/specification/>