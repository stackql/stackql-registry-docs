---
title: iscsi_disks
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_disks
  - storsimple_1200_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>iscsi_disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.iscsi_disks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The iSCSI disk properties. |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified iSCSI disk name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the iSCSI disks in a device. |
| <CopyableCode code="list_by_iscsi_server" /> | `SELECT` | <CopyableCode code="deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the disks in a iSCSI server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the iSCSI disk. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Deletes the iSCSI disk. |
| <CopyableCode code="_list_by_device" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the iSCSI disks in a device. |
| <CopyableCode code="_list_by_iscsi_server" /> | `EXEC` | <CopyableCode code="deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the disks in a iSCSI server. |
