---
title: quality_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - quality_monitors
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

Operations on a <code>quality_monitors</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quality_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.quality_monitors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="assets_dir" /> | `string` |
| <CopyableCode code="baseline_table_name" /> | `string` |
| <CopyableCode code="custom_metrics" /> | `array` |
| <CopyableCode code="dashboard_id" /> | `string` |
| <CopyableCode code="drift_metrics_table_name" /> | `string` |
| <CopyableCode code="inference_log" /> | `object` |
| <CopyableCode code="latest_monitor_failure_msg" /> | `string` |
| <CopyableCode code="monitor_version" /> | `string` |
| <CopyableCode code="notifications" /> | `object` |
| <CopyableCode code="output_schema_name" /> | `string` |
| <CopyableCode code="profile_metrics_table_name" /> | `string` |
| <CopyableCode code="schedule" /> | `object` |
| <CopyableCode code="slicing_exprs" /> | `array` |
| <CopyableCode code="snapshot" /> | `object` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="table_name" /> | `string` |
| <CopyableCode code="time_series" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="table_name, deployment_name" /> | Gets a monitor for the specified table. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="table_name, deployment_name" /> | Creates a new monitor for the specified table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="table_name, deployment_name" /> | Deletes a monitor for the specified table. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="table_name, deployment_name" /> | Updates a monitor for the specified table. |

## `SELECT` examples

```sql
SELECT
assets_dir,
baseline_table_name,
custom_metrics,
dashboard_id,
drift_metrics_table_name,
inference_log,
latest_monitor_failure_msg,
monitor_version,
notifications,
output_schema_name,
profile_metrics_table_name,
schedule,
slicing_exprs,
snapshot,
status,
table_name,
time_series
FROM databricks_workspace.unitycatalog.quality_monitors
WHERE table_name = '{{ table_name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>quality_monitors</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'quality_monitors', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.quality_monitors (
table_name,
deployment_name,
data__skip_builtin_dashboard,
data__warehouse_id,
data__assets_dir,
data__output_schema_name,
data__inference_log,
data__time_series,
data__snapshot,
data__slicing_exprs,
data__custom_metrics,
data__baseline_table_name,
data__schedule,
data__notifications
)
SELECT 
'{{ table_name }}',
'{{ deployment_name }}',
'{{ skip_builtin_dashboard }}',
'{{ warehouse_id }}',
'{{ assets_dir }}',
'{{ output_schema_name }}',
'{{ inference_log }}',
'{{ time_series }}',
'{{ snapshot }}',
'{{ slicing_exprs }}',
'{{ custom_metrics }}',
'{{ baseline_table_name }}',
'{{ schedule }}',
'{{ notifications }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: skip_builtin_dashboard
    value: true
  - name: warehouse_id
    value: string
  - name: assets_dir
    value: string
  - name: output_schema_name
    value: string
  - name: inference_log
    value:
      problem_type: PROBLEM_TYPE_CLASSIFICATION
      timestamp_col: string
      granularities:
      - string
      prediction_col: string
      label_col: string
      model_id_col: string
      prediction_proba_col: string
  - name: time_series
    value:
      timestamp_col: string
      granularities:
      - string
  - name: snapshot
    value: {}
  - name: slicing_exprs
    value:
    - string
  - name: custom_metrics
    value:
    - name: string
      definition: string
      input_columns:
      - string
      output_data_type: string
      type: CUSTOM_METRIC_TYPE_AGGREGATE
  - name: baseline_table_name
    value: string
  - name: schedule
    value:
      quartz_cron_expression: string
      timezone_id: string
      pause_status: UNPAUSED
  - name: notifications
    value:
      on_failure:
        email_addresses:
        - string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>quality_monitors</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.quality_monitors
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE table_name = '{{ table_name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>quality_monitors</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.quality_monitors
WHERE table_name = '{{ table_name }}' AND
deployment_name = '{{ deployment_name }}';
```
