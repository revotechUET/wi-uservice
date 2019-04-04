package wi.gen.ml;

import wi.gen.ml.CreateOperation;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.PathItem;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.media.Schema;
import org.openapitools.codegen.*;
import org.openapitools.codegen.CodegenOperation;
import org.openapitools.codegen.serializer.SerializerUtils;
import io.swagger.models.properties.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.*;
import java.io.File;

public class WipmGenerator extends DefaultCodegen implements CodegenConfig {
  private static final Logger LOGGER = LoggerFactory.getLogger(WipmGenerator.class);

  // source folder where to write the files
  protected String sourceFolder = "src";
  protected String apiVersion = "1.0.0";

  /**
   * Configures the type of generator.
   * 
   * @return  the CodegenType for this generator
   * @see     org.openapitools.codegen.CodegenType
   */
  public CodegenType getTag() {
    return CodegenType.SERVER;
  }

  /**
   * Configures a friendly name for the generator.  This will be used by the generator
   * to select the library with the -g flag.
   * 
   * @return the friendly name for the generator
   */
  public String getName() {
    return "wipm";
  }

  /**
   * Returns human-friendly help for the generator.  Provide the consumer with help
   * tips, parameters here
   * 
   * @return A string value for the help message
   */
  public String getHelp() {
    return "Generates a wipm server library.";
  }

  public WipmGenerator() {
    super();

    languageSpecificPrimitives.clear();
    languageSpecificPrimitives.add("int");
    languageSpecificPrimitives.add("float");
    languageSpecificPrimitives.add("List");
    languageSpecificPrimitives.add("Dict");
    languageSpecificPrimitives.add("bool");
    languageSpecificPrimitives.add("str");
    languageSpecificPrimitives.add("datetime");
    languageSpecificPrimitives.add("date");
    languageSpecificPrimitives.add("file");
    languageSpecificPrimitives.add("object");

    typeMapping.clear();
    typeMapping.put("integer", "int");
    typeMapping.put("float", "float");
    typeMapping.put("number", "float");
    typeMapping.put("long", "int");
    typeMapping.put("double", "float");
    typeMapping.put("array", "List");
    typeMapping.put("map", "Dict");
    typeMapping.put("boolean", "bool");
    typeMapping.put("string", "str");
    typeMapping.put("date", "date");
    typeMapping.put("DateTime", "datetime");
    typeMapping.put("object", "object");
    typeMapping.put("file", "file");
    typeMapping.put("UUID", "str");

    // set the output folder here
    outputFolder = "generated-code/wipm";

    /**
     * Models.  You can write model files using the modelTemplateFiles map.
     * if you want to create one template for file, you can do so here.
     * for multiple files for model, just put another entry in the `modelTemplateFiles` with
     * a different extension
     */
    modelTemplateFiles.put(
      "model.mustache", // the template to use
      ".py");       // the extension for each file to write

    /**
     * Api classes.  You can write classes for each Api file with the apiTemplateFiles map.
     * as with models, add multiple entries with different extensions for multiple files per
     * class
     */
    apiTemplateFiles.put(
      "api.mustache",   // the template to use
      ".py");       // the extension for each file to write

    /**
     * Template Location.  This is the location which templates will be read from.  The generator
     * will use the resource stream to attempt to read the templates.
     */
    templateDir = "wipm";

    additionalProperties.put("apiVersion", apiVersion);

    /**
     * Supporting Files.  You can write single files for the generator with the
     * entire object tree available.  If the input file has a suffix of `.mustache
     * it will be processed by the template engine.  Otherwise, it will be copied
     */
    supportingFiles.add(new SupportingFile("dev.config.py", "", "dev.config.py"));
    supportingFiles.add(new SupportingFile("prod.config.py", "", "prod.config.py"));
    supportingFiles.add(new SupportingFile("README.md", "", "README.md"));
    supportingFiles.add(new SupportingFile("requirements.txt", "", "requirements.txt"));
    supportingFiles.add(new SupportingFile("wsgi.py", "", "wsgi.py"));
    supportingFiles.add(new SupportingFile("model_helper.py", "src", "model_helper.py"));
    supportingFiles.add(new SupportingFile("config.py", "src", "config.py"));
    supportingFiles.add(new SupportingFile("data.py", "src/controllers", "data.py"));
    supportingFiles.add(new SupportingFile("controllers_init.py", "src/controllers", "__init__.py"));
    supportingFiles.add(new SupportingFile("ml_models_init.py", "src/ml_models", "__init__.py"));
    supportingFiles.add(new SupportingFile("result.py", "src/ml_models", "result.py"));
    supportingFiles.add(new SupportingFile("validator.py", "src/ml_models", "validator.py"));
    supportingFiles.add(new SupportingFile("__init__.py", "src", "__init__.py"));
    supportingFiles.add(new SupportingFile("openapi.mustache", "src/specs", "openapi.yaml"));
  }

