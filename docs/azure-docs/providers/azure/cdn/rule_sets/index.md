---
title: rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_sets
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
<tr><td><b>Name</b></td><td><code>rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.rule_sets</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Gets an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile. |
| `list_by_profile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor rule sets within a profile. |
| `create` | `INSERT` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Creates a new rule set within the specified profile. |
| `delete` | `DELETE` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Deletes an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile. |
| `_list_by_profile` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor rule sets within a profile. |
