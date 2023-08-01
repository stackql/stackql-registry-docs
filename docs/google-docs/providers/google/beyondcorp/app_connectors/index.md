---
title: app_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - app_connectors
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
<tr><td><b>Name</b></td><td><code>app_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.beyondcorp.app_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `appConnectors` | `array` | A list of BeyondCorp AppConnectors in the project. |
| `nextPageToken` | `string` | A token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | A list of locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_app_connectors_list` | `SELECT` | `locationsId, projectsId` | Lists AppConnectors in a given project and location. |
| `projects_locations_app_connectors_create` | `INSERT` | `locationsId, projectsId` | Creates a new AppConnector in a given project and location. |
| `projects_locations_app_connectors_delete` | `DELETE` | `appConnectorsId, locationsId, projectsId` | Deletes a single AppConnector. |
| `projects_locations_app_connectors_get` | `EXEC` | `appConnectorsId, locationsId, projectsId` | Gets details of a single AppConnector. |
| `projects_locations_app_connectors_patch` | `EXEC` | `appConnectorsId, locationsId, projectsId` | Updates the parameters of a single AppConnector. |
| `projects_locations_app_connectors_report_status` | `EXEC` | `appConnectorsId, locationsId, projectsId` | Report status for a given connector. |
| `projects_locations_app_connectors_resolve_instance_config` | `EXEC` | `appConnectorsId, locationsId, projectsId` | Gets instance configuration for a given AppConnector. An internal method called by a AppConnector to get its container config. |
