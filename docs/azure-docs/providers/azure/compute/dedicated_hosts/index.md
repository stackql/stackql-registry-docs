---
title: dedicated_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hosts
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
<tr><td><b>Name</b></td><td><code>dedicated_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.dedicated_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `properties` | `object` | Properties of the dedicated host. |
| `sku` | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DedicatedHosts_Get` | `SELECT` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Retrieves information about a dedicated host. |
| `DedicatedHosts_ListByHostGroup` | `SELECT` | `hostGroupName, resourceGroupName, subscriptionId` | Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts. |
| `DedicatedHosts_CreateOrUpdate` | `INSERT` | `hostGroupName, hostName, resourceGroupName, subscriptionId, data__sku` | Create or update a dedicated host . |
| `DedicatedHosts_Delete` | `DELETE` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Delete a dedicated host. |
| `DedicatedHosts_Restart` | `EXEC` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Restart the dedicated host. The operation will complete successfully once the dedicated host has restarted and is running. To determine the health of VMs deployed on the dedicated host after the restart check the Resource Health Center in the Azure Portal. Please refer to https://docs.microsoft.com/azure/service-health/resource-health-overview for more details. |
| `DedicatedHosts_Update` | `EXEC` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Update an dedicated host . |
