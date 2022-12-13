---
title: storage_spaces
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_spaces
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
<tr><td><b>Name</b></td><td><code>storage_spaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.storage_spaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | HybridAKSStorageSpec defines the desired state of HybridAKSStorage |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `storageSpaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List the Hybrid AKS storage object by resource group |
| `storageSpaces_ListBySubscription` | `SELECT` | `subscriptionId` | List the Hybrid AKS storage object by subscription |
| `storageSpaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, storageSpacesName, subscriptionId` | Puts the Hybrid AKS storage object |
| `storageSpaces_Delete` | `DELETE` | `resourceGroupName, storageSpacesName, subscriptionId` | Deletes the Hybrid AKS storage object |
| `storageSpaces_Retrieve` | `EXEC` | `resourceGroupName, storageSpacesName, subscriptionId` | Gets the Hybrid AKS storage space object |
| `storageSpaces_Update` | `EXEC` | `resourceGroupName, storageSpacesName, subscriptionId` | Patches the Hybrid AKS storage object |
