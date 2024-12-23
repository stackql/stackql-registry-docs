---
title: dashboard_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dashboard_schedules
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

Operations on a <code>dashboard_schedules</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.lakeview.dashboard_schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="cron_schedule" /> | `object` |
| <CopyableCode code="dashboard_id" /> | `string` |
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="pause_status" /> | `string` |
| <CopyableCode code="schedule_id" /> | `string` |
| <CopyableCode code="update_time" /> | `string` |
| <CopyableCode code="warehouse_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getschedule" /> | `SELECT` | <CopyableCode code="dashboard_id, schedule_id, deployment_name" /> |  |
| <CopyableCode code="listschedules" /> | `SELECT` | <CopyableCode code="dashboard_id, deployment_name" /> |  |
| <CopyableCode code="createschedule" /> | `INSERT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="deleteschedule" /> | `DELETE` | <CopyableCode code="dashboard_id, schedule_id, deployment_name" /> |  |
| <CopyableCode code="updateschedule" /> | `UPDATE` | <CopyableCode code="deployment_name" /> |  |

## `SELECT` examples

<Tabs
    defaultValue="listschedules"
    values={[
        { label: 'dashboard_schedules (listschedules)', value: 'listschedules' },
        { label: 'dashboard_schedules (getschedule)', value: 'getschedule' }
    ]
}>
<TabItem value="listschedules">

```sql
SELECT
create_time,
cron_schedule,
dashboard_id,
display_name,
etag,
pause_status,
schedule_id,
update_time,
warehouse_id
FROM databricks_workspace.lakeview.dashboard_schedules
WHERE dashboard_id = '{{ dashboard_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getschedule">

```sql
SELECT
create_time,
cron_schedule,
dashboard_id,
display_name,
etag,
pause_status,
schedule_id,
update_time,
warehouse_id
FROM databricks_workspace.lakeview.dashboard_schedules
WHERE dashboard_id = '{{ dashboard_id }}' AND
schedule_id = '{{ schedule_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dashboard_schedules</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'dashboard_schedules', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.lakeview.dashboard_schedules (
deployment_name,
data__cron_schedule,
data__pause_status,
data__display_name,
data__etag,
data__warehouse_id
)
SELECT 
'{{ deployment_name }}',
'{{ cron_schedule }}',
'{{ pause_status }}',
'{{ display_name }}',
'{{ etag }}',
'{{ warehouse_id }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: cron_schedule
    value:
      quartz_cron_expression: 0 0 8 * * ?
      timezone_id: Europe/London
  - name: pause_status
    value: UNPAUSED
  - name: display_name
    value: Monthly Traffic Report Snapshot
  - name: etag
    value: '80611980'
  - name: warehouse_id
    value: 47bb1c472649e711

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dashboard_schedules</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.lakeview.dashboard_schedules
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>dashboard_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.lakeview.dashboard_schedules
WHERE dashboard_id = '{{ dashboard_id }}' AND
schedule_id = '{{ schedule_id }}' AND
deployment_name = '{{ deployment_name }}';
```
