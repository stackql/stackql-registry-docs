---
title: savings_plan_order
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plan_order
  - billing_benefits
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
<tr><td><b>Name</b></td><td><code>savings_plan_order</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing_benefits.savings_plan_order" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Savings plan order properties |
| <CopyableCode code="sku" /> | `object` | The SKU to be applied for this resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="savingsPlanOrderId" /> | Get a savings plan order. |
| <CopyableCode code="list" /> | `SELECT` |  | List all Savings plan orders. |
| <CopyableCode code="_list" /> | `EXEC` |  | List all Savings plan orders. |
| <CopyableCode code="elevate" /> | `EXEC` | <CopyableCode code="savingsPlanOrderId" /> | Elevate as owner on savings plan order based on billing permissions. |
