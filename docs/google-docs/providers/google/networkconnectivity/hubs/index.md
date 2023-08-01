---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
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
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `hubs` | `array` | The requested hubs. |
| `nextPageToken` | `string` | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubsId, projectsId` | Gets details about a Network Connectivity Center hub. |
| `list` | `SELECT` | `projectsId` | Lists the Network Connectivity Center hubs associated with a given project. |
| `create` | `INSERT` | `projectsId` | Creates a new Network Connectivity Center hub in the specified project. |
| `delete` | `DELETE` | `hubsId, projectsId` | Deletes a Network Connectivity Center hub. |
| `patch` | `EXEC` | `hubsId, projectsId` | Updates the description and/or labels of a Network Connectivity Center hub. |
