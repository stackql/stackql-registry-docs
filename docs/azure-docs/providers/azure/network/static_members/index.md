---
title: static_members
hide_title: false
hide_table_of_contents: false
keywords:
  - static_members
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
<tr><td><b>Name</b></td><td><code>static_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.static_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of static member. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets the specified static member. |
| `list` | `SELECT` | `networkGroupName, networkManagerName, resourceGroupName, subscriptionId` | Lists the specified static member. |
| `create_or_update` | `INSERT` |  | Creates or updates a static member. |
| `delete` | `DELETE` |  | Deletes a static member. |
| `_list` | `EXEC` | `networkGroupName, networkManagerName, resourceGroupName, subscriptionId` | Lists the specified static member. |
