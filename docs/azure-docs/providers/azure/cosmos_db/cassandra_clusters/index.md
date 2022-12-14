---
title: cassandra_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>cassandra_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.cassandra_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `properties` | `object` | Properties of a managed Cassandra cluster. |
| `tags` | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| `type` | `string` | The type of Azure resource. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The location of the resource group to which the resource belongs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CassandraClusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get the properties of a managed Cassandra cluster. |
| `CassandraClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all managed Cassandra clusters in this resource group. |
| `CassandraClusters_ListBySubscription` | `SELECT` | `subscriptionId` | List all managed Cassandra clusters in this subscription. |
| `CassandraClusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a managed Cassandra cluster. |
| `CassandraClusters_CreateUpdate` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Create or update a managed Cassandra cluster. When updating, you must specify all writable properties. To update only some properties, use PATCH. |
| `CassandraClusters_Deallocate` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Deallocate the Managed Cassandra Cluster and Associated Data Centers. Deallocation will deallocate the host virtual machine of this cluster, and reserved the data disk. This won't do anything on an already deallocated cluster. Use Start to restart the cluster. |
| `CassandraClusters_GetBackup` | `EXEC` | `backupId, clusterName, resourceGroupName, subscriptionId` | Get the properties of an individual backup of this cluster that is available to restore. |
| `CassandraClusters_InvokeCommand` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__command, data__host` | Invoke a command like nodetool for cassandra maintenance  |
| `CassandraClusters_ListBackups` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List the backups of this cluster that are available to restore. |
| `CassandraClusters_Start` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Start the Managed Cassandra Cluster and Associated Data Centers. Start will start the host virtual machine of this cluster with reserved data disk. This won't do anything on an already running cluster. Use Deallocate to deallocate the cluster. |
| `CassandraClusters_Status` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets the CPU, memory, and disk usage statistics for each Cassandra node in a cluster. |
| `CassandraClusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates some of the properties of a managed Cassandra cluster. |
