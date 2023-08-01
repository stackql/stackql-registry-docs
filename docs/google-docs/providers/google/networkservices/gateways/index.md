---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
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
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `gateways` | `array` | List of Gateway resources. |
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gatewaysId, locationsId, projectsId` | Gets details of a single Gateway. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Gateways in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Gateway in a given project and location. |
| `delete` | `DELETE` | `gatewaysId, locationsId, projectsId` | Deletes a single Gateway. |
| `patch` | `EXEC` | `gatewaysId, locationsId, projectsId` | Updates the parameters of a single Gateway. |
