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
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudResourceName, resourceGroupName, subscriptionId` | Implements Cloud GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List of Clouds in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List of Clouds in a subscription. |
| `create_or_update` | `INSERT` | `cloudResourceName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Onboards the ScVmm fabric cloud as an Azure cloud resource. |
| `delete` | `DELETE` | `cloudResourceName, resourceGroupName, subscriptionId` | Deregisters the ScVmm fabric cloud from Azure. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List of Clouds in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List of Clouds in a subscription. |
| `update` | `EXEC` | `cloudResourceName, resourceGroupName, subscriptionId` | Updates the Clouds resource. |
