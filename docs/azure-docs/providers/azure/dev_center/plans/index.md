---
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
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
<tr><td><b>Name</b></td><td><code>plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the devcenter plan. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Gets a devcenter plan. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all devcenter plans in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all devcenter plans in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Creates or updates a devcenter plan resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Deletes a devcenter plan |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Partially updates a devcenter plan. |
