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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `nextPageToken` | `string` | If empty, the list is complete. If nonempty, the token to pass to the next request's ListCatalogItemRequest.page_token. |
| `catalogItems` | `array` | The catalog items. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_catalog_items_get` | `SELECT` | `catalogItemsId, catalogsId, locationsId, projectsId` | Gets a specific catalog item. |
| `projects_locations_catalogs_catalog_items_list` | `SELECT` | `catalogsId, locationsId, projectsId` | Gets a list of catalog items. |
| `projects_locations_catalogs_catalog_items_create` | `INSERT` | `catalogsId, locationsId, projectsId` | Creates a catalog item. |
| `projects_locations_catalogs_catalog_items_delete` | `DELETE` | `catalogItemsId, catalogsId, locationsId, projectsId` | Deletes a catalog item. |
| `projects_locations_catalogs_catalog_items_import` | `EXEC` | `catalogsId, locationsId, projectsId` | Bulk import of multiple catalog items. Request processing may be synchronous. No partial updating supported. Non-existing items will be created. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully updated. |
| `projects_locations_catalogs_catalog_items_patch` | `EXEC` | `catalogItemsId, catalogsId, locationsId, projectsId` | Updates a catalog item. Partial updating is supported. Non-existing items will be created. |
