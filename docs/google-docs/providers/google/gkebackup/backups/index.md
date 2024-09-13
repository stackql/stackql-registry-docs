
---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - gkebackup
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

Creates, updates, deletes or gets an <code>backup</code> resource or lists <code>backups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkebackup.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*` |
| <CopyableCode code="description" /> | `string` | Optional. User specified descriptive string for this Backup. |
| <CopyableCode code="allNamespaces" /> | `boolean` | Output only. If True, all namespaces were included in the Backup. |
| <CopyableCode code="clusterMetadata" /> | `object` | Information about the GKE cluster from which this Backup was created. |
| <CopyableCode code="completeTime" /> | `string` | Output only. Completion time of the Backup |
| <CopyableCode code="configBackupSizeBytes" /> | `string` | Output only. The size of the config backup in bytes. |
| <CopyableCode code="containsSecrets" /> | `boolean` | Output only. Whether or not the Backup contains Kubernetes Secrets. Controlled by the parent BackupPlan's include_secrets value. |
| <CopyableCode code="containsVolumeData" /> | `boolean` | Output only. Whether or not the Backup contains volume data. Controlled by the parent BackupPlan's include_volume_data value. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when this Backup resource was created. |
| <CopyableCode code="deleteLockDays" /> | `integer` | Optional. Minimum age for this Backup (in days). If this field is set to a non-zero value, the Backup will be "locked" against deletion (either manual or automatic deletion) for the number of days provided (measured from the creation time of the Backup). MUST be an integer value between 0-90 (inclusive). Defaults to parent BackupPlan's backup_delete_lock_days setting and may only be increased (either at creation time or in a subsequent update). |
| <CopyableCode code="deleteLockExpireTime" /> | `string` | Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days). |
| <CopyableCode code="encryptionKey" /> | `object` | Defined a customer managed encryption key that will be used to encrypt Backup artifacts. |
| <CopyableCode code="etag" /> | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackup`, and systems are expected to put that etag in the request to `UpdateBackup` or `DeleteBackup` to ensure that their change will be applied to the same version of the resource. |
| <CopyableCode code="labels" /> | `object` | Optional. A set of custom labels supplied by user. |
| <CopyableCode code="manual" /> | `boolean` | Output only. This flag indicates whether this Backup resource was created manually by a user or via a schedule in the BackupPlan. A value of True means that the Backup was created manually. |
| <CopyableCode code="permissiveMode" /> | `boolean` | Output only. If false, Backup will fail when Backup for GKE detects Kubernetes configuration that is non-standard or requires additional setup to restore. Inherited from the parent BackupPlan's permissive_mode value. |
| <CopyableCode code="podCount" /> | `integer` | Output only. The total number of Kubernetes Pods contained in the Backup. |
| <CopyableCode code="resourceCount" /> | `integer` | Output only. The total number of Kubernetes resources included in the Backup. |
| <CopyableCode code="retainDays" /> | `integer` | Optional. The age (in days) after which this Backup will be automatically deleted. Must be an integer value >= 0: - If 0, no automatic deletion will occur for this Backup. - If not 0, this must be >= delete_lock_days and <= 365. Once a Backup is created, this value may only be increased. Defaults to the parent BackupPlan's backup_retain_days value. |
| <CopyableCode code="retainExpireTime" /> | `string` | Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days). |
| <CopyableCode code="selectedApplications" /> | `object` | A list of namespaced Kubernetes resources. |
| <CopyableCode code="selectedNamespaces" /> | `object` | A list of Kubernetes Namespaces. |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. The total size of the Backup in bytes = config backup size + sum(volume backup sizes) |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the Backup |
| <CopyableCode code="stateReason" /> | `string` | Output only. Human-readable description of why the backup is in the current `state`. |
| <CopyableCode code="uid" /> | `string` | Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier) |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when this Backup resource was last updated. |
| <CopyableCode code="volumeCount" /> | `integer` | Output only. The total number of volume backups contained in the Backup. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupPlansId, backupsId, locationsId, projectsId" /> | Retrieve the details of a single Backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="backupPlansId, locationsId, projectsId" /> | Lists the Backups for a given BackupPlan. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="backupPlansId, locationsId, projectsId" /> | Creates a Backup for the given BackupPlan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupPlansId, backupsId, locationsId, projectsId" /> | Deletes an existing Backup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupPlansId, backupsId, locationsId, projectsId" /> | Update a Backup. |

## `SELECT` examples

Lists the Backups for a given BackupPlan.

