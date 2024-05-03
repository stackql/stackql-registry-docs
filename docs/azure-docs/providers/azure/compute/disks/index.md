---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
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
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="managedBy" /> | `string` | A relative URI containing the ID of the VM that has the disk attached. |
| <CopyableCode code="managedByExtended" /> | `array` | List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs. |
| <CopyableCode code="properties" /> | `object` | Disk resource properties. |
| <CopyableCode code="sku" /> | `object` | The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The Logical zone list for Disk. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Gets information about a disk. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the disks under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disks under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Creates or updates a disk. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Deletes a disk. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the disks under a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disks under a resource group. |
| <CopyableCode code="grant_access" /> | `EXEC` | <CopyableCode code="diskName, resourceGroupName, subscriptionId, data__access, data__durationInSeconds" /> | Grants access to a disk. |
| <CopyableCode code="revoke_access" /> | `EXEC` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Revokes access to a disk. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Updates (patches) a disk. |
