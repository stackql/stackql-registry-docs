---
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
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
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.subnets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the subnet. |
| `ipv6Native` | `boolean` | Indicates whether this is an IPv6 only subnet. |
| `mapCustomerOwnedIpOnLaunch` | `boolean` | Indicates whether a network interface created in this subnet (including a network interface created by &lt;a&gt;RunInstances&lt;/a&gt;) receives a customer-owned IPv4 address. |
| `availabilityZoneId` | `string` | The AZ ID of the subnet. |
| `enableDns64` | `boolean` | Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. |
| `cidrBlock` | `string` | The IPv4 CIDR block assigned to the subnet. |
| `subnetArn` | `string` | The Amazon Resource Name (ARN) of the subnet. |
| `customerOwnedIpv4Pool` | `string` | The customer-owned IPv4 address pool associated with the subnet. |
| `enableLniAtDeviceIndex` | `integer` |  Indicates the device position for local network interfaces in this subnet. For example, &lt;code&gt;1&lt;/code&gt; indicates local network interfaces in this subnet are the secondary network interface (eth1).  |
| `mapPublicIpOnLaunch` | `boolean` | Indicates whether instances launched in this subnet receive a public IPv4 address. |
| `assignIpv6AddressOnCreation` | `boolean` | Indicates whether a network interface created in this subnet (including a network interface created by &lt;a&gt;RunInstances&lt;/a&gt;) receives an IPv6 address. |
| `ipv6CidrBlockAssociationSet` | `array` | Information about the IPv6 CIDR blocks associated with the subnet. |
| `vpcId` | `string` | The ID of the VPC the subnet is in. |
| `state` | `string` | The current state of the subnet. |
| `subnetId` | `string` | The ID of the subnet. |
| `tagSet` | `array` | Any tags assigned to the subnet. |
| `defaultForAz` | `boolean` | Indicates whether this is the default subnet for the Availability Zone. |
| `availabilityZone` | `string` | The Availability Zone of the subnet. |
| `privateDnsNameOptionsOnLaunch` | `object` | Describes the options for instance hostnames. |
| `availableIpAddressCount` | `integer` | The number of unused private IPv4 addresses in the subnet. The IPv4 addresses for any stopped instances are considered unavailable. |
| `outpostArn` | `string` | The Amazon Resource Name (ARN) of the Outpost. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `subnets_Describe` | `SELECT` |  | &lt;p&gt;Describes one or more of your subnets.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html"&gt;Your VPC and subnets&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `subnet_Create` | `INSERT` | `VpcId` | &lt;p&gt;Creates a subnet in a specified VPC.&lt;/p&gt; &lt;p&gt;You must specify an IPv4 CIDR block for the subnet. After you create a subnet, you can't change its CIDR block. The allowed block size is between a /16 netmask (65,536 IP addresses) and /28 netmask (16 IP addresses). The CIDR block must not overlap with the CIDR block of an existing subnet in the VPC.&lt;/p&gt; &lt;p&gt;If you've associated an IPv6 CIDR block with your VPC, you can create a subnet with an IPv6 CIDR block that uses a /64 prefix length. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Amazon Web Services reserves both the first four and the last IPv4 address in each subnet's CIDR block. They're not available for use.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you add more than one subnet to a VPC, they're set up in a star topology with a logical router in the middle.&lt;/p&gt; &lt;p&gt;When you stop an instance in a subnet, it retains its private IPv4 address. It's therefore possible to have a subnet with no running instances (they're all stopped), but no remaining IP addresses available.&lt;/p&gt; &lt;p&gt;For more information about subnets, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html"&gt;Your VPC and subnets&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `subnet_Delete` | `DELETE` | `SubnetId` | Deletes the specified subnet. You must terminate all running instances in the subnet before you can delete the subnet. |
