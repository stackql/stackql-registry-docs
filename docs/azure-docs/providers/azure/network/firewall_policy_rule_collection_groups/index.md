---
title: firewall_policy_rule_collection_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_rule_collection_groups
  - network
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy_rule_collection_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_rule_collection_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the rule collection group. |
| <CopyableCode code="type" /> | `string` | Rule Group type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId" /> | Gets the specified FirewallPolicyRuleCollectionGroup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Lists all FirewallPolicyRuleCollectionGroups in a FirewallPolicy resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId" /> | Creates or updates the specified FirewallPolicyRuleCollectionGroup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId" /> | Deletes the specified FirewallPolicyRuleCollectionGroup. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Lists all FirewallPolicyRuleCollectionGroups in a FirewallPolicy resource. |
