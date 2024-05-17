---
title: instance_profiles_for_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_profiles_for_roles
  - iam_api
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
<tr><td><b>Name</b></td><td><code>instance_profiles_for_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam_api.instance_profiles_for_roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Arn" /> | `string` | &lt;p&gt;The Amazon Resource Name (ARN). ARNs are unique identifiers for Amazon Web Services resources.&lt;/p&gt; &lt;p&gt;For more information about ARNs, go to &lt;a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. &lt;/p&gt; |
| <CopyableCode code="CreateDate" /> | `string` | The date when the instance profile was created. |
| <CopyableCode code="InstanceProfileId" /> | `string` |  The stable and unique string identifying the instance profile. For more information about IDs, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html"&gt;IAM identifiers&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.  |
| <CopyableCode code="InstanceProfileName" /> | `string` | The name identifying the instance profile. |
| <CopyableCode code="Path" /> | `string` |  The path to the instance profile. For more information about paths, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html"&gt;IAM identifiers&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.  |
| <CopyableCode code="Roles" /> | `array` | &lt;p&gt;Contains a list of IAM roles.&lt;/p&gt; &lt;p&gt;This data type is used as a response element in the &lt;a&gt;ListRoles&lt;/a&gt; operation.&lt;/p&gt; |
| <CopyableCode code="Tags" /> | `array` | A list of tags that are attached to the instance profile. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="instance_profiles_for_roles_List" /> | `SELECT` | <CopyableCode code="RoleName, region" /> |
