---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource's name. |
| `labels` | `object` | Labels. |
| `updateTime` | `string` | Output only. The update time of the resource. |
| `createTime` | `string` | Output only. The create time of the resource. |
| `destinationAddress` | `string` | Required. Destination address for connection |
| `destinationPort` | `integer` | Destination port for connection |
| `displayName` | `string` | Required. Display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, privateConnectionsId, projectsId, routesId` | Use this method to get details about a route. |
| `list` | `SELECT` | `locationsId, privateConnectionsId, projectsId` | Use this method to list routes created for a private connectivity configuration in a project and location. |
| `create` | `INSERT` | `locationsId, privateConnectionsId, projectsId` | Use this method to create a route for a private connectivity configuration in a project and location. |
| `delete` | `DELETE` | `locationsId, privateConnectionsId, projectsId, routesId` | Use this method to delete a route. |
| `_list` | `EXEC` | `locationsId, privateConnectionsId, projectsId` | Use this method to list routes created for a private connectivity configuration in a project and location. |
