---
title: availability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets
  - system_center_vm_manager
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.availability_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId" /> | Implements AvailabilitySet GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of AvailabilitySets in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of AvailabilitySets in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Onboards the ScVmm availability set as an Azure resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId" /> | Deregisters the ScVmm availability set from Azure. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId" /> | Updates the AvailabilitySets resource. |
