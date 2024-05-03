---
title: azure_monitor_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_monitor_workspaces
  - monitor
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
<tr><td><b>Name</b></td><td><code>azure_monitor_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.azure_monitor_workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource entity tag (ETag) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId" /> | Returns the specified Azure Monitor Workspace |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Monitor Workspaces in the specified resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Azure Monitor Workspaces in the specified subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates an Azure Monitor Workspace |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId" /> | Deletes an Azure Monitor Workspace |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Monitor Workspaces in the specified resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all Azure Monitor Workspaces in the specified subscription |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId" /> | Updates part of an Azure Monitor Workspace |
