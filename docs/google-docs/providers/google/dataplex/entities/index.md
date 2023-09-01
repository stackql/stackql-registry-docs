---
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
  - dataplex
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
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.entities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Required. A user-provided entity ID. It is mutable, and will be used as the published table name. Specifying a new ID in an update entity request will override the existing value. The ID must contain only letters (a-z, A-Z), numbers (0-9), and underscores, and consist of 256 or fewer characters. |
| `name` | `string` | Output only. The resource name of the entity, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/zones/&#123;zone_id&#125;/entities/&#123;id&#125;. |
| `description` | `string` | Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters. |
| `schema` | `object` | Schema information describing the structure and layout of the data. |
| `uid` | `string` | Output only. System generated unique ID for the Entity. This ID will be different if the Entity is deleted and re-created with the same name. |
| `dataPath` | `string` | Required. Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as gs://bucket/path/to/data. For BigQuery data, this is the name of the table resource, such as projects/project_id/datasets/dataset_id/tables/table_id. |
| `catalogEntry` | `string` | Output only. The name of the associated Data Catalog entry. |
| `format` | `object` | Describes the format of the data within its storage location. |
| `createTime` | `string` | Output only. The time when the entity was created. |
| `system` | `string` | Required. Immutable. Identifies the storage system of the entity data. |
| `displayName` | `string` | Optional. Display name must be shorter than or equal to 256 characters. |
| `access` | `object` | Describes the access mechanism of the data within its storage location. |
| `etag` | `string` | Optional. The etag associated with the entity, which can be retrieved with a GetEntity request. Required for update and delete requests. |
| `compatibility` | `object` | Provides compatibility information for various metadata stores. |
| `dataPathPattern` | `string` | Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: gs://bucket/path/to/data/**/*.csv. |
| `updateTime` | `string` | Output only. The time when the entity was last updated. |
| `type` | `string` | Required. Immutable. The type of entity. |
| `asset` | `string` | Required. Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_entities_get` | `SELECT` | `entitiesId, lakesId, locationsId, projectsId, zonesId` | Get a metadata entity. |
| `projects_locations_lakes_zones_entities_list` | `SELECT` | `lakesId, locationsId, projectsId, zonesId` | List metadata entities in a zone. |
| `projects_locations_lakes_zones_entities_create` | `INSERT` | `lakesId, locationsId, projectsId, zonesId` | Create a metadata entity. |
| `projects_locations_lakes_zones_entities_delete` | `DELETE` | `entitiesId, lakesId, locationsId, projectsId, zonesId` | Delete a metadata entity. |
| `_projects_locations_lakes_zones_entities_list` | `EXEC` | `lakesId, locationsId, projectsId, zonesId` | List metadata entities in a zone. |
| `projects_locations_lakes_zones_entities_update` | `EXEC` | `entitiesId, lakesId, locationsId, projectsId, zonesId` | Update a metadata entity. Only supports full resource update. |
