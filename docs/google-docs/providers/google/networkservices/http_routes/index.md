---
title: http_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - http_routes
  - networkservices
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
<tr><td><b>Name</b></td><td><code>http_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.http_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the HttpRoute resource. It matches pattern `projects/*/locations/global/httpRoutes/http_route_name&gt;`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `rules` | `array` | Required. Rules that define how traffic is routed and handled. Rules will be matched sequentially based on the RouteMatch specified for the rule. |
| `gateways` | `array` | Optional. Gateways defines a list of gateways this HttpRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
| `meshes` | `array` | Optional. Meshes defines a list of meshes this HttpRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` The attached Mesh should be of a type SIDECAR |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `hostnames` | `array` | Required. Hostnames define a set of hosts that should match against the HTTP host header to select a HttpRoute to process the request. Hostname is the fully qualified domain name of a network host, as defined by RFC 1123 with the exception that: - IPs are not allowed. - A hostname may be prefixed with a wildcard label (*.). The wildcard label must appear by itself as the first label. Hostname can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.example.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. *.example.com). Note that as per RFC1035 and RFC1123, a label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character. No other punctuation is allowed. The routes associated with a Mesh or Gateways must have unique hostnames. If you attempt to attach multiple routes with conflicting hostnames, the configuration will be rejected. For example, while it is acceptable for routes for the hostnames "*.foo.bar.com" and "*.bar.com" to be associated with the same Mesh (or Gateways under the same scope), it is not possible to associate two routes both with "*.bar.com" or both with "bar.com". |
| `labels` | `object` | Optional. Set of label tags associated with the HttpRoute resource. |
| `selfLink` | `string` | Output only. Server-defined URL of this resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_httpRoutes_get` | `SELECT` | `httpRoutesId, locationsId, projectsId` | Gets details of a single HttpRoute. |
| `projects_locations_httpRoutes_list` | `SELECT` | `locationsId, projectsId` | Lists HttpRoute in a given project and location. |
| `projects_locations_httpRoutes_create` | `INSERT` | `locationsId, projectsId` | Creates a new HttpRoute in a given project and location. |
| `projects_locations_httpRoutes_delete` | `DELETE` | `httpRoutesId, locationsId, projectsId` | Deletes a single HttpRoute. |
| `projects_locations_httpRoutes_patch` | `EXEC` | `httpRoutesId, locationsId, projectsId` | Updates the parameters of a single HttpRoute. |
