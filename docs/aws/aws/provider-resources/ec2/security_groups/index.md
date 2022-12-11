---
title: security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - security_groups
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
<tr><td><b>Name</b></td><td><code>security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.security_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `vpcId` | `string` | [VPC only] The ID of the VPC for the security group. |
| `groupDescription` | `string` | A description of the security group. |
| `groupId` | `string` | The ID of the security group. |
| `groupName` | `string` | The name of the security group. |
| `ipPermissions` | `array` | The inbound rules associated with the security group. |
| `ipPermissionsEgress` | `array` | [VPC only] The outbound rules associated with the security group. |
| `ownerId` | `string` | The Amazon Web Services account ID of the owner of the security group. |
| `tagSet` | `array` | Any tags assigned to the security group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `security_groups_Describe` | `SELECT` |  | &lt;p&gt;Describes the specified security groups or all of your security groups.&lt;/p&gt; &lt;p&gt;A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html"&gt;Amazon EC2 security groups&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html"&gt;Security groups for your VPC&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `security_group_Create` | `INSERT` | `GroupDescription, GroupName` | &lt;p&gt;Creates a security group.&lt;/p&gt; &lt;p&gt;A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html"&gt;Amazon EC2 security groups&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html"&gt;Security groups for your VPC&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When you create a security group, you specify a friendly name of your choice. You can have a security group for use in EC2-Classic with the same name as a security group for use in a VPC. However, you can't have two security groups for use in EC2-Classic with the same name or two security groups for use in a VPC with the same name.&lt;/p&gt; &lt;p&gt;You have a default security group for use in EC2-Classic and a default security group for use in your VPC. If you don't specify a security group when you launch an instance, the instance is launched into the appropriate default security group. A default security group includes a default rule that grants instances unrestricted network access to each other.&lt;/p&gt; &lt;p&gt;You can add or remove rules from your security groups using &lt;a&gt;AuthorizeSecurityGroupIngress&lt;/a&gt;, &lt;a&gt;AuthorizeSecurityGroupEgress&lt;/a&gt;, &lt;a&gt;RevokeSecurityGroupIngress&lt;/a&gt;, and &lt;a&gt;RevokeSecurityGroupEgress&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about VPC security group limits, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html"&gt;Amazon VPC Limits&lt;/a&gt;.&lt;/p&gt; |
| `security_group_Delete` | `DELETE` |  | &lt;p&gt;Deletes a security group.&lt;/p&gt; &lt;p&gt;If you attempt to delete a security group that is associated with an instance, or is referenced by another security group, the operation fails with &lt;code&gt;InvalidGroup.InUse&lt;/code&gt; in EC2-Classic or &lt;code&gt;DependencyViolation&lt;/code&gt; in EC2-VPC.&lt;/p&gt; |
