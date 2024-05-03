---
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types
  - service_fabric_managed_clusters
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.node_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="properties" /> | `object` | Describes a node type in the cluster, each node type represents sub set of nodes in the cluster. |
| <CopyableCode code="sku" /> | `object` | Describes a node type sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Get a Service Fabric node type of a given managed cluster. |
| <CopyableCode code="list_by_managed_clusters" /> | `SELECT` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Gets all Node types of the specified managed cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric node type of a given managed cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric node type of a given managed cluster. |
| <CopyableCode code="_list_by_managed_clusters" /> | `EXEC` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Gets all Node types of the specified managed cluster. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Reimages one or more nodes on the node type. It will disable the fabric nodes, trigger a reimage on the VMs and activate the nodes back again. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Restarts one or more nodes on the node type. It will disable the fabric nodes, trigger a restart on the VMs and activate the nodes back again. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Update the configuration of a node type of a given managed cluster, only updating tags. |
