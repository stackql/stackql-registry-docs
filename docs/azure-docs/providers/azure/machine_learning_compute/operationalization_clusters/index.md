---
title: operationalization_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - operationalization_clusters
  - machine_learning_compute
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
<tr><td><b>Name</b></td><td><code>operationalization_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_compute.operationalization_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `properties` | `object` | Properties of an operationalization cluster |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `type` | `string` | Specifies the type of the resource. |
| `location` | `string` | Specifies the location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OperationalizationClusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets the operationalization cluster resource view. Note that the credentials are not returned by this call. Call ListKeys to get them. |
| `OperationalizationClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the clusters in the specified resource group. |
| `OperationalizationClusters_ListBySubscriptionId` | `SELECT` | `subscriptionId` | Gets the operationalization clusters in the specified subscription. |
| `OperationalizationClusters_CreateOrUpdate` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create or update an operationalization cluster. |
| `OperationalizationClusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes the specified cluster. |
| `OperationalizationClusters_CheckSystemServicesUpdatesAvailable` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Checks if updates are available for system services in the cluster. |
| `OperationalizationClusters_ListKeys` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets the credentials for the specified cluster such as Storage, ACR and ACS credentials. This is a long running operation because it fetches keys from dependencies. |
| `OperationalizationClusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | The PATCH operation can be used to update only the tags for a cluster. Use PUT operation to update other properties. |
| `OperationalizationClusters_UpdateSystemServices` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates system services in a cluster. |
