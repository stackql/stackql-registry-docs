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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>model</code> resource or lists <code>models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the Model. |
| <CopyableCode code="description" /> | `string` | The description of the Model. |
| <CopyableCode code="artifactUri" /> | `string` | Immutable. The path to the directory containing the Model artifact and any of its supporting files. Not required for AutoML Models. |
| <CopyableCode code="baseModelSource" /> | `object` | User input field to specify the base model source. Currently it only supports specifing the Model Garden models and Genie models. |
| <CopyableCode code="containerSpec" /> | `object` | Specification of a container for serving predictions. Some fields in this message correspond to fields in the [Kubernetes Container v1 core specification](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#container-v1-core). |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Model was uploaded into Vertex AI. |
| <CopyableCode code="dataStats" /> | `object` | Stats of data used for train or evaluate the Model. |
| <CopyableCode code="deployedModels" /> | `array` | Output only. The pointers to DeployedModels created from this Model. Note that Model could have been deployed to Endpoints in different Locations. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the Model. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="explanationSpec" /> | `object` | Specification of Model explanation. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="metadata" /> | `any` | Immutable. An additional information about the Model; the schema of the metadata can be found in metadata_schema. Unset if the Model does not have any additional information. |
| <CopyableCode code="metadataArtifact" /> | `string` | Output only. The resource name of the Artifact that was created in MetadataStore when creating the Model. The Artifact resource name pattern is `projects/{project}/locations/{location}/metadataStores/{metadata_store}/artifacts/{artifact}`. |
| <CopyableCode code="metadataSchemaUri" /> | `string` | Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Model, that is specific to it. Unset if the Model does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). AutoML Models always have this field populated by Vertex AI, if no additional metadata is needed, this field is set to an empty string. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |
| <CopyableCode code="modelSourceInfo" /> | `object` | Detail description of the source information of the model. |
| <CopyableCode code="originalModelInfo" /> | `object` | Contains information about the original Model if this Model is a copy. |
| <CopyableCode code="pipelineJob" /> | `string` | Optional. This field is populated if the model is produced by a pipeline job. |
| <CopyableCode code="predictSchemata" /> | `object` | Contains the schemata used in Model's predictions and explanations via PredictionService.Predict, PredictionService.Explain and BatchPredictionJob. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="supportedDeploymentResourcesTypes" /> | `array` | Output only. When this Model is deployed, its prediction resources are described by the `prediction_resources` field of the Endpoint.deployed_models object. Because not all Models support all resource configuration types, the configuration types this Model supports are listed here. If no configuration types are listed, the Model cannot be deployed to an Endpoint and does not support online predictions (PredictionService.Predict or PredictionService.Explain). Such a Model can serve predictions by using a BatchPredictionJob, if it has at least one entry each in supported_input_storage_formats and supported_output_storage_formats. |
| <CopyableCode code="supportedExportFormats" /> | `array` | Output only. The formats in which this Model may be exported. If empty, this Model is not available for export. |
| <CopyableCode code="supportedInputStorageFormats" /> | `array` | Output only. The formats this Model supports in BatchPredictionJob.input_config. If PredictSchemata.instance_schema_uri exists, the instances should be given as per that schema. The possible formats are: * `jsonl` The JSON Lines format, where each instance is a single line. Uses GcsSource. * `csv` The CSV format, where each instance is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsSource. * `tf-record` The TFRecord format, where each instance is a single record in tfrecord syntax. Uses GcsSource. * `tf-record-gzip` Similar to `tf-record`, but the file is gzipped. Uses GcsSource. * `bigquery` Each instance is a single row in BigQuery. Uses BigQuerySource. * `file-list` Each line of the file is the location of an instance to process, uses `gcs_source` field of the InputConfig object. If this Model doesn't support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain. |
| <CopyableCode code="supportedOutputStorageFormats" /> | `array` | Output only. The formats this Model supports in BatchPredictionJob.output_config. If both PredictSchemata.instance_schema_uri and PredictSchemata.prediction_schema_uri exist, the predictions are returned together with their instances. In other words, the prediction has the original instance data first, followed by the actual prediction content (as per the schema). The possible formats are: * `jsonl` The JSON Lines format, where each prediction is a single line. Uses GcsDestination. * `csv` The CSV format, where each prediction is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsDestination. * `bigquery` Each prediction is a single row in a BigQuery table, uses BigQueryDestination . If this Model doesn't support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain. |
| <CopyableCode code="trainingPipeline" /> | `string` | Output only. The resource name of the TrainingPipeline that uploaded this Model, if any. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Model was most recently updated. |
| <CopyableCode code="versionAliases" /> | `array` | User provided version aliases so that a model version can be referenced via alias (i.e. `projects/{project}/locations/{location}/models/{model_id}@{version_alias}` instead of auto-generated version id (i.e. `projects/{project}/locations/{location}/models/{model_id}@{version_id})`. The format is a-z{0,126}[a-z0-9] to distinguish from version_id. A default version alias will be created for the first version of the model, and there must be exactly one default version alias for a model. |
| <CopyableCode code="versionCreateTime" /> | `string` | Output only. Timestamp when this version was created. |
| <CopyableCode code="versionDescription" /> | `string` | The description of this version. |
| <CopyableCode code="versionId" /> | `string` | Output only. Immutable. The version ID of the model. A new version is committed when a new model version is uploaded or trained under an existing model id. It is an auto-incrementing decimal number in string representation. |
| <CopyableCode code="versionUpdateTime" /> | `string` | Output only. Timestamp when this version was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Gets a Model. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Models in a Location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Deletes a Model. A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Updates a Model. |
| <CopyableCode code="compute_tokens" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Return a list of tokens based on the input text. |
| <CopyableCode code="copy" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible. |
| <CopyableCode code="count_tokens" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Perform a token counting. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format. |
| <CopyableCode code="generate_content" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Generate content with multimodal inputs. |
| <CopyableCode code="merge_version_aliases" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Merges a set of aliases for a Model version. |
| <CopyableCode code="predict" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Perform an online prediction. |
| <CopyableCode code="raw_predict" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Perform an online prediction with an arbitrary HTTP payload. The response includes the following HTTP headers: * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. |
| <CopyableCode code="server_streaming_predict" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Perform a server-side streaming online prediction request for Vertex LLM streaming. |
| <CopyableCode code="stream_generate_content" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Generate content with multimodal inputs with streaming support. |
| <CopyableCode code="stream_raw_predict" /> | `EXEC` | <CopyableCode code="locationsId, modelsId, projectsId, publishersId" /> | Perform a streaming online prediction with an arbitrary HTTP payload. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Uploads a Model artifact into Vertex AI. |

## `SELECT` examples

Lists Models in a Location.

```sql
SELECT
name,
description,
artifactUri,
baseModelSource,
containerSpec,
createTime,
dataStats,
deployedModels,
displayName,
encryptionSpec,
etag,
explanationSpec,
labels,
metadata,
metadataArtifact,
metadataSchemaUri,
modelSourceInfo,
originalModelInfo,
pipelineJob,
predictSchemata,
satisfiesPzi,
satisfiesPzs,
supportedDeploymentResourcesTypes,
supportedExportFormats,
supportedInputStorageFormats,
supportedOutputStorageFormats,
trainingPipeline,
updateTime,
versionAliases,
versionCreateTime,
versionDescription,
versionId,
versionUpdateTime
FROM google.aiplatform.models
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a model only if the necessary resources are available.

```sql
UPDATE google.aiplatform.models
SET 
dataStats = '{{ dataStats }}',
supportedDeploymentResourcesTypes = '{{ supportedDeploymentResourcesTypes }}',
versionId = '{{ versionId }}',
createTime = '{{ createTime }}',
satisfiesPzi = true|false,
containerSpec = '{{ containerSpec }}',
versionAliases = '{{ versionAliases }}',
deployedModels = '{{ deployedModels }}',
baseModelSource = '{{ baseModelSource }}',
versionCreateTime = '{{ versionCreateTime }}',
etag = '{{ etag }}',
predictSchemata = '{{ predictSchemata }}',
modelSourceInfo = '{{ modelSourceInfo }}',
supportedOutputStorageFormats = '{{ supportedOutputStorageFormats }}',
metadata = '{{ metadata }}',
metadataSchemaUri = '{{ metadataSchemaUri }}',
supportedExportFormats = '{{ supportedExportFormats }}',
artifactUri = '{{ artifactUri }}',
supportedInputStorageFormats = '{{ supportedInputStorageFormats }}',
explanationSpec = '{{ explanationSpec }}',
satisfiesPzs = true|false,
versionUpdateTime = '{{ versionUpdateTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
trainingPipeline = '{{ trainingPipeline }}',
labels = '{{ labels }}',
versionDescription = '{{ versionDescription }}',
metadataArtifact = '{{ metadataArtifact }}',
pipelineJob = '{{ pipelineJob }}',
displayName = '{{ displayName }}',
encryptionSpec = '{{ encryptionSpec }}',
name = '{{ name }}',
originalModelInfo = '{{ originalModelInfo }}'
WHERE 
locationsId = '{{ locationsId }}'
AND modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified model resource.

```sql
DELETE FROM google.aiplatform.models
WHERE locationsId = '{{ locationsId }}'
AND modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```
