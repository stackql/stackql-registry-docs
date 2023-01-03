---
title: metadata_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_imports
  - metastore
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
<tr><td><b>Name</b></td><td><code>metadata_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.metadata_imports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}. |
| `description` | `string` | The description of the metadata import. |
| `createTime` | `string` | Output only. The time when the metadata import was started. |
| `databaseDump` | `object` | A specification of the location of and metadata about a database dump from a relational database management system. |
| `endTime` | `string` | Output only. The time when the metadata import finished. |
| `state` | `string` | Output only. The current state of the metadata import. |
| `updateTime` | `string` | Output only. The time when the metadata import was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_services_metadataImports_get` | `SELECT` | `locationsId, metadataImportsId, projectsId, servicesId` | Gets details of a single import. |
| `projects_locations_services_metadataImports_list` | `SELECT` | `locationsId, projectsId, servicesId` | Lists imports in a service. |
| `projects_locations_services_metadataImports_create` | `INSERT` | `locationsId, projectsId, servicesId` | Creates a new MetadataImport in a given project and location. |
| `projects_locations_services_metadataImports_patch` | `EXEC` | `locationsId, metadataImportsId, projectsId, servicesId` | Updates a single import. Only the description field of MetadataImport is supported to be updated. |
