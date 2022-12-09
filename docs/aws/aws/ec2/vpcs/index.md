---
title: vpcs
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcs
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
<tr><td><b>Name</b></td><td><code>vpcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpcs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the VPC. |
| `state` | `string` | The current state of the VPC. |
| `cidrBlockAssociationSet` | `array` | Information about the IPv4 CIDR blocks associated with the VPC. |
| `isDefault` | `boolean` | Indicates whether the VPC is the default VPC. |
| `dhcpOptionsId` | `string` | The ID of the set of DHCP options you've associated with the VPC. |
| `tagSet` | `array` | Any tags assigned to the VPC. |
| `vpcId` | `string` | The ID of the VPC. |
| `cidrBlock` | `string` | The primary IPv4 CIDR block for the VPC. |
| `instanceTenancy` | `string` | The allowed tenancy of instances launched into the VPC. |
| `ipv6CidrBlockAssociationSet` | `array` | Information about the IPv6 CIDR blocks associated with the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpcs_Describe` | `SELECT` |  | Describes one or more of your VPCs. |
| `vpc_Create` | `INSERT` |  | &lt;p&gt;Creates a VPC with the specified IPv4 CIDR block. The smallest VPC you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses). For more information about how large to make your VPC, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html"&gt;Your VPC and subnets&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can optionally request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (&lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html"&gt;BYOIP&lt;/a&gt;).&lt;/p&gt; &lt;p&gt;By default, each instance you launch in the VPC has the default DHCP options, which include only a default DNS server that we provide (AmazonProvidedDNS). For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html"&gt;DHCP options sets&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can specify the instance tenancy value for the VPC when you create it. You can't change this value for the VPC after you create it. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html"&gt;Dedicated Instances&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpc_Delete` | `DELETE` | `VpcId` | Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it. For example, you must terminate all instances running in the VPC, delete all security groups associated with the VPC (except the default one), delete all route tables associated with the VPC (except the default one), and so on. |
