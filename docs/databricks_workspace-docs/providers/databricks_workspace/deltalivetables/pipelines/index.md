---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - pipelines
  - deltalivetables
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

Operations on a <code>pipelines</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltalivetables.pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="creator_user_name" /> | `string` |
| <CopyableCode code="latest_updates" /> | `array` |
| <CopyableCode code="pipeline_id" /> | `string` |
| <CopyableCode code="run_as_user_name" /> | `string` |
| <CopyableCode code="spec" /> | `object` |
| <CopyableCode code="state" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pipeline_id, deployment_name" /> |  |
| <CopyableCode code="listpipelines" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists pipelines defined in the Delta Live Tables system. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new data processing pipeline based on the requested configuration. If successful, this method returns the ID of the new pipeline. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pipeline_id, deployment_name" /> | Deletes a pipeline. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="pipeline_id, deployment_name" /> | Updates a pipeline with the supplied configuration. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="pipeline_id, deployment_name" /> | Stops the pipeline by canceling the active update. If there is no active update for the pipeline, this request is a no-op. |

## `SELECT` examples

<Tabs
    defaultValue="listpipelines"
    values={[
        { label: 'pipelines (listpipelines)', value: 'listpipelines' },
        { label: 'pipelines (get)', value: 'get' }
    ]
}>
<TabItem value="listpipelines">

```sql
SELECT
name,
cluster_id,
creator_user_name,
latest_updates,
pipeline_id,
run_as_user_name,
spec,
state
FROM databricks_workspace.deltalivetables.pipelines
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
cluster_id,
creator_user_name,
latest_updates,
pipeline_id,
run_as_user_name,
spec,
state
FROM databricks_workspace.deltalivetables.pipelines
WHERE pipeline_id = '{{ pipeline_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipelines</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'pipelines', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.deltalivetables.pipelines (
deployment_name,
data__continuous,
data__name,
data__clusters,
data__libraries,
data__storage
)
SELECT 
'{{ deployment_name }}',
'{{ continuous }}',
'{{ name }}',
'{{ clusters }}',
'{{ libraries }}',
'{{ storage }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: continuous
    value: false
  - name: name
    value: Wikipedia pipeline (SQL)
  - name: clusters
    value:
    - label: default
      autoscale:
        min_workers: 1
        max_workers: 5
        mode: ENHANCED
  - name: libraries
    value:
    - notebook:
        path: /Users/username/DLT Notebooks/Delta Live Tables quickstart (SQL)
  - name: storage
    value: /Users/username/data

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pipelines</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.deltalivetables.pipelines
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE pipeline_id = '{{ pipeline_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.deltalivetables.pipelines
WHERE pipeline_id = '{{ pipeline_id }}' AND
deployment_name = '{{ deployment_name }}';
```
