---
title: client_vpn_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_routes
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_vpn_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.client_vpn_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A brief description of the route. |
| `destinationCidr` | `string` | The IPv4 address range, in CIDR notation, of the route destination. |
| `origin` | `string` | Indicates how the route was associated with the Client VPN endpoint. &lt;code&gt;associate&lt;/code&gt; indicates that the route was automatically added when the target network was associated with the Client VPN endpoint. &lt;code&gt;add-route&lt;/code&gt; indicates that the route was manually added using the &lt;b&gt;CreateClientVpnRoute&lt;/b&gt; action. |
| `status` | `object` | Describes the state of a Client VPN endpoint route. |
| `targetSubnet` | `string` | The ID of the subnet through which traffic is routed. |
| `type` | `string` | The route type. |
| `clientVpnEndpointId` | `string` | The ID of the Client VPN endpoint with which the route is associated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `client_vpn_routes_Describe` | `SELECT` | `ClientVpnEndpointId` | Describes the routes for the specified Client VPN endpoint. |
| `client_vpn_route_Create` | `INSERT` | `ClientVpnEndpointId, DestinationCidrBlock, TargetVpcSubnetId` | Adds a route to a network to a Client VPN endpoint. Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path for traﬃc to speciﬁc resources or networks. |
| `client_vpn_route_Delete` | `DELETE` | `ClientVpnEndpointId, DestinationCidrBlock` | Deletes a route from a Client VPN endpoint. You can only delete routes that you manually added using the &lt;b&gt;CreateClientVpnRoute&lt;/b&gt; action. You cannot delete routes that were automatically added when associating a subnet. To remove routes that have been automatically added, disassociate the target subnet from the Client VPN endpoint. |
