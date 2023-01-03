---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - bigqueryconnection
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigqueryconnection.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}` |
| `description` | `string` | User provided description. |
| `cloudSql` | `object` | Connection properties specific to the Cloud SQL. |
| `creationTime` | `string` | Output only. The creation timestamp of the connection. |
| `friendlyName` | `string` | User provided display name for the connection. |
| `hasCredential` | `boolean` | Output only. True, if credential is configured for this connection. |
| `lastModifiedTime` | `string` | Output only. The last update timestamp of the connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_connections_get` | `SELECT` | `connectionsId, locationsId, projectsId` | Returns specified connection. |
| `projects_locations_connections_list` | `SELECT` | `locationsId, projectsId` | Returns a list of connections in the given project. |
| `projects_locations_connections_create` | `INSERT` | `locationsId, projectsId` | Creates a new connection. |
| `projects_locations_connections_delete` | `DELETE` | `connectionsId, locationsId, projectsId` | Deletes connection and associated credential. |
| `projects_locations_connections_patch` | `EXEC` | `connectionsId, locationsId, projectsId` | Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask. |
| `projects_locations_connections_updateCredential` | `EXEC` | `connectionsId, locationsId, projectsId` | Sets the credential for the specified connection. |
