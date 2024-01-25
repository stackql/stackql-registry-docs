---
title: server_dns_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - server_dns_aliases
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
<tr><td><b>Name</b></td><td><code>server_dns_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_dns_aliases</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dnsAliasName, resourceGroupName, serverName, subscriptionId` | Gets a server DNS alias. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server DNS aliases for a server. |
| `create_or_update` | `INSERT` | `dnsAliasName, resourceGroupName, serverName, subscriptionId` | Creates a server DNS alias. |
| `delete` | `DELETE` | `dnsAliasName, resourceGroupName, serverName, subscriptionId` | Deletes the server DNS alias with the given name. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server DNS aliases for a server. |
| `acquire` | `EXEC` | `dnsAliasName, resourceGroupName, serverName, subscriptionId, data__oldServerDnsAliasId` | Acquires server DNS alias from another server. |
