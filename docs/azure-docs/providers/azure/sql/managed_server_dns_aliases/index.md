---
title: managed_server_dns_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_server_dns_aliases
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
<tr><td><b>Name</b></td><td><code>managed_server_dns_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_server_dns_aliases</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedServerDnsAliases_Get` | `SELECT` | `dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a server DNS alias. |
| `ManagedServerDnsAliases_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed server DNS aliases for a managed server. |
| `ManagedServerDnsAliases_CreateOrUpdate` | `INSERT` | `dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId` | Creates a managed server DNS alias. |
| `ManagedServerDnsAliases_Delete` | `DELETE` | `dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes the managed server DNS alias with the given name. |
| `ManagedServerDnsAliases_Acquire` | `EXEC` | `dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId, data__oldManagedServerDnsAliasResourceId` | Acquires managed server DNS alias from another managed server. |
