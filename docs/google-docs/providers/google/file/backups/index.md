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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

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
description,
labels,
sourceInstance,
sourceFileShare,
kmsKey,
tags
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ labels }}',
'{{ sourceInstance }}',
'{{ sourceFileShare }}',
'{{ kmsKey }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: state
      value: string
    - name: createTime
      value: string
    - name: labels
      value: object
    - name: capacityGb
      value: string
    - name: storageBytes
      value: string
    - name: sourceInstance
      value: string
    - name: sourceFileShare
      value: string
    - name: sourceInstanceTier
      value: string
    - name: downloadBytes
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: satisfiesPzi
      value: boolean
    - name: kmsKey
      value: string
    - name: tags
      value: object
    - name: fileSystemProtocol
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backups</code> resource.

```sql
/*+ update */
UPDATE google.file.backups
SET 
description = '{{ description }}',
labels = '{{ labels }}',
sourceInstance = '{{ sourceInstance }}',
sourceFileShare = '{{ sourceFileShare }}',
kmsKey = '{{ kmsKey }}',
tags = '{{ tags }}'
WHERE 
backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM google.file.backups
WHERE backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
