---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - event_hub
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
<tr><td><b>Id</b></td><td><code>azure.event_hub.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Event Hubs Cluster properties supplied in responses in List or Get operations. |
| `sku` | `object` | SKU parameters particular to a cluster instance. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets the resource description of the specified Event Hubs Cluster. |
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the available Event Hubs Clusters within an ARM resource group |
| `Clusters_ListBySubscription` | `SELECT` | `subscriptionId` | Lists the available Event Hubs Clusters within an ARM resource group |
| `Clusters_CreateOrUpdate` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Creates or updates an instance of an Event Hubs Cluster. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes an existing Event Hubs Cluster. This operation is idempotent. |
| `Clusters_ListAvailableClusterRegion` | `EXEC` | `subscriptionId` | List the quantity of available pre-provisioned Event Hubs Clusters, indexed by Azure region. |
| `Clusters_ListNamespaces` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List all Event Hubs Namespace IDs in an Event Hubs Dedicated Cluster. |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Modifies mutable properties on the Event Hubs Cluster. This operation is idempotent. |
