---
title: storage_mover
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_mover
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>storage_mover</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_mover.storage_mover</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The resource specific properties for the Storage Mover resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageMovers_Get` | `SELECT` | `resourceGroupName, storageMoverName, subscriptionId` | Gets a Storage Mover resource. |
| `StorageMovers_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Storage Movers in a resource group. |
| `StorageMovers_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all Storage Movers in a subscription. |
| `StorageMovers_CreateOrUpdate` | `INSERT` | `resourceGroupName, storageMoverName, subscriptionId` | Creates or updates a top-level Storage Mover resource. |
| `StorageMovers_Delete` | `DELETE` | `resourceGroupName, storageMoverName, subscriptionId` | Deletes a Storage Mover resource. |
| `StorageMovers_Update` | `EXEC` | `resourceGroupName, storageMoverName, subscriptionId` | Updates properties for a Storage Mover resource. Properties not specified in the request body will be unchanged. |
