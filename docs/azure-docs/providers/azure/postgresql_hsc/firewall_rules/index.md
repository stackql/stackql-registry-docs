---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - postgresql_hsc
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
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.firewall_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of a server group firewall rule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallRules_Get` | `SELECT` | `firewallRuleName, resourceGroupName, serverGroupName, subscriptionId` | Gets information about a server group firewall rule. |
| `FirewallRules_ListByServerGroup` | `SELECT` | `resourceGroupName, serverGroupName, subscriptionId` | List all the firewall rules in a given server group. |
| `FirewallRules_CreateOrUpdate` | `INSERT` | `firewallRuleName, resourceGroupName, serverGroupName, subscriptionId, data__properties` | Creates a new firewall rule or updates an existing firewall rule. |
| `FirewallRules_Delete` | `DELETE` | `firewallRuleName, resourceGroupName, serverGroupName, subscriptionId` | Deletes a server group firewall rule. |
