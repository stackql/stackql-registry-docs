---
title: meshes
hide_title: false
hide_table_of_contents: false
keywords:
  - meshes
  - networkservices
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
<tr><td><b>Name</b></td><td><code>meshes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.meshes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the Mesh resource. It matches pattern `projects/*/locations/global/meshes/`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `labels` | `object` | Optional. Set of label tags associated with the Mesh resource. |
| `selfLink` | `string` | Output only. Server-defined URL of this resource |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `interceptionPort` | `integer` | Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port '15001' is used as the interception port. This will is applicable only for sidecar proxy deployments. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_meshes_get` | `SELECT` | `locationsId, meshesId, projectsId` | Gets details of a single Mesh. |
| `projects_locations_meshes_list` | `SELECT` | `locationsId, projectsId` | Lists Meshes in a given project and location. |
| `projects_locations_meshes_create` | `INSERT` | `locationsId, projectsId` | Creates a new Mesh in a given project and location. |
| `projects_locations_meshes_delete` | `DELETE` | `locationsId, meshesId, projectsId` | Deletes a single Mesh. |
| `projects_locations_meshes_patch` | `EXEC` | `locationsId, meshesId, projectsId` | Updates the parameters of a single Mesh. |
