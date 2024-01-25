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
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `kind` | `string` | Kind of sql server. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a server. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a server. |
| `list` | `SELECT` | `subscriptionId` | Gets a list of all servers in the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of servers in a resource groups. |
| `create_or_update` | `INSERT` | `resourceGroupName, serverName, subscriptionId, data__location` | Creates or updates a server. |
| `delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of all servers in the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of servers in a resource groups. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Determines whether a resource can be created with the specified name. |
| `import_database` | `EXEC` | `resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Imports a bacpac into a new database. |
| `refresh_status` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Refresh external governance enablement status. |
| `update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates a server. |
