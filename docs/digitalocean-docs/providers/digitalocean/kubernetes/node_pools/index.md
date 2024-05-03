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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.node_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a specific node pool. |
| <CopyableCode code="name" /> | `string` | A human-readable name for the node pool. |
| <CopyableCode code="auto_scale" /> | `boolean` | A boolean value indicating whether auto-scaling is enabled for this node pool. |
| <CopyableCode code="count" /> | `integer` | The number of Droplet instances in the node pool. |
| <CopyableCode code="labels" /> | `object` | An object containing a set of Kubernetes labels. The keys and are values are both user-defined. |
| <CopyableCode code="max_nodes" /> | `integer` | The maximum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. |
| <CopyableCode code="min_nodes" /> | `integer` | The minimum number of nodes that this node pool can be auto-scaled to. The value will be `0` if `auto_scale` is set to `false`. |
| <CopyableCode code="nodes" /> | `array` | An object specifying the details of a specific worker node in a node pool. |
| <CopyableCode code="size" /> | `string` | The slug identifier for the type of Droplet used as workers in the node pool. |
| <CopyableCode code="tags" /> | `array` | An array containing the tags applied to the node pool. All node pools are automatically tagged `k8s`, `k8s-worker`, and `k8s:$K8S_CLUSTER_ID`. |
| <CopyableCode code="taints" /> | `array` | An array of taints to apply to all nodes in a pool. Taints will automatically be applied to all existing nodes and any subsequent nodes added to the pool. When a taint is removed, it is removed from all nodes in the pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_nodePool" /> | `SELECT` | <CopyableCode code="cluster_id, node_pool_id" /> | To show information about a specific node pool in a Kubernetes cluster, send<br />a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.<br /> |
| <CopyableCode code="list_nodePools" /> | `SELECT` | <CopyableCode code="cluster_id" /> | To list all of the node pools in a Kubernetes clusters, send a GET request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`.<br /> |
| <CopyableCode code="add_nodePool" /> | `INSERT` | <CopyableCode code="cluster_id, data__count, data__name, data__size" /> | To add an additional node pool to a Kubernetes clusters, send a POST request<br />to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools` with the following<br />attributes.<br /> |
| <CopyableCode code="delete_nodePool" /> | `DELETE` | <CopyableCode code="cluster_id, node_pool_id" /> | To delete a node pool, send a DELETE request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.<br /><br />A 204 status code with no body will be returned in response to a successful<br />request. Nodes in the pool will subsequently be drained and deleted.<br /> |
| <CopyableCode code="_get_nodePool" /> | `EXEC` | <CopyableCode code="cluster_id, node_pool_id" /> | To show information about a specific node pool in a Kubernetes cluster, send<br />a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.<br /> |
| <CopyableCode code="_list_nodePools" /> | `EXEC` | <CopyableCode code="cluster_id" /> | To list all of the node pools in a Kubernetes clusters, send a GET request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`.<br /> |
| <CopyableCode code="recycle_node_pool" /> | `EXEC` | <CopyableCode code="cluster_id, node_pool_id" /> | The endpoint has been deprecated. Please use the DELETE<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID/nodes/$NODE_ID`<br />method instead.<br /> |
| <CopyableCode code="update_nodePool" /> | `EXEC` | <CopyableCode code="cluster_id, node_pool_id, data__count, data__name" /> | To update the name of a node pool, edit the tags applied to it, or adjust its<br />number of nodes, send a PUT request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID` with the<br />following attributes.<br /> |
