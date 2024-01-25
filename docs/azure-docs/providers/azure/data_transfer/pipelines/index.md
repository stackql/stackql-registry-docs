---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - data_transfer
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_transfer.pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of pipeline |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `pipelineName, resourceGroupName, subscriptionId` | Gets pipeline resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets pipelines in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets pipelines in a subscription. |
| `create_or_update` | `INSERT` | `pipelineName, resourceGroupName, subscriptionId, data__location` | Creates or updates the pipeline resource. |
| `delete` | `DELETE` | `pipelineName, resourceGroupName, subscriptionId` | Deletes the pipeline resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets pipelines in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets pipelines in a subscription. |
| `approve_connection` | `EXEC` | `pipelineName, resourceGroupName, subscriptionId, data__id` | Approves the specified connection in a pipeline. |
| `reject_connection` | `EXEC` | `pipelineName, resourceGroupName, subscriptionId, data__id` | Rejects the specified connection in a pipeline. |
| `update` | `EXEC` | `pipelineName, resourceGroupName, subscriptionId` | Updates the pipeline resource. |
