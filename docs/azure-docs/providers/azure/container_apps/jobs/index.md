---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - container_apps
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Container Apps Job resource specific properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Create or Update a Container Apps Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Delete a Container Apps Job. |
| <CopyableCode code="jobs" /> | `EXEC` | <CopyableCode code="jobExecutionName, jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="proxy_get" /> | `EXEC` | <CopyableCode code="apiName, jobName, resourceGroupName, subscriptionId" /> | Get the properties of a Container App Job. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="stop_execution" /> | `EXEC` | <CopyableCode code="jobExecutionName, jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="stop_multiple_executions" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Patches a Container Apps Job using JSON Merge Patch |
