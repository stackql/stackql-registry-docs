---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | HybridAKSNetworkSpec defines the desired state of HybridAKSNetwork |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `virtualNetworks_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the Hybrid AKS virtual networks by resource group |
| `virtualNetworks_ListBySubscription` | `SELECT` | `subscriptionId` | Lists the Hybrid AKS virtual networks by subscription |
| `virtualNetworks_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworksName` | Puts the Hybrid AKS virtual network |
| `virtualNetworks_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworksName` | Deletes the Hybrid AKS virtual network |
| `virtualNetworks_Retrieve` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworksName` | Gets the Hybrid AKS virtual network |
| `virtualNetworks_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworksName` | Patches the Hybrid AKS virtual network |
