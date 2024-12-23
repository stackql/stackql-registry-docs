---
title: queries_legacy
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - queries_legacy
  - dbsql
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

Operations on a <code>queries_legacy</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queries_legacy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.queries_legacy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="can_edit" /> | `boolean` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="data_source_id" /> | `string` |
| <CopyableCode code="is_archived" /> | `boolean` |
| <CopyableCode code="is_draft" /> | `boolean` |
| <CopyableCode code="is_favorite" /> | `boolean` |
| <CopyableCode code="is_safe" /> | `boolean` |
| <CopyableCode code="last_modified_by" /> | `object` |
| <CopyableCode code="last_modified_by_id" /> | `integer` |
| <CopyableCode code="latest_query_data_id" /> | `string` |
| <CopyableCode code="options" /> | `object` |
| <CopyableCode code="parent" /> | `string` |
| <CopyableCode code="permission_tier" /> | `string` |
| <CopyableCode code="query" /> | `string` |
| <CopyableCode code="query_hash" /> | `string` |
| <CopyableCode code="run_as_role" /> | `string` |
| <CopyableCode code="tags" /> | `array` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="user" /> | `object` |
| <CopyableCode code="user_id" /> | `integer` |
| <CopyableCode code="visualizations" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="query_id, deployment_name" /> | Retrieve a query object definition along with contextual permissions information about the currently authenticated user. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets a list of queries. Optionally, this list can be filtered by a search term. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new query definition. Queries created with this endpoint belong to the authenticated user making the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="query_id, deployment_name" /> | Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and they cannot be used for alerts. The trash is deleted after 30 days. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="query_id, deployment_name" /> | Modify this query definition. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="query_id, deployment_name" /> | Restore a query that has been moved to the trash. A restored query appears in list views and searches. You can use restored queries for alerts. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'queries_legacy (list)', value: 'list' },
        { label: 'queries_legacy (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
description,
can_edit,
created_at,
data_source_id,
is_archived,
is_draft,
is_favorite,
is_safe,
last_modified_by,
last_modified_by_id,
latest_query_data_id,
options,
parent,
permission_tier,
query,
query_hash,
run_as_role,
tags,
updated_at,
user,
user_id,
visualizations
FROM databricks_workspace.dbsql.queries_legacy
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
description,
can_edit,
created_at,
data_source_id,
is_archived,
is_draft,
is_favorite,
is_safe,
last_modified_by,
last_modified_by_id,
latest_query_data_id,
options,
parent,
permission_tier,
query,
query_hash,
run_as_role,
tags,
updated_at,
user,
user_id,
visualizations
FROM databricks_workspace.dbsql.queries_legacy
WHERE query_id = '{{ query_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queries_legacy</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'queries_legacy', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.dbsql.queries_legacy (
deployment_name,
data__data_source_id,
data__query,
data__name,
data__parent,
data__description,
data__options,
data__run_as_role,
data__tags
)
SELECT 
'{{ deployment_name }}',
'{{ data_source_id }}',
'{{ query }}',
'{{ name }}',
'{{ parent }}',
'{{ description }}',
'{{ options }}',
'{{ run_as_role }}',
'{{ tags }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: data_source_id
    value: 0c205e24-5db2-4940-adb1-fb13c7ce960b
  - name: query
    value: SELECT field FROM table WHERE field = {{ param }}
  - name: name
    value: Orders by month by customer
  - name: parent
    value: folders/2025532471912059
  - name: description
    value: Summarizes total order dollars for customers in the Europe/Asia region.
  - name: options
    value:
      parameters:
      - title: customer
        name: param
        type: text
        value: acme
  - name: run_as_role
    value: viewer
  - name: tags
    value:
    - Payroll

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>queries_legacy</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.dbsql.queries_legacy
SET { field = value }
WHERE query_id = '{{ query_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>queries_legacy</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.dbsql.queries_legacy
WHERE query_id = '{{ query_id }}' AND
deployment_name = '{{ deployment_name }}';
```
