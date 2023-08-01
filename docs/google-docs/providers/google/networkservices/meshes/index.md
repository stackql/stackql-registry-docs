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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
| `meshes` | `array` | List of Mesh resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, meshesId, projectsId` | Gets details of a single Mesh. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Meshes in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Mesh in a given project and location. |
| `delete` | `DELETE` | `locationsId, meshesId, projectsId` | Deletes a single Mesh. |
| `patch` | `EXEC` | `locationsId, meshesId, projectsId` | Updates the parameters of a single Mesh. |
