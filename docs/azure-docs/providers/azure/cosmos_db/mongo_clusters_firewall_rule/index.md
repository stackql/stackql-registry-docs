---
title: mongo_clusters_firewall_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_clusters_firewall_rule
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>mongo_clusters_firewall_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.mongo_clusters_firewall_rule</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `firewallRuleName, mongoClusterName, resourceGroupName, subscriptionId` | Gets information about a mongo cluster firewall rule. |
| `list` | `SELECT` | `mongoClusterName, resourceGroupName, subscriptionId` | List all the firewall rules in a given mongo cluster. |
| `create_or_update` | `INSERT` | `firewallRuleName, mongoClusterName, resourceGroupName, subscriptionId, data__properties` | Creates a new firewall rule or updates an existing firewall rule on a mongo cluster. |
| `delete` | `DELETE` | `firewallRuleName, mongoClusterName, resourceGroupName, subscriptionId` | Deletes a mongo cluster firewall rule. |
| `_list` | `EXEC` | `mongoClusterName, resourceGroupName, subscriptionId` | List all the firewall rules in a given mongo cluster. |
