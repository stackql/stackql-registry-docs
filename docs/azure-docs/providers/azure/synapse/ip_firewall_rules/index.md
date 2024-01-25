---
title: ip_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_firewall_rules
  - synapse
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
<tr><td><b>Name</b></td><td><code>ip_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.ip_firewall_rules</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, ruleName, subscriptionId, workspaceName` | Get a firewall rule |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns a list of firewall rules |
| `create_or_update` | `INSERT` | `resourceGroupName, ruleName, subscriptionId, workspaceName` | Creates or updates a firewall rule |
| `delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId, workspaceName` | Deletes a firewall rule |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Returns a list of firewall rules |
| `replace_all` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Replaces firewall rules |
