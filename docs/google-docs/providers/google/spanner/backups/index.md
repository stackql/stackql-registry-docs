---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - spanner
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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only for the CreateBackup operation. Required for the UpdateBackup operation. A globally unique identifier for the backup which cannot be changed. Values are of the form `projects//instances//backups/a-z*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length. The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form `projects//instances/`. |
| <CopyableCode code="backupSchedules" /> | `array` | Output only. List of backup schedule URIs that are associated with creating this backup. This is only applicable for scheduled backups, and is empty for on-demand backups. To optimize for storage, whenever possible, multiple schedules are collapsed together to create one backup. In such cases, this field captures the list of all backup schedule URIs that are associated with creating this backup. If collapsing is not done, then this field captures the single backup schedule URI associated with creating this backup. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the CreateBackup request is received. If the request does not specify `version_time`, the `version_time` of the backup will be equivalent to the `create_time`. |
| <CopyableCode code="database" /> | `string` | Required for the CreateBackup operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects//instances//databases/`. |
| <CopyableCode code="databaseDialect" /> | `string` | Output only. The database dialect information for the backup. |
| <CopyableCode code="encryptionInfo" /> | `object` | Encryption information for a Cloud Spanner database or backup. |
| <CopyableCode code="encryptionInformation" /> | `array` | Output only. The encryption information for the backup, whether it is protected by one or more KMS keys. The information includes all Cloud KMS key versions used to encrypt the backup. The `encryption_status' field inside of each `EncryptionInfo` is not populated. At least one of the key versions must be available for the backup to be restored. If a key version is revoked in the middle of a restore, the restore behavior is undefined. |
| <CopyableCode code="exclusiveSizeBytes" /> | `string` | Output only. For a backup in an incremental backup chain, this is the storage space needed to keep the data that has changed since the previous backup. For all other backups, this is always the size of the backup. This value may change if backups on the same chain get deleted or expired. This field can be used to calculate the total storage space used by a set of backups. For example, the total space used by all backups of a database can be computed by summing up this field. |
| <CopyableCode code="expireTime" /> | `string` | Required for the CreateBackup operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup. |
| <CopyableCode code="freeableSizeBytes" /> | `string` | Output only. The number of bytes that will be freed by deleting this backup. This value will be zero if, for example, this backup is part of an incremental backup chain and younger backups in the chain require that we keep its data. For backups not in an incremental backup chain, this is always the size of the backup. This value may change if backups on the same chain get created, deleted or expired. |
| <CopyableCode code="incrementalBackupChainId" /> | `string` | Output only. Populated only for backups in an incremental backup chain. Backups share the same chain id if and only if they belong to the same incremental backup chain. Use this field to determine which backups are part of the same incremental backup chain. The ordering of backups in the chain can be determined by ordering the backup `version_time`. |
| <CopyableCode code="maxExpireTime" /> | `string` | Output only. The max allowed expiration time of the backup, with microseconds granularity. A backup's expiration time can be configured in multiple APIs: CreateBackup, UpdateBackup, CopyBackup. When updating or copying an existing backup, the expiration time specified must be less than `Backup.max_expire_time`. |
| <CopyableCode code="oldestVersionTime" /> | `string` | Output only. Data deleted at a time older than this is guaranteed not to be retained in order to support this backup. For a backup in an incremental backup chain, this is the version time of the oldest backup that exists or ever existed in the chain. For all other backups, this is the version time of the backup. This field can be used to understand what data is being retained by the backup system. |
| <CopyableCode code="referencingBackups" /> | `array` | Output only. The names of the destination backups being created by copying this source backup. The backup names are of the form `projects//instances//backups/`. Referencing backups may exist in different instances. The existence of any referencing backup prevents the backup from being deleted. When the copy operation is done (either successfully completed or cancelled or the destination backup is deleted), the reference to the backup is removed. |
| <CopyableCode code="referencingDatabases" /> | `array` | Output only. The names of the restored databases that reference the backup. The database names are of the form `projects//instances//databases/`. Referencing databases may exist in different instances. The existence of any referencing database prevents the backup from being deleted. When a restored database from the backup enters the `READY` state, the reference to the backup is removed. |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. Size of the backup in bytes. For a backup in an incremental backup chain, this is the sum of the `exclusive_size_bytes` of itself and all older backups in the chain. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |
| <CopyableCode code="versionTime" /> | `string` | The backup will contain an externally consistent copy of the database at the timestamp specified by `version_time`. If `version_time` is not specified, the system will set `version_time` to the `create_time` of the backup. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_backups_get" /> | `SELECT` | <CopyableCode code="backupsId, instancesId, projectsId" /> | Gets metadata on a pending or completed Backup. |
| <CopyableCode code="projects_instances_backups_list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Lists completed and pending backups. Backups returned are ordered by `create_time` in descending order, starting from the most recent `create_time`. |
| <CopyableCode code="projects_instances_backups_create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId" /> | Starts creating a new Cloud Spanner Backup. The returned backup long-running operation will have a name of the format `projects//instances//backups//operations/` and can be used to track creation of the backup. The metadata field type is CreateBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the creation and delete the backup. There can be only one pending backup creation per database. Backup creation of different databases can run concurrently. |
| <CopyableCode code="projects_instances_backups_delete" /> | `DELETE` | <CopyableCode code="backupsId, instancesId, projectsId" /> | Deletes a pending or completed Backup. |
| <CopyableCode code="projects_instances_backups_patch" /> | `UPDATE` | <CopyableCode code="backupsId, instancesId, projectsId" /> | Updates a pending or completed Backup. |
| <CopyableCode code="projects_instances_backups_copy" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Starts copying a Cloud Spanner Backup. The returned backup long-running operation will have a name of the format `projects//instances//backups//operations/` and can be used to track copying of the backup. The operation is associated with the destination backup. The metadata field type is CopyBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the copying and delete the destination backup. Concurrent CopyBackup requests can run on the same source backup. |

