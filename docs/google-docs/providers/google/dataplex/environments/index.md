---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - dataplex
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the environment, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id} |
| `description` | `string` | Optional. Description of the environment. |
| `createTime` | `string` | Output only. Environment creation time. |
| `infrastructureSpec` | `object` | Configuration for the underlying infrastructure used to run workloads. |
| `sessionSpec` | `object` |  |
| `uid` | `string` | Output only. System generated globally unique ID for the environment. This ID will be different if the environment is deleted and re-created with the same name. |
| `updateTime` | `string` | Output only. The time when the environment was last updated. |
| `state` | `string` | Output only. Current state of the environment. |
| `labels` | `object` | Optional. User defined labels for the environment. |
| `displayName` | `string` | Optional. User friendly display name. |
| `endpoints` | `object` |  |
| `sessionStatus` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_environments_get` | `SELECT` | `environmentsId, lakesId, locationsId, projectsId` | Get environment resource. |
| `projects_locations_lakes_environments_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists environments under the given lake. |
| `projects_locations_lakes_environments_create` | `INSERT` | `lakesId, locationsId, projectsId` | Create an environment resource. |
| `projects_locations_lakes_environments_delete` | `DELETE` | `environmentsId, lakesId, locationsId, projectsId` | Delete the environment resource. All the child resources must have been deleted before environment deletion can be initiated. |
| `projects_locations_lakes_environments_patch` | `EXEC` | `environmentsId, lakesId, locationsId, projectsId` | Update the environment resource. |
