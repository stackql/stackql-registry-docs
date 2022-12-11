---
title: nat_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways
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
<tr><td><b>Name</b></td><td><code>nat_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.nat_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `failureCode` | `string` | If the NAT gateway could not be created, specifies the error code for the failure. (&lt;code&gt;InsufficientFreeAddressesInSubnet&lt;/code&gt; \| &lt;code&gt;Gateway.NotAttached&lt;/code&gt; \| &lt;code&gt;InvalidAllocationID.NotFound&lt;/code&gt; \| &lt;code&gt;Resource.AlreadyAssociated&lt;/code&gt; \| &lt;code&gt;InternalError&lt;/code&gt; \| &lt;code&gt;InvalidSubnetID.NotFound&lt;/code&gt;) |
| `natGatewayAddressSet` | `array` | Information about the IP addresses and network interface associated with the NAT gateway. |
| `deleteTime` | `string` | The date and time the NAT gateway was deleted, if applicable. |
| `failureMessage` | `string` | &lt;p&gt;If the NAT gateway could not be created, specifies the error message for the failure, that corresponds to the error code.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For InsufficientFreeAddressesInSubnet: "Subnet has insufficient free addresses to create this NAT gateway"&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Gateway.NotAttached: "Network vpc-xxxxxxxx has no Internet gateway attached"&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For InvalidAllocationID.NotFound: "Elastic IP address eipalloc-xxxxxxxx could not be associated with this NAT gateway"&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Resource.AlreadyAssociated: "Elastic IP address eipalloc-xxxxxxxx is already associated"&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For InternalError: "Network interface eni-xxxxxxxx, created and used internally by this NAT gateway is in an invalid state. Please try again."&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For InvalidSubnetID.NotFound: "The specified subnet subnet-xxxxxxxx does not exist or could not be found."&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `natGatewayId` | `string` | The ID of the NAT gateway. |
| `subnetId` | `string` | The ID of the subnet in which the NAT gateway is located. |
| `tagSet` | `array` | The tags for the NAT gateway. |
| `createTime` | `string` | The date and time the NAT gateway was created. |
| `state` | `string` | &lt;p&gt;The state of the NAT gateway.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pending&lt;/code&gt;: The NAT gateway is being created and is not ready to process traffic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failed&lt;/code&gt;: The NAT gateway could not be created. Check the &lt;code&gt;failureCode&lt;/code&gt; and &lt;code&gt;failureMessage&lt;/code&gt; fields for the reason.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;available&lt;/code&gt;: The NAT gateway is able to process traffic. This status remains until you delete the NAT gateway, and does not indicate the health of the NAT gateway.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;deleting&lt;/code&gt;: The NAT gateway is in the process of being terminated and may still be processing traffic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;deleted&lt;/code&gt;: The NAT gateway has been terminated and is no longer processing traffic.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `connectivityType` | `string` | Indicates whether the NAT gateway supports public or private connectivity. |
| `provisionedBandwidth` | `object` | Reserved. If you need to sustain traffic greater than the &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html"&gt;documented limits&lt;/a&gt;, contact us through the &lt;a href="https://console.aws.amazon.com/support/home?"&gt;Support Center&lt;/a&gt;. |
| `vpcId` | `string` | The ID of the VPC in which the NAT gateway is located. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `nat_gateways_Describe` | `SELECT` |  | Describes one or more of your NAT gateways. |
| `nat_gateway_Create` | `INSERT` | `SubnetId` | &lt;p&gt;Creates a NAT gateway in the specified subnet. This action creates a network interface in the specified subnet with a private IP address from the IP address range of the subnet. You can create either a public NAT gateway or a private NAT gateway.&lt;/p&gt; &lt;p&gt;With a public NAT gateway, internet-bound traffic from a private subnet can be routed to the NAT gateway, so that instances in a private subnet can connect to the internet.&lt;/p&gt; &lt;p&gt;With a private NAT gateway, private communication is routed across VPCs and on-premises networks through a transit gateway or virtual private gateway. Common use cases include running large workloads behind a small pool of allowlisted IPv4 addresses, preserving private IPv4 addresses, and communicating between overlapping networks.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html"&gt;NAT gateways&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `nat_gateway_Delete` | `DELETE` | `NatGatewayId` | Deletes the specified NAT gateway. Deleting a public NAT gateway disassociates its Elastic IP address, but does not release the address from your account. Deleting a NAT gateway does not delete any NAT gateway routes in your route tables. |
