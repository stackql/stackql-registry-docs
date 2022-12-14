---
title: clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - clouds
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.clouds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource Type |
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | Gets or sets the location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clouds_Get` | `SELECT` | `cloudName, resourceGroupName, subscriptionId` | Implements Cloud GET method. |
| `Clouds_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of Clouds in a resource group. |
| `Clouds_ListBySubscription` | `SELECT` | `subscriptionId` | List of Clouds in a subscription. |
| `Clouds_CreateOrUpdate` | `INSERT` | `cloudName, resourceGroupName, subscriptionId, data__extendedLocation, data__location, data__properties` | Onboards the ScVmm fabric cloud as an Azure cloud resource. |
| `Clouds_Delete` | `DELETE` | `cloudName, resourceGroupName, subscriptionId` | Deregisters the ScVmm fabric cloud from Azure. |
| `Clouds_Update` | `EXEC` | `cloudName, resourceGroupName, subscriptionId` | Updates the Clouds resource. |
