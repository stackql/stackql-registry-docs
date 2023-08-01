---
title: private_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_connections
  - datastream
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
<tr><td><b>Id</b></td><td><code>google.datastream.private_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `privateConnections` | `array` | List of private connectivity configurations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, privateConnectionsId, projectsId` | Use this method to get details about a private connectivity configuration. |
| `list` | `SELECT` | `locationsId, projectsId` | Use this method to list private connectivity configurations in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Use this method to create a private connectivity configuration. |
| `delete` | `DELETE` | `locationsId, privateConnectionsId, projectsId` | Use this method to delete a private connectivity configuration. |
