---
title: provisioned_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioned_clusters
  - hybrid_aks
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
<tr><td><b>Name</b></td><td><code>provisioned_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.provisioned_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the Provisioned cluster. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `extendedLocation` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProvisionedClusters_Get` | `SELECT` | `provisionedClustersName, resourceGroupName, subscriptionId` | Gets the Hybrid AKS provisioned cluster |
| `ProvisionedClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the Hybrid AKS provisioned cluster in a resource group |
| `ProvisionedClusters_ListBySubscription` | `SELECT` | `subscriptionId` | Gets the Hybrid AKS provisioned cluster in a subscription |
| `ProvisionedClusters_CreateOrUpdate` | `INSERT` | `provisionedClustersName, resourceGroupName, subscriptionId` | Creates the Hybrid AKS provisioned cluster |
| `ProvisionedClusters_Delete` | `DELETE` | `provisionedClustersName, resourceGroupName, subscriptionId` | Deletes the Hybrid AKS provisioned cluster |
| `ProvisionedClusters_Update` | `EXEC` | `provisionedClustersName, resourceGroupName, subscriptionId` | Updates the Hybrid AKS provisioned cluster |
