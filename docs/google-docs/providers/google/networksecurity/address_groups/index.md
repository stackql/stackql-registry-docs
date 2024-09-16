---
title: address_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - address_groups
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>address_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>address_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.address_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_address_groups_get" /> | `SELECT` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Gets details of a single address group. |
| <CopyableCode code="organizations_locations_address_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists address groups in a given project and location. |
| <CopyableCode code="projects_locations_address_groups_get" /> | `SELECT` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Gets details of a single address group. |
| <CopyableCode code="projects_locations_address_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists address groups in a given project and location. |
| <CopyableCode code="organizations_locations_address_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new address group in a given project and location. |
| <CopyableCode code="projects_locations_address_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new address group in a given project and location. |
| <CopyableCode code="organizations_locations_address_groups_delete" /> | `DELETE` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Deletes an address group. |
| <CopyableCode code="projects_locations_address_groups_delete" /> | `DELETE` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Deletes a single address group. |
| <CopyableCode code="organizations_locations_address_groups_patch" /> | `UPDATE` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Updates parameters of an address group. |
| <CopyableCode code="projects_locations_address_groups_patch" /> | `UPDATE` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Updates the parameters of a single address group. |
| <CopyableCode code="organizations_locations_address_groups_clone_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Clones items from one address group to another. |
| <CopyableCode code="projects_locations_address_groups_clone_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Clones items from one address group to another. |

## `SELECT` examples

Lists address groups in a given project and location.

```sql
SELECT
column_anon
FROM google.networksecurity.address_groups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>address_groups</code> resource.

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
INSERT INTO google.networksecurity.address_groups (
locationsId,
projectsId,
name,
description,
createTime,
updateTime,
labels,
type,
items,
capacity,
selfLink,
purpose
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ type }}',
'{{ items }}',
'{{ capacity }}',
'{{ selfLink }}',
'{{ purpose }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: type
      value: '{{ type }}'
    - name: items
      value: '{{ items }}'
    - name: capacity
      value: '{{ capacity }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: purpose
      value: '{{ purpose }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>address_groups</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.address_groups
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
type = '{{ type }}',
items = '{{ items }}',
capacity = '{{ capacity }}',
selfLink = '{{ selfLink }}',
purpose = '{{ purpose }}'
WHERE 
addressGroupsId = '{{ addressGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>address_groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.address_groups
WHERE addressGroupsId = '{{ addressGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
