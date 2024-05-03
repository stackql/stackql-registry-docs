---
title: backup_schedule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedule_groups
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
<tr><td><b>Name</b></td><td><code>backup_schedule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.backup_schedule_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The Backup Schedule Group Properties |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId" /> | Returns the properties of the specified backup schedule group name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the backup schedule groups in a device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId, data__properties" /> | Creates or Updates the backup schedule Group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId" /> | Deletes the backup schedule group. |
| <CopyableCode code="_list_by_device" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the backup schedule groups in a device. |
