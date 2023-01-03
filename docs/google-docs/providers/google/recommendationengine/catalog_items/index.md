---
title: catalog_items
hide_title: false
hide_table_of_contents: false
keywords:
  - catalog_items
  - recommendationengine
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
<tr><td><b>Name</b></td><td><code>catalog_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.catalog_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Required. Catalog item identifier. UTF-8 encoded string with a length limit of 128 bytes. This id must be unique among all catalog items within the same catalog. It should also be used when logging user events in order for the user events to be joined with the Catalog. |
| `description` | `string` | Optional. Catalog item description. UTF-8 encoded string with a length limit of 5 KiB. |
| `languageCode` | `string` | Optional. Deprecated. The model automatically detects the text language. Your catalog can include text in different languages, but duplicating catalog items to provide text in multiple languages can result in degraded model performance. |
| `itemGroupId` | `string` | Optional. Variant group identifier for prediction results. UTF-8 encoded string with a length limit of 128 bytes. This field must be enabled before it can be used. [Learn more](/recommendations-ai/docs/catalog#item-group-id). |
| `itemAttributes` | `object` | FeatureMap represents extra features that customers want to include in the recommendation model for catalogs/user events as categorical/numerical features. |
| `productMetadata` | `object` | ProductCatalogItem captures item metadata specific to retail products. |
| `title` | `string` | Required. Catalog item title. UTF-8 encoded string with a length limit of 1 KiB. |
| `tags` | `array` | Optional. Filtering tags associated with the catalog item. Each tag should be a UTF-8 encoded string with a length limit of 1 KiB. This tag can be used for filtering recommendation results by passing the tag as part of the predict request filter. |
| `categoryHierarchies` | `array` | Required. Catalog item categories. This field is repeated for supporting one catalog item belonging to several parallel category hierarchies. For example, if a shoes product belongs to both ["Shoes & Accessories" -&gt; "Shoes"] and ["Sports & Fitness" -&gt; "Athletic Clothing" -&gt; "Shoes"], it could be represented as: "categoryHierarchies": [ { "categories": ["Shoes & Accessories", "Shoes"]}, { "categories": ["Sports & Fitness", "Athletic Clothing", "Shoes"] } ] |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_catalogItems_get` | `SELECT` | `catalogItemsId, catalogsId, locationsId, projectsId` | Gets a specific catalog item. |
| `projects_locations_catalogs_catalogItems_list` | `SELECT` | `catalogsId, locationsId, projectsId` | Gets a list of catalog items. |
| `projects_locations_catalogs_catalogItems_create` | `INSERT` | `catalogsId, locationsId, projectsId` | Creates a catalog item. |
| `projects_locations_catalogs_catalogItems_delete` | `DELETE` | `catalogItemsId, catalogsId, locationsId, projectsId` | Deletes a catalog item. |
| `projects_locations_catalogs_catalogItems_import` | `EXEC` | `catalogsId, locationsId, projectsId` | Bulk import of multiple catalog items. Request processing may be synchronous. No partial updating supported. Non-existing items will be created. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully updated. |
| `projects_locations_catalogs_catalogItems_patch` | `EXEC` | `catalogItemsId, catalogsId, locationsId, projectsId` | Updates a catalog item. Partial updating is supported. Non-existing items will be created. |
