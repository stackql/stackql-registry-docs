---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - sql
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
<tr><td><b>Id</b></td><td><code>azure.sql.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of sql server. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a server. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Servers_Get` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a server. |
| `Servers_List` | `SELECT` | `subscriptionId` | Gets a list of all servers in the subscription. |
| `Servers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of servers in a resource groups. |
| `Servers_CreateOrUpdate` | `INSERT` | `resourceGroupName, serverName, subscriptionId, data__location` | Creates or updates a server. |
| `Servers_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `Servers_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Determines whether a resource can be created with the specified name. |
| `Servers_ImportDatabase` | `EXEC` | `resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Imports a bacpac into a new database. |
| `Servers_Update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates a server. |
