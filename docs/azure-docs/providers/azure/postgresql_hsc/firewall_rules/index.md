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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, firewallRuleName, resourceGroupName, subscriptionId` | Gets information about a cluster firewall rule. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists all the firewall rules on cluster. |
| `create_or_update` | `INSERT` | `clusterName, firewallRuleName, resourceGroupName, subscriptionId, data__properties` | Creates a new cluster firewall rule or updates an existing cluster firewall rule. |
| `delete` | `DELETE` | `clusterName, firewallRuleName, resourceGroupName, subscriptionId` | Deletes a cluster firewall rule. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Lists all the firewall rules on cluster. |
