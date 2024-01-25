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
| `properties` | `object` | Describes a node type in the cluster, each node type represents sub set of nodes in the cluster. |
| `sku` | `object` | Describes a node type sku. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Get a Service Fabric node type of a given managed cluster. |
| `list_by_managed_clusters` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all Node types of the specified managed cluster. |
| `create_or_update` | `INSERT` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Create or update a Service Fabric node type of a given managed cluster. |
| `delete` | `DELETE` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Delete a Service Fabric node type of a given managed cluster. |
| `_list_by_managed_clusters` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all Node types of the specified managed cluster. |
| `reimage` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Reimages one or more nodes on the node type. It will disable the fabric nodes, trigger a reimage on the VMs and activate the nodes back again. |
| `restart` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Restarts one or more nodes on the node type. It will disable the fabric nodes, trigger a restart on the VMs and activate the nodes back again. |
| `update` | `EXEC` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` | Update the configuration of a node type of a given managed cluster, only updating tags. |
