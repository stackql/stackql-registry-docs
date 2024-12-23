---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dashboards
  - lakeview
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
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.lakeview.dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="dashboard_id" /> | `string` |
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="lifecycle_state" /> | `string` |
| <CopyableCode code="parent_path" /> | `string` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="serialized_dashboard" /> | `string` |
| <CopyableCode code="update_time" /> | `string` |
| <CopyableCode code="warehouse_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dashboard_id, deployment_name" /> | Get a draft dashboard. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a draft dashboard. |
| <CopyableCode code="trash" /> | `DELETE` | <CopyableCode code="dashboard_id, deployment_name" /> | Trash a dashboard. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Update a draft dashboard. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Migrates a classic SQL dashboard to Lakeview. |
| <CopyableCode code="publish" /> | `EXEC` | <CopyableCode code="dashboard_id, deployment_name" /> | Publish the current draft dashboard. |
| <CopyableCode code="unpublish" /> | `EXEC` | <CopyableCode code="dashboard_id, deployment_name" /> | Unpublish the dashboard. |

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
create_time,
dashboard_id,
display_name,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time,
warehouse_id
FROM databricks_workspace.lakeview.dashboards
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
create_time,
dashboard_id,
display_name,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time,
warehouse_id
FROM databricks_workspace.lakeview.dashboards
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
INSERT INTO databricks_workspace.lakeview.dashboards (
deployment_name,
data__display_name,
data__warehouse_id,
data__etag,
data__serialized_dashboard,
data__parent_path
)
SELECT 
'{{ deployment_name }}',
'{{ display_name }}',
'{{ warehouse_id }}',
'{{ etag }}',
'{{ serialized_dashboard }}',
'{{ parent_path }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: display_name
    value: Monthly Traffic Report
  - name: warehouse_id
    value: 47bb1c472649e711
  - name: etag
    value: '80611980'
  - name: serialized_dashboard
    value: '{"pages":[{"name":"b532570b","displayName":"New Page"}]}'
  - name: parent_path
    value: /path/to/dir

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dashboards</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.lakeview.dashboards
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>dashboards</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.lakeview.dashboards
WHERE dashboard_id = '{{ dashboard_id }}' AND
deployment_name = '{{ deployment_name }}';
```
