---
title: ip_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_groups
  - network
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
<tr><td><b>Name</b></td><td><code>ip_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.ip_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The IpGroups property information. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IpGroups_Get` | `SELECT` | `ipGroupsName, resourceGroupName, subscriptionId` | Gets the specified ipGroups. |
| `IpGroups_List` | `SELECT` | `subscriptionId` | Gets all IpGroups in a subscription. |
| `IpGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all IpGroups in a resource group. |
| `IpGroups_CreateOrUpdate` | `INSERT` | `ipGroupsName, resourceGroupName, subscriptionId` | Creates or updates an ipGroups in a specified resource group. |
| `IpGroups_Delete` | `DELETE` | `ipGroupsName, resourceGroupName, subscriptionId` | Deletes the specified ipGroups. |
| `IpGroups_UpdateGroups` | `EXEC` | `ipGroupsName, resourceGroupName, subscriptionId` | Updates tags of an IpGroups resource. |
