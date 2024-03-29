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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | The resource name of the connection in the form of: `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/connections/&#123;connection_id&#125;` |
| `description` | `string` | User provided description. |
| `friendlyName` | `string` | User provided display name for the connection. |
| `hasCredential` | `boolean` | Output only. True, if credential is configured for this connection. |
| `lastModifiedTime` | `string` | Output only. The last update timestamp of the connection. |
| `cloudSql` | `object` | Connection properties specific to the Cloud SQL. |
| `creationTime` | `string` | Output only. The creation timestamp of the connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionsId, locationsId, projectsId` | Returns specified connection. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns a list of connections in the given project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new connection. |
| `delete` | `DELETE` | `connectionsId, locationsId, projectsId` | Deletes connection and associated credential. |
| `_list` | `EXEC` | `locationsId, projectsId` | Returns a list of connections in the given project. |
| `patch` | `EXEC` | `connectionsId, locationsId, projectsId` | Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask. |
