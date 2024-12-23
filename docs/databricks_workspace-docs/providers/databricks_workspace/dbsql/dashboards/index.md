---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dashboards
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

Operations on a <code>dashboards</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="can_edit" /> | `boolean` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="dashboard_filters_enabled" /> | `boolean` |
| <CopyableCode code="is_archived" /> | `boolean` |
| <CopyableCode code="is_draft" /> | `boolean` |
| <CopyableCode code="is_favorite" /> | `boolean` |
| <CopyableCode code="options" /> | `object` |
| <CopyableCode code="parent" /> | `string` |
| <CopyableCode code="permission_tier" /> | `string` |
| <CopyableCode code="slug" /> | `string` |
| <CopyableCode code="tags" /> | `array` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="user" /> | `object` |
| <CopyableCode code="user_id" /> | `integer` |
| <CopyableCode code="widgets" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dashboard_id, deployment_name" /> | Returns a JSON representation of a dashboard object, including its visualization and query objects. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Fetch a paginated list of dashboard objects. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dashboard_id, deployment_name" /> | Moves a dashboard to the trash. Trashed dashboards do not appear in list views or searches, and cannot be shared. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dashboard_id, deployment_name" /> | Modify this dashboard definition. This operation only affects attributes of the dashboard object. It does not add, modify, or remove widgets. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="dashboard_id, deployment_name" /> | A restored dashboard appears in list views and searches and can be shared. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'dashboards (list)', value: 'list' },
        { label: 'dashboards (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
can_edit,
created_at,
dashboard_filters_enabled,
is_archived,
is_draft,
is_favorite,
options,
parent,
permission_tier,
slug,
tags,
updated_at,
user,
user_id,
widgets
FROM databricks_workspace.dbsql.dashboards
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
can_edit,
created_at,
dashboard_filters_enabled,
is_archived,
is_draft,
is_favorite,
options,
parent,
permission_tier,
slug,
tags,
updated_at,
user,
user_id,
widgets
FROM databricks_workspace.dbsql.dashboards
WHERE dashboard_id = '{{ dashboard_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dashboards</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'dashboards', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.dbsql.dashboards (
deployment_name,
data__name,
data__parent,
data__tags,
data__is_favorite,
data__run_as_role,
data__dashboard_filters_enabled
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ parent }}',
'{{ tags }}',
'{{ is_favorite }}',
'{{ run_as_role }}',
'{{ dashboard_filters_enabled }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: Sales Dashboard
  - name: parent
    value: folders/2025532471912059
  - name: tags
    value:
    - Payroll
  - name: is_favorite
    value: true
  - name: run_as_role
    value: viewer
  - name: dashboard_filters_enabled
    value: true

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dashboards</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.dbsql.dashboards
SET { field = value }
WHERE dashboard_id = '{{ dashboard_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>dashboards</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.dbsql.dashboards
WHERE dashboard_id = '{{ dashboard_id }}' AND
deployment_name = '{{ deployment_name }}';
```
