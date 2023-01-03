---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - vision
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vision.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the product. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`. This field is ignored when creating a product. |
| `description` | `string` | User-provided metadata to be stored with this product. Must be at most 4096 characters long. |
| `displayName` | `string` | The user-provided name for this Product. Must not be empty. Must be at most 4096 characters long. |
| `productCategory` | `string` | Immutable. The category for the product identified by the reference image. This should be one of "homegoods-v2", "apparel-v2", "toys-v2", "packagedgoods-v1" or "general-v1". The legacy categories "homegoods", "apparel", and "toys" are still supported, but these should not be used for new products. |
| `productLabels` | `array` | Key-value pairs that can be attached to a product. At query time, constraints can be specified based on the product_labels. Note that integer values can be provided as strings, e.g. "1199". Only strings with integer values can match a range-based restriction which is to be supported soon. Multiple values can be assigned to the same key. One product may have up to 500 product_labels. Notice that the total number of distinct product_labels over all products in one ProductSet cannot exceed 1M, otherwise the product search pipeline will refuse to work for that ProductSet. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_productSets_products_list` | `SELECT` | `locationsId, productSetsId, projectsId` | Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. |
| `projects_locations_products_get` | `SELECT` | `locationsId, productsId, projectsId` | Gets information associated with a Product. Possible errors: * Returns NOT_FOUND if the Product does not exist. |
| `projects_locations_products_list` | `SELECT` | `locationsId, projectsId` | Lists products in an unspecified order. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. |
| `projects_locations_products_create` | `INSERT` | `locationsId, projectsId` | Creates and returns a new product resource. Possible errors: * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters. * Returns INVALID_ARGUMENT if description is longer than 4096 characters. * Returns INVALID_ARGUMENT if product_category is missing or invalid. |
| `projects_locations_products_delete` | `DELETE` | `locationsId, productsId, projectsId` | Permanently deletes a product and its reference images. Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed. |
| `projects_locations_products_patch` | `EXEC` | `locationsId, productsId, projectsId` | Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now. If labels are updated, the change will not be reflected in queries until the next index time. Possible errors: * Returns NOT_FOUND if the Product does not exist. * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters. * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters. * Returns INVALID_ARGUMENT if product_category is present in update_mask. |
| `projects_locations_products_purge` | `EXEC` | `locationsId, projectsId` | Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet. If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted. It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted. It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion. If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet. The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) |
