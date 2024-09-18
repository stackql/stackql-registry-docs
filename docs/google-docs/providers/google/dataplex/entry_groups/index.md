---
title: entry_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - entry_groups
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>entry_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entry_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.entry_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the EntryGroup, in the format projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the EntryGroup. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the EntryGroup was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the service, and might be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the EntryGroup. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the EntryGroup. If you delete and recreate the EntryGroup with the same name, this ID will be different. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the EntryGroup was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_get" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Gets an EntryGroup. |
| <CopyableCode code="projects_locations_entry_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists EntryGroup resources in a project and location. |
| <CopyableCode code="projects_locations_entry_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an EntryGroup. |
| <CopyableCode code="projects_locations_entry_groups_delete" /> | `DELETE` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Deletes an EntryGroup. |
| <CopyableCode code="projects_locations_entry_groups_patch" /> | `UPDATE` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Updates an EntryGroup. |

## `SELECT` examples

Lists EntryGroup resources in a project and location.

```sql
SELECT
name,
description,
createTime,
displayName,
etag,
labels,
uid,
updateTime
FROM google.dataplex.entry_groups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entry_groups</code> resource.

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
INSERT INTO google.dataplex.entry_groups (
locationsId,
projectsId,
description,
displayName,
labels,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
uid: string
createTime: string
updateTime: string
description: string
displayName: string
labels: object
etag: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>entry_groups</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.entry_groups
SET 
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
etag = '{{ etag }}'
WHERE 
entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>entry_groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.entry_groups
WHERE entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
