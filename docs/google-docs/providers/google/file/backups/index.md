
---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - file
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.file.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the backup, in the format `projects/{project_number}/locations/{location_id}/backups/{backup_id}`. |
| <CopyableCode code="description" /> | `string` | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected. |
| <CopyableCode code="capacityGb" /> | `string` | Output only. Capacity of the source file share when the backup was created. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the backup was created. |
| <CopyableCode code="downloadBytes" /> | `string` | Output only. Amount of bytes that will be downloaded if the backup is restored. This may be different than storage bytes, since sequential backups of the same disk will share storage. |
| <CopyableCode code="fileSystemProtocol" /> | `string` | Output only. The file system protocol of the source Filestore instance that this backup is created from. |
| <CopyableCode code="kmsKey" /> | `string` | Immutable. KMS key name used for data encryption. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user provided metadata. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="sourceFileShare" /> | `string` | Name of the file share in the source Filestore instance that the backup is created from. |
| <CopyableCode code="sourceInstance" /> | `string` | The resource name of the source Filestore instance, in the format `projects/{project_number}/locations/{location_id}/instances/{instance_id}`, used to create this backup. |
| <CopyableCode code="sourceInstanceTier" /> | `string` | Output only. The service tier of the source Filestore instance that this backup is created from. |
| <CopyableCode code="state" /> | `string` | Output only. The backup state. |
| <CopyableCode code="storageBytes" /> | `string` | Output only. The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion. |
| <CopyableCode code="tags" /> | `object` | Optional. Input only. Immutable. Tag key-value pairs are bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Gets the details of a specific backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all backups in a project for either a specified location or for all locations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a backup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Deletes a backup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Updates the settings of a specific backup. |

## `SELECT` examples

Lists all backups in a project for either a specified location or for all locations.

```sql
SELECT
name,
description,
capacityGb,
createTime,
downloadBytes,
fileSystemProtocol,
kmsKey,
labels,
satisfiesPzi,
satisfiesPzs,
sourceFileShare,
sourceInstance,
sourceInstanceTier,
state,
storageBytes,
tags
FROM google.file.backups
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
INSERT INTO google.file.backups (
locationsId,
projectsId,
name,
description,
state,
createTime,
labels,
capacityGb,
storageBytes,
sourceInstance,
sourceFileShare,
sourceInstanceTier,
downloadBytes,
satisfiesPzs,
satisfiesPzi,
kmsKey,
tags,
fileSystemProtocol
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ state }}',
'{{ createTime }}',
'{{ labels }}',
'{{ capacityGb }}',
'{{ storageBytes }}',
'{{ sourceInstance }}',
'{{ sourceFileShare }}',
'{{ sourceInstanceTier }}',
'{{ downloadBytes }}',
true|false,
true|false,
'{{ kmsKey }}',
'{{ tags }}',
'{{ fileSystemProtocol }}'
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
      - name: description
        value: '{{ description }}'
      - name: state
        value: '{{ state }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: capacityGb
        value: '{{ capacityGb }}'
      - name: storageBytes
        value: '{{ storageBytes }}'
      - name: sourceInstance
        value: '{{ sourceInstance }}'
      - name: sourceFileShare
        value: '{{ sourceFileShare }}'
      - name: sourceInstanceTier
        value: '{{ sourceInstanceTier }}'
      - name: downloadBytes
        value: '{{ downloadBytes }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'
      - name: kmsKey
        value: '{{ kmsKey }}'
      - name: tags
        value: '{{ tags }}'
      - name: fileSystemProtocol
        value: '{{ fileSystemProtocol }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a backup only if the necessary resources are available.

```sql
UPDATE google.file.backups
SET 
name = '{{ name }}',
description = '{{ description }}',
state = '{{ state }}',
createTime = '{{ createTime }}',
labels = '{{ labels }}',
capacityGb = '{{ capacityGb }}',
storageBytes = '{{ storageBytes }}',
sourceInstance = '{{ sourceInstance }}',
sourceFileShare = '{{ sourceFileShare }}',
sourceInstanceTier = '{{ sourceInstanceTier }}',
downloadBytes = '{{ downloadBytes }}',
satisfiesPzs = true|false,
satisfiesPzi = true|false,
kmsKey = '{{ kmsKey }}',
tags = '{{ tags }}',
fileSystemProtocol = '{{ fileSystemProtocol }}'
WHERE 
backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified backup resource.

```sql
DELETE FROM google.file.backups
WHERE backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
