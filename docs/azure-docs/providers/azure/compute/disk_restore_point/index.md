---
title: disk_restore_point
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_restore_point
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
<tr><td><b>Name</b></td><td><code>disk_restore_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_restore_point" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Properties of an incremental disk restore point |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName" /> | Get disk restorePoint resource |
| <CopyableCode code="list_by_restore_point" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName" /> | Lists diskRestorePoints under a vmRestorePoint. |
| <CopyableCode code="grant_access" /> | `EXEC` | <CopyableCode code="diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName, data__access, data__durationInSeconds" /> | Grants access to a diskRestorePoint. |
| <CopyableCode code="revoke_access" /> | `EXEC` | <CopyableCode code="diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName" /> | Revokes access to a diskRestorePoint. |
