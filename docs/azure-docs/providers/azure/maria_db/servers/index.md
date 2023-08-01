---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - maria_db
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
<tr><td><b>Id</b></td><td><code>azure.maria_db.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sku` | `object` | Billing information related properties of a server. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Servers_Get` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets information about a server. |
| `Servers_List` | `SELECT` | `subscriptionId` | List all the servers in a given subscription. |
| `Servers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the servers in a given resource group. |
| `Servers_Create` | `INSERT` | `resourceGroupName, serverName, subscriptionId, data__location, data__properties` | Creates a new server or updates an existing server. The update action will overwrite the existing server. |
| `Servers_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `Servers_Restart` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Restarts a server. |
| `Servers_Start` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Starts a stopped server. |
| `Servers_Stop` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Stops a running server. |
| `Servers_Update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
