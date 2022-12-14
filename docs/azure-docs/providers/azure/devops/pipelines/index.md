---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - devops
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
<tr><td><b>Id</b></td><td><code>azure.devops.pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
| `properties` | `object` | Custom properties of a Pipeline. |
| `tags` | `object` | Resource Tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pipelines_Get` | `SELECT` | `pipelineName, resourceGroupName, subscriptionId` | Gets an existing Azure Pipeline. |
| `Pipelines_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Azure Pipelines under the specified resource group. |
| `Pipelines_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all Azure Pipelines under the specified subscription. |
| `Pipelines_CreateOrUpdate` | `INSERT` | `pipelineName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an Azure Pipeline. |
| `Pipelines_Delete` | `DELETE` | `pipelineName, resourceGroupName, subscriptionId` | Deletes an Azure Pipeline. |
| `Pipelines_Update` | `EXEC` | `pipelineName, resourceGroupName, subscriptionId` | Updates the properties of an Azure Pipeline. Currently, only tags can be updated. |
