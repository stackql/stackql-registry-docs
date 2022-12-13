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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.node_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `type` | `string` | Azure resource type. |
| `properties` | `object` | Describes a node type in the cluster, each node type represents sub set of nodes in the cluster. |
| `sku` | `object` | Describes a node type sku. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NodeTypes_Get` | `SELECT` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Get a Service Fabric node type of a given managed cluster. |
| `NodeTypes_ListByManagedClusters` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all Node types of the specified managed cluster. |
| `NodeTypes_CreateOrUpdate` | `INSERT` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Create or update a Service Fabric node type of a given managed cluster. |
| `NodeTypes_Delete` | `DELETE` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Delete a Service Fabric node type of a given managed cluster. |
| `NodeTypes_DeleteNode` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId, data__nodes` | Deletes one or more nodes on the node type. It will disable the fabric nodes, trigger a delete on the VMs and removes the state from the cluster. |
| `NodeTypes_Reimage` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId, data__nodes` | Reimages one or more nodes on the node type. It will disable the fabric nodes, trigger a reimage on the VMs and activate the nodes back again. |
| `NodeTypes_Restart` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId, data__nodes` | Restarts one or more nodes on the node type. It will disable the fabric nodes, trigger a restart on the VMs and activate the nodes back again. |
| `NodeTypes_Update` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Update the configuration of a node type of a given managed cluster, only updating tags. |
