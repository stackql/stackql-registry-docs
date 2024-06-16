---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Snapshot properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName" /> | Get details of the specified snapshot |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | List all snapshots associated with the volume |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__location" /> | Create the specified snapshot within the given volume |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName" /> | Delete snapshot |
| <CopyableCode code="restore_files" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__filePaths" /> | Restore the specified files from the specified snapshot to the active filesystem |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName" /> | Patch a snapshot |
