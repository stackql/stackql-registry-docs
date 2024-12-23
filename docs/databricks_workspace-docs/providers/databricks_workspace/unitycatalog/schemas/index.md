---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - schemas
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

Operations on a <code>schemas</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="browse_only" /> | `boolean` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="catalog_type" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="effective_predictive_optimization_flag" /> | `object` |
| <CopyableCode code="enable_predictive_optimization" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="properties" /> | `object` |
| <CopyableCode code="schema_id" /> | `string` |
| <CopyableCode code="storage_location" /> | `string` |
| <CopyableCode code="storage_root" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="full_name, deployment_name" /> | Gets the specified schema within the metastore. The caller must be a metastore admin, the owner of the schema, or a user that has the |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalog_name, deployment_name" /> | Gets an array of schemas for a catalog in the metastore. If the caller is the metastore admin or the owner of the parent catalog, all schemas for the catalog will be retrieved. Otherwise, only schemas owned by the caller (or for which the caller has the |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new schema for catalog in the Metatastore. The caller must be a metastore admin, or have the |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="full_name, deployment_name" /> | Deletes the specified schema from the parent catalog. The caller must be the owner of the schema or an owner of the parent catalog. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="full_name, deployment_name" /> | Updates a schema for a catalog. The caller must be the owner of the schema or a metastore admin. If the caller is a metastore admin, only the |

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'schemas (get)', value: 'get' },
        { label: 'schemas (list)', value: 'list' }
    ]
}>
<TabItem value="get">

```sql
SELECT
name,
browse_only,
catalog_name,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
full_name,
metastore_id,
owner,
properties,
schema_id,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.schemas
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="list">

```sql
SELECT
name,
browse_only,
catalog_name,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
full_name,
metastore_id,
owner,
properties,
schema_id,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.schemas
WHERE catalog_name = '{{ catalog_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schemas</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'schemas', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.schemas (
deployment_name,
data__name,
data__catalog_name,
data__comment,
data__properties,
data__storage_root
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ catalog_name }}',
'{{ comment }}',
'{{ properties }}',
'{{ storage_root }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: catalog_name
    value: string
  - name: comment
    value: string
  - name: properties
    value:
      property1: string
      property2: string
  - name: storage_root
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>schemas</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.unitycatalog.schemas
SET { field = value }
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>schemas</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.schemas
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```
