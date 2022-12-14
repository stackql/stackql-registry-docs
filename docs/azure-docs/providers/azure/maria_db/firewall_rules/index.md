---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - maria_db
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
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.firewall_rules</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallRules_Get` | `SELECT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Gets information about a server firewall rule. |
| `FirewallRules_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the firewall rules in a given server. |
| `FirewallRules_CreateOrUpdate` | `INSERT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId, data__properties` | Creates a new firewall rule or updates an existing firewall rule. |
| `FirewallRules_Delete` | `DELETE` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Deletes a server firewall rule. |
