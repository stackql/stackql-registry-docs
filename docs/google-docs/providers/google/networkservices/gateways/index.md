---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
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
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `type` | `string` | Immutable. The type of the customer managed gateway. This field is required. If unspecified, an error is returned. |
| `scope` | `string` | Required. Immutable. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens. |
| `selfLink` | `string` | Output only. Server-defined URL of this resource |
| `ports` | `array` | Required. One or more port numbers (1-65535), on which the Gateway will receive traffic. The proxy binds to the specified ports. Gateways of type 'SECURE_WEB_GATEWAY' are limited to 1 port. Gateways of type 'OPEN_MESH' listen on 0.0.0.0 and support multiple ports. |
| `labels` | `object` | Optional. Set of label tags associated with the Gateway resource. |
| `serverTlsPolicy` | `string` | Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gateways_get` | `SELECT` | `gatewaysId, locationsId, projectsId` | Gets details of a single Gateway. |
| `projects_locations_gateways_list` | `SELECT` | `locationsId, projectsId` | Lists Gateways in a given project and location. |
| `projects_locations_gateways_create` | `INSERT` | `locationsId, projectsId` | Creates a new Gateway in a given project and location. |
| `projects_locations_gateways_delete` | `DELETE` | `gatewaysId, locationsId, projectsId` | Deletes a single Gateway. |
| `projects_locations_gateways_patch` | `EXEC` | `gatewaysId, locationsId, projectsId` | Updates the parameters of a single Gateway. |
