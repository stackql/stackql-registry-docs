---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `networks` | `array` | The list of networks. |
| `nextPageToken` | `string` | A token identifying a page of results from the server. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, networksId, projectsId` | Get details of a single network. |
| `list` | `SELECT` | `locationsId, projectsId` | List network in a given project and location. |
| `patch` | `EXEC` | `locationsId, networksId, projectsId` | Update details of a single network. |
| `rename` | `EXEC` | `locationsId, networksId, projectsId` | RenameNetwork sets a new name for a network. Use with caution, previous names become immediately invalidated. |
