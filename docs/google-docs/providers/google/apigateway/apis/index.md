---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - apigateway
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
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigateway.apis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachableLocations` | `array` | Locations that could not be reached. |
| `apis` | `array` | APIs. |
| `nextPageToken` | `string` | Next page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apisId, locationsId, projectsId` | Gets details of a single Api. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Apis in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Api in a given project and location. |
| `delete` | `DELETE` | `apisId, locationsId, projectsId` | Deletes a single Api. |
| `patch` | `EXEC` | `apisId, locationsId, projectsId` | Updates the parameters of a single Api. |
