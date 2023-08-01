---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |
| `routes` | `array` | The requested routes. |
| `unreachable` | `array` | RouteTables that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubsId, projectsId, routeTablesId, routesId` | Gets details about the specified route. |
| `list` | `SELECT` | `hubsId, projectsId, routeTablesId` | Lists routes in a given project. |
