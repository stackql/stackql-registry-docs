---
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
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

Creates, updates, deletes or gets an <code>entry</code> resource or lists <code>entries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The relative resource name of the entry, in the format projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}. |
| <CopyableCode code="aspects" /> | `object` | Optional. The aspects that are attached to the entry. Depending on how the aspect is attached to the entry, the format of the aspect key can be one of the following: If the aspect is attached directly to the entry: {project_id_or_number}.{location_id}.{aspect_type_id} If the aspect is attached to an entry's path: {project_id_or_number}.{location_id}.{aspect_type_id}@{path} |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the entry was created in Dataplex. |
| <CopyableCode code="entrySource" /> | `object` | Information related to the source system of the data resource that is represented by the entry. |
| <CopyableCode code="entryType" /> | `string` | Required. Immutable. The relative resource name of the entry type that was used to create this entry, in the format projects/{project_id_or_number}/locations/{location_id}/entryTypes/{entry_type_id}. |
| <CopyableCode code="fullyQualifiedName" /> | `string` | Optional. A name for the entry that can be referenced by an external system. For more information, see Fully qualified names (https://cloud.google.com/data-catalog/docs/fully-qualified-names). The maximum size of the field is 4000 characters. |
| <CopyableCode code="parentEntry" /> | `string` | Optional. Immutable. The resource name of the parent entry. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the entry was last updated in Dataplex. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_entries_get" /> | `SELECT` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Gets an Entry. |
| <CopyableCode code="projects_locations_entry_groups_entries_list" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Lists Entries within an EntryGroup. |
| <CopyableCode code="projects_locations_entry_groups_entries_create" /> | `INSERT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Creates an Entry. |
| <CopyableCode code="projects_locations_entry_groups_entries_delete" /> | `DELETE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Deletes an Entry. |
| <CopyableCode code="projects_locations_entry_groups_entries_patch" /> | `UPDATE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Updates an Entry. |

## `SELECT` examples

Lists Entries within an EntryGroup.

```sql
SELECT
name,
aspects,
createTime,
entrySource,
entryType,
fullyQualifiedName,
parentEntry,
updateTime
FROM google.dataplex.entries
WHERE entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entries</code> resource.

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
INSERT INTO google.dataplex.entries (
entryGroupsId,
locationsId,
projectsId,
name,
entryType,
createTime,
updateTime,
aspects,
parentEntry,
fullyQualifiedName,
entrySource
)
SELECT 
'{{ entryGroupsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ entryType }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ aspects }}',
'{{ parentEntry }}',
'{{ fullyQualifiedName }}',
'{{ entrySource }}'
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
      - name: entryType
        value: '{{ entryType }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: aspects
        value: '{{ aspects }}'
      - name: parentEntry
        value: '{{ parentEntry }}'
      - name: fullyQualifiedName
        value: '{{ fullyQualifiedName }}'
      - name: entrySource
        value: '{{ entrySource }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a entry only if the necessary resources are available.

```sql
UPDATE google.dataplex.entries
SET 
name = '{{ name }}',
entryType = '{{ entryType }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
aspects = '{{ aspects }}',
parentEntry = '{{ parentEntry }}',
fullyQualifiedName = '{{ fullyQualifiedName }}',
entrySource = '{{ entrySource }}'
WHERE 
entriesId = '{{ entriesId }}'
AND entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified entry resource.

```sql
DELETE FROM google.dataplex.entries
WHERE entriesId = '{{ entriesId }}'
AND entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
