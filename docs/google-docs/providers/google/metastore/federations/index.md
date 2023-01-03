---
title: federations
hide_title: false
hide_table_of_contents: false
keywords:
  - federations
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
<tr><td><b>Name</b></td><td><code>federations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.federations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the federation, of the form: projects/{project_number}/locations/{location_id}/federations/{federation_id}`. |
| `updateTime` | `string` | Output only. The time when the metastore federation was last updated. |
| `version` | `string` | Immutable. The Apache Hive metastore version of the federation. All backend metastore versions must be compatible with the federation version. |
| `endpointUri` | `string` | Output only. The federation endpoint. |
| `uid` | `string` | Output only. The globally unique resource identifier of the metastore federation. |
| `labels` | `object` | User-defined labels for the metastore federation. |
| `createTime` | `string` | Output only. The time when the metastore federation was created. |
| `state` | `string` | Output only. The current state of the federation. |
| `stateMessage` | `string` | Output only. Additional information about the current state of the metastore federation, if available. |
| `backendMetastores` | `object` | A map from BackendMetastore rank to BackendMetastores from which the federation service serves metadata at query time. The map key represents the order in which BackendMetastores should be evaluated to resolve database names at query time and should be greater than or equal to zero. A BackendMetastore with a lower number will be evaluated before a BackendMetastore with a higher number. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_federations_get` | `SELECT` | `federationsId, locationsId, projectsId` | Gets the details of a single federation. |
| `projects_locations_federations_list` | `SELECT` | `locationsId, projectsId` | Lists federations in a project and location. |
| `projects_locations_federations_create` | `INSERT` | `locationsId, projectsId` | Creates a metastore federation in a project and location. |
| `projects_locations_federations_delete` | `DELETE` | `federationsId, locationsId, projectsId` | Deletes a single federation. |
| `projects_locations_federations_patch` | `EXEC` | `federationsId, locationsId, projectsId` | Updates the fields of a federation. |
