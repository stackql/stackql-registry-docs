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
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `availabilitySetResourceName, resourceGroupName, subscriptionId` | Implements AvailabilitySet GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List of AvailabilitySets in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List of AvailabilitySets in a subscription. |
| `create_or_update` | `INSERT` | `availabilitySetResourceName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Onboards the ScVmm availability set as an Azure resource. |
| `delete` | `DELETE` | `availabilitySetResourceName, resourceGroupName, subscriptionId` | Deregisters the ScVmm availability set from Azure. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List of AvailabilitySets in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List of AvailabilitySets in a subscription. |
| `update` | `EXEC` | `availabilitySetResourceName, resourceGroupName, subscriptionId` | Updates the AvailabilitySets resource. |
