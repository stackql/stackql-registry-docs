---
title: network_acls
hide_title: false
hide_table_of_contents: false
keywords:
  - network_acls
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
<tr><td><b>Name</b></td><td><code>network_acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_acls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `default` | `boolean` | Indicates whether this is the default network ACL for the VPC. |
| `entrySet` | `array` | One or more entries (rules) in the network ACL. |
| `networkAclId` | `string` | The ID of the network ACL. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the network ACL. |
| `tagSet` | `array` | Any tags assigned to the network ACL. |
| `vpcId` | `string` | The ID of the VPC for the network ACL. |
| `associationSet` | `array` | Any associations between the network ACL and one or more subnets |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `network_acls_Describe` | `SELECT` |  | &lt;p&gt;Describes one or more of your network ACLs.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html"&gt;Network ACLs&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `network_acl_Create` | `INSERT` | `VpcId` | &lt;p&gt;Creates a network ACL in a VPC. Network ACLs provide an optional layer of security (in addition to security groups) for the instances in your VPC.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html"&gt;Network ACLs&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `network_acl_Delete` | `DELETE` | `NetworkAclId` | Deletes the specified network ACL. You can't delete the ACL if it's associated with any subnets. You can't delete the default network ACL. |
