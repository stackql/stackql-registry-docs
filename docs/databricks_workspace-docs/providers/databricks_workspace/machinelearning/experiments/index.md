---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - experiments
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

Operations on a <code>experiments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="artifact_location" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="experiment_id" /> | `string` |
| <CopyableCode code="last_update_time" /> | `integer` |
| <CopyableCode code="lifecycle_stage" /> | `string` |
| <CopyableCode code="tags" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getbyname" /> | `SELECT` | <CopyableCode code="experiment_name, deployment_name" /> | Gets metadata for an experiment. |
| <CopyableCode code="getexperiment" /> | `SELECT` | <CopyableCode code="experiment_id, deployment_name" /> | Gets metadata for an experiment. This method works on deleted experiments. |
| <CopyableCode code="listexperiments" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets a list of all experiments. |
| <CopyableCode code="searchexperiments" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Searches for experiments that satisfy specified search criteria. |
| <CopyableCode code="createexperiment" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that another experiment with the same name does not already exist and fails if another experiment with the same name already exists. |
| <CopyableCode code="deleteexperiment" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the experiment uses FileStore, artifacts associated with experiment are also deleted. |
| <CopyableCode code="updateexperiment" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates experiment metadata. |
| <CopyableCode code="restoreexperiment" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Restore an experiment marked for deletion. This also restores associated metadata, runs, metrics, params, and tags. If experiment uses FileStore, underlying artifacts associated with experiment are also restored. |

## `SELECT` examples

<Tabs
    defaultValue="searchexperiments"
    values={[
        { label: 'experiments (searchexperiments)', value: 'searchexperiments' },
        { label: 'experiments (listexperiments)', value: 'listexperiments' },
        { label: 'experiments (getexperiment)', value: 'getexperiment' },
        { label: 'experiments (getbyname)', value: 'getbyname' }
    ]
}>
<TabItem value="searchexperiments">

```sql
SELECT
name,
artifact_location,
creation_time,
experiment_id,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="listexperiments">

```sql
SELECT
name,
artifact_location,
creation_time,
experiment_id,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getexperiment">

```sql
SELECT
name,
artifact_location,
creation_time,
experiment_id,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE experiment_id = '{{ experiment_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getbyname">

```sql
SELECT
name,
artifact_location,
creation_time,
experiment_id,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE experiment_name = '{{ experiment_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>experiments</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'experiments', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.machinelearning.experiments (
deployment_name,
data__name,
data__artifact_location,
data__tags
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ artifact_location }}',
'{{ tags }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: artifact_location
    value: string
  - name: tags
    value:
    - key: string
      value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>experiments</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.machinelearning.experiments
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>experiments</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}';
```
