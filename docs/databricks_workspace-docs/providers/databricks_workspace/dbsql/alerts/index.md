---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - alerts
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

Operations on a <code>alerts</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="condition" /> | `object` |
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="lifecycle_state" /> | `string` |
| <CopyableCode code="owner_user_name" /> | `string` |
| <CopyableCode code="parent_path" /> | `string` |
| <CopyableCode code="query_id" /> | `string` |
| <CopyableCode code="seconds_to_retrigger" /> | `integer` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="update_time" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Gets an alert. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets a list of alerts accessible to the user, ordered by creation time. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates an alert. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Moves an alert to the trash. Trashed alerts immediately disappear from searches and list views, and can no longer trigger. You can restore a trashed alert through the UI. A trashed alert is permanently deleted after 30 days. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Updates an alert. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'alerts (list)', value: 'list' },
        { label: 'alerts (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
condition,
create_time,
display_name,
lifecycle_state,
owner_user_name,
parent_path,
query_id,
seconds_to_retrigger,
state,
update_time
FROM databricks_workspace.dbsql.alerts
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
condition,
create_time,
display_name,
lifecycle_state,
owner_user_name,
parent_path,
query_id,
seconds_to_retrigger,
state,
update_time
FROM databricks_workspace.dbsql.alerts
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>alerts</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'alerts', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.dbsql.alerts (
deployment_name,
data__alert
)
SELECT 
'{{ deployment_name }}',
'{{ alert }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: alert
    value:
      seconds_to_retrigger: 0
      display_name: Test alert
      condition:
        op: GREATER_THAN
        operand:
          column:
            name: foo
        threshold:
          value:
            double_value: 1
      query_id: dee5cca8-1c79-4b5e-a71m1-e7f9d241bdf6
      parent_path: /Workspace/Users/user.name@acme.com

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>alerts</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.dbsql.alerts
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>alerts</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.dbsql.alerts
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
