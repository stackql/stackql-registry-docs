---
title: customer_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateways
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
<tr><td><b>Name</b></td><td><code>customer_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.customer_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | The current state of the customer gateway (&lt;code&gt;pending \| available \| deleting \| deleted&lt;/code&gt;). |
| `tagSet` | `array` | Any tags assigned to the customer gateway. |
| `type` | `string` | The type of VPN connection the customer gateway supports (&lt;code&gt;ipsec.1&lt;/code&gt;). |
| `bgpAsn` | `string` | The customer gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN). |
| `certificateArn` | `string` | The Amazon Resource Name (ARN) for the customer gateway certificate. |
| `customerGatewayId` | `string` | The ID of the customer gateway. |
| `deviceName` | `string` | The name of customer gateway device. |
| `ipAddress` | `string` | The Internet-routable IP address of the customer gateway's outside interface. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customer_gateways_Describe` | `SELECT` |  | &lt;p&gt;Describes one or more of your VPN customer gateways.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| `customer_gateway_Create` | `INSERT` | `BgpAsn, Type` | &lt;p&gt;Provides information to Amazon Web Services about your VPN customer gateway device. The customer gateway is the appliance at your end of the VPN connection. (The device on the Amazon Web Services side of the VPN connection is the virtual private gateway.) You must provide the internet-routable IP address of the customer gateway's external interface. The IP address must be static and can be behind a device performing network address translation (NAT).&lt;/p&gt; &lt;p&gt;For devices that use Border Gateway Protocol (BGP), you can also provide the device's BGP Autonomous System Number (ASN). You can use an existing ASN assigned to your network. If you don't have an ASN already, you can use a private ASN. For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-options.html"&gt;Customer gateway options for your Site-to-Site VPN connection&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To create more than one customer gateway with the same VPN type, IP address, and BGP ASN, specify a unique device name for each customer gateway. An identical request returns information about the existing customer gateway; it doesn't create a new customer gateway.&lt;/p&gt; |
| `customer_gateway_Delete` | `DELETE` | `CustomerGatewayId` | Deletes the specified customer gateway. You must delete the VPN connection before you can delete the customer gateway. |
