---
title: vpc_classic_link
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_classic_link
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
<tr><td><b>Name</b></td><td><code>vpc_classic_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_classic_link</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `classicLinkEnabled` | `boolean` | Indicates whether the VPC is enabled for ClassicLink. |
| `tagSet` | `array` | Any tags assigned to the VPC. |
| `vpcId` | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_classic_link_Describe` | `SELECT` |  | Describes the ClassicLink status of one or more VPCs. |
| `vpc_classic_link_Disable` | `EXEC` | `VpcId` | Disables ClassicLink for a VPC. You cannot disable ClassicLink for a VPC that has EC2-Classic instances linked to it. |
| `vpc_classic_link_Enable` | `EXEC` | `VpcId` | Enables a VPC for ClassicLink. You can then link EC2-Classic instances to your ClassicLink-enabled VPC to allow communication over private IP addresses. You cannot enable your VPC for ClassicLink if any of your VPC route tables have existing routes for address ranges within the &lt;code&gt;10.0.0.0/8&lt;/code&gt; IP address range, excluding local routes for VPCs in the &lt;code&gt;10.0.0.0/16&lt;/code&gt; and &lt;code&gt;10.1.0.0/16&lt;/code&gt; IP address ranges. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html"&gt;ClassicLink&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. |
