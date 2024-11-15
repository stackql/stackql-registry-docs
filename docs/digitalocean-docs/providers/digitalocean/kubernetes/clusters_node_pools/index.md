---
title: clusters_node_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_node_pools
  - kubernetes
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>clusters_node_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters_node_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_get_node_pool" /> | `SELECT` | <CopyableCode code="cluster_id, node_pool_id" /> | To show information about a specific node pool in a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`. |
| <CopyableCode code="kubernetes_list_node_pools" /> | `SELECT` | <CopyableCode code="cluster_id" /> | To list all of the node pools in a Kubernetes clusters, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`. |
| <CopyableCode code="kubernetes_add_node_pool" /> | `INSERT` | <CopyableCode code="cluster_id" /> | To add an additional node pool to a Kubernetes clusters, send a POST request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools` with the following attributes. |
| <CopyableCode code="kubernetes_delete_node_pool" /> | `DELETE` | <CopyableCode code="cluster_id, node_pool_id" /> | To delete a node pool, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`. A 204 status code with no body will be returned in response to a successful request. Nodes in the pool will subsequently be drained and deleted. |
| <CopyableCode code="kubernetes_recycle_node_pool" /> | `EXEC` | <CopyableCode code="cluster_id, node_pool_id" /> | The endpoint has been deprecated. Please use the DELETE `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID/nodes/$NODE_ID` method instead. |
| <CopyableCode code="kubernetes_update_node_pool" /> | `EXEC` | <CopyableCode code="cluster_id, node_pool_id" /> | To update the name of a node pool, edit the tags applied to it, or adjust its number of nodes, send a PUT request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID` with the following attributes. |

## `SELECT` examples

To list all of the node pools in a Kubernetes clusters, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`.


```sql
SELECT
column_anon
FROM digitalocean.kubernetes.clusters_node_pools
WHERE cluster_id = '{{ cluster_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters_node_pools</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.kubernetes.clusters_node_pools (
data__size,
data__name,
data__count,
data__tags,
data__labels,
data__taints,
data__auto_scale,
data__min_nodes,
data__max_nodes,
cluster_id
)
SELECT 
'{{ size }}',
'{{ name }}',
'{{ count }}',
'{{ tags }}',
'{{ labels }}',
'{{ taints }}',
'{{ auto_scale }}',
'{{ min_nodes }}',
'{{ max_nodes }}',
'{{ cluster_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.kubernetes.clusters_node_pools (
cluster_id
)
SELECT 
'{{ cluster_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: clusters_node_pools
  props:
    - name: cluster_id
      value: string
    - name: size
      value: string
    - name: name
      value: string
    - name: count
      value: integer
    - name: tags
      value: array
    - name: labels
      value: object
    - name: taints
      value: array
      props:
        - name: key
          value: string
        - name: value
          value: string
        - name: effect
          value: string
    - name: auto_scale
      value: boolean
    - name: min_nodes
      value: integer
    - name: max_nodes
      value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>clusters_node_pools</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.kubernetes.clusters_node_pools
WHERE cluster_id = '{{ cluster_id }}'
AND node_pool_id = '{{ node_pool_id }}';
```
