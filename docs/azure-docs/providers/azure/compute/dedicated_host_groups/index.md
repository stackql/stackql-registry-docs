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
| `location` | `string` | Resource location |
| `properties` | `object` | Dedicated Host Group Properties. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `zones` | `array` | Availability Zone to use for this host group. Only single zone is supported. The zone can be assigned only during creation. If not provided, the group supports all zones in the region. If provided, enforces each host in the group to be in the same zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hostGroupName, resourceGroupName, subscriptionId` | Retrieves information about a dedicated host group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the dedicated host groups in the specified resource group. Use the nextLink property in the response to get the next page of dedicated host groups. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all of the dedicated host groups in the subscription. Use the nextLink property in the response to get the next page of dedicated host groups. |
| `create_or_update` | `INSERT` | `hostGroupName, resourceGroupName, subscriptionId` | Create or update a dedicated host group. For details of Dedicated Host and Dedicated Host Groups please see [Dedicated Host Documentation] (https://go.microsoft.com/fwlink/?linkid=2082596) |
| `delete` | `DELETE` | `hostGroupName, resourceGroupName, subscriptionId` | Delete a dedicated host group. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the dedicated host groups in the specified resource group. Use the nextLink property in the response to get the next page of dedicated host groups. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all of the dedicated host groups in the subscription. Use the nextLink property in the response to get the next page of dedicated host groups. |
| `update` | `EXEC` | `hostGroupName, resourceGroupName, subscriptionId` | Update an dedicated host group. |
