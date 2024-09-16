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
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: status
      value: '{{ status }}'
    - name: sourceDisk
      value: '{{ sourceDisk }}'
    - name: sourceDiskId
      value: '{{ sourceDiskId }}'
    - name: diskSizeGb
      value: '{{ diskSizeGb }}'
    - name: storageBytes
      value: '{{ storageBytes }}'
    - name: storageBytesStatus
      value: '{{ storageBytesStatus }}'
    - name: licenses
      value:
        - name: type
          value: '{{ type }}'
    - name: snapshotEncryptionKey
      value:
        - name: rawKey
          value: '{{ rawKey }}'
        - name: rsaEncryptedKey
          value: '{{ rsaEncryptedKey }}'
        - name: kmsKeyName
          value: '{{ kmsKeyName }}'
        - name: sha256
          value: '{{ sha256 }}'
        - name: kmsKeyServiceAccount
          value: '{{ kmsKeyServiceAccount }}'
    - name: labels
      value: '{{ labels }}'
    - name: labelFingerprint
      value: '{{ labelFingerprint }}'
    - name: licenseCodes
      value:
        - name: type
          value: '{{ type }}'
        - name: format
          value: '{{ format }}'
    - name: storageLocations
      value:
        - name: type
          value: '{{ type }}'
    - name: autoCreated
      value: '{{ autoCreated }}'
    - name: guestOsFeatures
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: downloadBytes
      value: '{{ downloadBytes }}'
    - name: chainName
      value: '{{ chainName }}'
    - name: satisfiesPzs
      value: '{{ satisfiesPzs }}'
    - name: locationHint
      value: '{{ locationHint }}'
    - name: sourceSnapshotSchedulePolicy
      value: '{{ sourceSnapshotSchedulePolicy }}'
    - name: sourceSnapshotSchedulePolicyId
      value: '{{ sourceSnapshotSchedulePolicyId }}'
    - name: sourceInstantSnapshot
      value: '{{ sourceInstantSnapshot }}'
    - name: sourceInstantSnapshotId
      value: '{{ sourceInstantSnapshotId }}'
    - name: architecture
      value: '{{ architecture }}'
    - name: snapshotType
      value: '{{ snapshotType }}'
    - name: creationSizeBytes
      value: '{{ creationSizeBytes }}'
    - name: enableConfidentialCompute
      value: '{{ enableConfidentialCompute }}'
    - name: sourceDiskForRecoveryCheckpoint
      value: '{{ sourceDiskForRecoveryCheckpoint }}'

```
</TabItem>
</Tabs>
