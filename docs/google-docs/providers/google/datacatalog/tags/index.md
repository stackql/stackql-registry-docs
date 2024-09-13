---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - datacatalog
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

Creates, updates, deletes or gets an <code>tag</code> resource or lists <code>tags</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the tag in URL format where tag ID is a system-generated identifier. Note: The tag itself might not be stored in the location specified in its name. |
| <CopyableCode code="column" /> | `string` | Resources like entry can have schemas associated with them. This scope allows you to attach tags to an individual column based on that schema. To attach a tag to a nested column, separate column names with a dot (`.`). Example: `column.nested_column`. |
| <CopyableCode code="fields" /> | `object` | Required. Maps the ID of a tag field to its value and additional information about that field. Tag template defines valid field IDs. A tag must have at least 1 field and at most 500 fields. |
| <CopyableCode code="template" /> | `string` | Required. The resource name of the tag template this tag uses. Example: `projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE_ID}` This field cannot be modified after creation. |
| <CopyableCode code="templateDisplayName" /> | `string` | Output only. The display name of the tag template. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_entries_tags_list" /> | `SELECT` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| <CopyableCode code="projects_locations_entry_groups_tags_list" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_create" /> | `INSERT` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Creates a tag and assigns it to: * An Entry if the method name is `projects.locations.entryGroups.entries.tags.create`. * Or EntryGroupif the method name is `projects.locations.entryGroups.tags.create`. Note: The project identified by the `parent` parameter for the [tag] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters) and the [tag template] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters) used to create the tag must be in the same organization. |
| <CopyableCode code="projects_locations_entry_groups_tags_create" /> | `INSERT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Creates a tag and assigns it to: * An Entry if the method name is `projects.locations.entryGroups.entries.tags.create`. * Or EntryGroupif the method name is `projects.locations.entryGroups.tags.create`. Note: The project identified by the `parent` parameter for the [tag] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters) and the [tag template] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters) used to create the tag must be in the same organization. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_delete" /> | `DELETE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId, tagsId" /> | Deletes a tag. |
| <CopyableCode code="projects_locations_entry_groups_tags_delete" /> | `DELETE` | <CopyableCode code="entryGroupsId, locationsId, projectsId, tagsId" /> | Deletes a tag. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_patch" /> | `UPDATE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId, tagsId" /> | Updates an existing tag. |
| <CopyableCode code="projects_locations_entry_groups_tags_patch" /> | `UPDATE` | <CopyableCode code="entryGroupsId, locationsId, projectsId, tagsId" /> | Updates an existing tag. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_reconcile" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | `ReconcileTags` creates or updates a list of tags on the entry. If the ReconcileTagsRequest.force_delete_missing parameter is set, the operation deletes tags not included in the input tag list. `ReconcileTags` returns a long-running operation resource that can be queried with Operations.GetOperation to return ReconcileTagsMetadata and a ReconcileTagsResponse message. |

## `SELECT` examples

Lists tags assigned to an Entry. The columns in the response are lowercased.

```sql
SELECT
name,
column,
fields,
template,
templateDisplayName
FROM google.datacatalog.tags
WHERE entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tags</code> resource.

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
INSERT INTO google.datacatalog.tags (
entryGroupsId,
locationsId,
projectsId,
name,
template,
templateDisplayName,
column,
fields
)
SELECT 
'{{ entryGroupsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ template }}',
'{{ templateDisplayName }}',
'{{ column }}',
'{{ fields }}'
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
      - name: template
        value: '{{ template }}'
      - name: templateDisplayName
        value: '{{ templateDisplayName }}'
      - name: column
        value: '{{ column }}'
      - name: fields
        value: '{{ fields }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a tag only if the necessary resources are available.

```sql
UPDATE google.datacatalog.tags
SET 
name = '{{ name }}',
template = '{{ template }}',
templateDisplayName = '{{ templateDisplayName }}',
column = '{{ column }}',
fields = '{{ fields }}'
WHERE 
entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tagsId = '{{ tagsId }}';
```

## `DELETE` example

Deletes the specified tag resource.

```sql
DELETE FROM google.datacatalog.tags
WHERE entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tagsId = '{{ tagsId }}';
```
