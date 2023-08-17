---
title: tls_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - tls_routes
  - networkservices
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
<tr><td><b>Name</b></td><td><code>tls_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.tls_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the TlsRoute resource. It matches pattern `projects/*/locations/global/tlsRoutes/tls_route_name&gt;`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `gateways` | `array` | Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
| `meshes` | `array` | Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` The attached Mesh should be of a type SIDECAR |
| `rules` | `array` | Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match. |
| `selfLink` | `string` | Output only. Server-defined URL of this resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, tlsRoutesId` | Gets details of a single TlsRoute. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists TlsRoute in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new TlsRoute in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, tlsRoutesId` | Deletes a single TlsRoute. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists TlsRoute in a given project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, tlsRoutesId` | Updates the parameters of a single TlsRoute. |
