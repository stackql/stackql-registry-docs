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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.lke.clusters_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This Node Pool's unique ID.<br /> |
| <CopyableCode code="autoscaler" /> | `object` | When enabled, the number of nodes autoscales within the defined minimum and maximum values.<br /> |
| <CopyableCode code="count" /> | `integer` | The number of nodes in the Node Pool. |
| <CopyableCode code="disks" /> | `array` | This Node Pool's custom disk layout.<br /> |
| <CopyableCode code="nodes" /> | `array` | Status information for the Nodes which are members of this Node Pool. If a Linode has not been provisioned for a given Node slot, the instance_id will be returned as null.<br /> |
| <CopyableCode code="tags" /> | `array` | An array of tags applied to this object. Tags are for organizational purposes only.<br /> |
| <CopyableCode code="type" /> | `string` | The Linode Type for all of the nodes in the Node Pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLKEClusterPools" /> | `SELECT` | <CopyableCode code="clusterId" /> | Returns all active Node Pools on a Kubernetes cluster.<br /> |
| <CopyableCode code="getLKENodePool" /> | `SELECT` | <CopyableCode code="clusterId, poolId" /> | Get a specific Node Pool by ID.<br /> |
| <CopyableCode code="deleteLKENodePool" /> | `DELETE` | <CopyableCode code="clusterId, poolId" /> | Delete a specific Node Pool from a Kubernetes cluster.<br /><br />**Deleting a Node Pool is a destructive action and cannot be undone.**<br /><br />Deleting a Node Pool will delete all Linodes within that Pool.<br /> |
| <CopyableCode code="_getLKEClusterPools" /> | `EXEC` | <CopyableCode code="clusterId" /> | Returns all active Node Pools on a Kubernetes cluster.<br /> |
| <CopyableCode code="_getLKENodePool" /> | `EXEC` | <CopyableCode code="clusterId, poolId" /> | Get a specific Node Pool by ID.<br /> |
| <CopyableCode code="postLKEClusterPoolRecycle" /> | `EXEC` | <CopyableCode code="clusterId, poolId" /> | Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted<br />and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are<br />installed with the latest available patch for the Cluster's Kubernetes Version.<br /><br />**Any local storage on deleted Linodes (such as "hostPath" and "emptyDir" volumes, or "local" PersistentVolumes) will be erased.**<br /> |
| <CopyableCode code="postLKEClusterPools" /> | `EXEC` | <CopyableCode code="clusterId, data__count, data__type" /> | Creates a new Node Pool for the designated Kubernetes cluster.<br /> |
| <CopyableCode code="putLKENodePool" /> | `EXEC` | <CopyableCode code="clusterId, poolId" /> | Updates a Node Pool's count and autoscaler configuration.<br /><br />Linodes will be created or deleted to match changes to the Node Pool's count.<br /><br />**Any local storage on deleted Linodes (such as "hostPath" and "emptyDir" volumes, or "local" PersistentVolumes) will be erased.**<br /> |
