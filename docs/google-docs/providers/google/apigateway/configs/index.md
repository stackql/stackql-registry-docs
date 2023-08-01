---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
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
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigateway.configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `apiConfigs` | `array` | API Configs. |
| `nextPageToken` | `string` | Next page token. |
| `unreachableLocations` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apisId, configsId, locationsId, projectsId` | Gets details of a single ApiConfig. |
| `list` | `SELECT` | `apisId, locationsId, projectsId` | Lists ApiConfigs in a given project and location. |
| `create` | `INSERT` | `apisId, locationsId, projectsId` | Creates a new ApiConfig in a given project and location. |
| `delete` | `DELETE` | `apisId, configsId, locationsId, projectsId` | Deletes a single ApiConfig. |
| `patch` | `EXEC` | `apisId, configsId, locationsId, projectsId` | Updates the parameters of a single ApiConfig. |
