---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.file.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the snapshot, in the format `projects/{project_id}/locations/{location_id}/instances/{instance_id}/snapshots/{snapshot_id}`. |
| <CopyableCode code="description" /> | `string` | A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the snapshot was created. |
| <CopyableCode code="filesystemUsedBytes" /> | `string` | Output only. The amount of bytes needed to allocate a full copy of the snapshot content |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user provided metadata. |
| <CopyableCode code="state" /> | `string` | Output only. The snapshot state. |
| <CopyableCode code="tags" /> | `object` | Optional. Input only. Immutable. Tag key-value pairs are bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId, snapshotsId" /> | Gets the details of a specific snapshot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Lists all snapshots in a project for either a specified location or for all locations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Creates a snapshot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId, snapshotsId" /> | Deletes a snapshot. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instancesId, locationsId, projectsId, snapshotsId" /> | Updates the settings of a specific snapshot. |

## `SELECT` examples

Lists all snapshots in a project for either a specified location or for all locations.

```sql
SELECT
name,
description,
createTime,
filesystemUsedBytes,
labels,
state,
tags
FROM google.file.snapshots
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>snapshots</code> resource.

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
INSERT INTO google.file.snapshots (
instancesId,
locationsId,
projectsId,
description,
labels,
tags
)
SELECT 
'{{ instancesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ labels }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
description: string
state: string
createTime: string
labels: object
filesystemUsedBytes: string
tags: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>snapshots</code> resource.

```sql
/*+ update */
UPDATE google.file.snapshots
SET 
description = '{{ description }}',
labels = '{{ labels }}',
tags = '{{ tags }}'
WHERE 
instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND snapshotsId = '{{ snapshotsId }}';
```

## `DELETE` example

Deletes the specified <code>snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM google.file.snapshots
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND snapshotsId = '{{ snapshotsId }}';
```
