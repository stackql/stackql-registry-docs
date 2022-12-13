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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerDnsAliases_Get` | `SELECT` | `dnsAliasName, resourceGroupName, serverName, subscriptionId` | Gets a server DNS alias. |
| `ServerDnsAliases_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server DNS aliases for a server. |
| `ServerDnsAliases_CreateOrUpdate` | `INSERT` | `dnsAliasName, resourceGroupName, serverName, subscriptionId` | Creates a server DNS alias. |
| `ServerDnsAliases_Delete` | `DELETE` | `dnsAliasName, resourceGroupName, serverName, subscriptionId` | Deletes the server DNS alias with the given name. |
| `ServerDnsAliases_Acquire` | `EXEC` | `dnsAliasName, resourceGroupName, serverName, subscriptionId, data__oldServerDnsAliasId` | Acquires server DNS alias from another server. |
