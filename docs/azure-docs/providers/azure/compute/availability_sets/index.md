---
title: availability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets
  - compute
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
<tr><td><b>Name</b></td><td><code>availability_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.availability_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The instance view of a resource. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Retrieves information about an availability set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all availability sets in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all availability sets in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Create or update an availability set. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Delete an availability set. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Update an availability set. |
