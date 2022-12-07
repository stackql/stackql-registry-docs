---
title: client_vpn_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_endpoints
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
<tr><td><b>Name</b></td><td><code>client_vpn_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.client_vpn_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A brief description of the endpoint. |
| `securityGroupIdSet` | `array` | The IDs of the security groups for the target network. |
| `connectionLogOptions` | `object` | Information about the client connection logging options for a Client VPN endpoint. |
| `vpnProtocol` | `string` | The protocol used by the VPN session. |
| `status` | `object` | Describes the state of a Client VPN endpoint. |
| `clientVpnEndpointId` | `string` | The ID of the Client VPN endpoint. |
| `sessionTimeoutHours` | `integer` | &lt;p&gt;The maximum VPN session duration time in hours.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;8 \| 10 \| 12 \| 24&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;24&lt;/code&gt; &lt;/p&gt; |
| `vpnPort` | `integer` | The port number for the Client VPN endpoint. |
| `associatedTargetNetwork` | `array` | Information about the associated target networks. A target network is a subnet in a VPC.This property is deprecated. To view the target networks associated with a Client VPN endpoint, call DescribeClientVpnTargetNetworks and inspect the clientVpnTargetNetworks response element. |
| `clientLoginBannerOptions` | `object` | Current state of options for customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established. |
| `deletionTime` | `string` | The date and time the Client VPN endpoint was deleted, if applicable. |
| `creationTime` | `string` | The date and time the Client VPN endpoint was created. |
| `tagSet` | `array` | Any tags assigned to the Client VPN endpoint. |
| `clientCidrBlock` | `string` | The IPv4 address range, in CIDR notation, from which client IP addresses are assigned. |
| `selfServicePortalUrl` | `string` | The URL of the self-service portal. |
| `transportProtocol` | `string` | The transport protocol used by the Client VPN endpoint. |
| `serverCertificateArn` | `string` | The ARN of the server certificate. |
| `dnsServer` | `array` | Information about the DNS servers to be used for DNS resolution.  |
| `vpcId` | `string` | The ID of the VPC. |
| `dnsName` | `string` | The DNS name to be used by clients when connecting to the Client VPN endpoint. |
| `authenticationOptions` | `array` | Information about the authentication method used by the Client VPN endpoint. |
| `splitTunnel` | `boolean` | &lt;p&gt;Indicates whether split-tunnel is enabled in the Client VPN endpoint.&lt;/p&gt; &lt;p&gt;For information about split-tunnel VPN endpoints, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html"&gt;Split-Tunnel Client VPN endpoint&lt;/a&gt; in the &lt;i&gt;Client VPN Administrator Guide&lt;/i&gt;.&lt;/p&gt; |
| `clientConnectOptions` | `object` | The options for managing connection authorization for new client connections. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `client_vpn_endpoints_Describe` | `SELECT` |  | Describes one or more Client VPN endpoints in the account. |
| `client_vpn_endpoint_Create` | `INSERT` | `Authentication, ClientCidrBlock, ConnectionLogOptions, ServerCertificateArn` | Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated. |
| `client_vpn_endpoint_Delete` | `DELETE` | `ClientVpnEndpointId` | Deletes the specified Client VPN endpoint. You must disassociate all target networks before you can delete a Client VPN endpoint. |
| `client_vpn_endpoint_Modify` | `EXEC` | `ClientVpnEndpointId` | Modifies the specified Client VPN endpoint. Modifying the DNS server resets existing client connections. |
