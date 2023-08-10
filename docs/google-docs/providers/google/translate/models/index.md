---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - translate
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
<tr><td><b>Id</b></td><td><code>google.translate.models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the model, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/models/&#123;model_id&#125;` |
| `trainExampleCount` | `integer` | Output only. Number of examples (sentence pairs) used to train the model. |
| `validateExampleCount` | `integer` | Output only. Number of examples (sentence pairs) used to validate the model. |
| `dataset` | `string` | The dataset from which the model is trained, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;` |
| `displayName` | `string` | The name of the model to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| `updateTime` | `string` | Output only. Timestamp when this model was last updated. |
| `targetLanguageCode` | `string` | Output only. The BCP-47 language code of the target language. |
| `testExampleCount` | `integer` | Output only. Number of examples (sentence pairs) used to test the model. |
| `createTime` | `string` | Output only. Timestamp when the model resource was created, which is also when the training started. |
| `sourceLanguageCode` | `string` | Output only. The BCP-47 language code of the source language. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_models_get` | `SELECT` | `locationsId, modelsId, projectsId` | Gets a model. |
| `projects_locations_models_list` | `SELECT` | `locationsId, projectsId` | Lists models. |
| `projects_locations_models_create` | `INSERT` | `locationsId, projectsId` | Creates a Model. |
| `projects_locations_models_delete` | `DELETE` | `locationsId, modelsId, projectsId` | Deletes a model. |
| `_projects_locations_models_list` | `EXEC` | `locationsId, projectsId` | Lists models. |
