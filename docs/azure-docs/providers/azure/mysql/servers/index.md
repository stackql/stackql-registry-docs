---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - mysql
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Properties to configure Identity for Bring your Own Keys |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a server. |
| `sku` | `object` | Billing information related properties of a server. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets information about a server. |
| `list` | `SELECT` | `subscriptionId` | List all the servers in a given subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the servers in a given resource group. |
| `create` | `INSERT` | `resourceGroupName, serverName, subscriptionId` | Creates a new server or updates an existing server. The update action will overwrite the existing server. |
| `delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `_list` | `EXEC` | `subscriptionId` | List all the servers in a given subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the servers in a given resource group. |
| `failover` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Manual failover a server. |
| `reset_gtid` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Resets GTID on a server. |
| `restart` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Restarts a server. |
| `start` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Starts a server. |
| `stop` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Stops a server. |
| `update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
