---
title: volume_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_snapshots
  - elastic_san
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
<tr><td><b>Name</b></td><td><code>volume_snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.volume_snapshots" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName" /> | Get a Volume Snapshot. |
| <CopyableCode code="list_by_volume_group" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName, data__properties" /> | Create a Volume Snapshot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName" /> | Delete a Volume Snapshot. |
| <CopyableCode code="_list_by_volume_group" /> | `EXEC` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter |
