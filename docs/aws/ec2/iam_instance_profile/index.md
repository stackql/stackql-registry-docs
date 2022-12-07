---
title: iam_instance_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - iam_instance_profile
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
<tr><td><b>Name</b></td><td><code>iam_instance_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.iam_instance_profile</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `iam_instance_profile_Associate` | `EXEC` | `IamInstanceProfile, InstanceId` | Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance. |
| `iam_instance_profile_Disassociate` | `EXEC` | `AssociationId` | &lt;p&gt;Disassociates an IAM instance profile from a running or stopped instance.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DescribeIamInstanceProfileAssociations&lt;/a&gt; to get the association ID.&lt;/p&gt; |
