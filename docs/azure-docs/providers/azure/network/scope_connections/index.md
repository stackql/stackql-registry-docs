---
title: scope_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_connections
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
<tr><td><b>Name</b></td><td><code>scope_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.scope_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Scope connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScopeConnections_Get` | `SELECT` |  | Get specified scope connection created by this Network Manager. |
| `ScopeConnections_List` | `SELECT` | `networkManagerName, resourceGroupName, subscriptionId` | List all scope connections created by this network manager. |
| `ScopeConnections_CreateOrUpdate` | `INSERT` |  | Creates or updates scope connection from Network Manager |
| `ScopeConnections_Delete` | `DELETE` |  | Delete the pending scope connection created by this network manager. |
