
---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
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

Creates, updates, deletes or gets an <code>table</code> resource or lists <code>tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.biglake.tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id} |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the table. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time of the table. Only set after the table is deleted. |
| <CopyableCode code="etag" /> | `string` | The checksum of a table object computed by the server based on the value of other fields. It may be sent on update requests to ensure the client has an up-to-date value before proceeding. It is only checked for update table operations. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time when this table is considered expired. Only set after the table is deleted. |
| <CopyableCode code="hiveOptions" /> | `object` | Options of a Hive table. |
| <CopyableCode code="type" /> | `string` | The table type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last modification time of the table. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Gets the table specified by the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | List all tables in a specified database. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Creates a new table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Deletes an existing table specified by the table ID. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Updates an existing table specified by the table ID. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Renames an existing table specified by the table ID. |

## `SELECT` examples

List all tables in a specified database.

```sql
SELECT
name,
createTime,
deleteTime,
etag,
expireTime,
hiveOptions,
type,
updateTime
FROM google.biglake.tables
WHERE catalogsId = '{{ catalogsId }}'
AND databasesId = '{{ databasesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tables</code> resource.

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
INSERT INTO google.biglake.tables (
catalogsId,
databasesId,
locationsId,
projectsId,
hiveOptions,
name,
createTime,
updateTime,
deleteTime,
expireTime,
type,
etag
)
SELECT 
'{{ catalogsId }}',
'{{ databasesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ hiveOptions }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ expireTime }}',
'{{ type }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: hiveOptions
        value: '{{ hiveOptions }}'
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
      - name: type
        value: '{{ type }}'
      - name: etag
        value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a table only if the necessary resources are available.

```sql
UPDATE google.biglake.tables
SET 
hiveOptions = '{{ hiveOptions }}',
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
expireTime = '{{ expireTime }}',
type = '{{ type }}',
etag = '{{ etag }}'
WHERE 
catalogsId = '{{ catalogsId }}'
AND databasesId = '{{ databasesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tablesId = '{{ tablesId }}';
```

## `DELETE` example

Deletes the specified table resource.

```sql
DELETE FROM google.biglake.tables
WHERE catalogsId = '{{ catalogsId }}'
AND databasesId = '{{ databasesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tablesId = '{{ tablesId }}';
```
