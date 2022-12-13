---
title: governance_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_rules
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
<tr><td><b>Name</b></td><td><code>governance_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.governance_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Describes properties of an governanceRule |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GovernanceRules_Get` | `SELECT` | `api-version, ruleId, subscriptionId` | Get a specific governanceRule for the requested scope by ruleId |
| `GovernanceRules_CreateOrUpdate` | `INSERT` | `api-version, ruleId, subscriptionId` | Creates or update a security GovernanceRule on the given subscription. |
| `GovernanceRules_Delete` | `DELETE` | `api-version, ruleId, subscriptionId` | Delete a GovernanceRule over a given scope |
| `GovernanceRules_RuleIdExecuteSingleSecurityConnector` | `EXEC` | `api-version, resourceGroupName, ruleId, securityConnectorName, subscriptionId` | Execute a security GovernanceRule on the given security connector. |
| `GovernanceRules_RuleIdExecuteSingleSubscription` | `EXEC` | `api-version, ruleId, subscriptionId` | Execute a security GovernanceRule on the given subscription. |
