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
| `properties` | `object` | The collection details |
| `systemData` | `object` | Read only system data |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `collectionId, privateStoreId` | Gets private store collection |
| `list` | `SELECT` | `privateStoreId` | Gets private store collections list |
| `create_or_update` | `INSERT` | `collectionId, privateStoreId` | Create or update private store collection |
| `delete` | `DELETE` | `collectionId, privateStoreId` | Delete a collection from the given private store. |
| `_list` | `EXEC` | `privateStoreId` | Gets private store collections list |
| `approve_all_items` | `EXEC` | `collectionId, privateStoreId` | Delete all existing offers from the collection and enable approve all items. |
| `disable_approve_all_items` | `EXEC` | `collectionId, privateStoreId` | Disable approve all items for the collection. |
| `post` | `EXEC` | `collectionId, privateStoreId` | Delete Private store collection. This is a workaround. |
| `transfer_offers` | `EXEC` | `collectionId, privateStoreId` | transferring offers (copy or move) from source collection to target collection(s) |
