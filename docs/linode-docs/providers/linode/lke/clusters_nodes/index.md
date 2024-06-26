---
title: clusters_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_nodes
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
<tr><td><b>Name</b></td><td><code>clusters_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.lke.clusters_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Node's ID.<br /> |
| <CopyableCode code="instance_id" /> | `integer` | The Linode's ID. If no Linode is currently provisioned for this Node, this is `null`.<br /> |
| <CopyableCode code="status" /> | `string` | The creation status of this Node. This status is distinct from this Node's readiness as a Kubernetes Node Object as determined by the command `kubectl get nodes`.<br /><br />`not_ready` indicates that the Linode is still being created.<br /><br />`ready` indicates that the Linode has successfully been created and is running Kubernetes software.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLKEClusterNode" /> | `SELECT` | <CopyableCode code="clusterId, nodeId" /> | Returns the values for a specified node object.<br /> |
| <CopyableCode code="deleteLKEClusterNode" /> | `DELETE` | <CopyableCode code="clusterId, nodeId" /> | Deletes a specific Node from a Node Pool.<br /><br />**Deleting a Node is a destructive action and cannot be undone.**<br /><br />Deleting a Node will reduce the size of the Node Pool it belongs to.<br /> |
| <CopyableCode code="_getLKEClusterNode" /> | `EXEC` | <CopyableCode code="clusterId, nodeId" /> | Returns the values for a specified node object.<br /> |
| <CopyableCode code="postLKEClusterNodeRecycle" /> | `EXEC` | <CopyableCode code="clusterId, nodeId" /> | Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted<br />and replaced with a new Linode, which may take a few minutes. Replacement Nodes are<br />installed with the latest available patch for the Cluster's Kubernetes Version.<br /><br />**Any local storage on deleted Linodes (such as "hostPath" and "emptyDir" volumes, or "local" PersistentVolumes) will be erased.**<br /> |
