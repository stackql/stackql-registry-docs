---
title: auto_scale_vcores
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scale_vcores
  - powerbi_dedicated
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
<tr><td><b>Name</b></td><td><code>auto_scale_vcores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_dedicated.auto_scale_vcores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the PowerBI Dedicated resource. |
| `name` | `string` | The name of the PowerBI Dedicated resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
| `type` | `string` | The type of the PowerBI Dedicated resource. |
| `location` | `string` | Location of the PowerBI Dedicated resource. |
| `properties` | `object` | Properties of an auto scale v-core resource. |
| `sku` | `object` | Represents the SKU name and Azure pricing tier for auto scale v-core resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AutoScaleVCores_Get` | `SELECT` | `resourceGroupName, subscriptionId, vcoreName` | Gets details about the specified auto scale v-core. |
| `AutoScaleVCores_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the auto scale v-cores for the given resource group. |
| `AutoScaleVCores_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the auto scale v-cores for the given subscription. |
| `AutoScaleVCores_Create` | `INSERT` | `resourceGroupName, subscriptionId, vcoreName, data__sku` | Provisions the specified auto scale v-core based on the configuration specified in the request. |
| `AutoScaleVCores_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vcoreName` | Deletes the specified auto scale v-core. |
| `AutoScaleVCores_Update` | `EXEC` | `resourceGroupName, subscriptionId, vcoreName` | Updates the current state of the specified auto scale v-core. |
