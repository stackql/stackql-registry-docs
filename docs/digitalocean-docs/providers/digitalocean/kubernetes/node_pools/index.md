---
title: node_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - node_pools
  - kubernetes
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.kubernetes.node_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference a specific node pool. |
| `name` | `string` | A human-readable name for the node pool. |
| `count` | `integer` | The number of Droplet instances in the node pool. |
| `size` | `string` | The slug identifier for the type of Droplet used as workers in the node pool. |
| `labels` | `object` | An object containing a set of Kubernetes labels. The keys and are values are both user-defined. |
| `min_nodes` | `integer` | The minimum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. |
| `nodes` | `array` | An object specifying the details of a specific worker node in a node pool. |
| `tags` | `array` | An array containing the tags applied to the node pool. All node pools are automatically tagged `k8s`, `k8s-worker`, and `k8s:$K8S_CLUSTER_ID`. |
| `taints` | `array` | An array of taints to apply to all nodes in a pool. Taints will automatically be applied to all existing nodes and any subsequent nodes added to the pool. When a taint is removed, it is removed from all nodes in the pool. |
| `auto_scale` | `boolean` | A boolean value indicating whether auto-scaling is enabled for this node pool. |
| `max_nodes` | `integer` | The maximum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_nodePool` | `SELECT` | `cluster_id, node_pool_id` | To show information about a specific node pool in a Kubernetes cluster, send<br />a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.<br /> |
| `list_nodePools` | `SELECT` | `cluster_id` | To list all of the node pools in a Kubernetes clusters, send a GET request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`.<br /> |
| `add_nodePool` | `INSERT` | `cluster_id, data__count, data__name, data__size` | To add an additional node pool to a Kubernetes clusters, send a POST request<br />to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools` with the following<br />attributes.<br /> |
| `delete_nodePool` | `DELETE` | `cluster_id, node_pool_id` | To delete a node pool, send a DELETE request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.<br /><br />A 204 status code with no body will be returned in response to a successful<br />request. Nodes in the pool will subsequently be drained and deleted.<br /> |
| `_get_nodePool` | `EXEC` | `cluster_id, node_pool_id` | To show information about a specific node pool in a Kubernetes cluster, send<br />a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.<br /> |
| `_list_nodePools` | `EXEC` | `cluster_id` | To list all of the node pools in a Kubernetes clusters, send a GET request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`.<br /> |
| `recycle_node_pool` | `EXEC` | `cluster_id, node_pool_id` | The endpoint has been deprecated. Please use the DELETE<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID/nodes/$NODE_ID`<br />method instead.<br /> |
| `update_nodePool` | `EXEC` | `cluster_id, node_pool_id, data__count, data__name` | To update the name of a node pool, edit the tags applied to it, or adjust its<br />number of nodes, send a PUT request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID` with the<br />following attributes.<br /> |
