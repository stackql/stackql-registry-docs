---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
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
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.firewall_rules</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Gets information about a server firewall rule. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the firewall rules in a given server. |
| `create_or_update` | `INSERT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId, data__properties` | Creates a new firewall rule or updates an existing firewall rule. |
| `delete` | `DELETE` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Deletes a firewall rule. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | List all the firewall rules in a given server. |
