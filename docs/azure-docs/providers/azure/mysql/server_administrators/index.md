---
title: server_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - server_administrators
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
<tr><td><b>Name</b></td><td><code>server_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.server_administrators</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerAdministrators_List` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Returns a list of server Administrators. |
| `ServerAdministrators_CreateOrUpdate` | `INSERT` | `resourceGroupName, serverName, subscriptionId` | Creates or update active directory administrator on an existing server. The update action will overwrite the existing administrator. |
| `ServerAdministrators_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes server active directory administrator. |
| `ServerAdministrators_Get` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets information about a AAD server administrator. |
