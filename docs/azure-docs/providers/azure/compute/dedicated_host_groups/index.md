---
title: dedicated_host_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_host_groups
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
<tr><td><b>Name</b></td><td><code>dedicated_host_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.dedicated_host_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `zones` | `array` | Availability Zone to use for this host group. Only single zone is supported. The zone can be assigned only during creation. If not provided, the group supports all zones in the region. If provided, enforces each host in the group to be in the same zone. |
| `location` | `string` | Resource location |
| `properties` | `object` | Dedicated Host Group Properties. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DedicatedHostGroups_Get` | `SELECT` | `hostGroupName, resourceGroupName, subscriptionId` | Retrieves information about a dedicated host group. |
| `DedicatedHostGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the dedicated host groups in the specified resource group. Use the nextLink property in the response to get the next page of dedicated host groups. |
| `DedicatedHostGroups_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all of the dedicated host groups in the subscription. Use the nextLink property in the response to get the next page of dedicated host groups. |
| `DedicatedHostGroups_CreateOrUpdate` | `INSERT` | `hostGroupName, resourceGroupName, subscriptionId` | Create or update a dedicated host group. For details of Dedicated Host and Dedicated Host Groups please see [Dedicated Host Documentation] (https://go.microsoft.com/fwlink/?linkid=2082596) |
| `DedicatedHostGroups_Delete` | `DELETE` | `hostGroupName, resourceGroupName, subscriptionId` | Delete a dedicated host group. |
| `DedicatedHostGroups_Update` | `EXEC` | `hostGroupName, resourceGroupName, subscriptionId` | Update an dedicated host group. |
