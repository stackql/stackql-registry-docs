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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*` |
| `description` | `string` | Optional. User specified descriptive string for this Backup. |
| `containsSecrets` | `boolean` | Output only. Whether or not the Backup contains Kubernetes Secrets. Controlled by the parent BackupPlan's include_secrets value. |
| `retainExpireTime` | `string` | Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days). |
| `sizeBytes` | `string` | Output only. The total size of the Backup in bytes = config backup size + sum(volume backup sizes) |
| `encryptionKey` | `object` | Defined a customer managed encryption key that will be used to encrypt Backup artifacts. |
| `updateTime` | `string` | Output only. The timestamp when this Backup resource was last updated. |
| `labels` | `object` | Optional. A set of custom labels supplied by user. |
| `completeTime` | `string` | Output only. Completion time of the Backup |
| `stateReason` | `string` | Output only. Human-readable description of why the backup is in the current `state`. |
| `manual` | `boolean` | Output only. This flag indicates whether this Backup resource was created manually by a user or via a schedule in the BackupPlan. A value of True means that the Backup was created manually. |
| `deleteLockExpireTime` | `string` | Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days). |
| `retainDays` | `integer` | Optional. The age (in days) after which this Backup will be automatically deleted. Must be an integer value &gt;= 0: - If 0, no automatic deletion will occur for this Backup. - If not 0, this must be &gt;= delete_lock_days and &lt;= 365. Once a Backup is created, this value may only be increased. Defaults to the parent BackupPlan's backup_retain_days value. |
| `containsVolumeData` | `boolean` | Output only. Whether or not the Backup contains volume data. Controlled by the parent BackupPlan's include_volume_data value. |
| `deleteLockDays` | `integer` | Optional. Minimum age for this Backup (in days). If this field is set to a non-zero value, the Backup will be "locked" against deletion (either manual or automatic deletion) for the number of days provided (measured from the creation time of the Backup). MUST be an integer value between 0-90 (inclusive). Defaults to parent BackupPlan's backup_delete_lock_days setting and may only be increased (either at creation time or in a subsequent update). |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier) |
| `volumeCount` | `integer` | Output only. The total number of volume backups contained in the Backup. |
| `allNamespaces` | `boolean` | Output only. If True, all namespaces were included in the Backup. |
| `configBackupSizeBytes` | `string` | Output only. The size of the config backup in bytes. |
| `clusterMetadata` | `object` | Information about the GKE cluster from which this Backup was created. |
| `podCount` | `integer` | Output only. The total number of Kubernetes Pods contained in the Backup. |
| `resourceCount` | `integer` | Output only. The total number of Kubernetes resources included in the Backup. |
| `createTime` | `string` | Output only. The timestamp when this Backup resource was created. |
| `selectedApplications` | `object` | A list of namespaced Kubernetes resources. |
| `state` | `string` | Output only. Current state of the Backup |
| `selectedNamespaces` | `object` | A list of Kubernetes Namespaces |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackup`, and systems are expected to put that etag in the request to `UpdateBackup` or `DeleteBackup` to ensure that their change will be applied to the same version of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupPlansId, backupsId, locationsId, projectsId` | Retrieve the details of a single Backup. |
| `list` | `SELECT` | `backupPlansId, locationsId, projectsId` | Lists the Backups for a given BackupPlan. |
| `create` | `INSERT` | `backupPlansId, locationsId, projectsId` | Creates a Backup for the given BackupPlan. |
| `delete` | `DELETE` | `backupPlansId, backupsId, locationsId, projectsId` | Deletes an existing Backup. |
| `_list` | `EXEC` | `backupPlansId, locationsId, projectsId` | Lists the Backups for a given BackupPlan. |
| `patch` | `EXEC` | `backupPlansId, backupsId, locationsId, projectsId` | Update a Backup. |
