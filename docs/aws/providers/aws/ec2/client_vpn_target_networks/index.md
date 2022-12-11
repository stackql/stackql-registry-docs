---
title: client_vpn_target_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_target_networks
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
<tr><td><b>Name</b></td><td><code>client_vpn_target_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.client_vpn_target_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `object` | Describes the state of a target network association. |
| `targetNetworkId` | `string` | The ID of the subnet specified as the target network. |
| `vpcId` | `string` | The ID of the VPC in which the target network (subnet) is located. |
| `associationId` | `string` | The ID of the association. |
| `clientVpnEndpointId` | `string` | The ID of the Client VPN endpoint with which the target network is associated. |
| `securityGroups` | `array` | The IDs of the security groups applied to the target network association. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `client_vpn_target_networks_Describe` | `SELECT` | `ClientVpnEndpointId` | Describes the target networks associated with the specified Client VPN endpoint. |
| `client_vpn_target_network_Associate` | `EXEC` | `ClientVpnEndpointId, SubnetId` | &lt;p&gt;Associates a target network with a Client VPN endpoint. A target network is a subnet in a VPC. You can associate multiple subnets from the same VPC with a Client VPN endpoint. You can associate only one subnet in each Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy.&lt;/p&gt; &lt;p&gt;If you specified a VPC when you created the Client VPN endpoint or if you have previous subnet associations, the specified subnet must be in the same VPC. To specify a subnet that's in a different VPC, you must first modify the Client VPN endpoint (&lt;a&gt;ModifyClientVpnEndpoint&lt;/a&gt;) and change the VPC that's associated with it.&lt;/p&gt; |
| `client_vpn_target_network_Disassociate` | `EXEC` | `AssociationId, ClientVpnEndpointId` | &lt;p&gt;Disassociates a target network from the specified Client VPN endpoint. When you disassociate the last target network from a Client VPN, the following happens:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The route that was automatically added for the VPC is deleted&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All active client connections are terminated&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;New client connections are disallowed&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Client VPN endpoint's status changes to &lt;code&gt;pending-associate&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
