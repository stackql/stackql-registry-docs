
---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - alloydb
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the backup resource with the format: * projects/{project}/locations/{region}/backups/{backup_id} where the cluster and backup ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the backup resource name is the name of the parent resource: * projects/{project}/locations/{region} |
| <CopyableCode code="description" /> | `string` | User-provided description of the backup. |
| <CopyableCode code="annotations" /> | `object` | Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 |
| <CopyableCode code="clusterName" /> | `string` | Required. The full resource name of the backup source cluster (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}). |
| <CopyableCode code="clusterUid" /> | `string` | Output only. The system-generated UID of the cluster which was used to create this resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp |
| <CopyableCode code="databaseVersion" /> | `string` | Output only. The database engine major version of the cluster this backup was created from. Any restored cluster created from this backup will have the same database version. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Delete time stamp |
| <CopyableCode code="displayName" /> | `string` | User-settable and human-readable display name for the Backup. |
| <CopyableCode code="encryptionConfig" /> | `object` | EncryptionConfig describes the encryption config of a cluster or a backup that is encrypted with a CMEK (customer-managed encryption key). |
| <CopyableCode code="encryptionInfo" /> | `object` | EncryptionInfo describes the encryption information of a cluster or a backup. |
| <CopyableCode code="etag" /> | `string` | For Resource freshness validation (https://google.aip.dev/154) |
| <CopyableCode code="expiryQuantity" /> | `object` | A backup's position in a quantity-based retention queue, of backups with the same source cluster and type, with length, retention, specified by the backup's retention policy. Once the position is greater than the retention, the backup is eligible to be garbage collected. Example: 5 backups from the same source cluster and type with a quantity-based retention of 3 and denoted by backup_id (position, retention). Safe: backup_5 (1, 3), backup_4, (2, 3), backup_3 (3, 3). Awaiting garbage collection: backup_2 (4, 3), backup_1 (5, 3) |
| <CopyableCode code="expiryTime" /> | `string` | Output only. The time at which after the backup is eligible to be garbage collected. It is the duration specified by the backup's retention policy, added to the backup's create_time. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Reconciling (https://google.aip.dev/128#reconciliation), if true, indicates that the service is actively updating the resource. This can happen due to user-triggered updates or system actions like failover or maintenance. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. The size of the backup in bytes. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |
| <CopyableCode code="type" /> | `string` | The backup type, which suggests the trigger for the backup. |
| <CopyableCode code="uid" /> | `string` | Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Gets details of a single Backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Backups in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Backup in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Deletes a single Backup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Updates the parameters of a single Backup. |

## `SELECT` examples

Lists Backups in a given project and location.

```sql
SELECT
name,
description,
annotations,
clusterName,
clusterUid,
createTime,
databaseVersion,
deleteTime,
displayName,
encryptionConfig,
encryptionInfo,
etag,
expiryQuantity,
expiryTime,
labels,
reconciling,
satisfiesPzs,
sizeBytes,
state,
type,
uid,
updateTime
FROM google.alloydb.backups
WHERE locationsId = '{{ locationsId }}'
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
INSERT INTO google.alloydb.backups (
locationsId,
projectsId,
name,
displayName,
uid,
createTime,
updateTime,
deleteTime,
labels,
state,
type,
description,
clusterUid,
clusterName,
reconciling,
encryptionConfig,
encryptionInfo,
etag,
annotations,
sizeBytes,
expiryTime,
expiryQuantity,
satisfiesPzs,
databaseVersion
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ labels }}',
'{{ state }}',
'{{ type }}',
'{{ description }}',
'{{ clusterUid }}',
'{{ clusterName }}',
true|false,
'{{ encryptionConfig }}',
'{{ encryptionInfo }}',
'{{ etag }}',
'{{ annotations }}',
'{{ sizeBytes }}',
'{{ expiryTime }}',
'{{ expiryQuantity }}',
true|false,
'{{ databaseVersion }}'
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
      - name: displayName
        value: '{{ displayName }}'
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: state
        value: '{{ state }}'
      - name: type
        value: '{{ type }}'
      - name: description
        value: '{{ description }}'
      - name: clusterUid
        value: '{{ clusterUid }}'
      - name: clusterName
        value: '{{ clusterName }}'
      - name: reconciling
        value: '{{ reconciling }}'
      - name: encryptionConfig
        value: '{{ encryptionConfig }}'
      - name: encryptionInfo
        value: '{{ encryptionInfo }}'
      - name: etag
        value: '{{ etag }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: sizeBytes
        value: '{{ sizeBytes }}'
      - name: expiryTime
        value: '{{ expiryTime }}'
      - name: expiryQuantity
        value: '{{ expiryQuantity }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: databaseVersion
        value: '{{ databaseVersion }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a backup only if the necessary resources are available.

```sql
UPDATE google.alloydb.backups
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
labels = '{{ labels }}',
state = '{{ state }}',
type = '{{ type }}',
description = '{{ description }}',
clusterUid = '{{ clusterUid }}',
clusterName = '{{ clusterName }}',
reconciling = true|false,
encryptionConfig = '{{ encryptionConfig }}',
encryptionInfo = '{{ encryptionInfo }}',
etag = '{{ etag }}',
annotations = '{{ annotations }}',
sizeBytes = '{{ sizeBytes }}',
expiryTime = '{{ expiryTime }}',
expiryQuantity = '{{ expiryQuantity }}',
satisfiesPzs = true|false,
databaseVersion = '{{ databaseVersion }}'
WHERE 
backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified backup resource.

```sql
DELETE FROM google.alloydb.backups
WHERE backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