## `SELECT` examples

Lists completed and pending backups. Backups returned are ordered by `create_time` in descending order, starting from the most recent `create_time`.

```sql
SELECT
name,
backupSchedules,
createTime,
database,
databaseDialect,
encryptionInfo,
encryptionInformation,
exclusiveSizeBytes,
expireTime,
freeableSizeBytes,
incrementalBackupChainId,
maxExpireTime,
oldestVersionTime,
referencingBackups,
referencingDatabases,
sizeBytes,
state,
versionTime
FROM google.spanner.backups
WHERE instancesId = '{{ instancesId }}'
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
INSERT INTO google.spanner.backups (
instancesId,
projectsId,
database,
versionTime,
expireTime,
name
)
SELECT 
'{{ instancesId }}',
'{{ projectsId }}',
'{{ database }}',
'{{ versionTime }}',
'{{ expireTime }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
database: string
versionTime: string
expireTime: string
name: string
createTime: string
sizeBytes: string
freeableSizeBytes: string
exclusiveSizeBytes: string
state: string
referencingDatabases:
  - type: string
encryptionInfo:
  encryptionType: string
  encryptionStatus:
    code: integer
    message: string
    details:
      - type: string
        additionalProperties: any
  kmsKeyVersion: string
encryptionInformation:
  - encryptionType: string
    kmsKeyVersion: string
databaseDialect: string
referencingBackups:
  - type: string
maxExpireTime: string
backupSchedules:
  - type: string
incrementalBackupChainId: string
oldestVersionTime: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backups</code> resource.

```sql
/*+ update */
UPDATE google.spanner.backups
SET 
database = '{{ database }}',
versionTime = '{{ versionTime }}',
expireTime = '{{ expireTime }}',
name = '{{ name }}'
WHERE 
backupsId = '{{ backupsId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.backups
WHERE backupsId = '{{ backupsId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
