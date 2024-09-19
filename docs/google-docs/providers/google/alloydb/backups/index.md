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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

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
displayName,
labels,
type,
description,
clusterName,
encryptionConfig,
etag,
annotations
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ labels }}',
'{{ type }}',
'{{ description }}',
'{{ clusterName }}',
'{{ encryptionConfig }}',
'{{ etag }}',
'{{ annotations }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: uid
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: deleteTime
      value: string
    - name: labels
      value: object
    - name: state
      value: string
    - name: type
      value: string
    - name: description
      value: string
    - name: clusterUid
      value: string
    - name: clusterName
      value: string
    - name: reconciling
      value: boolean
    - name: encryptionConfig
      value:
        - name: kmsKeyName
          value: string
    - name: encryptionInfo
      value:
        - name: encryptionType
          value: string
        - name: kmsKeyVersions
          value:
            - string
    - name: etag
      value: string
    - name: annotations
      value: object
    - name: sizeBytes
      value: string
    - name: expiryTime
      value: string
    - name: expiryQuantity
      value:
        - name: retentionCount
          value: integer
        - name: totalRetentionCount
          value: integer
    - name: satisfiesPzs
      value: boolean
    - name: databaseVersion
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backups</code> resource.

```sql
/*+ update */
UPDATE google.alloydb.backups
SET 
displayName = '{{ displayName }}',
labels = '{{ labels }}',
type = '{{ type }}',
description = '{{ description }}',
clusterName = '{{ clusterName }}',
encryptionConfig = '{{ encryptionConfig }}',
etag = '{{ etag }}',
annotations = '{{ annotations }}'
WHERE 
backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM google.alloydb.backups
WHERE backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
