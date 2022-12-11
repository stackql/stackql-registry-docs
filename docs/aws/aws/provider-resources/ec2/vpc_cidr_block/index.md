---
title: vpc_cidr_block
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_cidr_block
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
<tr><td><b>Name</b></td><td><code>vpc_cidr_block</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_cidr_block</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_cidr_block_Associate` | `EXEC` | `VpcId` | &lt;p&gt;Associates a CIDR block with your VPC. You can associate a secondary IPv4 CIDR block, an Amazon-provided IPv6 CIDR block, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (&lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html"&gt;BYOIP&lt;/a&gt;). The IPv6 CIDR block size is fixed at /56.&lt;/p&gt; &lt;p&gt;You must specify one of the following in the request: an IPv4 CIDR block, an IPv6 pool, or an Amazon-provided IPv6 CIDR block.&lt;/p&gt; &lt;p&gt;For more information about associating CIDR blocks with your VPC and applicable restrictions, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#VPC_Sizing"&gt;VPC and subnet sizing&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpc_cidr_block_Disassociate` | `EXEC` | `AssociationId` | &lt;p&gt;Disassociates a CIDR block from a VPC. To disassociate the CIDR block, you must specify its association ID. You can get the association ID by using &lt;a&gt;DescribeVpcs&lt;/a&gt;. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it. &lt;/p&gt; &lt;p&gt;You cannot disassociate the CIDR block with which you originally created the VPC (the primary CIDR block).&lt;/p&gt; |
