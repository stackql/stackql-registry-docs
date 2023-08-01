---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - ids
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ids.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Locations that could not be reached. |
| `endpoints` | `array` | The list of endpoints response. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointsId, locationsId, projectsId` | Gets details of a single Endpoint. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Endpoints in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Endpoint in a given project and location. |
| `delete` | `DELETE` | `endpointsId, locationsId, projectsId` | Deletes a single Endpoint. |
| `patch` | `EXEC` | `endpointsId, locationsId, projectsId` | Updates the parameters of a single Endpoint. |
