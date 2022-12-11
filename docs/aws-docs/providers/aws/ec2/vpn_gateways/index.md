---
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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
<tr><td><b>Name</b></td><td><code>vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpn_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | The current state of the virtual private gateway. |
| `tagSet` | `array` | Any tags assigned to the virtual private gateway. |
| `type` | `string` | The type of VPN connection the virtual private gateway supports. |
| `vpnGatewayId` | `string` | The ID of the virtual private gateway. |
| `amazonSideAsn` | `integer` | The private Autonomous System Number (ASN) for the Amazon side of a BGP session. |
| `attachments` | `array` | Any VPCs attached to the virtual private gateway. |
| `availabilityZone` | `string` | The Availability Zone where the virtual private gateway was created, if applicable. This field may be empty or not returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpn_gateways_Describe` | `SELECT` |  | &lt;p&gt;Describes one or more of your virtual private gateways.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpn_gateway_Create` | `INSERT` | `Type` | &lt;p&gt;Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpn_gateway_Delete` | `DELETE` | `VpnGatewayId` | Deletes the specified virtual private gateway. You must first detach the virtual private gateway from the VPC. Note that you don't need to delete the virtual private gateway if you plan to delete and recreate the VPN connection between your VPC and your network. |
| `vpn_gateway_Attach` | `EXEC` | `VpcId, VpnGatewayId` | &lt;p&gt;Attaches a virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpn_gateway_Detach` | `EXEC` | `VpcId, VpnGatewayId` | &lt;p&gt;Detaches a virtual private gateway from a VPC. You do this if you're planning to turn off the VPC and not use it anymore. You can confirm a virtual private gateway has been completely detached from a VPC by describing the virtual private gateway (any attachments to the virtual private gateway are also described).&lt;/p&gt; &lt;p&gt;You must wait for the attachment's state to switch to &lt;code&gt;detached&lt;/code&gt; before you can delete the VPC or attach a different VPC to the virtual private gateway.&lt;/p&gt; |
