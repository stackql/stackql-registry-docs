---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - volumes
  - unitycatalog
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>volumes</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.volumes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="schema_name" /> | `string` |
| <CopyableCode code="storage_location" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |
| <CopyableCode code="volume_id" /> | `string` |
| <CopyableCode code="volume_type" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalog_name, schema_name, deployment_name" /> | Gets an array of volumes for the current metastore under the parent catalog and schema. |
| <CopyableCode code="read" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets a volume from the metastore for a specific catalog and schema. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new volume. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes a volume from the specified parent catalog and schema. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the specified volume under the specified parent catalog and schema. |

## `SELECT` examples

<Tabs
    defaultValue="read"
    values={[
        { label: 'volumes (read)', value: 'read' },
        { label: 'volumes (list)', value: 'list' }
    ]
}>
<TabItem value="read">

```sql
SELECT
name,
catalog_name,
comment,
created_at,
created_by,
full_name,
metastore_id,
owner,
schema_name,
storage_location,
updated_at,
updated_by,
volume_id,
volume_type
FROM databricks_workspace.unitycatalog.volumes
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="list">

```sql
SELECT
name,
catalog_name,
comment,
created_at,
created_by,
full_name,
metastore_id,
owner,
schema_name,
storage_location,
updated_at,
updated_by,
volume_id,
volume_type
FROM databricks_workspace.unitycatalog.volumes
WHERE catalog_name = '{{ catalog_name }}' AND
schema_name = '{{ schema_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volumes</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'volumes', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.volumes (
deployment_name,
data__catalog_name,
data__schema_name,
data__name,
data__volume_type,
data__storage_location,
data__comment
)
SELECT 
'{{ deployment_name }}',
'{{ catalog_name }}',
'{{ schema_name }}',
'{{ name }}',
'{{ volume_type }}',
'{{ storage_location }}',
'{{ comment }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: catalog_name
    value: main
  - name: schema_name
    value: default
  - name: name
    value: my_volume
  - name: volume_type
    value: EXTERNAL
  - name: storage_location
    value: s3://my-bucket/hello/world/my-volume
  - name: comment
    value: This is my first volume

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>volumes</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.volumes
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>volumes</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.volumes
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
