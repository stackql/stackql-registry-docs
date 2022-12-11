---
title: vpn_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connections
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
<tr><td><b>Name</b></td><td><code>vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpn_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `options` | `object` | Describes VPN connection options. |
| `state` | `string` | The current state of the VPN connection. |
| `customerGatewayConfiguration` | `string` | The configuration information for the VPN connection's customer gateway (in the native XML format). This element is always present in the &lt;a&gt;CreateVpnConnection&lt;/a&gt; response; however, it's present in the &lt;a&gt;DescribeVpnConnections&lt;/a&gt; response only if the VPN connection is in the &lt;code&gt;pending&lt;/code&gt; or &lt;code&gt;available&lt;/code&gt; state. |
| `vgwTelemetry` | `array` | Information about the VPN tunnel. |
| `category` | `string` | The category of the VPN connection. A value of &lt;code&gt;VPN&lt;/code&gt; indicates an Amazon Web Services VPN connection. A value of &lt;code&gt;VPN-Classic&lt;/code&gt; indicates an Amazon Web Services Classic VPN connection. |
| `vpnGatewayId` | `string` | The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection. |
| `coreNetworkAttachmentArn` | `string` | The ARN of the core network attachment. |
| `customerGatewayId` | `string` | The ID of the customer gateway at your end of the VPN connection. |
| `routes` | `array` | The static routes associated with the VPN connection. |
| `vpnConnectionId` | `string` | The ID of the VPN connection. |
| `type` | `string` | The type of VPN connection. |
| `tagSet` | `array` | Any tags assigned to the VPN connection. |
| `transitGatewayId` | `string` | The ID of the transit gateway associated with the VPN connection. |
| `gatewayAssociationState` | `string` | The current state of the gateway association. |
| `coreNetworkArn` | `string` | The ARN of the core network. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpn_connections_Describe` | `SELECT` |  | &lt;p&gt;Describes one or more of your VPN connections.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpn_connection_Create` | `INSERT` | `CustomerGatewayId, Type` | &lt;p&gt;Creates a VPN connection between an existing virtual private gateway or transit gateway and a customer gateway. The supported connection type is &lt;code&gt;ipsec.1&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The response includes information that you need to give to your network administrator to configure your customer gateway.&lt;/p&gt; &lt;important&gt; &lt;p&gt;We strongly recommend that you use HTTPS when calling this operation because the response contains sensitive cryptographic information for configuring your customer gateway device.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you decide to shut down your VPN connection for any reason and later create a new VPN connection, you must reconfigure your customer gateway with the new information returned from this call.&lt;/p&gt; &lt;p&gt;This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpn_connection_Delete` | `DELETE` | `VpnConnectionId` | &lt;p&gt;Deletes the specified VPN connection.&lt;/p&gt; &lt;p&gt;If you're deleting the VPC and its associated components, we recommend that you detach the virtual private gateway from the VPC and delete the VPC before deleting the VPN connection. If you believe that the tunnel credentials for your VPN connection have been compromised, you can delete the VPN connection and create a new one that has new keys, without needing to delete the VPC or virtual private gateway. If you create a new VPN connection, you must reconfigure the customer gateway device using the new configuration information returned with the new VPN connection ID.&lt;/p&gt; &lt;p&gt;For certificate-based authentication, delete all Certificate Manager (ACM) private certificates used for the Amazon Web Services-side tunnel endpoints for the VPN connection before deleting the VPN connection.&lt;/p&gt; |
| `vpn_connection_Modify` | `EXEC` | `VpnConnectionId` | &lt;p&gt;Modifies the customer gateway or the target gateway of an Amazon Web Services Site-to-Site VPN connection. To modify the target gateway, the following migration options are available:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An existing virtual private gateway to a new virtual private gateway&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An existing virtual private gateway to a transit gateway&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An existing transit gateway to a new transit gateway&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An existing transit gateway to a virtual private gateway&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Before you perform the migration to the new gateway, you must configure the new gateway. Use &lt;a&gt;CreateVpnGateway&lt;/a&gt; to create a virtual private gateway, or &lt;a&gt;CreateTransitGateway&lt;/a&gt; to create a transit gateway.&lt;/p&gt; &lt;p&gt;This step is required when you migrate from a virtual private gateway with static routes to a transit gateway. &lt;/p&gt; &lt;p&gt;You must delete the static routes before you migrate to the new gateway.&lt;/p&gt; &lt;p&gt;Keep a copy of the static route before you delete it. You will need to add back these routes to the transit gateway after the VPN connection migration is complete.&lt;/p&gt; &lt;p&gt;After you migrate to the new gateway, you might need to modify your VPC route table. Use &lt;a&gt;CreateRoute&lt;/a&gt; and &lt;a&gt;DeleteRoute&lt;/a&gt; to make the changes described in &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-target.html#step-update-routing"&gt;Update VPC route tables&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When the new gateway is a transit gateway, modify the transit gateway route table to allow traffic between the VPC and the Amazon Web Services Site-to-Site VPN connection. Use &lt;a&gt;CreateTransitGatewayRoute&lt;/a&gt; to add the routes.&lt;/p&gt; &lt;p&gt; If you deleted VPN static routes, you must add the static routes to the transit gateway route table.&lt;/p&gt; &lt;p&gt;After you perform this operation, the VPN endpoint's IP addresses on the Amazon Web Services side and the tunnel options remain intact. Your Amazon Web Services Site-to-Site VPN connection will be temporarily unavailable for a brief period while we provision the new endpoints.&lt;/p&gt; |
