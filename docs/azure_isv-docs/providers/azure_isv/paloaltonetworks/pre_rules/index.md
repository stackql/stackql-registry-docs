---
title: pre_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - pre_rules
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
<tr><td><b>Name</b></td><td><code>pre_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.pre_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | definition of rule |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `globalRulestackName, priority` | Get a PreRulesResource |
| `list` | `SELECT` | `globalRulestackName` | List PreRulesResource resources by Tenant |
| `create_or_update` | `INSERT` | `globalRulestackName, priority, data__properties` | Create a PreRulesResource |
| `delete` | `DELETE` | `globalRulestackName, priority` | Delete a PreRulesResource |
| `_list` | `EXEC` | `globalRulestackName` | List PreRulesResource resources by Tenant |
| `refresh_counters` | `EXEC` | `globalRulestackName, priority` | Refresh counters |
| `reset_counters` | `EXEC` | `globalRulestackName, priority` | Reset counters |
