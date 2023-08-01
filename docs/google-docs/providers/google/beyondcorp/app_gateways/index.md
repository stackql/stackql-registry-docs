---
title: app_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - app_gateways
  - beyondcorp
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
<tr><td><b>Name</b></td><td><code>app_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.beyondcorp.app_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | A list of locations that could not be reached. |
| `appGateways` | `array` | A list of BeyondCorp AppGateways in the project. |
| `nextPageToken` | `string` | A token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_app_gateways_list` | `SELECT` | `locationsId, projectsId` | Lists AppGateways in a given project and location. |
| `projects_locations_app_gateways_create` | `INSERT` | `locationsId, projectsId` | Creates a new AppGateway in a given project and location. |
| `projects_locations_app_gateways_delete` | `DELETE` | `appGatewaysId, locationsId, projectsId` | Deletes a single AppGateway. |
| `projects_locations_app_gateways_get` | `EXEC` | `appGatewaysId, locationsId, projectsId` | Gets details of a single AppGateway. |
