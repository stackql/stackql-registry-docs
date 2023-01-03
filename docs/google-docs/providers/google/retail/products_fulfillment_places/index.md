---
title: products_fulfillment_places
hide_title: false
hide_table_of_contents: false
keywords:
  - products_fulfillment_places
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
<tr><td><b>Name</b></td><td><code>products_fulfillment_places</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.products_fulfillment_places</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_branches_products_addFulfillmentPlaces` | `INSERT` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Incrementally adds place IDs to Product.fulfillment_info.place_ids. This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by GetProduct or ListProducts. This feature is only available for users who have Retail Search enabled. Please enable Retail Search on Cloud Console before using this feature. |
| `projects_locations_catalogs_branches_products_removeFulfillmentPlaces` | `DELETE` | `branchesId, catalogsId, locationsId, productsId, projectsId` | Incrementally removes place IDs from a Product.fulfillment_info.place_ids. This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by GetProduct or ListProducts. This feature is only available for users who have Retail Search enabled. Please enable Retail Search on Cloud Console before using this feature. |
