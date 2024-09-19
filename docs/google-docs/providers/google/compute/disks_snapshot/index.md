---
title: disks_snapshot
hide_title: false
hide_table_of_contents: false
keywords:
  - disks_snapshot
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

Creates, updates, deletes, gets or lists a <code>disks_snapshot</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disks_snapshot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.disks_snapshot" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_snapshot" /> | `INSERT` | <CopyableCode code="disk, project, zone" /> | Creates a snapshot of a specified persistent disk. For regular snapshot creation, consider using snapshots.insert instead, as that method supports more features, such as creating snapshots in a project different from the source disk project. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disks_snapshot</code> resource.

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
INSERT INTO google.compute.disks_snapshot (
disk,
project,
zone,
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
'{{ zone }}',
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
{{ autoCreated }},
'{{ guestOsFeatures }}',
'{{ downloadBytes }}',
'{{ chainName }}',
{{ satisfiesPzs }},
'{{ locationHint }}',
'{{ sourceSnapshotSchedulePolicy }}',
'{{ sourceSnapshotSchedulePolicyId }}',
'{{ sourceInstantSnapshot }}',
'{{ sourceInstantSnapshotId }}',
'{{ architecture }}',
'{{ snapshotType }}',
'{{ creationSizeBytes }}',
{{ enableConfidentialCompute }},
'{{ sourceDiskForRecoveryCheckpoint }}',
'{{ sourceInstantSnapshotEncryptionKey }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: status
      value: string
    - name: sourceDisk
      value: string
    - name: sourceDiskId
      value: string
    - name: diskSizeGb
      value: string
    - name: storageBytes
      value: string
    - name: storageBytesStatus
      value: string
    - name: licenses
      value:
        - string
    - name: snapshotEncryptionKey
      value:
        - name: rawKey
          value: string
        - name: rsaEncryptedKey
          value: string
        - name: kmsKeyName
          value: string
        - name: sha256
          value: string
        - name: kmsKeyServiceAccount
          value: string
    - name: selfLink
      value: string
    - name: labels
      value: object
    - name: labelFingerprint
      value: string
    - name: licenseCodes
      value:
        - string
    - name: storageLocations
      value:
        - string
    - name: autoCreated
      value: boolean
    - name: guestOsFeatures
      value:
        - - name: type
            value: string
    - name: downloadBytes
      value: string
    - name: chainName
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: locationHint
      value: string
    - name: sourceSnapshotSchedulePolicy
      value: string
    - name: sourceSnapshotSchedulePolicyId
      value: string
    - name: sourceInstantSnapshot
      value: string
    - name: sourceInstantSnapshotId
      value: string
    - name: architecture
      value: string
    - name: snapshotType
      value: string
    - name: creationSizeBytes
      value: string
    - name: enableConfidentialCompute
      value: boolean
    - name: sourceDiskForRecoveryCheckpoint
      value: string
    - name: satisfiesPzi
      value: boolean

```
</TabItem>
</Tabs>
