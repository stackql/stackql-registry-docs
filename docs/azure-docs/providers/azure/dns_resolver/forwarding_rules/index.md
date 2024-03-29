---
title: forwarding_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_rules
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
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.forwarding_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | ETag of the forwarding rule. |
| `properties` | `object` | Represents the properties of a forwarding rule within a DNS forwarding ruleset. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId` | Gets properties of a forwarding rule in a DNS forwarding ruleset. |
| `list` | `SELECT` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId` | Lists forwarding rules in a DNS forwarding ruleset. |
| `create_or_update` | `INSERT` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a forwarding rule in a DNS forwarding ruleset. |
| `delete` | `DELETE` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId` | Deletes a forwarding rule in a DNS forwarding ruleset. WARNING: This operation cannot be undone. |
| `_list` | `EXEC` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId` | Lists forwarding rules in a DNS forwarding ruleset. |
| `update` | `EXEC` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId` | Updates a forwarding rule in a DNS forwarding ruleset. |
