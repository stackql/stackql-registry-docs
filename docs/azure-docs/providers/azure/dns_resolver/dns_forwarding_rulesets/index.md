---
title: dns_forwarding_rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_forwarding_rulesets
  - dns_resolver
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
<tr><td><b>Name</b></td><td><code>dns_forwarding_rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.dns_forwarding_rulesets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | ETag of the DNS forwarding ruleset. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Represents the properties of a DNS forwarding ruleset. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId` | Gets a DNS forwarding ruleset properties. |
| `list` | `SELECT` | `subscriptionId` | Lists DNS forwarding rulesets in all resource groups of a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists DNS forwarding rulesets within a resource group. |
| `list_by_virtual_network` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Lists DNS forwarding ruleset resource IDs attached to a virtual network. |
| `create_or_update` | `INSERT` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a DNS forwarding ruleset. |
| `delete` | `DELETE` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId` | Deletes a DNS forwarding ruleset. WARNING: This operation cannot be undone. All forwarding rules within the ruleset will be deleted. |
| `_list` | `EXEC` | `subscriptionId` | Lists DNS forwarding rulesets in all resource groups of a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists DNS forwarding rulesets within a resource group. |
| `update` | `EXEC` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId` | Updates a DNS forwarding ruleset. |
