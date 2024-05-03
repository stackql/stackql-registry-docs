---
title: firewall_policy_idps_signatures_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_idps_signatures_overrides
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
<tr><td><b>Name</b></td><td><code>firewall_policy_idps_signatures_overrides</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_idps_signatures_overrides" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Will contain the resource id of the signature override resource |
| <CopyableCode code="name" /> | `string` | Contains the name of the resource (default) |
| <CopyableCode code="properties" /> | `object` | Will contain the properties of the resource (the actual signature overrides) |
| <CopyableCode code="type" /> | `string` | Will contain the type of the resource: Microsoft.Network/firewallPolicies/intrusionDetectionSignaturesOverrides |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Returns all signatures overrides objects for a specific policy as a list containing a single value. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Returns all signatures overrides objects for a specific policy as a list containing a single value. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Returns all signatures overrides for a specific policy. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Will update the status of policy's signature overrides for IDPS |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Will override/create a new signature overrides for the policy's IDPS |
