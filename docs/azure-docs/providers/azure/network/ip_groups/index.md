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
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The IpGroups property information. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ipGroupsName, resourceGroupName, subscriptionId` | Gets the specified ipGroups. |
| `list` | `SELECT` | `subscriptionId` | Gets all IpGroups in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all IpGroups in a resource group. |
| `create_or_update` | `INSERT` | `ipGroupsName, resourceGroupName, subscriptionId` | Creates or updates an ipGroups in a specified resource group. |
| `delete` | `DELETE` | `ipGroupsName, resourceGroupName, subscriptionId` | Deletes the specified ipGroups. |
| `_list` | `EXEC` | `subscriptionId` | Gets all IpGroups in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all IpGroups in a resource group. |
