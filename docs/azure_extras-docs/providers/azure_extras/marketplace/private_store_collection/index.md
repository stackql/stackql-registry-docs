---
title: private_store_collection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_collection
  - marketplace
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
<tr><td><b>Name</b></td><td><code>private_store_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.marketplace.private_store_collection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `systemData` | `object` | Read only system data |
| `type` | `string` | The type of the resource. |
| `properties` | `object` | The collection details |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateStoreCollection_Get` | `SELECT` | `collectionId, privateStoreId` | Gets private store collection |
| `PrivateStoreCollection_List` | `SELECT` | `privateStoreId` | Gets private store collections list |
| `PrivateStoreCollection_CreateOrUpdate` | `INSERT` | `collectionId, privateStoreId` | Create or update private store collection |
| `PrivateStoreCollection_Delete` | `DELETE` | `collectionId, privateStoreId` | Delete a collection from the given private store. |
| `PrivateStoreCollection_ApproveAllItems` | `EXEC` | `collectionId, privateStoreId` | Delete all existing offers from the collection and enable approve all items. |
| `PrivateStoreCollection_DisableApproveAllItems` | `EXEC` | `collectionId, privateStoreId` | Disable approve all items for the collection. |
| `PrivateStoreCollection_Post` | `EXEC` | `collectionId, privateStoreId` | Delete Private store collection. This is a workaround. |
| `PrivateStoreCollection_TransferOffers` | `EXEC` | `collectionId, privateStoreId` | transferring offers (copy or move) from source collection to target collection(s) |
