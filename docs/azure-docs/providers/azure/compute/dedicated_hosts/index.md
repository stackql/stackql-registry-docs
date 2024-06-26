---
title: dedicated_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hosts
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
<tr><td><b>Name</b></td><td><code>dedicated_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.dedicated_hosts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the dedicated host. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Retrieves information about a dedicated host. |
| <CopyableCode code="list_by_host_group" /> | `SELECT` | <CopyableCode code="hostGroupName, resourceGroupName, subscriptionId" /> | Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId, data__sku" /> | Create or update a dedicated host . |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Delete a dedicated host. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Redeploy the dedicated host. The operation will complete successfully once the dedicated host has migrated to a new node and is running. To determine the health of VMs deployed on the dedicated host after the redeploy check the Resource Health Center in the Azure Portal. Please refer to https://docs.microsoft.com/azure/service-health/resource-health-overview for more details. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Restart the dedicated host. The operation will complete successfully once the dedicated host has restarted and is running. To determine the health of VMs deployed on the dedicated host after the restart check the Resource Health Center in the Azure Portal. Please refer to https://docs.microsoft.com/azure/service-health/resource-health-overview for more details. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Update a dedicated host . |
