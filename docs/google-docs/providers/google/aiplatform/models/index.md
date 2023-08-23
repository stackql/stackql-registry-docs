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
| `name` | `string` | Output only. The resource name of the PublisherModel. |
| `versionId` | `string` | Output only. Immutable. The version ID of the PublisherModel. A new version is committed when a new model version is uploaded under an existing model id. It is an auto-incrementing decimal number in string representation. |
| `frameworks` | `array` | Optional. Additional information about the model's Frameworks. |
| `launchStage` | `string` | Optional. Indicates the launch stage of the model. |
| `openSourceCategory` | `string` | Required. Indicates the open source category of the publisher model. |
| `predictSchemata` | `object` | Contains the schemata used in Model's predictions and explanations via PredictionService.Predict, PredictionService.Explain and BatchPredictionJob. |
| `publisherModelTemplate` | `string` | Optional. Output only. Immutable. Used to indicate this model has a publisher model and provide the template of the publisher model resource name. |
| `supportedActions` | `object` | Actions could take on this Publisher Model. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `modelsId, publishersId` | Gets a Model Garden publisher model. |
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
