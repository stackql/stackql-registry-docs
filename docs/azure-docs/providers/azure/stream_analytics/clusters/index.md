---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sku` | `object` | The SKU of the cluster. This determines the size/capacity of the cluster. Required on PUT (CreateOrUpdate) requests. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | The current entity tag for the cluster. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties associated with a Stream Analytics cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets information about the specified cluster. |
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the clusters in the given resource group. |
| `Clusters_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all of the clusters in the given subscription. |
| `Clusters_CreateOrUpdate` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Creates a Stream Analytics Cluster or replaces an already existing cluster. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes the specified cluster. |
| `Clusters_ListStreamingJobs` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Lists all of the streaming jobs in the given cluster. |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates an existing cluster. This can be used to partially update (ie. update one or two properties) a cluster without affecting the rest of the cluster definition. |
