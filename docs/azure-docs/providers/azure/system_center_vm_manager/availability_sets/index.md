---
title: availability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets
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
<tr><td><b>Name</b></td><td><code>availability_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.availability_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource Type |
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AvailabilitySets_Get` | `SELECT` | `availabilitySetName, resourceGroupName, subscriptionId` | Implements AvailabilitySet GET method. |
| `AvailabilitySets_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of AvailabilitySets in a resource group. |
| `AvailabilitySets_ListBySubscription` | `SELECT` | `subscriptionId` | List of AvailabilitySets in a subscription. |
| `AvailabilitySets_CreateOrUpdate` | `INSERT` | `availabilitySetName, resourceGroupName, subscriptionId` | Onboards the ScVmm availability set as an Azure resource. |
| `AvailabilitySets_Delete` | `DELETE` | `availabilitySetName, resourceGroupName, subscriptionId` | Deregisters the ScVmm availability set from Azure. |
| `AvailabilitySets_Update` | `EXEC` | `availabilitySetName, resourceGroupName, subscriptionId` | Updates the AvailabilitySets resource. |
