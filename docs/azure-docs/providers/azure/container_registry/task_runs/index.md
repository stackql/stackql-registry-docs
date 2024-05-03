---
title: task_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - task_runs
  - container_registry
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
<tr><td><b>Name</b></td><td><code>task_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.task_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of task run. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Gets the detailed information for a given task run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the task runs for a specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Creates a task run for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Deletes a specified task run resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the task runs for a specified container registry. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Updates a task run with the specified parameters. |
