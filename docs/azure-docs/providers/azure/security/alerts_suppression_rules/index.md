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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_suppression_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.alerts_suppression_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | describes AlertsSuppressionRule properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertsSuppressionRuleName, api-version, subscriptionId" /> | Get dismiss rule, with name: &#123;alertsSuppressionRuleName&#125;, for the given subscription |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List of all the dismiss rules for the given subscription |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="alertsSuppressionRuleName, api-version, subscriptionId" /> | Delete dismiss alert rule for this subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="alertsSuppressionRuleName, api-version, subscriptionId" /> | Update existing rule or create new rule if it doesn't exist |
