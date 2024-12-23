---
title: global_init_scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - global_init_scripts
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

Operations on a <code>global_init_scripts</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_init_scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.global_init_scripts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="enabled" /> | `boolean` |
| <CopyableCode code="position" /> | `integer` |
| <CopyableCode code="script" /> | `string` |
| <CopyableCode code="script_id" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="script_id, deployment_name" /> | Manage a specific global init script with ID |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Manages global init scripts for this workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Manages global init scripts for this workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="script_id, deployment_name" /> | Manage a specific global init script with ID |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="script_id, deployment_name" /> | Manage a specific global init script with ID |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'global_init_scripts (list)', value: 'list' },
        { label: 'global_init_scripts (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
created_at,
created_by,
enabled,
position,
script,
script_id,
updated_at,
updated_by
FROM databricks_workspace.compute.global_init_scripts
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
created_at,
created_by,
enabled,
position,
script,
script_id,
updated_at,
updated_by
FROM databricks_workspace.compute.global_init_scripts
WHERE script_id = '{{ script_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>global_init_scripts</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'global_init_scripts', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.global_init_scripts (
deployment_name,
data__name,
data__script,
data__position,
data__enabled
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ script }}',
'{{ position }}',
'{{ enabled }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: My example script name
  - name: script
    value: ZWNobyBoZWxsbw==
  - name: position
    value: 0
  - name: enabled
    value: false

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>global_init_scripts</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.compute.global_init_scripts
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE script_id = '{{ script_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>global_init_scripts</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.compute.global_init_scripts
WHERE script_id = '{{ script_id }}' AND
deployment_name = '{{ deployment_name }}';
```
