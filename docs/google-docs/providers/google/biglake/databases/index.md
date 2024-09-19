---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.biglake.databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the database. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time of the database. Only set after the database is deleted. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time when this database is considered expired. Only set after the database is deleted. |
| <CopyableCode code="hiveOptions" /> | `object` | Options of a Hive database. |
| <CopyableCode code="type" /> | `string` | The database type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last modification time of the database. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Gets the database specified by the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | List all databases in a specified catalog. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Creates a new database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Deletes an existing database specified by the database ID. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Updates an existing database specified by the database ID. |

## `SELECT` examples

List all databases in a specified catalog.

```sql
SELECT
name,
createTime,
deleteTime,
expireTime,
hiveOptions,
type,
updateTime
FROM google.biglake.databases
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>databases</code> resource.

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
INSERT INTO google.biglake.databases (
catalogsId,
locationsId,
projectsId,
hiveOptions,
type
)
SELECT 
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ hiveOptions }}',
'{{ type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: hiveOptions
      value:
        - name: locationUri
          value: string
        - name: parameters
          value: object
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: deleteTime
      value: string
    - name: expireTime
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>databases</code> resource.

```sql
/*+ update */
UPDATE google.biglake.databases
SET 
hiveOptions = '{{ hiveOptions }}',
type = '{{ type }}'
WHERE 
catalogsId = '{{ catalogsId }}'
AND databasesId = '{{ databasesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM google.biglake.databases
WHERE catalogsId = '{{ catalogsId }}'
AND databasesId = '{{ databasesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
