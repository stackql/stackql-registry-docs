---
title: service_connection_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - service_connection_maps
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>service_connection_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.service_connection_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |
| `serviceConnectionMaps` | `array` | ServiceConnectionMaps to be returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceConnectionMapsId` | Gets details of a single ServiceConnectionMap. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceConnectionMaps in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceConnectionMap in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceConnectionMapsId` | Deletes a single ServiceConnectionMap. |
| `patch` | `EXEC` | `locationsId, projectsId, serviceConnectionMapsId` | Updates the parameters of a single ServiceConnectionMap. |
