---
title: volumes_replications
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_replications
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

Creates, updates, deletes, gets or lists a <code>volumes_replications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes_replications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volumes_replications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpointType" /> | `string` | Indicates whether the local volume is the source or destination for the Volume Replication |
| <CopyableCode code="remoteVolumeRegion" /> | `string` | The remote region for the other end of the Volume Replication. |
| <CopyableCode code="remoteVolumeResourceId" /> | `string` | The resource ID of the remote volume. |
| <CopyableCode code="replicationId" /> | `string` | UUID v4 used to identify the replication. |
| <CopyableCode code="replicationSchedule" /> | `string` | Schedule |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | List all replications for a specified volume |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Delete the replication connection on the destination volume, and send release to the source replication |

## `SELECT` examples

List all replications for a specified volume


```sql
SELECT
endpointType,
remoteVolumeRegion,
remoteVolumeResourceId,
replicationId,
replicationSchedule
FROM azure_isv.netapp.volumes_replications
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
## `DELETE` example

Deletes the specified <code>volumes_replications</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.volumes_replications
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
