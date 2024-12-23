---
title: alerts_legacy
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - alerts_legacy
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

Operations on a <code>alerts_legacy</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_legacy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.alerts_legacy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="last_triggered_at" /> | `string` |
| <CopyableCode code="options" /> | `object` |
| <CopyableCode code="parent" /> | `string` |
| <CopyableCode code="query" /> | `object` |
| <CopyableCode code="rearm" /> | `integer` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="user" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alert_id, deployment_name" /> | Gets an alert. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets a list of alerts. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a condition of its result, and notifies users or notification destinations if the condition was met. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="alert_id, deployment_name" /> | Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="alert_id, deployment_name" /> | Updates an alert. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'alerts_legacy (list)', value: 'list' },
        { label: 'alerts_legacy (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
created_at,
last_triggered_at,
options,
parent,
query,
rearm,
state,
updated_at,
user
FROM databricks_workspace.dbsql.alerts_legacy
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
created_at,
last_triggered_at,
options,
parent,
query,
rearm,
state,
updated_at,
user
FROM databricks_workspace.dbsql.alerts_legacy
WHERE alert_id = '{{ alert_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>alerts_legacy</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'alerts_legacy', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.dbsql.alerts_legacy (
deployment_name,
data__name,
data__options,
data__query_id,
data__rearm,
data__parent
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ options }}',
'{{ query_id }}',
'{{ rearm }}',
'{{ parent }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: Total Trips > 300
  - name: options
    value:
      column: total_trips
      custom_body: Total trips exceeded
      custom_subject: The total trips has exceeded 300.
      muted: false
      op: '>'
      value: null
      empty_result_state: unknown
  - name: query_id
    value: dee5cca8-1c79-4b5e-a711-e7f9d241bdf6
  - name: rearm
    value: 0
  - name: parent
    value: folders/2025532471912059

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>alerts_legacy</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.dbsql.alerts_legacy
SET { field = value }
WHERE alert_id = '{{ alert_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>alerts_legacy</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.dbsql.alerts_legacy
WHERE alert_id = '{{ alert_id }}' AND
deployment_name = '{{ deployment_name }}';
```
