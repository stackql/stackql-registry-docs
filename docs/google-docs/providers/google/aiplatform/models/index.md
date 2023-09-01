---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - aiplatform
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the Model. |
| `description` | `string` | The description of the Model. |
| `pipelineJob` | `string` | Optional. This field is populated if the model is produced by a pipeline job. |
| `artifactUri` | `string` | Immutable. The path to the directory containing the Model artifact and any of its supporting files. Not present for AutoML Models or Large Models. |
| `supportedExportFormats` | `array` | Output only. The formats in which this Model may be exported. If empty, this Model is not available for export. |
| `metadataArtifact` | `string` | Output only. The resource name of the Artifact that was created in MetadataStore when creating the Model. The Artifact resource name pattern is `projects/&#123;project&#125;/locations/&#123;location&#125;/metadataStores/&#123;metadata_store&#125;/artifacts/&#123;artifact&#125;`. |
| `trainingPipeline` | `string` | Output only. The resource name of the TrainingPipeline that uploaded this Model, if any. |
| `supportedDeploymentResourcesTypes` | `array` | Output only. When this Model is deployed, its prediction resources are described by the `prediction_resources` field of the Endpoint.deployed_models object. Because not all Models support all resource configuration types, the configuration types this Model supports are listed here. If no configuration types are listed, the Model cannot be deployed to an Endpoint and does not support online predictions (PredictionService.Predict or PredictionService.Explain). Such a Model can serve predictions by using a BatchPredictionJob, if it has at least one entry each in supported_input_storage_formats and supported_output_storage_formats. |
| `predictSchemata` | `object` | Contains the schemata used in Model's predictions and explanations via PredictionService.Predict, PredictionService.Explain and BatchPredictionJob. |
| `explanationSpec` | `object` | Specification of Model explanation. |
| `metadataSchemaUri` | `string` | Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Model, that is specific to it. Unset if the Model does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). AutoML Models always have this field populated by Vertex AI, if no additional metadata is needed, this field is set to an empty string. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |
| `displayName` | `string` | Required. The display name of the Model. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| `versionUpdateTime` | `string` | Output only. Timestamp when this version was most recently updated. |
| `versionId` | `string` | Output only. Immutable. The version ID of the model. A new version is committed when a new model version is uploaded or trained under an existing model id. It is an auto-incrementing decimal number in string representation. |
| `versionDescription` | `string` | The description of this version. |
| `modelSourceInfo` | `object` | Detail description of the source information of the model. |
| `supportedOutputStorageFormats` | `array` | Output only. The formats this Model supports in BatchPredictionJob.output_config. If both PredictSchemata.instance_schema_uri and PredictSchemata.prediction_schema_uri exist, the predictions are returned together with their instances. In other words, the prediction has the original instance data first, followed by the actual prediction content (as per the schema). The possible formats are: * `jsonl` The JSON Lines format, where each prediction is a single line. Uses GcsDestination. * `csv` The CSV format, where each prediction is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsDestination. * `bigquery` Each prediction is a single row in a BigQuery table, uses BigQueryDestination . If this Model doesn't support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain. |
| `versionAliases` | `array` | User provided version aliases so that a model version can be referenced via alias (i.e. `projects/&#123;project&#125;/locations/&#123;location&#125;/models/&#123;model_id&#125;@&#123;version_alias&#125;` instead of auto-generated version id (i.e. `projects/&#123;project&#125;/locations/&#123;location&#125;/models/&#123;model_id&#125;@&#123;version_id&#125;)`. The format is a-z&#123;0,126&#125;[a-z0-9] to distinguish from version_id. A default version alias will be created for the first version of the model, and there must be exactly one default version alias for a model. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `createTime` | `string` | Output only. Timestamp when this Model was uploaded into Vertex AI. |
| `supportedInputStorageFormats` | `array` | Output only. The formats this Model supports in BatchPredictionJob.input_config. If PredictSchemata.instance_schema_uri exists, the instances should be given as per that schema. The possible formats are: * `jsonl` The JSON Lines format, where each instance is a single line. Uses GcsSource. * `csv` The CSV format, where each instance is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsSource. * `tf-record` The TFRecord format, where each instance is a single record in tfrecord syntax. Uses GcsSource. * `tf-record-gzip` Similar to `tf-record`, but the file is gzipped. Uses GcsSource. * `bigquery` Each instance is a single row in BigQuery. Uses BigQuerySource. * `file-list` Each line of the file is the location of an instance to process, uses `gcs_source` field of the InputConfig object. If this Model doesn't support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain. |
| `deployedModels` | `array` | Output only. The pointers to DeployedModels created from this Model. Note that Model could have been deployed to Endpoints in different Locations. |
| `metadata` | `any` | Immutable. An additional information about the Model; the schema of the metadata can be found in metadata_schema. Unset if the Model does not have any additional information. |
| `labels` | `object` | The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `containerSpec` | `object` | Specification of a container for serving predictions. Some fields in this message correspond to fields in the [Kubernetes Container v1 core specification](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#container-v1-core). |
| `updateTime` | `string` | Output only. Timestamp when this Model was most recently updated. |
| `versionCreateTime` | `string` | Output only. Timestamp when this version was created. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `originalModelInfo` | `object` | Contains information about the original Model if this Model is a copy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, modelsId, projectsId` | Gets a Model. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Models in a Location. |
| `delete` | `DELETE` | `locationsId, modelsId, projectsId` | Deletes a Model. A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Models in a Location. |
| `copy` | `EXEC` | `locationsId, projectsId` | Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible. |
| `export` | `EXEC` | `locationsId, modelsId, projectsId` | Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format. |
| `merge_version_aliases` | `EXEC` | `locationsId, modelsId, projectsId` | Merges a set of aliases for a Model version. |
| `patch` | `EXEC` | `locationsId, modelsId, projectsId` | Updates a Model. |
| `predict` | `EXEC` | `locationsId, modelsId, projectsId, publishersId` | Perform an online prediction. |
| `raw_predict` | `EXEC` | `locationsId, modelsId, projectsId, publishersId` | Perform an online prediction with an arbitrary HTTP payload. The response includes the following HTTP headers: * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. |
| `server_streaming_predict` | `EXEC` | `locationsId, modelsId, projectsId, publishersId` | Perform a server-side streaming online prediction request for Vertex LLM streaming. |
| `upload` | `EXEC` | `locationsId, projectsId` | Uploads a Model artifact into Vertex AI. |
