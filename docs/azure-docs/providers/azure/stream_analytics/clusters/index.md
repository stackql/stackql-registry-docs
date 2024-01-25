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
| `etag` | `string` | The current entity tag for the cluster. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties associated with a Stream Analytics cluster. |
| `sku` | `object` | The SKU of the cluster. This determines the size/capacity of the cluster. Required on PUT (CreateOrUpdate) requests. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets information about the specified cluster. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the clusters in the given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all of the clusters in the given subscription. |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Creates a Stream Analytics Cluster or replaces an already existing cluster. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes the specified cluster. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the clusters in the given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all of the clusters in the given subscription. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates an existing cluster. This can be used to partially update (ie. update one or two properties) a cluster without affecting the rest of the cluster definition. |
