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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RuleSets_Get` | `SELECT` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Gets an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile. |
| `RuleSets_ListByProfile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor rule sets within a profile. |
| `RuleSets_Create` | `INSERT` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Creates a new rule set within the specified profile. |
| `RuleSets_Delete` | `DELETE` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Deletes an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile. |
| `RuleSets_ListResourceUsage` | `EXEC` | `profileName, resourceGroupName, ruleSetName, subscriptionId` | Checks the quota and actual usage of endpoints under the given CDN profile. |
