---
title: network_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connections
  - dev_center
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
<tr><td><b>Name</b></td><td><code>network_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.network_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets a network connection resource |
| `list_by_resource_group` | `SELECT` |  | Lists network connections in a resource group |
| `list_by_subscription` | `SELECT` |  | Lists network connections in a subscription |
| `create_or_update` | `INSERT` |  | Creates or updates a Network Connections resource |
| `delete` | `DELETE` |  | Deletes a Network Connections resource |
| `_list_by_resource_group` | `EXEC` |  | Lists network connections in a resource group |
| `_list_by_subscription` | `EXEC` |  | Lists network connections in a subscription |
| `run_health_checks` | `EXEC` | `networkConnectionName, resourceGroupName, subscriptionId` | Triggers a new health check run. The execution and health check result can be tracked via the network Connection health check details |
| `update` | `EXEC` |  | Partially updates a Network Connection |
