---
title: entry_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entry_types
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

Creates, updates, deletes, gets or lists a <code>entry_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entry_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.entry_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the EntryType, of the form: projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the EntryType. |
| <CopyableCode code="authorization" /> | `object` | Authorization for an Entry Type. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the EntryType was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | Optional. This checksum is computed by the service, and might be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the EntryType. |
| <CopyableCode code="platform" /> | `string` | Optional. The platform that Entries of this type belongs to. |
| <CopyableCode code="requiredAspects" /> | `array` | AspectInfo for the entry type. |
| <CopyableCode code="system" /> | `string` | Optional. The system that Entries of this type belongs to. Examples include CloudSQL, MariaDB etc |
| <CopyableCode code="typeAliases" /> | `array` | Optional. Indicates the classes this Entry Type belongs to, for example, TABLE, DATABASE, MODEL. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the EntryType. This ID will be different if the EntryType is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the EntryType was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_types_get" /> | `SELECT` | <CopyableCode code="entryTypesId, locationsId, projectsId" /> | Gets an EntryType. |
| <CopyableCode code="projects_locations_entry_types_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists EntryType resources in a project and location. |
| <CopyableCode code="projects_locations_entry_types_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an EntryType. |
| <CopyableCode code="projects_locations_entry_types_delete" /> | `DELETE` | <CopyableCode code="entryTypesId, locationsId, projectsId" /> | Deletes an EntryType. |
| <CopyableCode code="projects_locations_entry_types_patch" /> | `UPDATE` | <CopyableCode code="entryTypesId, locationsId, projectsId" /> | Updates an EntryType. |

## `SELECT` examples

Lists EntryType resources in a project and location.

```sql
SELECT
name,
description,
authorization,
createTime,
displayName,
etag,
labels,
platform,
requiredAspects,
system,
typeAliases,
uid,
updateTime
FROM google.dataplex.entry_types
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entry_types</code> resource.

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
INSERT INTO google.dataplex.entry_types (
locationsId,
projectsId,
description,
displayName,
labels,
etag,
typeAliases,
platform,
system,
requiredAspects,
authorization
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ etag }}',
'{{ typeAliases }}',
'{{ platform }}',
'{{ system }}',
'{{ requiredAspects }}',
'{{ authorization }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: description
      value: '{{ description }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: labels
      value: '{{ labels }}'
    - name: etag
      value: '{{ etag }}'
    - name: typeAliases
      value:
        - name: type
          value: '{{ type }}'
    - name: platform
      value: '{{ platform }}'
    - name: system
      value: '{{ system }}'
    - name: requiredAspects
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: authorization
      value:
        - name: alternateUsePermission
          value: '{{ alternateUsePermission }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>entry_types</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.entry_types
SET 
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
typeAliases = '{{ typeAliases }}',
platform = '{{ platform }}',
system = '{{ system }}',
requiredAspects = '{{ requiredAspects }}',
authorization = '{{ authorization }}'
WHERE 
entryTypesId = '{{ entryTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>entry_types</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.entry_types
WHERE entryTypesId = '{{ entryTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
