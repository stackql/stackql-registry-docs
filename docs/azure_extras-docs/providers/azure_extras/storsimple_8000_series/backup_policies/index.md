---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
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
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.backup_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the backup policy. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified backup policy name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets all the backup policies in a device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the backup policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the backup policy. |
| <CopyableCode code="_list_by_device" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets all the backup policies in a device. |
| <CopyableCode code="backup_now" /> | `EXEC` | <CopyableCode code="backupPolicyName, backupType, deviceName, managerName, resourceGroupName, subscriptionId" /> | Backup the backup policy now. |