```sql
SELECT
name,
description,
allNamespaces,
clusterMetadata,
completeTime,
configBackupSizeBytes,
containsSecrets,
containsVolumeData,
createTime,
deleteLockDays,
deleteLockExpireTime,
encryptionKey,
etag,
labels,
manual,
permissiveMode,
podCount,
resourceCount,
retainDays,
retainExpireTime,
selectedApplications,
selectedNamespaces,
sizeBytes,
state,
stateReason,
uid,
updateTime,
volumeCount
FROM google.gkebackup.backups
WHERE backupPlansId = '{{ backupPlansId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backups</code> resource.

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
INSERT INTO google.gkebackup.backups (
backupPlansId,
locationsId,
projectsId,
name,
uid,
createTime,
updateTime,
manual,
labels,
deleteLockDays,
deleteLockExpireTime,
retainDays,
retainExpireTime,
encryptionKey,
allNamespaces,
selectedNamespaces,
selectedApplications,
containsVolumeData,
containsSecrets,
clusterMetadata,
state,
stateReason,
completeTime,
resourceCount,
volumeCount,
sizeBytes,
etag,
description,
podCount,
configBackupSizeBytes,
permissiveMode
)
SELECT 
'{{ backupPlansId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
true|false,
'{{ labels }}',
'{{ deleteLockDays }}',
'{{ deleteLockExpireTime }}',
'{{ retainDays }}',
'{{ retainExpireTime }}',
'{{ encryptionKey }}',
true|false,
'{{ selectedNamespaces }}',
'{{ selectedApplications }}',
true|false,
true|false,
'{{ clusterMetadata }}',
'{{ state }}',
'{{ stateReason }}',
'{{ completeTime }}',
'{{ resourceCount }}',
'{{ volumeCount }}',
'{{ sizeBytes }}',
'{{ etag }}',
'{{ description }}',
'{{ podCount }}',
'{{ configBackupSizeBytes }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: manual
        value: '{{ manual }}'
      - name: labels
        value: '{{ labels }}'
      - name: deleteLockDays
        value: '{{ deleteLockDays }}'
      - name: deleteLockExpireTime
        value: '{{ deleteLockExpireTime }}'
      - name: retainDays
        value: '{{ retainDays }}'
      - name: retainExpireTime
        value: '{{ retainExpireTime }}'
      - name: encryptionKey
        value: '{{ encryptionKey }}'
      - name: allNamespaces
        value: '{{ allNamespaces }}'
      - name: selectedNamespaces
        value: '{{ selectedNamespaces }}'
      - name: selectedApplications
        value: '{{ selectedApplications }}'
      - name: containsVolumeData
        value: '{{ containsVolumeData }}'
      - name: containsSecrets
        value: '{{ containsSecrets }}'
      - name: clusterMetadata
        value: '{{ clusterMetadata }}'
      - name: state
        value: '{{ state }}'
      - name: stateReason
        value: '{{ stateReason }}'
      - name: completeTime
        value: '{{ completeTime }}'
      - name: resourceCount
        value: '{{ resourceCount }}'
      - name: volumeCount
        value: '{{ volumeCount }}'
      - name: sizeBytes
        value: '{{ sizeBytes }}'
      - name: etag
        value: '{{ etag }}'
      - name: description
        value: '{{ description }}'
      - name: podCount
        value: '{{ podCount }}'
      - name: configBackupSizeBytes
        value: '{{ configBackupSizeBytes }}'
      - name: permissiveMode
        value: '{{ permissiveMode }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a backup only if the necessary resources are available.

```sql
UPDATE google.gkebackup.backups
SET 
name = '{{ name }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
manual = true|false,
labels = '{{ labels }}',
deleteLockDays = '{{ deleteLockDays }}',
deleteLockExpireTime = '{{ deleteLockExpireTime }}',
retainDays = '{{ retainDays }}',
retainExpireTime = '{{ retainExpireTime }}',
encryptionKey = '{{ encryptionKey }}',
allNamespaces = true|false,
selectedNamespaces = '{{ selectedNamespaces }}',
selectedApplications = '{{ selectedApplications }}',
containsVolumeData = true|false,
containsSecrets = true|false,
clusterMetadata = '{{ clusterMetadata }}',
state = '{{ state }}',
stateReason = '{{ stateReason }}',
completeTime = '{{ completeTime }}',
resourceCount = '{{ resourceCount }}',
volumeCount = '{{ volumeCount }}',
sizeBytes = '{{ sizeBytes }}',
etag = '{{ etag }}',
description = '{{ description }}',
podCount = '{{ podCount }}',
configBackupSizeBytes = '{{ configBackupSizeBytes }}',
permissiveMode = true|false
WHERE 
backupPlansId = '{{ backupPlansId }}'
AND backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified backup resource.

```sql
DELETE FROM google.gkebackup.backups
WHERE backupPlansId = '{{ backupPlansId }}'
AND backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
