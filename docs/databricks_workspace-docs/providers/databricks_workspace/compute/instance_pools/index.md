---
title: instance_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - instance_pools
  - compute
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

Operations on a <code>instance_pools</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.instance_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="aws_attributes" /> | `object` |
| <CopyableCode code="default_tags" /> | `object` |
| <CopyableCode code="disk_spec" /> | `object` |
| <CopyableCode code="enable_elastic_disk" /> | `boolean` |
| <CopyableCode code="idle_instance_autotermination_minutes" /> | `integer` |
| <CopyableCode code="instance_pool_id" /> | `string` |
| <CopyableCode code="instance_pool_name" /> | `string` |
| <CopyableCode code="min_idle_instances" /> | `integer` |
| <CopyableCode code="node_type_id" /> | `string` |
| <CopyableCode code="preloaded_spark_versions" /> | `array` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="stats" /> | `object` |
| <CopyableCode code="status" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instance_pool_id, deployment_name" /> | Retrieve the information for an instance pool based on its identifier. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets a list of instance pools with their statistics. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new instance pool using idle and ready-to-use cloud instances. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously. |
| <CopyableCode code="edit" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Modifies the configuration of an existing instance pool. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'instance_pools (list)', value: 'list' },
        { label: 'instance_pools (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
aws_attributes,
default_tags,
disk_spec,
enable_elastic_disk,
idle_instance_autotermination_minutes,
instance_pool_id,
instance_pool_name,
min_idle_instances,
node_type_id,
preloaded_spark_versions,
state,
stats,
status
FROM databricks_workspace.compute.instance_pools
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
aws_attributes,
default_tags,
disk_spec,
enable_elastic_disk,
idle_instance_autotermination_minutes,
instance_pool_id,
instance_pool_name,
min_idle_instances,
node_type_id,
preloaded_spark_versions,
state,
stats,
status
FROM databricks_workspace.compute.instance_pools
WHERE instance_pool_id = '{{ instance_pool_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_pools</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'instance_pools', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.instance_pools (
deployment_name,
data__instance_pool_name,
data__node_type_id,
data__min_idle_instances,
data__aws_attributes,
data__custom_tags
)
SELECT 
'{{ deployment_name }}',
'{{ instance_pool_name }}',
'{{ node_type_id }}',
'{{ min_idle_instances }}',
'{{ aws_attributes }}',
'{{ custom_tags }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: instance_pool_name
    value: my-pool
  - name: node_type_id
    value: i3.xlarge
  - name: min_idle_instances
    value: 10
  - name: aws_attributes
    value:
      availability: SPOT
  - name: custom_tags
    value:
    - key: my-key
      value: my-value

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>instance_pools</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.compute.instance_pools
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>instance_pools</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.compute.instance_pools
WHERE deployment_name = '{{ deployment_name }}';
```
