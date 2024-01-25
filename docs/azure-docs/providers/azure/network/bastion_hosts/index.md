---
title: bastion_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_hosts
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
<tr><td><b>Name</b></td><td><code>bastion_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.bastion_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the Bastion Host. |
| `sku` | `object` | The sku of this Bastion Host. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bastionHostName, resourceGroupName, subscriptionId` | Gets the specified Bastion Host. |
| `list` | `SELECT` | `subscriptionId` | Lists all Bastion Hosts in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Bastion Hosts in a resource group. |
| `create_or_update` | `INSERT` | `bastionHostName, resourceGroupName, subscriptionId` | Creates or updates the specified Bastion Host. |
| `delete` | `DELETE` | `bastionHostName, resourceGroupName, subscriptionId` | Deletes the specified Bastion Host. |
| `_list` | `EXEC` | `subscriptionId` | Lists all Bastion Hosts in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Bastion Hosts in a resource group. |
| `bastion_hosts` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Returns the list of currently active sessions on the Bastion. |
