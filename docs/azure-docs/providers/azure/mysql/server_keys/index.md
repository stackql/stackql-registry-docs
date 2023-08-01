---
title: server_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - server_keys
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
<tr><td><b>Name</b></td><td><code>server_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.server_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of encryption protector used to protect the key. |
| `properties` | `object` | Properties for a key execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerKeys_Get` | `SELECT` | `keyName, resourceGroupName, serverName, subscriptionId` | Gets a MySQL Server key. |
| `ServerKeys_List` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of  Server keys. |
| `ServerKeys_CreateOrUpdate` | `INSERT` | `keyName, resourceGroupName, serverName, subscriptionId` | Creates or updates a MySQL Server key. |
| `ServerKeys_Delete` | `DELETE` | `keyName, resourceGroupName, serverName, subscriptionId` | Deletes the MySQL Server key with the given name. |
