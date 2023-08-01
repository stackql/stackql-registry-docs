---
title: grpc_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - grpc_routes
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
<tr><td><b>Name</b></td><td><code>grpc_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.grpc_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `grpcRoutes` | `array` | List of GrpcRoute resources. |
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `grpcRoutesId, locationsId, projectsId` | Gets details of a single GrpcRoute. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists GrpcRoutes in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new GrpcRoute in a given project and location. |
| `delete` | `DELETE` | `grpcRoutesId, locationsId, projectsId` | Deletes a single GrpcRoute. |
| `patch` | `EXEC` | `grpcRoutesId, locationsId, projectsId` | Updates the parameters of a single GrpcRoute. |
