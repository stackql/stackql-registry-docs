---
title: vpc_classic_link_dns_support
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_classic_link_dns_support
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_classic_link_dns_support</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_classic_link_dns_support</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `classicLinkDnsSupported` | `boolean` | Indicates whether ClassicLink DNS support is enabled for the VPC. |
| `vpcId` | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_classic_link_dns_support_Describe` | `SELECT` | `region` | Describes the ClassicLink DNS support status of one or more VPCs. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html"&gt;ClassicLink&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. |
| `vpc_classic_link_dns_support_Disable` | `EXEC` | `region` | &lt;p&gt;Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve to public IP addresses when addressed between a linked EC2-Classic instance and instances in the VPC to which it's linked. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html"&gt;ClassicLink&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You must specify a VPC ID in the request.&lt;/p&gt; |
| `vpc_classic_link_dns_support_Enable` | `EXEC` | `region` | &lt;p&gt;Enables a VPC to support DNS hostname resolution for ClassicLink. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html"&gt;ClassicLink&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You must specify a VPC ID in the request.&lt;/p&gt; |
