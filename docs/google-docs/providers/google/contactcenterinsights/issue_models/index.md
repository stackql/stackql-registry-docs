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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Immutable. The resource name of the issue model. Format: projects/{project}/locations/{location}/issueModels/{issue_model} |
| `inputDataConfig` | `object` | Configs for the input data used to create the issue model. |
| `state` | `string` | Output only. State of the model. |
| `trainingStats` | `object` | Aggregated statistics about an issue model. |
| `updateTime` | `string` | Output only. The most recent time at which the issue model was updated. |
| `createTime` | `string` | Output only. The time at which this issue model was created. |
| `displayName` | `string` | The representative name for the issue model. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_issueModels_get` | `SELECT` | `issueModelsId, locationsId, projectsId` | Gets an issue model. |
| `projects_locations_issueModels_list` | `SELECT` | `locationsId, projectsId` | Lists issue models. |
| `projects_locations_issueModels_create` | `INSERT` | `locationsId, projectsId` | Creates an issue model. |
| `projects_locations_issueModels_delete` | `DELETE` | `issueModelsId, locationsId, projectsId` | Deletes an issue model. |
| `projects_locations_issueModels_calculateIssueModelStats` | `EXEC` | `issueModelsId, locationsId, projectsId` | Gets an issue model's statistics. |
| `projects_locations_issueModels_deploy` | `EXEC` | `issueModelsId, locationsId, projectsId` | Deploys an issue model. Returns an error if a model is already deployed. An issue model can only be used in analysis after it has been deployed. |
| `projects_locations_issueModels_patch` | `EXEC` | `issueModelsId, locationsId, projectsId` | Updates an issue model. |
| `projects_locations_issueModels_undeploy` | `EXEC` | `issueModelsId, locationsId, projectsId` | Undeploys an issue model. An issue model can not be used in analysis after it has been undeployed. |
