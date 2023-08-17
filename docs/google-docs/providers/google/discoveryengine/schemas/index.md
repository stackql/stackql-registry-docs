---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
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
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.discoveryengine.schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The full resource name of the schema, in the format of `projects/&#123;project&#125;/locations/&#123;location&#125;/collections/&#123;collection&#125;/dataStores/&#123;data_store&#125;/schemas/&#123;schema&#125;`. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |
| `jsonSchema` | `string` | The JSON representation of the schema. |
| `structSchema` | `object` | The structured representation of the schema. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_collections_data_stores_schemas_list` | `SELECT` | `collectionsId, dataStoresId, locationsId, projectsId` | Gets a list of Schemas. |
| `projects_locations_data_stores_schemas_list` | `SELECT` | `dataStoresId, locationsId, projectsId` | Gets a list of Schemas. |
| `projects_locations_collections_data_stores_schemas_create` | `INSERT` | `collectionsId, dataStoresId, locationsId, projectsId` | Creates a Schema. |
| `projects_locations_data_stores_schemas_create` | `INSERT` | `dataStoresId, locationsId, projectsId` | Creates a Schema. |
| `projects_locations_collections_data_stores_schemas_delete` | `DELETE` | `collectionsId, dataStoresId, locationsId, projectsId, schemasId` | Deletes a Schema. |
| `projects_locations_data_stores_schemas_delete` | `DELETE` | `dataStoresId, locationsId, projectsId, schemasId` | Deletes a Schema. |
| `_projects_locations_collections_data_stores_schemas_list` | `EXEC` | `collectionsId, dataStoresId, locationsId, projectsId` | Gets a list of Schemas. |
| `_projects_locations_data_stores_schemas_list` | `EXEC` | `dataStoresId, locationsId, projectsId` | Gets a list of Schemas. |
| `projects_locations_collections_data_stores_schemas_get` | `EXEC` | `collectionsId, dataStoresId, locationsId, projectsId, schemasId` | Gets a Schema. |
| `projects_locations_collections_data_stores_schemas_patch` | `EXEC` | `collectionsId, dataStoresId, locationsId, projectsId, schemasId` | Updates a Schema. |
| `projects_locations_data_stores_schemas_get` | `EXEC` | `dataStoresId, locationsId, projectsId, schemasId` | Gets a Schema. |
| `projects_locations_data_stores_schemas_patch` | `EXEC` | `dataStoresId, locationsId, projectsId, schemasId` | Updates a Schema. |
