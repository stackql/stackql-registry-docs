---
title: private_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_connections
  - datamigration
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
<tr><td><b>Name</b></td><td><code>private_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.private_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `privateConnections` | `array` | List of private connections. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, privateConnectionsId, projectsId` | Gets details of a single private connection. |
| `list` | `SELECT` | `locationsId, projectsId` | Retrieves a list of private connections in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new private connection in a given project and location. |
| `delete` | `DELETE` | `locationsId, privateConnectionsId, projectsId` | Deletes a single Database Migration Service private connection. |
