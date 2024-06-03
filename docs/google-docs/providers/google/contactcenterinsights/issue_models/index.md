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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>issue_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.issue_models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the issue model. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/issueModels/&#123;issue_model&#125; |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this issue model was created. |
| <CopyableCode code="displayName" /> | `string` | The representative name for the issue model. |
| <CopyableCode code="inputDataConfig" /> | `object` | Configs for the input data used to create the issue model. |
| <CopyableCode code="issueCount" /> | `string` | Output only. Number of issues in this issue model. |
| <CopyableCode code="languageCode" /> | `string` | Language of the model. |
| <CopyableCode code="modelType" /> | `string` | Type of the model. |
| <CopyableCode code="state" /> | `string` | Output only. State of the model. |
| <CopyableCode code="trainingStats" /> | `object` | Aggregated statistics about an issue model. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time at which the issue model was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Gets an issue model. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists issue models. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an issue model. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Deletes an issue model. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Updates an issue model. |
| <CopyableCode code="calculate_issue_model_stats" /> | `EXEC` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Gets an issue model's statistics. |
| <CopyableCode code="deploy" /> | `EXEC` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Deploys an issue model. Returns an error if a model is already deployed. An issue model can only be used in analysis after it has been deployed. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Exports an issue model to the provided destination. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Imports an issue model from a Cloud Storage bucket. |
| <CopyableCode code="undeploy" /> | `EXEC` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Undeploys an issue model. An issue model can not be used in analysis after it has been undeployed. |
