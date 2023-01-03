---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
  - firestore
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
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firestore.indexes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. A server defined name for this index. The form of this name for composite indexes will be: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}` For single field indexes, this field will be empty. |
| `queryScope` | `string` | Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection id. Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection id as this index. |
| `state` | `string` | Output only. The serving state of the index. |
| `fields` | `array` | The fields supported by this index. For composite indexes, this is always 2 or more fields. The last field entry is always for the field path `__name__`. If, on creation, `__name__` was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the `__name__` will be ordered ASCENDING (unless explicitly specified). For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_databases_collectionGroups_indexes_get` | `SELECT` | `collectionGroupsId, databasesId, indexesId, projectsId` | Gets a composite index. |
| `projects_databases_collectionGroups_indexes_list` | `SELECT` | `collectionGroupsId, databasesId, projectsId` | Lists composite indexes. |
| `projects_databases_collectionGroups_indexes_create` | `INSERT` | `collectionGroupsId, databasesId, projectsId` | Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata. |
| `projects_databases_collectionGroups_indexes_delete` | `DELETE` | `collectionGroupsId, databasesId, indexesId, projectsId` | Deletes a composite index. |