  /**
   * Escapes a reserved word as defined in the `reservedWords` array. Handle escaping
   * those terms here.  This logic is only called if a variable matches the reserved words
   * 
   * @return the escaped term
   */
  @Override
  public String escapeReservedWord(String name) {
    return "_" + name;  // add an underscore to the name
  }

  // Don't replace `_` by Underscore 
  @Override
  public String toVarName(String name) {
    return name;
  }

  /**
   * Location to write model files.  You can use the modelPackage() as defined when the class is
   * instantiated
   */
  public String modelFileFolder() {
    return outputFolder + "/" + sourceFolder + "/ml_models/models";
  }

  /**
   * Location to write api files.  You can use the apiPackage() as defined when the class is
   * instantiated
   */
  @Override
  public String apiFileFolder() {
    return outputFolder + "/" + sourceFolder + "/controllers";
  }

  /**
   * override with any special text escaping logic to handle unsafe
   * characters so as to avoid code injection
   *
   * @param input String to be cleaned up
   * @return string with unsafe characters removed or escaped
   */
  @Override
  public String escapeUnsafeCharacters(String input) {
    //TODO: check that this logic is safe to escape unsafe characters to avoid code injection
    return input;
  }

  /**
   * Escape single and/or double quote to avoid code injection
   *
   * @param input String to be cleaned up
   * @return string with quotation mark removed or escaped
   */
  public String escapeQuotationMark(String input) {
    //TODO: check that this logic is safe to escape quotation mark to avoid code injection
    return input.replace("\"", "\\\"");
  }

  @Override
  public String toApiFilename(String name) {
    return "create";
  }
  
  /**
  * extract api and model from openAPI object 
  *
  * @param objs map of object
  **/
  public void extractApisAndModels(Map<String, Object> objs) {
    OpenAPI openAPI = (OpenAPI) objs.get("openAPI");

    /*
     * Convert properties components from Map to Set
     */
    Set<Map.Entry<String, Schema>> schemas = openAPI.getComponents().getSchemas().entrySet();
    Map<String, Set<Map.Entry<String, Schema>>> componentsSet = new HashMap<String, Set<Map.Entry<String, Schema>>>();
    for (Map.Entry<String, Schema> schema : schemas) {
      if (schema.getValue().getProperties() != null) {
        Set<Map.Entry<String, Schema>> schemaPropertiesSet = schema.getValue().getProperties().entrySet();
        componentsSet.put(schema.getKey(), schemaPropertiesSet);
      }
    }
    objs.put("components", (Object) componentsSet.entrySet());

    /*
     * Normalize paths object for render in mustache
     */
    Set<Map.Entry<String, PathItem>> paths = openAPI.getPaths().entrySet();
    Map<String, CreateOperation> pathsSet = new HashMap<String, CreateOperation>();
    for (Map.Entry<String, PathItem> path : paths) {
      Operation postOperation = path.getValue().getPost();
      CreateOperation ops = new CreateOperation();
      ops.setOperationId(postOperation.getOperationId());
      ops.setDescription(postOperation.getDescription());
      if (postOperation != null){
        String ref = postOperation.getRequestBody().get$ref();
        ops.setDefinitionRef(ref);
      }
      pathsSet.put(path.getKey(), ops);
    }
    objs.put("paths", (Object) pathsSet.entrySet());
  }

  @Override
  public Map<String, Object> postProcessSupportingFileData(Map<String, Object> objs) {
    extractApisAndModels(objs);
    return super.postProcessSupportingFileData(objs);
  }
  
}

