---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - apigeeregistry
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
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.apis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `apis` | `array` | The APIs from the specified publisher. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_list` | `SELECT` | `locationsId, projectsId` | Returns matching APIs. |
| `projects_locations_apis_create` | `INSERT` | `locationsId, projectsId` | Creates a specified API. |
| `projects_locations_apis_delete` | `DELETE` | `apisId, locationsId, projectsId` | Removes a specified API and all of the resources that it owns. |
| `projects_locations_apis_get` | `EXEC` | `apisId, locationsId, projectsId` | Returns a specified API. |
| `projects_locations_apis_patch` | `EXEC` | `apisId, locationsId, projectsId` | Used to modify a specified API. |
