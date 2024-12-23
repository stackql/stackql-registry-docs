---
title: model_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_versions
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

Operations on a <code>model_versions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="creation_timestamp" /> | `integer` |
| <CopyableCode code="current_stage" /> | `string` |
| <CopyableCode code="last_updated_timestamp" /> | `integer` |
| <CopyableCode code="run_id" /> | `string` |
| <CopyableCode code="run_link" /> | `string` |
| <CopyableCode code="source" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="status_message" /> | `string` |
| <CopyableCode code="tags" /> | `array` |
| <CopyableCode code="user_id" /> | `string` |
| <CopyableCode code="version" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getmodelversion" /> | `SELECT` | <CopyableCode code="name, version, deployment_name" /> | Get a model version. |
| <CopyableCode code="searchmodelversions" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Searches for specific model versions based on the supplied |
| <CopyableCode code="createmodelversion" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a model version. |
| <CopyableCode code="deletemodelversion" /> | `DELETE` | <CopyableCode code="name, version, deployment_name" /> | Deletes a model version. |
| <CopyableCode code="updatemodelversion" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the model version. |

## `SELECT` examples

<Tabs
    defaultValue="searchmodelversions"
    values={[
        { label: 'model_versions (searchmodelversions)', value: 'searchmodelversions' },
        { label: 'model_versions (getmodelversion)', value: 'getmodelversion' }
    ]
}>
<TabItem value="searchmodelversions">

```sql
SELECT
name,
description,
creation_timestamp,
current_stage,
last_updated_timestamp,
run_id,
run_link,
source,
status,
status_message,
tags,
user_id,
version
FROM databricks_workspace.machinelearning.model_versions
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getmodelversion">

```sql
SELECT
name,
description,
creation_timestamp,
current_stage,
last_updated_timestamp,
run_id,
run_link,
source,
status,
status_message,
tags,
user_id,
version
FROM databricks_workspace.machinelearning.model_versions
WHERE name = '{{ name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_versions</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'model_versions', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.machinelearning.model_versions (
deployment_name,
data__name,
data__source,
data__run_id,
data__tags,
data__run_link,
data__description
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ source }}',
'{{ run_id }}',
'{{ tags }}',
'{{ run_link }}',
'{{ description }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: source
    value: string
  - name: run_id
    value: string
  - name: tags
    value:
    - key: string
      value: string
  - name: run_link
    value: string
  - name: description
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>model_versions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.machinelearning.model_versions
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>model_versions</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.model_versions
WHERE name = '{{ name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```
