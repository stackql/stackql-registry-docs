---
title: server_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - server_keys
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
<tr><td><b>Name</b></td><td><code>server_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties for a server key execution. |
| `kind` | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerKeys_Get` | `SELECT` | `keyName, resourceGroupName, serverName, subscriptionId` | Gets a server key. |
| `ServerKeys_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server keys. |
| `ServerKeys_CreateOrUpdate` | `INSERT` | `keyName, resourceGroupName, serverName, subscriptionId` | Creates or updates a server key. |
| `ServerKeys_Delete` | `DELETE` | `keyName, resourceGroupName, serverName, subscriptionId` | Deletes the server key with the given name. |
