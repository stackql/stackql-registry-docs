---
title: management_group_network_manager_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_network_manager_connections
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
<tr><td><b>Name</b></td><td><code>management_group_network_manager_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.management_group_network_manager_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Information about the network manager connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagementGroupNetworkManagerConnections_Get` | `SELECT` |  | Get a specified connection created by this management group. |
| `ManagementGroupNetworkManagerConnections_List` | `SELECT` | `managementGroupId` | List all network manager connections created by this management group. |
| `ManagementGroupNetworkManagerConnections_CreateOrUpdate` | `INSERT` |  | Create a network manager connection on this management group. |
| `ManagementGroupNetworkManagerConnections_Delete` | `DELETE` |  | Delete specified pending connection created by this management group. |
