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
| `name` | `string` | Required. Unique resource name of the AppConnection. The name is ignored when creating a AppConnection. |
| `applicationEndpoint` | `object` | ApplicationEndpoint represents a remote application endpoint. |
| `uid` | `string` | Output only. A unique identifier for the instance generated by the system. |
| `type` | `string` | Required. The type of network connectivity used by the AppConnection. |
| `connectors` | `array` | Optional. List of [google.cloud.beyondcorp.v1main.Connector.name] that are authorised to be associated with this AppConnection. |
| `displayName` | `string` | Optional. An arbitrary user-provided name for the AppConnection. Cannot exceed 64 characters. |
| `labels` | `object` | Optional. Resource labels to represent user provided metadata. |
| `createTime` | `string` | Output only. Timestamp when the resource was created. |
| `updateTime` | `string` | Output only. Timestamp when the resource was last modified. |
| `gateway` | `object` | Gateway represents a user facing component that serves as an entrance to enable connectivity. |
| `state` | `string` | Output only. The current state of the AppConnection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_app_connections_get` | `SELECT` | `appConnectionsId, locationsId, projectsId` | Gets details of a single AppConnection. |
| `projects_locations_app_connections_list` | `SELECT` | `locationsId, projectsId` | Lists AppConnections in a given project and location. |
| `projects_locations_app_connections_create` | `INSERT` | `locationsId, projectsId` | Creates a new AppConnection in a given project and location. |
| `projects_locations_app_connections_delete` | `DELETE` | `appConnectionsId, locationsId, projectsId` | Deletes a single AppConnection. |
| `_projects_locations_app_connections_list` | `EXEC` | `locationsId, projectsId` | Lists AppConnections in a given project and location. |
| `projects_locations_app_connections_patch` | `EXEC` | `appConnectionsId, locationsId, projectsId` | Updates the parameters of a single AppConnection. |
| `projects_locations_app_connections_resolve` | `EXEC` | `locationsId, projectsId` | Resolves AppConnections details for a given AppConnector. An internal method called by a connector to find AppConnections to connect to. |
