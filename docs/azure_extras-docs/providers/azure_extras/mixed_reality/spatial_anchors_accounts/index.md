---
title: spatial_anchors_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - spatial_anchors_accounts
  - mixed_reality
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>spatial_anchors_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mixed_reality.spatial_anchors_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `plan` | `object` | Identity for the resource. |
| `properties` | `object` | Common Properties shared by Mixed Reality Accounts |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `object` | The resource model definition representing SKU |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SpatialAnchorsAccounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieve a Spatial Anchors Account. |
| `SpatialAnchorsAccounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List Resources by Resource Group |
| `SpatialAnchorsAccounts_ListBySubscription` | `SELECT` | `subscriptionId` | List Spatial Anchors Accounts by Subscription |
| `SpatialAnchorsAccounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creating or Updating a Spatial Anchors Account. |
| `SpatialAnchorsAccounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete a Spatial Anchors Account. |
| `SpatialAnchorsAccounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | List Both of the 2 Keys of a Spatial Anchors Account |
| `SpatialAnchorsAccounts_RegenerateKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Regenerate specified Key of a Spatial Anchors Account |
| `SpatialAnchorsAccounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updating a Spatial Anchors Account |
