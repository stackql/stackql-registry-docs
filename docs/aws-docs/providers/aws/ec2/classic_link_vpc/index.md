---
title: classic_link_vpc
hide_title: false
hide_table_of_contents: false
keywords:
  - classic_link_vpc
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
<tr><td><b>Name</b></td><td><code>classic_link_vpc</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.classic_link_vpc</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `classic_link_vpc_Attach` | `EXEC` | `InstanceId, SecurityGroupId, VpcId` | &lt;p&gt;Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC's security groups. You cannot link an EC2-Classic instance to more than one VPC at a time. You can only link an instance that's in the &lt;code&gt;running&lt;/code&gt; state. An instance is automatically unlinked from a VPC when it's stopped - you can link it to the VPC again when you restart it.&lt;/p&gt; &lt;p&gt;After you've linked an instance, you cannot change the VPC security groups that are associated with it. To change the security groups, you must first unlink the instance, and then link it again.&lt;/p&gt; &lt;p&gt;Linking your instance to a VPC is sometimes referred to as &lt;i&gt;attaching&lt;/i&gt; your instance.&lt;/p&gt; |
| `classic_link_vpc_Detach` | `EXEC` | `InstanceId, VpcId` | Unlinks (detaches) a linked EC2-Classic instance from a VPC. After the instance has been unlinked, the VPC security groups are no longer associated with it. An instance is automatically unlinked from a VPC when it's stopped. |
