---
title: lakes
hide_title: false
hide_table_of_contents: false
keywords:
  - lakes
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
<tr><td><b>Name</b></td><td><code>lakes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.lakes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the lake, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;. |
| `description` | `string` | Optional. Description of the lake. |
| `metastore` | `object` | Settings to manage association of Dataproc Metastore with a lake. |
| `createTime` | `string` | Output only. The time when the lake was created. |
| `labels` | `object` | Optional. User-defined labels for the lake. |
| `updateTime` | `string` | Output only. The time when the lake was last updated. |
| `displayName` | `string` | Optional. User friendly display name. |
| `state` | `string` | Output only. Current state of the lake. |
| `serviceAccount` | `string` | Output only. Service account associated with this lake. This service account must be authorized to access or operate on resources managed by the lake. |
| `metastoreStatus` | `object` | Status of Lake and Dataproc Metastore service instance association. |
| `uid` | `string` | Output only. System generated globally unique ID for the lake. This ID will be different if the lake is deleted and re-created with the same name. |
| `assetStatus` | `object` | Aggregated status of the underlying assets of a lake or zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_get` | `SELECT` | `lakesId, locationsId, projectsId` | Retrieves a lake resource. |
| `projects_locations_lakes_list` | `SELECT` | `locationsId, projectsId` | Lists lake resources in a project and location. |
| `projects_locations_lakes_create` | `INSERT` | `locationsId, projectsId` | Creates a lake resource. |
| `projects_locations_lakes_delete` | `DELETE` | `lakesId, locationsId, projectsId` | Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted. |
| `_projects_locations_lakes_list` | `EXEC` | `locationsId, projectsId` | Lists lake resources in a project and location. |
| `projects_locations_lakes_patch` | `EXEC` | `lakesId, locationsId, projectsId` | Updates a lake resource. |
