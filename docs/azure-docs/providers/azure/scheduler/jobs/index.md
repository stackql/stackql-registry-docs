---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - scheduler
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scheduler.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the job resource identifier. |
| <CopyableCode code="name" /> | `string` | Gets the job resource name. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Gets the job resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Gets a job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, jobCollectionName, resourceGroupName, subscriptionId" /> | Lists all jobs under the specified job collection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Provisions a new job or updates an existing job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Deletes a job. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Patches an existing job. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Runs a job. |
