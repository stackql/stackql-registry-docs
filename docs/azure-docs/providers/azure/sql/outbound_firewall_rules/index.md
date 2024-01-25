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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `outboundRuleFqdn, resourceGroupName, serverName, subscriptionId` | Gets an outbound firewall rule. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets all outbound firewall rules on a server. |
| `create_or_update` | `INSERT` | `outboundRuleFqdn, resourceGroupName, serverName, subscriptionId` | Create a outbound firewall rule with a given name. |
| `delete` | `DELETE` | `outboundRuleFqdn, resourceGroupName, serverName, subscriptionId` | Deletes a outbound firewall rule with a given name. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets all outbound firewall rules on a server. |
