---
title: backups_volume_latest_restore_status
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_volume_latest_restore_status
  - netapp
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>backups_volume_latest_restore_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups_volume_latest_restore_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backups_volume_latest_restore_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="errorMessage" /> | `string` | Displays error message if the restore is in an error state |
| <CopyableCode code="healthy" /> | `boolean` | Restore health status |
| <CopyableCode code="mirrorState" /> | `string` | The status of the restore |
| <CopyableCode code="relationshipStatus" /> | `string` | Status of the restore SnapMirror relationship |
| <CopyableCode code="totalTransferBytes" /> | `integer` | Displays the total bytes transferred |
| <CopyableCode code="unhealthyReason" /> | `string` | Reason for the unhealthy restore relationship |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Get the latest status of the restore for a volume |

## `SELECT` examples

Get the latest status of the restore for a volume


```sql
SELECT
errorMessage,
healthy,
mirrorState,
relationshipStatus,
totalTransferBytes,
unhealthyReason
FROM azure_isv.netapp.backups_volume_latest_restore_status
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```