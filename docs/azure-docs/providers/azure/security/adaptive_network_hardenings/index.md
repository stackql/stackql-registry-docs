---
title: adaptive_network_hardenings
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_network_hardenings
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adaptive_network_hardenings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.adaptive_network_hardenings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Adaptive Network Hardening resource properties |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="adaptiveNetworkHardeningResourceName, api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId" /> | Gets a single Adaptive Network Hardening resource |
| <CopyableCode code="list_by_extended_resource" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId" /> | Gets a list of Adaptive Network Hardenings resources in scope of an extended resource. |
| <CopyableCode code="_list_by_extended_resource" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId" /> | Gets a list of Adaptive Network Hardenings resources in scope of an extended resource. |
| <CopyableCode code="enforce" /> | `EXEC` | <CopyableCode code="adaptiveNetworkHardeningEnforceAction, adaptiveNetworkHardeningResourceName, api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId, data__networkSecurityGroups, data__rules" /> | Enforces the given rules on the NSG(s) listed in the request |
