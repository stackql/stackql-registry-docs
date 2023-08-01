---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
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
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.discoveryengine.documents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token that can be sent as ListDocumentsRequest.page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `documents` | `array` | The Documents. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_collections_data_stores_branches_documents_list` | `SELECT` | `branchesId, collectionsId, dataStoresId, locationsId, projectsId` | Gets a list of Documents. |
| `projects_locations_data_stores_branches_documents_list` | `SELECT` | `branchesId, dataStoresId, locationsId, projectsId` | Gets a list of Documents. |
| `projects_locations_collections_data_stores_branches_documents_create` | `INSERT` | `branchesId, collectionsId, dataStoresId, locationsId, projectsId` | Creates a Document. |
| `projects_locations_data_stores_branches_documents_create` | `INSERT` | `branchesId, dataStoresId, locationsId, projectsId` | Creates a Document. |
| `projects_locations_collections_data_stores_branches_documents_delete` | `DELETE` | `branchesId, collectionsId, dataStoresId, documentsId, locationsId, projectsId` | Deletes a Document. |
| `projects_locations_data_stores_branches_documents_delete` | `DELETE` | `branchesId, dataStoresId, documentsId, locationsId, projectsId` | Deletes a Document. |
| `projects_locations_collections_data_stores_branches_documents_get` | `EXEC` | `branchesId, collectionsId, dataStoresId, documentsId, locationsId, projectsId` | Gets a Document. |
| `projects_locations_collections_data_stores_branches_documents_import` | `EXEC` | `branchesId, collectionsId, dataStoresId, locationsId, projectsId` | Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items will be created. Note: It is possible for a subset of the Documents to be successfully updated. |
| `projects_locations_collections_data_stores_branches_documents_patch` | `EXEC` | `branchesId, collectionsId, dataStoresId, documentsId, locationsId, projectsId` | Updates a Document. |
| `projects_locations_collections_data_stores_branches_documents_purge` | `EXEC` | `branchesId, collectionsId, dataStoresId, locationsId, projectsId` | Permanently deletes all selected Documents in a branch. This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments. To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false. |
| `projects_locations_data_stores_branches_documents_get` | `EXEC` | `branchesId, dataStoresId, documentsId, locationsId, projectsId` | Gets a Document. |
| `projects_locations_data_stores_branches_documents_import` | `EXEC` | `branchesId, dataStoresId, locationsId, projectsId` | Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items will be created. Note: It is possible for a subset of the Documents to be successfully updated. |
| `projects_locations_data_stores_branches_documents_patch` | `EXEC` | `branchesId, dataStoresId, documentsId, locationsId, projectsId` | Updates a Document. |
| `projects_locations_data_stores_branches_documents_purge` | `EXEC` | `branchesId, dataStoresId, locationsId, projectsId` | Permanently deletes all selected Documents in a branch. This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments. To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false. |
