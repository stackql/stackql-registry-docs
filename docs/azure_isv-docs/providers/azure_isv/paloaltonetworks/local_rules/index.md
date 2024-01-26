---
title: local_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rules
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>local_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.local_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | definition of rule |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `localRulestackName, priority, resourceGroupName, subscriptionId` | Get a LocalRulesResource |
| `list_by_local_rulestacks` | `SELECT` | `localRulestackName, resourceGroupName, subscriptionId` | List LocalRulesResource resources by LocalRulestacks |
| `create_or_update` | `INSERT` | `localRulestackName, priority, resourceGroupName, subscriptionId, data__properties` | Create a LocalRulesResource |
| `delete` | `DELETE` | `localRulestackName, priority, resourceGroupName, subscriptionId` | Delete a LocalRulesResource |
| `_list_by_local_rulestacks` | `EXEC` | `localRulestackName, resourceGroupName, subscriptionId` | List LocalRulesResource resources by LocalRulestacks |
| `refresh_counters` | `EXEC` | `localRulestackName, priority, resourceGroupName, subscriptionId` | Refresh counters |
| `reset_counters` | `EXEC` | `localRulestackName, priority, resourceGroupName, subscriptionId` | Reset counters |
