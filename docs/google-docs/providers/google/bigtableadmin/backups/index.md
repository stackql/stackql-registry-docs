---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - bigtableadmin
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigtableadmin.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/_a-zA-Z0-9*` The final segment of the name must be between 1 and 50 characters in length. The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. |
| <CopyableCode code="encryptionInfo" /> | `object` | Encryption information for a given resource. If this resource is protected with customer managed encryption, the in-use Cloud Key Management Service (Cloud KMS) key version is specified along with its status. |
| <CopyableCode code="endTime" /> | `string` | Output only. `end_time` is the time that the backup was finished. The row data in the backup will be no newer than this timestamp. |
| <CopyableCode code="expireTime" /> | `string` | Required. The expiration time of the backup. When creating a backup or updating its `expire_time`, the value must be greater than the backup creation time by: - At least 6 hours - At most 90 days Once the `expire_time` has passed, Cloud Bigtable will delete the backup. |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. Size of the backup in bytes. |
| <CopyableCode code="sourceBackup" /> | `string` | Output only. Name of the backup from which this backup was copied. If a backup is not created by copying a backup, this field will be empty. Values are of the form: projects//instances//clusters//backups/ |
| <CopyableCode code="sourceTable" /> | `string` | Required. Immutable. Name of the table from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects/{project}/instances/{instance}/tables/{source_table}`. |
| <CopyableCode code="startTime" /> | `string` | Output only. `start_time` is the time that the backup was started (i.e. approximately the time the CreateBackup request is received). The row data in this backup will be no older than this timestamp. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, clustersId, instancesId, projectsId" /> | Gets metadata on a pending or completed Cloud Bigtable Backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Lists Cloud Bigtable backups. Returns both completed and pending backups. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Starts creating a new Cloud Bigtable Backup. The returned backup long-running operation can be used to track creation of the backup. The metadata field type is CreateBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the creation and delete the backup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, clustersId, instancesId, projectsId" /> | Deletes a pending or completed Cloud Bigtable backup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupsId, clustersId, instancesId, projectsId" /> | Updates a pending or completed Cloud Bigtable Backup. |
| <CopyableCode code="copy" /> | `EXEC` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Copy a Cloud Bigtable backup to a new backup in the destination cluster located in the destination instance and project. |

## `SELECT` examples

Lists Cloud Bigtable backups. Returns both completed and pending backups.

```sql
SELECT
name,
encryptionInfo,
endTime,
expireTime,
sizeBytes,
sourceBackup,
sourceTable,
startTime,
state
FROM google.bigtableadmin.backups
WHERE clustersId = '{{ clustersId }}'
AND instancesId = '{{ instancesId }}'
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
INSERT INTO google.bigtableadmin.backups (
clustersId,
instancesId,
projectsId,
name,
sourceTable,
sourceBackup,
expireTime,
startTime,
endTime,
sizeBytes,
state,
encryptionInfo
)
SELECT 
'{{ clustersId }}',
'{{ instancesId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ sourceTable }}',
'{{ sourceBackup }}',
'{{ expireTime }}',
'{{ startTime }}',
'{{ endTime }}',
'{{ sizeBytes }}',
'{{ state }}',
'{{ encryptionInfo }}'
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
      - name: sourceTable
        value: '{{ sourceTable }}'
      - name: sourceBackup
        value: '{{ sourceBackup }}'
      - name: expireTime
        value: '{{ expireTime }}'
      - name: startTime
        value: '{{ startTime }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: sizeBytes
        value: '{{ sizeBytes }}'
      - name: state
        value: '{{ state }}'
      - name: encryptionInfo
        value: '{{ encryptionInfo }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backups</code> resource.

```sql
/*+ update */
UPDATE google.bigtableadmin.backups
SET 
name = '{{ name }}',
sourceTable = '{{ sourceTable }}',
sourceBackup = '{{ sourceBackup }}',
expireTime = '{{ expireTime }}',
startTime = '{{ startTime }}',
endTime = '{{ endTime }}',
sizeBytes = '{{ sizeBytes }}',
state = '{{ state }}',
encryptionInfo = '{{ encryptionInfo }}'
WHERE 
backupsId = '{{ backupsId }}'
AND clustersId = '{{ clustersId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigtableadmin.backups
WHERE backupsId = '{{ backupsId }}'
AND clustersId = '{{ clustersId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
