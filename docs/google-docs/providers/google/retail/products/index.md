---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - retail
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token that can be sent as ListProductsRequest.page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `products` | `array` | The Products. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_branches_products_list` | `SELECT` | `branchesId, catalogsId, locationsId, projectsId` | Gets a list of Products. |
| `projects_locations_catalogs_branches_products_create` | `INSERT` | `branchesId, catalogsId, locationsId, projectsId` | Creates a Product. |
| `projects_locations_catalogs_branches_products_delete` | `DELETE` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Deletes a Product. |
| `projects_locations_catalogs_branches_products_get` | `EXEC` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Gets a Product. |
| `projects_locations_catalogs_branches_products_import` | `EXEC` | `branchesId, catalogsId, locationsId, projectsId` | Bulk import of multiple Products. Request processing may be synchronous. Non-existing items are created. Note that it is possible for a subset of the Products to be successfully updated. |
| `projects_locations_catalogs_branches_products_patch` | `EXEC` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Updates a Product. |
| `projects_locations_catalogs_branches_products_purge` | `EXEC` | `branchesId, catalogsId, locationsId, projectsId` | Permanently deletes all selected Products under a branch. This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of Products, this operation could take hours to complete. Before the operation completes, some Products may still be returned by ProductService.GetProduct or ProductService.ListProducts. Depending on the number of Products, this operation could take hours to complete. To get a sample of Products that would be deleted, set PurgeProductsRequest.force to false. |
| `projects_locations_catalogs_branches_products_set_inventory` | `EXEC` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Updates inventory information for a Product while respecting the last update timestamps of each inventory field. This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts. When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request. If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used. If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved. Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces. The returned Operations is obsolete after one day, and the GetOperation API returns `NOT_FOUND` afterwards. If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete. |
