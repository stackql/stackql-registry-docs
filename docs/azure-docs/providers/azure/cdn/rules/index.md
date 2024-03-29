---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - cdn
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.rules</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId` | Gets an existing delivery rule within a rule set. |
| `list_by_rule_set` | `SELECT` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Lists all of the existing delivery rules within a rule set. |
| `create` | `INSERT` | `profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId` | Creates a new delivery rule within the specified rule set. |
| `delete` | `DELETE` | `profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId` | Deletes an existing delivery rule within a rule set. |
| `_list_by_rule_set` | `EXEC` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Lists all of the existing delivery rules within a rule set. |
| `update` | `EXEC` | `profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId` | Updates an existing delivery rule within a rule set. |
