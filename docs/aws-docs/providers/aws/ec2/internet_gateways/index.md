---
title: internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateways
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
<tr><td><b>Name</b></td><td><code>internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.internet_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tagSet` | `array` | Any tags assigned to the internet gateway. |
| `attachmentSet` | `array` | Any VPCs attached to the internet gateway. |
| `internetGatewayId` | `string` | The ID of the internet gateway. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the internet gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `internet_gateways_Describe` | `SELECT` |  | Describes one or more of your internet gateways. |
| `internet_gateway_Create` | `INSERT` |  | &lt;p&gt;Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using &lt;a&gt;AttachInternetGateway&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about your VPC and internet gateway, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/"&gt;Amazon Virtual Private Cloud User Guide&lt;/a&gt;.&lt;/p&gt; |
| `internet_gateway_Delete` | `DELETE` | `InternetGatewayId` | Deletes the specified internet gateway. You must detach the internet gateway from the VPC before you can delete it. |
| `internet_gateway_Attach` | `EXEC` | `InternetGatewayId, VpcId` | Attaches an internet gateway or a virtual private gateway to a VPC, enabling connectivity between the internet and the VPC. For more information about your VPC and internet gateway, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/"&gt;Amazon Virtual Private Cloud User Guide&lt;/a&gt;. |
| `internet_gateway_Detach` | `EXEC` | `InternetGatewayId, VpcId` | Detaches an internet gateway from a VPC, disabling connectivity between the internet and the VPC. The VPC must not contain any running instances with Elastic IP addresses or public IPv4 addresses. |
