---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - servicenetworking
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
<tr><td><b>Id</b></td><td><code>google.servicenetworking.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `network` | `string` | The name of service consumer's VPC network that's connected with service producer network, in the following format: `projects/{project}/global/networks/{network}`. `{project}` is a project number, such as in `12345` that includes the VPC service consumer's VPC network. `{network}` is the name of the service consumer's VPC network. |
| `peering` | `string` | Output only. The name of the VPC Network Peering connection that was created by the service producer. |
| `reservedPeeringRanges` | `array` | The name of one or more allocated IP address ranges for this service producer of type `PEERING`. Note that invoking CreateConnection method with a different range when connection is already established will not modify already provisioned service producer subnetworks. If CreateConnection method is invoked repeatedly to reconnect when peering connection had been disconnected on the consumer side, leaving this field empty will restore previously allocated IP ranges. |
| `service` | `string` | Output only. The name of the peering service that's associated with this connection, in the following format: `services/{service name}`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `services_connections_list` | `SELECT` | `servicesId` | List the private connections that are configured in a service consumer's VPC network. |
| `services_connections_create` | `INSERT` | `servicesId` | Creates a private connection that establishes a VPC Network Peering connection to a VPC network in the service producer's organization. The administrator of the service consumer's VPC network invokes this method. The administrator must assign one or more allocated IP ranges for provisioning subnetworks in the service producer's VPC network. This connection is used for all supported services in the service producer's organization, so it only needs to be invoked once. |
| `services_connections_patch` | `EXEC` | `connectionsId, servicesId` | Updates the allocated ranges that are assigned to a connection. |
