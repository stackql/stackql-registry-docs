---
title: region_disks_snapshot
hide_title: false
hide_table_of_contents: false
keywords:
  - region_disks_snapshot
  - compute
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

Creates, updates, deletes, gets or lists a <code>region_disks_snapshot</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_disks_snapshot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_disks_snapshot" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_snapshot" /> | `INSERT` | <CopyableCode code="disk, project, region" /> | Creates a snapshot of a specified persistent disk. For regular snapshot creation, consider using snapshots.insert instead, as that method supports more features, such as creating snapshots in a project different from the source disk project. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_disks_snapshot</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.compute.region_disks_snapshot (
disk,
project,
region,
name,
description,
status,
sourceDisk,
sourceDiskId,
diskSizeGb,
storageBytes,
storageBytesStatus,
licenses,
snapshotEncryptionKey,
sourceDiskEncryptionKey,
labels,
labelFingerprint,
licenseCodes,
storageLocations,
autoCreated,
guestOsFeatures,
downloadBytes,
chainName,
satisfiesPzs,
locationHint,
sourceSnapshotSchedulePolicy,
sourceSnapshotSchedulePolicyId,
sourceInstantSnapshot,
sourceInstantSnapshotId,
architecture,
snapshotType,
creationSizeBytes,
enableConfidentialCompute,
sourceDiskForRecoveryCheckpoint,
sourceInstantSnapshotEncryptionKey
)
SELECT 
'{{ disk }}',
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ status }}',
'{{ sourceDisk }}',
'{{ sourceDiskId }}',
'{{ diskSizeGb }}',
'{{ storageBytes }}',
'{{ storageBytesStatus }}',
'{{ licenses }}',
'{{ snapshotEncryptionKey }}',
'{{ sourceDiskEncryptionKey }}',
'{{ labels }}',
'{{ labelFingerprint }}',
'{{ licenseCodes }}',
'{{ storageLocations }}',
true|false,
'{{ guestOsFeatures }}',
'{{ downloadBytes }}',
'{{ chainName }}',
true|false,
'{{ locationHint }}',
'{{ sourceSnapshotSchedulePolicy }}',
'{{ sourceSnapshotSchedulePolicyId }}',
'{{ sourceInstantSnapshot }}',
'{{ sourceInstantSnapshotId }}',
'{{ architecture }}',
'{{ snapshotType }}',
'{{ creationSizeBytes }}',
true|false,
'{{ sourceDiskForRecoveryCheckpoint }}',
'{{ sourceInstantSnapshotEncryptionKey }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
kind: string
id: string
creationTimestamp: string
name: string
description: string
status: string
sourceDisk: string
sourceDiskId: string
diskSizeGb: string
storageBytes: string
storageBytesStatus: string
licenses:
  - type: string
snapshotEncryptionKey:
  rawKey: string
  rsaEncryptedKey: string
  kmsKeyName: string
  sha256: string
  kmsKeyServiceAccount: string
selfLink: string
labels: object
labelFingerprint: string
licenseCodes:
  - type: string
    format: string
storageLocations:
  - type: string
autoCreated: boolean
guestOsFeatures:
  - type: string
downloadBytes: string
chainName: string
satisfiesPzs: boolean
locationHint: string
sourceSnapshotSchedulePolicy: string
sourceSnapshotSchedulePolicyId: string
sourceInstantSnapshot: string
sourceInstantSnapshotId: string
architecture: string
snapshotType: string
creationSizeBytes: string
enableConfidentialCompute: boolean
sourceDiskForRecoveryCheckpoint: string
satisfiesPzi: boolean

```
</TabItem>
</Tabs>
