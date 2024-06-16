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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.forwarding_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the forwarding rule. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a forwarding rule within a DNS forwarding ruleset. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId" /> | Gets properties of a forwarding rule in a DNS forwarding ruleset. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId" /> | Lists forwarding rules in a DNS forwarding ruleset. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a forwarding rule in a DNS forwarding ruleset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId" /> | Deletes a forwarding rule in a DNS forwarding ruleset. WARNING: This operation cannot be undone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId" /> | Updates a forwarding rule in a DNS forwarding ruleset. |
