---
title: i_pv6_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - i_pv6_firewall_rules
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
<tr><td><b>Name</b></td><td><code>i_pv6_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.i_pv6_firewall_rules</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IPv6FirewallRules_Get` | `SELECT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Gets an IPv6 firewall rule. |
| `IPv6FirewallRules_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of IPv6 firewall rules. |
| `IPv6FirewallRules_CreateOrUpdate` | `INSERT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Creates or updates an IPv6 firewall rule. |
| `IPv6FirewallRules_Delete` | `DELETE` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Deletes an IPv6 firewall rule. |
