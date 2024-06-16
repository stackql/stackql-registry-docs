---
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.job_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Job definition properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets a Job Definition resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Job Definitions in a Project. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId, data__properties" /> | Creates or updates a Job Definition resource, which contains configuration for a single unit of managed data transfer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes a Job Definition resource. |
| <CopyableCode code="start_job" /> | `EXEC` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Creates a new Job Run resource for the specified Job Definition and passes it to the Agent for execution. |
| <CopyableCode code="stop_job" /> | `EXEC` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Requests the Agent of any active instance of this Job Definition to stop. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Updates properties for a Job Definition resource. Properties not specified in the request body will be unchanged. |
