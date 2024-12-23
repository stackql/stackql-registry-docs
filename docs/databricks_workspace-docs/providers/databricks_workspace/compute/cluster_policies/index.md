---
title: cluster_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - cluster_policies
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

Operations on a <code>cluster_policies</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.cluster_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="created_at_timestamp" /> | `integer` |
| <CopyableCode code="creator_user_name" /> | `string` |
| <CopyableCode code="definition" /> | `object` |
| <CopyableCode code="is_default" /> | `boolean` |
| <CopyableCode code="libraries" /> | `array` |
| <CopyableCode code="max_clusters_per_user" /> | `integer` |
| <CopyableCode code="policy_family_definition_overrides" /> | `object` |
| <CopyableCode code="policy_family_id" /> | `string` |
| <CopyableCode code="policy_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policy_id, deployment_name" /> | Get a cluster policy entity. Creation and editing is available to admins only. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Returns a list of policies accessible by the requesting user. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new policy with prescribed settings. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited. |
| <CopyableCode code="edit" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Update an existing policy for cluster. This operation may make some clusters governed by the previous policy invalid. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'cluster_policies (list)', value: 'list' },
        { label: 'cluster_policies (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
description,
created_at_timestamp,
creator_user_name,
definition,
is_default,
libraries,
max_clusters_per_user,
policy_family_definition_overrides,
policy_family_id,
policy_id
FROM databricks_workspace.compute.cluster_policies
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
description,
created_at_timestamp,
creator_user_name,
definition,
is_default,
libraries,
max_clusters_per_user,
policy_family_definition_overrides,
policy_family_id,
policy_id
FROM databricks_workspace.compute.cluster_policies
WHERE policy_id = '{{ policy_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_policies</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'cluster_policies', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.cluster_policies (
deployment_name,
data__definition,
data__name
)
SELECT 
'{{ deployment_name }}',
'{{ definition }}',
'{{ name }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: definition
    value: '{ "custom_tags.test_tag": { "type": "fixed", "value": "test_value" } }'
  - name: name
    value: Test policy

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>cluster_policies</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.compute.cluster_policies
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>cluster_policies</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.compute.cluster_policies
WHERE deployment_name = '{{ deployment_name }}';
```
