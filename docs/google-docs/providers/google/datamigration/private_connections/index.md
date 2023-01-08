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
| `name` | `string` | The resource's name. |
| `vpcPeeringConfig` | `object` | The VPC Peering configuration is used to create VPC peering with the consumer's VPC. |
| `createTime` | `string` | Output only. The create time of the resource. |
| `displayName` | `string` | The private connection display name. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `labels` | `object` | The resource labels for private connections to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `&#123; "name": "wrench", "mass": "1.3kg", "count": "3" &#125;`. |
| `state` | `string` | Output only. The state of the Private Connection. |
| `updateTime` | `string` | Output only. The last update time of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_privateConnections_get` | `SELECT` | `locationsId, privateConnectionsId, projectsId` | Gets details of a single private connection. |
| `projects_locations_privateConnections_list` | `SELECT` | `locationsId, projectsId` | Retrieves a list of private connections in a given project and location. |
| `projects_locations_privateConnections_create` | `INSERT` | `locationsId, projectsId` | Creates a new private connection in a given project and location. |
| `projects_locations_privateConnections_delete` | `DELETE` | `locationsId, privateConnectionsId, projectsId` | Deletes a single Database Migration Service private connection. |
