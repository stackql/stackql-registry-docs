---
title: app_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - app_connections
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
<tr><td><b>Name</b></td><td><code>app_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.beyondcorp.app_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `appConnections` | `array` | A list of BeyondCorp AppConnections in the project. |
| `nextPageToken` | `string` | A token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | A list of locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_app_connections_list` | `SELECT` | `locationsId, projectsId` | Lists AppConnections in a given project and location. |
| `projects_locations_app_connections_create` | `INSERT` | `locationsId, projectsId` | Creates a new AppConnection in a given project and location. |
| `projects_locations_app_connections_delete` | `DELETE` | `appConnectionsId, locationsId, projectsId` | Deletes a single AppConnection. |
| `projects_locations_app_connections_get` | `EXEC` | `appConnectionsId, locationsId, projectsId` | Gets details of a single AppConnection. |
| `projects_locations_app_connections_patch` | `EXEC` | `appConnectionsId, locationsId, projectsId` | Updates the parameters of a single AppConnection. |
| `projects_locations_app_connections_resolve` | `EXEC` | `locationsId, projectsId` | Resolves AppConnections details for a given AppConnector. An internal method called by a connector to find AppConnections to connect to. |
