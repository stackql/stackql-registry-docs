---
title: outbound_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_firewall_rules
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
<tr><td><b>Name</b></td><td><code>outbound_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.outbound_firewall_rules</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OutboundFirewallRules_Get` | `SELECT` | `outboundRuleFqdn, resourceGroupName, serverName, subscriptionId` | Gets an outbound firewall rule. |
| `OutboundFirewallRules_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets all outbound firewall rules on a server. |
| `OutboundFirewallRules_CreateOrUpdate` | `INSERT` | `outboundRuleFqdn, resourceGroupName, serverName, subscriptionId` | Create a outbound firewall rule with a given name. |
| `OutboundFirewallRules_Delete` | `DELETE` | `outboundRuleFqdn, resourceGroupName, serverName, subscriptionId` | Deletes a outbound firewall rule with a given name. |
