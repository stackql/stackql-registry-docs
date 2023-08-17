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
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.node_pools</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_clusters_node_pools_get` | `SELECT` | `clustersId, locationsId, nodePoolsId, projectsId` | Retrieves the requested node pool. |
| `projects_locations_clusters_node_pools_list` | `SELECT` | `clustersId, locationsId, projectsId` | Lists the node pools for a cluster. |
| `projects_zones_clusters_node_pools_get` | `SELECT` | `clusterId, nodePoolId, projectId, zone` | Retrieves the requested node pool. |
| `projects_zones_clusters_node_pools_list` | `SELECT` | `clusterId, projectId, zone` | Lists the node pools for a cluster. |
| `projects_locations_clusters_node_pools_create` | `INSERT` | `clustersId, locationsId, projectsId` | Creates a node pool for a cluster. |
| `projects_zones_clusters_node_pools_create` | `INSERT` | `clusterId, projectId, zone` | Creates a node pool for a cluster. |
| `projects_locations_clusters_node_pools_delete` | `DELETE` | `clustersId, locationsId, nodePoolsId, projectsId` | Deletes a node pool from a cluster. |
| `projects_zones_clusters_node_pools_delete` | `DELETE` | `clusterId, nodePoolId, projectId, zone` | Deletes a node pool from a cluster. |
| `projects_locations_clusters_node_pools_complete_upgrade` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete. |
| `projects_locations_clusters_node_pools_rollback` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| `projects_locations_clusters_node_pools_set_autoscaling` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the autoscaling settings for the specified node pool. |
| `projects_locations_clusters_node_pools_set_management` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the NodeManagement options for a node pool. |
| `projects_locations_clusters_node_pools_set_size` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |
| `projects_locations_clusters_node_pools_update` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Updates the version and/or image type for the specified node pool. |
| `projects_zones_clusters_node_pools_autoscaling` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the autoscaling settings for the specified node pool. |
| `projects_zones_clusters_node_pools_rollback` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| `projects_zones_clusters_node_pools_set_management` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the NodeManagement options for a node pool. |
| `projects_zones_clusters_node_pools_set_size` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |
| `projects_zones_clusters_node_pools_update` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Updates the version and/or image type for the specified node pool. |
