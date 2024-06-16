---
title: disk_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_pools
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>disk_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.disk_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives. |
| <CopyableCode code="managedBy" /> | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| <CopyableCode code="managedByExtended" /> | `array` | List of Azure resource ids that manage this resource. |
| <CopyableCode code="properties" /> | `object` | Disk Pool response properties. |
| <CopyableCode code="sku" /> | `object` | Sku for ARM resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Get a Disk pool. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of DiskPools in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of Disk Pools in a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId, data__location, data__properties, data__sku" /> | Create or Update Disk pool. This create or update operation can take 15 minutes to complete. This is expected service behavior. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Delete a Disk pool; attached disks are not affected. This delete operation can take 10 minutes to complete. This is expected service behavior. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Shuts down the Disk Pool and releases the compute resources. You are not billed for the compute resources that this Disk Pool uses. This operation can take 10 minutes to complete. This is expected service behavior. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | The operation to start a Disk Pool. This start operation can take 10 minutes to complete. This is expected service behavior. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId, data__properties" /> | Update a Disk pool. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Upgrade replaces the underlying virtual machine hosts one at a time. This operation can take 10-15 minutes to complete. This is expected service behavior. |
