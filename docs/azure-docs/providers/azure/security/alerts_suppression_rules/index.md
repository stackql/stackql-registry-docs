---
title: alerts_suppression_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_suppression_rules
  - security
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
<tr><td><b>Name</b></td><td><code>alerts_suppression_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.alerts_suppression_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | describes AlertsSuppressionRule properties |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `alertsSuppressionRuleName, api-version, subscriptionId` | Get dismiss rule, with name: &#123;alertsSuppressionRuleName&#125;, for the given subscription |
| `list` | `SELECT` | `api-version, subscriptionId` | List of all the dismiss rules for the given subscription |
| `delete` | `DELETE` | `alertsSuppressionRuleName, api-version, subscriptionId` | Delete dismiss alert rule for this subscription. |
| `_list` | `EXEC` | `api-version, subscriptionId` | List of all the dismiss rules for the given subscription |
| `update` | `EXEC` | `alertsSuppressionRuleName, api-version, subscriptionId` | Update existing rule or create new rule if it doesn't exist |
