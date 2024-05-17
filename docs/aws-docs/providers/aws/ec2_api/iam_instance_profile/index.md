---
title: iam_instance_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - iam_instance_profile
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iam_instance_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.iam_instance_profile" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="iam_instance_profile_Associate" /> | `EXEC` | <CopyableCode code="IamInstanceProfile, InstanceId, region" /> | Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance. |
| <CopyableCode code="iam_instance_profile_Disassociate" /> | `EXEC` | <CopyableCode code="AssociationId, region" /> | &lt;p&gt;Disassociates an IAM instance profile from a running or stopped instance.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DescribeIamInstanceProfileAssociations&lt;/a&gt; to get the association ID.&lt;/p&gt; |
