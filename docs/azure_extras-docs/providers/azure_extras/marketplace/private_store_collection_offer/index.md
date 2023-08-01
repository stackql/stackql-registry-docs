---
title: private_store_collection_offer
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_collection_offer
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
<tr><td><b>Name</b></td><td><code>private_store_collection_offer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.marketplace.private_store_collection_offer</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` |  |
| `systemData` | `object` | Read only system data |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateStoreCollectionOffer_Get` | `SELECT` | `collectionId, offerId, privateStoreId` | Gets information about a specific offer. |
| `PrivateStoreCollectionOffer_List` | `SELECT` | `collectionId, privateStoreId` | Get a list of all private offers in the given private store and collection |
| `PrivateStoreCollectionOffer_CreateOrUpdate` | `INSERT` | `collectionId, offerId, privateStoreId` | Update or add an offer to a specific collection of the private store. |
| `PrivateStoreCollectionOffer_Delete` | `DELETE` | `collectionId, offerId, privateStoreId` | Deletes an offer from the given collection of private store. |
| `PrivateStoreCollectionOffer_Post` | `EXEC` | `collectionId, offerId, privateStoreId` | Delete Private store offer. This is a workaround. |
| `PrivateStoreCollectionOffer_UpsertOfferWithMultiContext` | `EXEC` | `collectionId, offerId, privateStoreId` | Upsert an offer with multiple context details. |
