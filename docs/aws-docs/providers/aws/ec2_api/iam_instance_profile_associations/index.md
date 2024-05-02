---
title: iam_instance_profile_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - iam_instance_profile_associations
  - ec2_api
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
<tr><td><b>Name</b></td><td><code>iam_instance_profile_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.iam_instance_profile_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `associationId` | `string` | The ID of the association. |
| `iamInstanceProfile` | `object` | Describes an IAM instance profile. |
| `instanceId` | `string` | The ID of the instance. |
| `state` | `string` | The state of the association. |
| `timestamp` | `string` | The time the IAM instance profile was associated with the instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `iam_instance_profile_associations_Describe` | `SELECT` | `region` | Describes your IAM instance profile associations. |
| `iam_instance_profile_association_Replace` | `EXEC` | `AssociationId, IamInstanceProfile, region` | &lt;p&gt;Replaces an IAM instance profile for the specified running instance. You can use this action to change the IAM instance profile that's associated with an instance without having to disassociate the existing IAM instance profile first.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DescribeIamInstanceProfileAssociations&lt;/a&gt; to get the association ID.&lt;/p&gt; |
