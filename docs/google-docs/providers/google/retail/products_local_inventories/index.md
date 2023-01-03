---
title: products_local_inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - products_local_inventories
  - retail
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
<tr><td><b>Name</b></td><td><code>products_local_inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.products_local_inventories</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_branches_products_addLocalInventories` | `INSERT` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field. This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by GetProduct or ListProducts. Local inventory information can only be modified using this method. CreateProduct and UpdateProduct has no effect on local inventories. This feature is only available for users who have Retail Search enabled. Please enable Retail Search on Cloud Console before using this feature. |
| `projects_locations_catalogs_branches_products_removeLocalInventories` | `DELETE` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Remove local inventory information for a Product at a list of places at a removal timestamp. This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by GetProduct or ListProducts. Local inventory information can only be removed using this method. CreateProduct and UpdateProduct has no effect on local inventories. This feature is only available for users who have Retail Search enabled. Please enable Retail Search on Cloud Console before using this feature. |
