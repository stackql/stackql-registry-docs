---
title: issue_models
hide_title: false
hide_table_of_contents: false
keywords:
  - issue_models
  - contactcenterinsights
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
<tr><td><b>Name</b></td><td><code>issue_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.issue_models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the issue model. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/issueModels/&#123;issue_model&#125; |
| `updateTime` | `string` | Output only. The most recent time at which the issue model was updated. |
| `createTime` | `string` | Output only. The time at which this issue model was created. |
| `state` | `string` | Output only. State of the model. |
| `displayName` | `string` | The representative name for the issue model. |
| `inputDataConfig` | `object` | Configs for the input data used to create the issue model. |
| `languageCode` | `string` | Language of the model. |
| `modelType` | `string` | Type of the model. |
| `trainingStats` | `object` | Aggregated statistics about an issue model. |
| `issueCount` | `string` | Output only. Number of issues in this issue model. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `issueModelsId, locationsId, projectsId` | Gets an issue model. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists issue models. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates an issue model. |
| `delete` | `DELETE` | `issueModelsId, locationsId, projectsId` | Deletes an issue model. |
| `calculate_issue_model_stats` | `EXEC` | `issueModelsId, locationsId, projectsId` | Gets an issue model's statistics. |
| `deploy` | `EXEC` | `issueModelsId, locationsId, projectsId` | Deploys an issue model. Returns an error if a model is already deployed. An issue model can only be used in analysis after it has been deployed. |
| `patch` | `EXEC` | `issueModelsId, locationsId, projectsId` | Updates an issue model. |
| `undeploy` | `EXEC` | `issueModelsId, locationsId, projectsId` | Undeploys an issue model. An issue model can not be used in analysis after it has been undeployed. |
