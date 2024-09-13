---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - biglake
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

Creates, updates, deletes or gets an <code>catalog</code> resource or lists <code>catalogs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.biglake.catalogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id} |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the catalog. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time of the catalog. Only set after the catalog is deleted. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time when this catalog is considered expired. Only set after the catalog is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last modification time of the catalog. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Gets the catalog specified by the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all catalogs in a specified project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new catalog. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Deletes an existing catalog specified by the catalog ID. |

## `SELECT` examples

List all catalogs in a specified project.

```sql
SELECT
name,
createTime,
deleteTime,
expireTime,
updateTime
FROM google.biglake.catalogs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>catalogs</code> resource.

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
INSERT INTO google.biglake.catalogs (
locationsId,
projectsId,
name,
createTime,
updateTime,
deleteTime,
expireTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ expireTime }}'
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
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: expireTime
        value: '{{ expireTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified catalog resource.

```sql
DELETE FROM google.biglake.catalogs
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
