---
title: hybrid_use_benefit
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_use_benefit
  - software_plan
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
<tr><td><b>Name</b></td><td><code>hybrid_use_benefit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.software_plan.hybrid_use_benefit" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `integer` | Indicates the revision of the hybrid use benefit |
| <CopyableCode code="properties" /> | `object` | Hybrid use benefit properties |
| <CopyableCode code="sku" /> | `object` | The SKU to be applied for this resource |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planId, scope" /> | Gets a given plan ID |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get all hybrid use benefits associated with an ARM resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="planId, scope, data__sku" /> | Create a new hybrid use benefit under a given scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planId, scope" /> | Deletes a given plan ID |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="scope" /> | Get all hybrid use benefits associated with an ARM resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="planId, scope, data__sku" /> | Updates an existing hybrid use benefit |
