---
title: client_vpn_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_endpoints
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
<tr><td><b>Name</b></td><td><code>client_vpn_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.client_vpn_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A brief description of the endpoint. |
| <CopyableCode code="associatedTargetNetwork" /> | `array` | Information about the associated target networks. A target network is a subnet in a VPC.This property is deprecated. To view the target networks associated with a Client VPN endpoint, call DescribeClientVpnTargetNetworks and inspect the clientVpnTargetNetworks response element. |
| <CopyableCode code="authenticationOptions" /> | `array` | Information about the authentication method used by the Client VPN endpoint. |
| <CopyableCode code="clientCidrBlock" /> | `string` | The IPv4 address range, in CIDR notation, from which client IP addresses are assigned. |
| <CopyableCode code="clientConnectOptions" /> | `object` | The options for managing connection authorization for new client connections. |
| <CopyableCode code="clientLoginBannerOptions" /> | `object` | Current state of options for customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established. |
| <CopyableCode code="clientVpnEndpointId" /> | `string` | The ID of the Client VPN endpoint. |
| <CopyableCode code="connectionLogOptions" /> | `object` | Information about the client connection logging options for a Client VPN endpoint. |
| <CopyableCode code="creationTime" /> | `string` | The date and time the Client VPN endpoint was created. |
| <CopyableCode code="deletionTime" /> | `string` | The date and time the Client VPN endpoint was deleted, if applicable. |
| <CopyableCode code="dnsName" /> | `string` | The DNS name to be used by clients when connecting to the Client VPN endpoint. |
| <CopyableCode code="dnsServer" /> | `array` | Information about the DNS servers to be used for DNS resolution.  |
| <CopyableCode code="securityGroupIdSet" /> | `array` | The IDs of the security groups for the target network. |
| <CopyableCode code="selfServicePortalUrl" /> | `string` | The URL of the self-service portal. |
| <CopyableCode code="serverCertificateArn" /> | `string` | The ARN of the server certificate. |
| <CopyableCode code="sessionTimeoutHours" /> | `integer` | &lt;p&gt;The maximum VPN session duration time in hours.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;8 \| 10 \| 12 \| 24&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;24&lt;/code&gt; &lt;/p&gt; |
| <CopyableCode code="splitTunnel" /> | `boolean` | &lt;p&gt;Indicates whether split-tunnel is enabled in the Client VPN endpoint.&lt;/p&gt; &lt;p&gt;For information about split-tunnel VPN endpoints, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html"&gt;Split-Tunnel Client VPN endpoint&lt;/a&gt; in the &lt;i&gt;Client VPN Administrator Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="status" /> | `object` | Describes the state of a Client VPN endpoint. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the Client VPN endpoint. |
| <CopyableCode code="transportProtocol" /> | `string` | The transport protocol used by the Client VPN endpoint. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC. |
| <CopyableCode code="vpnPort" /> | `integer` | The port number for the Client VPN endpoint. |
| <CopyableCode code="vpnProtocol" /> | `string` | The protocol used by the VPN session. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="client_vpn_endpoints_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more Client VPN endpoints in the account. |
| <CopyableCode code="client_vpn_endpoint_Create" /> | `INSERT` | <CopyableCode code="Authentication, ClientCidrBlock, ConnectionLogOptions, ServerCertificateArn, region" /> | Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated. |
| <CopyableCode code="client_vpn_endpoint_Delete" /> | `DELETE` | <CopyableCode code="ClientVpnEndpointId, region" /> | Deletes the specified Client VPN endpoint. You must disassociate all target networks before you can delete a Client VPN endpoint. |
| <CopyableCode code="client_vpn_endpoint_Modify" /> | `EXEC` | <CopyableCode code="ClientVpnEndpointId, region" /> | Modifies the specified Client VPN endpoint. Modifying the DNS server resets existing client connections. |
