---
title: virtual_network_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_rules
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
<tr><td><b>Name</b></td><td><code>virtual_network_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.virtual_network_rules</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkRules_Get` | `SELECT` | `resourceGroupName, serverName, subscriptionId, virtualNetworkRuleName` | Gets a virtual network rule. |
| `VirtualNetworkRules_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of virtual network rules in a server. |
| `VirtualNetworkRules_CreateOrUpdate` | `INSERT` | `resourceGroupName, serverName, subscriptionId, virtualNetworkRuleName` | Creates or updates an existing virtual network rule. |
| `VirtualNetworkRules_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId, virtualNetworkRuleName` | Deletes the virtual network rule with the given name. |
