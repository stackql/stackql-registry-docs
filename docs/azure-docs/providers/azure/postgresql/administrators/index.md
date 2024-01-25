---
title: administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - administrators
  - postgresql
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
<tr><td><b>Name</b></td><td><code>administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.administrators</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `objectId, resourceGroupName, serverName, subscriptionId` | Gets information about a server. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the AAD administrators for a given server. |
| `create` | `INSERT` | `objectId, resourceGroupName, serverName, subscriptionId` | Creates a new server. |
| `delete` | `DELETE` | `objectId, resourceGroupName, serverName, subscriptionId` | Deletes an Active Directory Administrator associated with the server. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | List all the AAD administrators for a given server. |
