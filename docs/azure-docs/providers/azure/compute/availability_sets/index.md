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
| `AvailabilitySets_Get` | `SELECT` | `availabilitySetName, resourceGroupName, subscriptionId` | Retrieves information about an availability set. |
| `AvailabilitySets_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all availability sets in a resource group. |
| `AvailabilitySets_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all availability sets in a subscription. |
| `AvailabilitySets_CreateOrUpdate` | `INSERT` | `availabilitySetName, resourceGroupName, subscriptionId` | Create or update an availability set. |
| `AvailabilitySets_Delete` | `DELETE` | `availabilitySetName, resourceGroupName, subscriptionId` | Delete an availability set. |
| `AvailabilitySets_ListAvailableSizes` | `EXEC` | `availabilitySetName, resourceGroupName, subscriptionId` | Lists all available virtual machine sizes that can be used to create a new virtual machine in an existing availability set. |
| `AvailabilitySets_Update` | `EXEC` | `availabilitySetName, resourceGroupName, subscriptionId` | Update an availability set. |
