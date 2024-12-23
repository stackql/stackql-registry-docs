---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - clusters
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

Operations on a <code>clusters</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="autotermination_minutes" /> | `integer` |
| <CopyableCode code="aws_attributes" /> | `object` |
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="cluster_name" /> | `string` |
| <CopyableCode code="cluster_source" /> | `string` |
| <CopyableCode code="creator_user_name" /> | `string` |
| <CopyableCode code="default_tags" /> | `object` |
| <CopyableCode code="disk_spec" /> | `object` |
| <CopyableCode code="driver_instance_source" /> | `object` |
| <CopyableCode code="driver_node_type_id" /> | `string` |
| <CopyableCode code="enable_elastic_disk" /> | `boolean` |
| <CopyableCode code="enable_local_disk_encryption" /> | `boolean` |
| <CopyableCode code="init_scripts_safe_mode" /> | `boolean` |
| <CopyableCode code="instance_source" /> | `object` |
| <CopyableCode code="last_state_loss_time" /> | `integer` |
| <CopyableCode code="node_type_id" /> | `string` |
| <CopyableCode code="num_workers" /> | `integer` |
| <CopyableCode code="spark_context_id" /> | `integer` |
| <CopyableCode code="spark_version" /> | `string` |
| <CopyableCode code="start_time" /> | `integer` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="state_message" /> | `string` |
| <CopyableCode code="terminated_time" /> | `integer` |
| <CopyableCode code="termination_reason" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cluster_id, deployment_name" /> | Retrieves the information for a cluster given its identifier. Clusters can be described while they are running, or up to 60 days after they are terminated. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Return information about all pinned and active clusters, and all clusters terminated within the last 30 days. Clusters terminated prior to this period are not included. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new Spark cluster. This method will acquire new instances from the cloud provider if necessary. This method is asynchronous; the returned |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the termination has completed, the cluster will be in a |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the configuration of a cluster to match the partial set of attributes and size. Denote which fields to update using the |
| <CopyableCode code="edit" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Updates the configuration of a cluster to match the provided attributes and size. A cluster can be updated if it is in a |
| <CopyableCode code="changeowner" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Change the owner of the cluster. You must be an admin and the cluster must be terminated to perform this operation. The service principal application ID can be supplied as an argument to |
| <CopyableCode code="permanentdelete" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously removed. |
| <CopyableCode code="pin" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a cluster that is already pinned will have no effect. This API can only be called by workspace admins. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Starts a terminated Spark cluster with the supplied ID. This works similar to |
| <CopyableCode code="unpin" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API. Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace admins. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'clusters (list)', value: 'list' },
        { label: 'clusters (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
autotermination_minutes,
aws_attributes,
cluster_id,
cluster_name,
cluster_source,
creator_user_name,
default_tags,
disk_spec,
driver_instance_source,
driver_node_type_id,
enable_elastic_disk,
enable_local_disk_encryption,
init_scripts_safe_mode,
instance_source,
last_state_loss_time,
node_type_id,
num_workers,
spark_context_id,
spark_version,
start_time,
state,
state_message,
terminated_time,
termination_reason
FROM databricks_workspace.compute.clusters
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
autotermination_minutes,
aws_attributes,
cluster_id,
cluster_name,
cluster_source,
creator_user_name,
default_tags,
disk_spec,
driver_instance_source,
driver_node_type_id,
enable_elastic_disk,
enable_local_disk_encryption,
init_scripts_safe_mode,
instance_source,
last_state_loss_time,
node_type_id,
num_workers,
spark_context_id,
spark_version,
start_time,
state,
state_message,
terminated_time,
termination_reason
FROM databricks_workspace.compute.clusters
WHERE cluster_id = '{{ cluster_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'clusters', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.clusters (
deployment_name,
data__cluster_name,
data__is_single_node,
data__kind,
data__spark_version,
data__node_type_id,
data__aws_attributes
)
SELECT 
'{{ deployment_name }}',
'{{ cluster_name }}',
'{{ is_single_node }}',
'{{ kind }}',
'{{ spark_version }}',
'{{ node_type_id }}',
'{{ aws_attributes }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: cluster_name
    value: single-node-with-kind-cluster
  - name: is_single_node
    value: true
  - name: kind
    value: CLASSIC_PREVIEW
  - name: spark_version
    value: 14.3.x-scala2.12
  - name: node_type_id
    value: i3.xlarge
  - name: aws_attributes
    value:
      first_on_demand: 1
      availability: SPOT_WITH_FALLBACK
      zone_id: auto
      spot_bid_price_percent: 100
      ebs_volume_count: 0

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.compute.clusters
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>clusters</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.compute.clusters
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.compute.clusters
WHERE deployment_name = '{{ deployment_name }}';
```
