---
title: warehouses
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - warehouses
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

Operations on a <code>warehouses</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warehouses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.warehouses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="auto_stop_mins" /> | `string` |
| <CopyableCode code="channel" /> | `object` |
| <CopyableCode code="cluster_size" /> | `string` |
| <CopyableCode code="creator_name" /> | `string` |
| <CopyableCode code="enable_photon" /> | `boolean` |
| <CopyableCode code="enable_serverless_compute" /> | `boolean` |
| <CopyableCode code="health" /> | `object` |
| <CopyableCode code="instance_profile_arn" /> | `string` |
| <CopyableCode code="jdbc_url" /> | `string` |
| <CopyableCode code="max_num_clusters" /> | `integer` |
| <CopyableCode code="min_num_clusters" /> | `string` |
| <CopyableCode code="num_active_sessions" /> | `integer` |
| <CopyableCode code="num_clusters" /> | `integer` |
| <CopyableCode code="odbc_params" /> | `object` |
| <CopyableCode code="spot_instance_policy" /> | `string` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="tags" /> | `object` |
| <CopyableCode code="warehouse_type" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Gets the information for a single SQL warehouse. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists all SQL warehouses that a user has manager permissions on. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new SQL warehouse. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Deletes a SQL warehouse. |
| <CopyableCode code="edit" /> | `REPLACE` | <CopyableCode code="id, deployment_name" /> | Updates the configuration for a SQL warehouse. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="id, deployment_name" /> | Starts a SQL warehouse. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="id, deployment_name" /> | Stops a SQL warehouse. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'warehouses (list)', value: 'list' },
        { label: 'warehouses (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
auto_stop_mins,
channel,
cluster_size,
creator_name,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type
FROM databricks_workspace.dbsql.warehouses
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
auto_stop_mins,
channel,
cluster_size,
creator_name,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type
FROM databricks_workspace.dbsql.warehouses
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>warehouses</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'warehouses', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.dbsql.warehouses (
deployment_name,
data__name,
data__cluster_size,
data__min_num_clusters,
data__max_num_clusters,
data__auto_stop_mins,
data__creator_name,
data__instance_profile_arn,
data__tags,
data__spot_instance_policy,
data__enable_photon,
data__channel,
data__enable_serverless_compute,
data__warehouse_type
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ cluster_size }}',
'{{ min_num_clusters }}',
'{{ max_num_clusters }}',
'{{ auto_stop_mins }}',
'{{ creator_name }}',
'{{ instance_profile_arn }}',
'{{ tags }}',
'{{ spot_instance_policy }}',
'{{ enable_photon }}',
'{{ channel }}',
'{{ enable_serverless_compute }}',
'{{ warehouse_type }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: cluster_size
    value: string
  - name: min_num_clusters
    value: '1'
  - name: max_num_clusters
    value: 0
  - name: auto_stop_mins
    value: '120'
  - name: creator_name
    value: string
  - name: instance_profile_arn
    value: string
  - name: tags
    value:
      custom_tags:
      - key: string
        value: string
  - name: spot_instance_policy
    value: POLICY_UNSPECIFIED
  - name: enable_photon
    value: true
  - name: channel
    value:
      name: CHANNEL_NAME_PREVIEW
      dbsql_version: string
  - name: enable_serverless_compute
    value: true
  - name: warehouse_type
    value: TYPE_UNSPECIFIED

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>warehouses</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.dbsql.warehouses
SET { field = value }
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>warehouses</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.dbsql.warehouses
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
