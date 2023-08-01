---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - discoveryengine
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.discoveryengine.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `operations` | `array` | A list of operations that matches the specified filter in the request. |
| `nextPageToken` | `string` | The standard List next-page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_collections_data_stores_branches_operations_list` | `SELECT` | `branchesId, collectionsId, dataStoresId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_collections_data_stores_models_operations_list` | `SELECT` | `collectionsId, dataStoresId, locationsId, modelsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_collections_data_stores_operations_list` | `SELECT` | `collectionsId, dataStoresId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_collections_data_stores_schemas_operations_list` | `SELECT` | `collectionsId, dataStoresId, locationsId, projectsId, schemasId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_collections_engines_operations_list` | `SELECT` | `collectionsId, enginesId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_collections_operations_list` | `SELECT` | `collectionsId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_data_stores_branches_operations_list` | `SELECT` | `branchesId, dataStoresId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_data_stores_models_operations_list` | `SELECT` | `dataStoresId, locationsId, modelsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_data_stores_operations_list` | `SELECT` | `dataStoresId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_operations_list` | `SELECT` | `locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_operations_list` | `SELECT` | `projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_collections_data_stores_branches_operations_get` | `EXEC` | `branchesId, collectionsId, dataStoresId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_collections_data_stores_models_operations_get` | `EXEC` | `collectionsId, dataStoresId, locationsId, modelsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_collections_data_stores_operations_get` | `EXEC` | `collectionsId, dataStoresId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_collections_data_stores_schemas_operations_get` | `EXEC` | `collectionsId, dataStoresId, locationsId, operationsId, projectsId, schemasId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_collections_data_stores_site_search_engine_operations_get` | `EXEC` | `collectionsId, dataStoresId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_collections_data_stores_site_search_engine_target_sites_operations_get` | `EXEC` | `collectionsId, dataStoresId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_collections_engines_operations_get` | `EXEC` | `collectionsId, enginesId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_collections_operations_get` | `EXEC` | `collectionsId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_data_stores_branches_operations_get` | `EXEC` | `branchesId, dataStoresId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_data_stores_models_operations_get` | `EXEC` | `dataStoresId, locationsId, modelsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_data_stores_operations_get` | `EXEC` | `dataStoresId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_operations_get` | `EXEC` | `locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_operations_get` | `EXEC` | `operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
