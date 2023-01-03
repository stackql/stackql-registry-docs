---
title: node_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - node_pools
  - container
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.node_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the node pool. |
| `podIpv4CidrSize` | `integer` | [Output only] The pod CIDR block size per node in this node pool. |
| `instanceGroupUrls` | `array` | [Output only] The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool. During the node pool blue-green upgrade operation, the URLs contain both blue and green resources. |
| `networkConfig` | `object` | Parameters for node pool-level network config. |
| `version` | `string` | The version of the Kubernetes of this node. |
| `initialNodeCount` | `integer` | The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. |
| `upgradeSettings` | `object` | These upgrade settings control the level of parallelism and the level of disruption caused by an upgrade. maxUnavailable controls the number of nodes that can be simultaneously unavailable. maxSurge controls the number of additional nodes that can be added to the node pool temporarily for the time of the upgrade to increase the number of available nodes. (maxUnavailable + maxSurge) determines the level of parallelism (how many nodes are being upgraded at the same time). Note: upgrades inevitably introduce some disruption since workloads need to be moved from old nodes to new, upgraded ones. Even if maxUnavailable=0, this holds true. (Disruption stays within the limits of PodDisruptionBudget, if it is configured.) Consider a hypothetical node pool with 5 nodes having maxSurge=2, maxUnavailable=1. This means the upgrade process upgrades 3 nodes simultaneously. It creates 2 additional (upgraded) nodes, then it brings down 3 old (not yet upgraded) nodes at the same time. This ensures that there are always at least 4 nodes available. These upgrade settings configure the upgrade strategy for the node pool. Use strategy to switch between the strategies applied to the node pool. If the strategy is ROLLING, use max_surge and max_unavailable to control the level of parallelism and the level of disruption caused by upgrade. 1. maxSurge controls the number of additional nodes that can be added to the node pool temporarily for the time of the upgrade to increase the number of available nodes. 2. maxUnavailable controls the number of nodes that can be simultaneously unavailable. 3. (maxUnavailable + maxSurge) determines the level of parallelism (how many nodes are being upgraded at the same time). If the strategy is BLUE_GREEN, use blue_green_settings to configure the blue-green upgrade related settings. 1. standard_rollout_policy is the default policy. The policy is used to control the way blue pool gets drained. The draining is executed in the batch mode. The batch size could be specified as either percentage of the node pool size or the number of nodes. batch_soak_duration is the soak time after each batch gets drained. 2. node_pool_soak_duration is the soak time after all blue nodes are drained. After this period, the blue pool nodes will be deleted. |
| `config` | `object` | Parameters that describe the nodes in a cluster. GKE Autopilot clusters do not recognize parameters in `NodeConfig`. Use AutoprovisioningNodePoolDefaults instead. |
| `management` | `object` | NodeManagement defines the set of node management services turned on for the node pool. |
| `conditions` | `array` | Which conditions caused the current node pool state. |
| `autoscaling` | `object` | NodePoolAutoscaling contains information required by cluster autoscaler to adjust the size of the node pool to the current cluster usage. |
| `locations` | `array` | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located. If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead. Warning: changing node pool locations will result in nodes being added and/or removed. |
| `status` | `string` | [Output only] The status of the nodes in this pool instance. |
| `maxPodsConstraint` | `object` | Constraints applied to pods. |
| `updateInfo` | `object` | UpdateInfo contains resource (instance groups, etc), status and other intermediate information relevant to a node pool upgrade. |
| `statusMessage` | `string` | [Output only] Deprecated. Use conditions instead. Additional information about the current status of this node pool instance, if available. |
| `selfLink` | `string` | [Output only] Server-defined URL for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_clusters_nodePools_get` | `SELECT` | `clustersId, locationsId, nodePoolsId, projectsId` | Retrieves the requested node pool. |
| `projects_locations_clusters_nodePools_list` | `SELECT` | `clustersId, locationsId, projectsId` | Lists the node pools for a cluster. |
| `projects_zones_clusters_nodePools_get` | `SELECT` | `clusterId, nodePoolId, projectId, zone` | Retrieves the requested node pool. |
| `projects_zones_clusters_nodePools_list` | `SELECT` | `clusterId, projectId, zone` | Lists the node pools for a cluster. |
| `projects_locations_clusters_nodePools_create` | `INSERT` | `clustersId, locationsId, projectsId` | Creates a node pool for a cluster. |
| `projects_zones_clusters_nodePools_create` | `INSERT` | `clusterId, projectId, zone` | Creates a node pool for a cluster. |
| `projects_locations_clusters_nodePools_delete` | `DELETE` | `clustersId, locationsId, nodePoolsId, projectsId` | Deletes a node pool from a cluster. |
| `projects_zones_clusters_nodePools_delete` | `DELETE` | `clusterId, nodePoolId, projectId, zone` | Deletes a node pool from a cluster. |
| `projects_locations_clusters_nodePools_completeUpgrade` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete. |
| `projects_locations_clusters_nodePools_rollback` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| `projects_locations_clusters_nodePools_setAutoscaling` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the autoscaling settings for the specified node pool. |
| `projects_locations_clusters_nodePools_setManagement` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the NodeManagement options for a node pool. |
| `projects_locations_clusters_nodePools_setSize` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |
| `projects_locations_clusters_nodePools_update` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Updates the version and/or image type for the specified node pool. |
| `projects_zones_clusters_nodePools_autoscaling` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the autoscaling settings for the specified node pool. |
| `projects_zones_clusters_nodePools_rollback` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| `projects_zones_clusters_nodePools_setManagement` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the NodeManagement options for a node pool. |
| `projects_zones_clusters_nodePools_setSize` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |
| `projects_zones_clusters_nodePools_update` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Updates the version and/or image type for the specified node pool. |
