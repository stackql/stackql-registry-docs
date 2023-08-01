---
title: spokes
hide_title: false
hide_table_of_contents: false
keywords:
  - spokes
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
<tr><td><b>Name</b></td><td><code>spokes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.spokes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `spokes` | `array` | The requested spokes. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, spokesId` | Gets details about a Network Connectivity Center spoke. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists the Network Connectivity Center spokes in a specified project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a Network Connectivity Center spoke. |
| `delete` | `DELETE` | `locationsId, projectsId, spokesId` | Deletes a Network Connectivity Center spoke. |
| `accept` | `EXEC` | `locationsId, projectsId, spokesId` | Accepts a proposal to attach a Network Connectivity Center spoke to the hub. |
| `patch` | `EXEC` | `locationsId, projectsId, spokesId` | Updates the parameters of a Network Connectivity Center spoke. |
| `reject` | `EXEC` | `locationsId, projectsId, spokesId` | Rejects a Network Connectivity Center spoke from being attached to the hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub. |
