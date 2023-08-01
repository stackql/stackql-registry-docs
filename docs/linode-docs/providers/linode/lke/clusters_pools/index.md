---
title: clusters_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_pools
  - lke
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.lke.clusters_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This Node Pool's unique ID.<br /> |
| `nodes` | `array` | Status information for the Nodes which are members of this Node Pool. If a Linode has not been provisioned for a given Node slot, the instance_id will be returned as null.<br /> |
| `tags` | `array` | An array of tags applied to this object. Tags are for organizational purposes only.<br /> |
| `type` | `string` | The Linode Type for all of the nodes in the Node Pool. |
| `autoscaler` | `object` | When enabled, the number of nodes autoscales within the defined minimum and maximum values.<br /> |
| `count` | `integer` | The number of nodes in the Node Pool. |
| `disks` | `array` | This Node Pool's custom disk layout.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLKEClusterPools` | `SELECT` | `clusterId` | Returns all active Node Pools on a Kubernetes cluster.<br /> |
| `getLKENodePool` | `SELECT` | `clusterId, poolId` | Get a specific Node Pool by ID.<br /> |
| `deleteLKENodePool` | `DELETE` | `clusterId, poolId` | Delete a specific Node Pool from a Kubernetes cluster.<br /><br />**Deleting a Node Pool is a destructive action and cannot be undone.**<br /><br />Deleting a Node Pool will delete all Linodes within that Pool.<br /> |
| `_getLKEClusterPools` | `EXEC` | `clusterId` | Returns all active Node Pools on a Kubernetes cluster.<br /> |
| `_getLKENodePool` | `EXEC` | `clusterId, poolId` | Get a specific Node Pool by ID.<br /> |
| `postLKEClusterPoolRecycle` | `EXEC` | `clusterId, poolId` | Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted<br />and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are<br />installed with the latest available patch for the Cluster's Kubernetes Version.<br /><br />**Any local storage on deleted Linodes (such as "hostPath" and "emptyDir" volumes, or "local" PersistentVolumes) will be erased.**<br /> |
| `postLKEClusterPools` | `EXEC` | `clusterId, data__count, data__type` | Creates a new Node Pool for the designated Kubernetes cluster.<br /> |
| `putLKENodePool` | `EXEC` | `clusterId, poolId` | Updates a Node Pool's count and autoscaler configuration.<br /><br />Linodes will be created or deleted to match changes to the Node Pool's count.<br /><br />**Any local storage on deleted Linodes (such as "hostPath" and "emptyDir" volumes, or "local" PersistentVolumes) will be erased.**<br /> |
