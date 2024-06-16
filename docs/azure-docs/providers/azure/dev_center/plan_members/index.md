---
title: plan_members
hide_title: false
hide_table_of_contents: false
keywords:
  - plan_members
  - dev_center
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
<tr><td><b>Name</b></td><td><code>plan_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.plan_members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the devcenter plan member. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Gets a devcenter plan member. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Lists all of the members assigned to a devcenter plan. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Creates or updates a devcenter plan member resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Deletes a devcenter plan member |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Partially updates a devcenter plan. |
