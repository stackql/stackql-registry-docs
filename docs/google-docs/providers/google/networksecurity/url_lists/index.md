---
title: url_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - url_lists
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

Creates, updates, deletes, gets or lists a <code>url_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>url_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.url_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the resource provided by the user. Name is of the form projects/{project}/locations/{location}/urlLists/{url_list} url_list should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the security policy was created. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the security policy was updated. |
| <CopyableCode code="values" /> | `array` | Required. FQDNs and URLs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_url_lists_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, urlListsId" /> | Gets details of a single UrlList. |
| <CopyableCode code="projects_locations_url_lists_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists UrlLists in a given project and location. |
| <CopyableCode code="projects_locations_url_lists_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new UrlList in a given project and location. |
| <CopyableCode code="projects_locations_url_lists_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, urlListsId" /> | Deletes a single UrlList. |
| <CopyableCode code="projects_locations_url_lists_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, urlListsId" /> | Updates the parameters of a single UrlList. |

## `SELECT` examples

Lists UrlLists in a given project and location.

```sql
SELECT
name,
description,
createTime,
updateTime,
values
FROM google.networksecurity.url_lists
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>url_lists</code> resource.

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
INSERT INTO google.networksecurity.url_lists (
locationsId,
projectsId,
name,
createTime,
updateTime,
description,
values
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ values }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: description
      value: '{{ description }}'
    - name: values
      value: '{{ values }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>url_lists</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.url_lists
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
values = '{{ values }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND urlListsId = '{{ urlListsId }}';
```

## `DELETE` example

Deletes the specified <code>url_lists</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.url_lists
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND urlListsId = '{{ urlListsId }}';
```
