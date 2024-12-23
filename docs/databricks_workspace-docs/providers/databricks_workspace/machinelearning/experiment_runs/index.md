---
title: experiment_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - experiment_runs
  - machinelearning
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

Operations on a <code>experiment_runs</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiment_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="data" /> | `object` |
| <CopyableCode code="info" /> | `object` |
| <CopyableCode code="inputs" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getrun" /> | `SELECT` | <CopyableCode code="run_id, deployment_name" /> | Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the same key are logged for a run, return only the value with the latest timestamp. |
| <CopyableCode code="searchruns" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Searches for runs that satisfy expressions. |
| <CopyableCode code="createrun" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new run within an experiment. A run is usually a single execution of a machine learning or data ETL pipeline. MLflow uses runs to track the |
| <CopyableCode code="deleterun" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Marks a run for deletion. |
| <CopyableCode code="deleteruns" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Bulk delete runs in an experiment that were created prior to or at the specified timestamp. Deletes at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the client code snippet on |
| <CopyableCode code="updaterun" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates run metadata. |
| <CopyableCode code="logbatch" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server will respond with an error (non-200 status code). |
| <CopyableCode code="loginputs" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Experimental: This API may change or be removed in a future release without warning. |
| <CopyableCode code="logmetric" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Logs a metric for a run. A metric is a key-value pair (string key, float value) with an associated timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be logged multiple times. |
| <CopyableCode code="logmodel" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Experimental: This API may change or be removed in a future release without warning. |
| <CopyableCode code="logparam" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A param can be logged only once for a run. |
| <CopyableCode code="restorerun" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Restores a deleted run. |
| <CopyableCode code="restoreruns" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Bulk restore runs in an experiment that were deleted no earlier than the specified timestamp. Restores at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the client code snippet on |

## `SELECT` examples

<Tabs
    defaultValue="searchruns"
    values={[
        { label: 'experiment_runs (searchruns)', value: 'searchruns' },
        { label: 'experiment_runs (getrun)', value: 'getrun' }
    ]
}>
<TabItem value="searchruns">

```sql
SELECT
data,
info,
inputs
FROM databricks_workspace.machinelearning.experiment_runs
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getrun">

```sql
SELECT
data,
info,
inputs
FROM databricks_workspace.machinelearning.experiment_runs
WHERE run_id = '{{ run_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>experiment_runs</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'experiment_runs', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.machinelearning.experiment_runs (
deployment_name,
data__experiment_id,
data__user_id,
data__start_time,
data__tags
)
SELECT 
'{{ deployment_name }}',
'{{ experiment_id }}',
'{{ user_id }}',
'{{ start_time }}',
'{{ tags }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: experiment_id
    value: string
  - name: user_id
    value: string
  - name: start_time
    value: 0
  - name: tags
    value:
    - key: string
      value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>experiment_runs</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.machinelearning.experiment_runs
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>experiment_runs</code> resource.

<Tabs
    defaultValue="deleterun"
    values={[
        { label: 'deleterun', value: 'deleterun' },
        { label: 'deleteruns', value: 'deleteruns' }
    ]
}>
<TabItem value="deleterun">

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.experiment_runs
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="deleteruns">

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.experiment_runs
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
