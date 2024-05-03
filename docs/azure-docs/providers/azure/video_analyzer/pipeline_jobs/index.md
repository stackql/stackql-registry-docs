---
title: pipeline_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_jobs
  - video_analyzer
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.pipeline_jobs" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Retrieves a specific pipeline job by name. If a pipeline job with that name has been previously created, the call will return the JSON representation of that instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves a list of all live pipelines that have been created, along with their JSON representations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Creates a new pipeline job or updates an existing one, with the given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Deletes a pipeline job with the given name. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves a list of all live pipelines that have been created, along with their JSON representations. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Cancels a pipeline job with the given name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Updates an existing pipeline job with the given name. Properties that can be updated include: description. |
