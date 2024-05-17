---
title: client_vpn_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_routes
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_vpn_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.client_vpn_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A brief description of the route. |
| <CopyableCode code="clientVpnEndpointId" /> | `string` | The ID of the Client VPN endpoint with which the route is associated. |
| <CopyableCode code="destinationCidr" /> | `string` | The IPv4 address range, in CIDR notation, of the route destination. |
| <CopyableCode code="origin" /> | `string` | Indicates how the route was associated with the Client VPN endpoint. &lt;code&gt;associate&lt;/code&gt; indicates that the route was automatically added when the target network was associated with the Client VPN endpoint. &lt;code&gt;add-route&lt;/code&gt; indicates that the route was manually added using the &lt;b&gt;CreateClientVpnRoute&lt;/b&gt; action. |
| <CopyableCode code="status" /> | `object` | Describes the state of a Client VPN endpoint route. |
| <CopyableCode code="targetSubnet" /> | `string` | The ID of the subnet through which traffic is routed. |
| <CopyableCode code="type" /> | `string` | The route type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="client_vpn_routes_Describe" /> | `SELECT` | <CopyableCode code="ClientVpnEndpointId, region" /> | Describes the routes for the specified Client VPN endpoint. |
| <CopyableCode code="client_vpn_route_Create" /> | `INSERT` | <CopyableCode code="ClientVpnEndpointId, DestinationCidrBlock, TargetVpcSubnetId, region" /> | Adds a route to a network to a Client VPN endpoint. Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path for traﬃc to speciﬁc resources or networks. |
| <CopyableCode code="client_vpn_route_Delete" /> | `DELETE` | <CopyableCode code="ClientVpnEndpointId, DestinationCidrBlock, region" /> | Deletes a route from a Client VPN endpoint. You can only delete routes that you manually added using the &lt;b&gt;CreateClientVpnRoute&lt;/b&gt; action. You cannot delete routes that were automatically added when associating a subnet. To remove routes that have been automatically added, disassociate the target subnet from the Client VPN endpoint. |
