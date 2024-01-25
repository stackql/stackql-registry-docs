---
title: availability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets
  - compute
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
<tr><td><b>Name</b></td><td><code>availability_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.availability_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | The instance view of a resource. |
| `sku` | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `availabilitySetName, resourceGroupName, subscriptionId` | Retrieves information about an availability set. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all availability sets in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all availability sets in a subscription. |
| `create_or_update` | `INSERT` | `availabilitySetName, resourceGroupName, subscriptionId` | Create or update an availability set. |
| `delete` | `DELETE` | `availabilitySetName, resourceGroupName, subscriptionId` | Delete an availability set. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all availability sets in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all availability sets in a subscription. |
| `update` | `EXEC` | `availabilitySetName, resourceGroupName, subscriptionId` | Update an availability set. |
