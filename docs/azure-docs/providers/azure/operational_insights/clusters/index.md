---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - operational_insights
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
<tr><td><b>Id</b></td><td><code>azure.operational_insights.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sku` | `object` | The cluster sku definition. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Cluster properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets a Log Analytics cluster instance. |
| `Clusters_List` | `SELECT` | `subscriptionId` | Gets the Log Analytics clusters in a subscription. |
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets Log Analytics clusters in a resource group. |
| `Clusters_CreateOrUpdate` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create or update a Log Analytics cluster. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a cluster instance. |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates a Log Analytics cluster. |
