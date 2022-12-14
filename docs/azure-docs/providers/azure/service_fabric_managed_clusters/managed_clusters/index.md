---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
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
<tr><td><b>Name</b></td><td><code>managed_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.managed_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `sku` | `object` | Service Fabric managed cluster Sku definition |
| `type` | `string` | Azure resource type. |
| `location` | `string` | Azure resource location. |
| `tags` | `object` | Azure resource tags. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `etag` | `string` | Azure resource etag. |
| `properties` | `object` | Describes the managed cluster resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedClusters_Get` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric managed cluster resource created or in the process of being created in the specified resource group. |
| `ManagedClusters_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `ManagedClusters_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `ManagedClusters_CreateOrUpdate` | `INSERT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric managed cluster resource with the specified name. |
| `ManagedClusters_Delete` | `DELETE` | `api-version, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric managed cluster resource with the specified name. |
| `ManagedClusters_Update` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Update the tags of of a Service Fabric managed cluster resource with the specified name. |
