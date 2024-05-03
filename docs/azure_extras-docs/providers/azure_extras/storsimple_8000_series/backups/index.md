---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - storsimple_8000_series
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the backup. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the backups in a device. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the backup. |
| <CopyableCode code="_list_by_device" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the backups in a device. |
| <CopyableCode code="clone" /> | `EXEC` | <CopyableCode code="backupElementName, backupName, deviceName, managerName, resourceGroupName, subscriptionId, data__backupElement, data__targetAccessControlRecordIds, data__targetDeviceId, data__targetVolumeName" /> | Clones the backup element as a new volume. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="backupName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Restores the backup on the device. |
